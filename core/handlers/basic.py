from aiogram import Bot
from aiogram.types import Message
import json
# from core.keyboards.reply import reply_keyboard,loc_tel_poll_keyboard,get_reply_keyboard
from core.keyboards.inline import select_macbook,get_inline_keyboard
# from core.utils.dbconnect import Request


async def get_start(message:Message,counter:str):
    await message.answer(f"Сообщение №{counter}")
    await message.answer(f"Привет {message.from_user.first_name},рад тебя видеть!",
                         reply_markup=get_inline_keyboard())

async def get_location(message:Message,bot:Bot):
    await message.answer(f"Ты отправил свою локацию\r\a"
                         f"{message.location.latitude}\r\n{message.location.latitude}")


async def get_pic(message:Message,bot:Bot):
    await message.answer(f"Отлично,ты отправил какую-то хуйню,я сохраню её")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path,'photo.jpg')

async def get_hello (message:Message,bot:Bot):
    await message.answer(f"Привет {message.from_user.first_name},я бот от Kowent`а")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)

async def get_inline(message:Message,bot:Bot):
    await message.answer(f"Привет {message.from_user.first_name}.Показываю инлайн кнопки",
                         reply_markup=select_macbook)
