from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
import asyncio

from python_code import basic_func

async def main():
    bot = Bot(
        token="8430300206:AAFsJdfVubx80QRjQ-z1P7SmYut3YKGEiE8",
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(basic_func.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())