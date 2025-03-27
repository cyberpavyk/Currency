from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



values = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Получить курс💱', callback_data='get_cot'),
     InlineKeyboardButton(text='Калькулятор валют⚙️', callback_data='calc')]
])





values_end = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Получить актуальный курс💱',callback_data='get_cot')],
    [
        InlineKeyboardButton(text='В главное меню',callback_data='back_to_main')
    ]
])




platforms = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Investing", callback_data='investing'),
        InlineKeyboardButton(text="XE", callback_data='xe')
    ],
    [
        InlineKeyboardButton(text="ЦБ", callback_data='cb'),
        InlineKeyboardButton(text="ABCEX", callback_data='abcex')
    ],
    [
        InlineKeyboardButton(text='На главное меню', callback_data='back_to_main')
    ]
])




xe_couples = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text="CNY/USD", callback_data='xe_cny_usd'),
        InlineKeyboardButton(text="EUR/USD", callback_data='xe_eur_usd')
        ],
        
        [
            InlineKeyboardButton(text="USD/RUB", callback_data='xe_rub_usd'),
            InlineKeyboardButton(text="EUR/RUB", callback_data='xe_eur_rub'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_to_plat')
        ]

        ])

cb_couples = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text="USD/RUB", callback_data='cb_usd_rub'),
        InlineKeyboardButton(text="CNY/RUB", callback_data='cb_cny_rub')
        ],
        
        [
            InlineKeyboardButton(text="EUR/RUB", callback_data='cb_eur_rub') 
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_to_plat')
        ]

        ])



investing_couples = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="USD/RUB", callback_data='inv_usd_rub') 
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_to_plat')
        ]

        ])


abcex_couples = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="USDT/RUB", callback_data='abcex_usdt_rub') 
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_to_plat')
        ]
        ])







exit_inv =  InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='back_to_inv'),
    ]
])


exit_cb =  InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='back_to_cb'),
    ]
])





exit_xe =  InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='back_to_xe'),
    ]
])


exit_abcex =  InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='back_to_abcex'),
    ]
])




back_to_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='На главное меню', callback_data='back_to_main')
    ]
])