from handlers import dp
from aiogram import executor

async def on_start(_):
    print('Бот запущен')
    # await dp.bot.send_message(message.from_user.id, f'К чату присоединился {message.from_user.full_name}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)