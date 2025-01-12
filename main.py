from aiogram import Bot , Dispatcher, F
from aiogram.types import Message,ContentType
import asyncio
import logging
import asyncpg
from core.handlers.basic import get_start, get_pic, get_hello
from core.settings import settings
from aiogram.filters import Command  #,CommandStart
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact,get_true_contact
from core.utils.commands import set_commands
from core.handlers.basic import get_location
from core.handlers.basic import get_inline
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import order,pre_checkout_query,successful_payment,shipping_check
# from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
# from core.middlewares.dbmiddleware import DbSession
from core.handlers import form
from core.utils.statesform import StepsForm
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def start_bot(bot:Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id,text="Бот запущен!")


async def stop_bot(bot:Bot):
    await bot.send_message(settings.bots.admin_id,text="Бот остановлен!")


async def create_pool():
    return await asyncpg.create_pool(user="postgres.qjaivxfyumbdyionolty",password="0kjTy5xZ07eHeQAZ",database="users",
                                     host="aws-0-eu-central-1.pooler.supabase.com",port=5432,command_timeout=10)


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token)
    pool_connect = await create_pool()


    dp = Dispatcher()
    # dp.update.middleware.register(DbSession(pool_connect))
    # dp.message.middleware.register(CounterMiddleware())
    dp.update.middleware.register(OfficeHoursMiddleware())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(form.get_form,Command(commands="form"))
    dp.message.register(form.get_name,StepsForm.GET_NAME)
    dp.message.register(order, Command(commands="pay"))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment)
    dp.shipping_query.register(shipping_check)
    dp.message.register(get_inline, Command(commands="inline"))
    dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.message.register(get_location,F.location)
    dp.message.register(get_hello, F.text == "Привет")
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_pic,F.photo)
    dp.message.register(get_start,Command(commands=["start","run"])) #можно использовать CommandStart


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close() #Await — это ключевое слово, которое используется в асинхронных функциях для того,
                                  # чтобы указать, что здесь необходимо дождаться завершения промиса


if __name__ == "__main__":
    asyncio.run(start())