from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from read import read_token
import logging

# level log
logging.basicConfig(level=logging.INFO)


# login bot
bot = Bot(token=read_token('config/config.json'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# start
if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
