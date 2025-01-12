from aiogram import Bot
from aiogram.types import Message,LabeledPrice,PreCheckoutQuery,InlineKeyboardButton,InlineKeyboardMarkup,\
ShippingOption,ShippingQuery


keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оплатить заказ",
            pay=True
        )
    ],
    [
        InlineKeyboardButton(
            text="Ссылка",
            url="https://t.me/kowent"
        )
    ]
])

BY_SHIPPING = ShippingOption(
    id="by",
    title="Доставка в Беларусь",
    prices=[
        LabeledPrice(
            label="Доставка Белпочтой",
            amount=5000
        )
    ]
)

RU_SHIPPING = ShippingOption(
    id="ru",
    title="Доставка в Россию",
    prices=[
        LabeledPrice(
            label="Доствка Почтой России",
            amount=6000
        ),
        LabeledPrice(
            label="Доставка CDEK",
            amount=3000
        )
    ]
)

UA_SHIPPING = ShippingOption(
    id="ua",
    title="Доставка в Украину",
    prices=[
        LabeledPrice(
            label="Доставка Укрпочтой",
            amount=7000
        )
    ]
)

CITIES_SHIPPING = ShippingOption(
    id="capitals",
    title="Быстрая доставка в столицы СНГ",
    prices=[
        LabeledPrice(
            label="Доставка курьером Торрето",
            amount=2000
        )
    ]
)

async def shipping_check(shipping_query:ShippingQuery,bot:Bot):
    shipping_options = []
    countries = ["BY","RU","UA"]
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id,ok=False,
                                               error_message="В вашу страну не осуществляется доставка")
    if shipping_query.shipping_address.country_code == "BY":
        shipping_options.append(BY_SHIPPING)
    if shipping_query.shipping_address.country_code == "RU":
        shipping_options.append(RU_SHIPPING)
    if shipping_query.shipping_address.country_code == "UA":
        shipping_options.append(UA_SHIPPING)
    cities = ["Минск","Москва","Киев"]
    if shipping_query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)
    await bot.answer_shipping_query(shipping_query.id,ok=True,shipping_options=shipping_options)



async def order(message:Message,bot:Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка через Telegram",
        description="Учимся греть гоев через телеграм",
        payload="Ба бу беее ба бу биии",
        provider_token="1744374395:TEST:919aeb3eb9bd02fe6f4a",
        currency="rub",
        prices=[
            LabeledPrice(
                label="Доступ к приватке",
                amount=99000
            ),
            LabeledPrice(
                label="НДС",
                amount=20000
            ),
            LabeledPrice(
                label="Скидка",
                amount=-20000
            ),
            LabeledPrice(
                label="Бонус",
                amount=-40000
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000,2000,3000,4000],
        start_parameter="kowent",
        provider_data=None,
        photo_url="https://i.pinimg.com/736x/b7/d6/9f/b7d69fcf3c0415654eb839607ae3ffa9.jpg",
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        is_flexible=True,
        send_email_to_provider=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query:PreCheckoutQuery,bot:Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id,ok=True)


async def successful_payment(message:Message):
    msg = f"Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}."\
          f"\r\nнаш менеджер получил заявку и уже набирает Ваш номер телефона."\
          f"\r\nПока можете скачать цифровую версию нашего продукта https://t.me/kowent"
    await message.answer(msg)