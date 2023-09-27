from content import keyboards
from aiogram.dispatcher.storage import FSMContext


async def back(*args):
    if type(args[-1]) is FSMContext:
        await args[2].finish()

    await args[0].send_message(
        chat_id=args[1].chat.id,
        text="Выбери что то из меню блеа",
        reply_markup=keyboards["keyboard"]
    )

