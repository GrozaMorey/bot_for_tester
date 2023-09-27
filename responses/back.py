from content import keyboards


async def back(bot, message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Выбери что то из меню блеа",
        reply_markup=keyboards["keyboard"]
    )
