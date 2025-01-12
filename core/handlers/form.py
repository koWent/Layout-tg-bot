from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm

async def get_form(message:Message,state:FSMContext):
    await message.answer(f"{message.from_user.first_name},давай знакомится.Введи своё имя")
    await state.set_state(StepsForm.GET_NAME)

async def get_name(message:Message,state:FSMContext):
    await message.answer(f"Приятно познакомится {message.text},теперь введи свою фамилию")
    await state.update_data(name=message.text)