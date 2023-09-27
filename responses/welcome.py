from models import session, User
from content import keyboards

async def welcome(bot, message):
    print("sdsd")
    user = session.query(User).filter_by(username=message.from_user.username).first()
    if not user:
        user = User(username=message.from_user.username, chat_id=message.chat.id)
        session.add(user)
        session.commit()

    elif not user.chat_id:
        user.chat_id = message.chat.id
        session.add(user)
        session.commit()

    await bot.send_message(user.chat_id,
                           text=f"Добро пожаловать {message.from_user.first_name}👋 !\n\n Что бы продолжить нажми на одну из кнопок в меню",
                           reply_markup=keyboards["keyboard"]
                           )