from aiogram.types import Message
from aiogram import Bot


async def get_true_contact(message:Message,bot:Bot,phone:str):
    await message.answer(f"Ты отправил свой контакт {phone}")

async def get_fake_contact(message:Message,bot:Bot):
    await message.answer(f"Ты отправил не свой контакт")