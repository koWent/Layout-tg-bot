from aiogram import Bot
from aiogram.types import BotCommand,BotCommandScopeDefault


async def set_commands(bot:Bot):
    commands = [
        BotCommand(
            command="start",
            description="Начало работы"
        ),
        BotCommand(
            command="help",
            description="Помощь"
        ),
        BotCommand(
            command="cancel",
            description="Сбросить"
        ),
        BotCommand(
            command="inline",
            description="Инлайн клавиатура"
        ),
        BotCommand(
            command="pay",
            description="Оплата через телеграм"
        ),
        BotCommand(
            command="form",
            description="Заполнить форму"
        )
    ]

    await bot.set_my_commands(commands,BotCommandScopeDefault())