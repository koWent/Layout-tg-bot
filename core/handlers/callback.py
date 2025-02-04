from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callbackdata import MacInfo


# async def select_macbook(call:CallbackQuery,bot:Bot):
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[2]
#     chip = call.data.split('_')[3]
#     year = call.data.split('_')[4]
#     answer = f'{call.message.from_user.first_name}, ты выбрал Apple Macbook {model}, с диаганалью экрана'\
#     f'{size} дюймов, на чипе {chip} {year} года.'
#     await call.message.answer(answer)
#     await call.answer()

async def select_macbook(call:CallbackQuery,bot:Bot, callback_data: MacInfo):
    model = callback_data.model
    size = callback_data.size
    chip = callback_data.model
    year = callback_data.year
    answer = f'{call.message.from_user.first_name}, ты выбрал Apple Macbook {model}, с диаганалью экрана'\
    f'{size} дюймов, на чипе {chip} {year} года.'
    await call.message.answer(answer)
    await call.answer()