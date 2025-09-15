from aiogram import types, Dispatcher, Bot, F, Router, filters

router = Router()

@router.message(filters.CommandStart())
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text="Відкрити сайт 🌐", 
                url="https://codeboulder.github.io/test_mini-app/"
            )]
        ]
    )

    await message.answer("Посилання ⬇️", reply_markup=markup)