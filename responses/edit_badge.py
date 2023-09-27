from stages import EditBadge
from models import session, User
from content import keyboards
import datetime

async def edit_badge_stage_1(bot, message):
    await EditBadge.waiting_for_number_badge.set()

    await bot.send_message(
        chat_id=message.chat.id,
        text="Введите новый номер бейджика",
    )


async def edit_badge_stage_2(bot, message, state):
    user = session.query(User).filter_by(username=message.from_user.username).first()

    user.number_badge = int(message.text)
    user.update_badge = datetime.datetime.now() + datetime.timedelta(days=30)

    session.add(user)
    session.commit()

    await state.finish()

    await bot.send_message(
        chat_id=message.chat.id,
        text="Данные успешно изменены",
        reply_markup=keyboards["info_keyboard"],
    )
