import random

from loader import dp
from aiogram.types import Message
import game


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}\n'
                             f'Мы будем играть в конфеты. Введи команду /max_count и максимальное количество конфет'
                             f'от 2 до 149, которое можно взять') 
                            
        my_game = [message.from_user.id, message.from_user.first_name, 150]
        game.total.append(my_game)


@dp.message_handler(commands=['max_count'])
async def max_take(message: Message):
    global max_count
    max_count = message.text.split()[1]
    if max_count.isdigit() and 2 < int(max_count) < 149:
        await message.answer(f' Бери от 1 до {max_count} конфет...')
    else:
        await message.answer(f'Введите число от 2 до 149')
        

@dp.message_handler()
async def mes_game(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            count = message.text
            if count.isdigit() and 0 < int(count) <= int(max_count):
                duel[2] -= int(count)
                if await check_win(message, 'Ты', duel):
                    return True
                await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n'
                                     f'Теперь ход бота...')
                bot_take = random.randint(1, 28) if duel[2] > 28 else duel[2]
                duel[2] -= bot_take
                if await check_win(message, 'Бот', duel):
                    return True
                await message.answer(f'Бот Виталий взял {bot_take} конфет и '
                                        f'на столе осталось {duel[2]}\n'
                                        f'Теперь твой ход...')
            else:
                await message.answer(f'Введите число от 1 до 28')
            
async def check_win(message: Message, win: str, duel: list):
    if duel[2] <= 0:
        await message.answer(f'{win} победил! Поздравляю!')
        game.total.remove(duel)
        return True
    return False



