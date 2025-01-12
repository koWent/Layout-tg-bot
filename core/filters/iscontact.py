from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsTrueContact(BaseFilter):
    async def __call__(self,message:Message) -> bool:
        if message.contact.user_id == message.from_user.id:
            return {"Телефон":message.contact.phone_number}
        else:
            return False