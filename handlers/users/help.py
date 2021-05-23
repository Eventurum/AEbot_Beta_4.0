from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Данный бот находится в стадии разработки.\n\n",

            "Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/admins - Написать администраторам",
            "/menu - Сделать заказ")

    await message.answer("\n".join(text))
