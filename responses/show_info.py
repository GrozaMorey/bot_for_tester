from models import session, User
from content import keyboards


async def show_info(bot, message):
    user = session.query(User).filter_by(username=message.from_user.username).first()

    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Оплачена ли подписка: {'Да' if user.pay_in_mouth else 'Нет'}\n"
             f" Действительна до {str(user.expired)}\n "
             f"Номер бейджика: {str(user.number_badge)}",
        reply_markup=keyboards["info_keyboard"]
    )
