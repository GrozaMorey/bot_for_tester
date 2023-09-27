from content import keyboards


async def buy_subscribe(bot, message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Я скрыл клавиатуру если хочешь вернуться нажми назад 🔙",
        reply_markup=keyboards["menu_keyboard"]
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="Выбери насколько ты хочешь купить подписку",
        reply_markup=keyboards["Купить подписку 🤑"]
    )
