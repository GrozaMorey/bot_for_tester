from aiogram import Bot, Dispatcher, executor, types
from models import session, User, Transaction, SuccessTransaction
from content import content, answers, keyboards, items, prices, img, get_answers
import datetime
from responses import welcome, buy_subscrube, back, show_info, edit_badge
from stages import EditBadge
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_KEY = "6216320540:AAHv5cUkrYWrLU4h5LJ7N-kUKx7LPLAuC54"
PAYMENTS_PROVIDER_TOKEN = '381764678:TEST:63344'

bot = Bot(token=API_KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

responses = {
    "welcome": welcome.welcome,
    "Купить подписку 🤑": buy_subscrube.buy_subscribe,
    "Назад 🔙": back.back,
    "Посмотреть информацию ℹ️": show_info.show_info,
    "Изменить номер бейджика 🪛": edit_badge.edit_badge_stage_1,
}


@dp.message_handler(commands=["start"])
async def hello(message: types.Message):
    await responses["welcome"](bot, message)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    if message.text in responses:
        await responses[message.text](bot, message)

@dp.message_handler(state=EditBadge.waiting_for_number_badge)
async def handle_text(message: types.Message, state: FSMContext):
    await edit_badge.edit_badge_stage_2(bot, message, state)

@dp.callback_query_handler(lambda c: True)
async def callback(callback: types.CallbackQuery):
    user = session.query(User).filter_by(username=callback.from_user.username).first()
    await bot.send_invoice(callback.message.chat.id, title=items["desk"][0],
                           description=items["desk"][1],
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='RUB',
                           photo_url=img["subscribe"],
                           photo_height=512,
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,
                           prices=prices,
                           payload=user.id,
                           need_shipping_address=None,
                           )

@dp.pre_checkout_query_handler()
async def pre_check_query(pre_query: types.PreCheckoutQuery):
    transaction = Transaction(
        user_id=pre_query.invoice_payload,
        transaction_id=pre_query.id,
    )

    session.add(transaction)
    session.commit()

    await bot.answer_pre_checkout_query(pre_query.id, ok=True)

@dp.message_handler(content_types=types.message.ContentType.SUCCESSFUL_PAYMENT)
async def success_payment(message: types.Message):
    success_transaction = SuccessTransaction(
        user_id=message.successful_payment.invoice_payload,
        telegram_payment_charge_id=message.successful_payment.telegram_payment_charge_id,
        provider_payment_charge_id=message.successful_payment.provider_payment_charge_id,
    )

    user = session.query(User).filter_by(id=message.successful_payment.invoice_payload).first()
    user.pay_in_mouth = True
    user.expired = datetime.datetime.now() + datetime.timedelta(days=30)

    session.add(success_transaction)
    session.add(user)
    session.commit()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
