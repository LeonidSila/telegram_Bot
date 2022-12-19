from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup
from data_base import sqlite_db
import aiogram, telebot
from aiogram.dispatcher import FSMContext



my_chat_id = '-1001813095954'


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_id, 'Давай смотреть!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/@ysait_bot')
    

# @dp.message_handler(commands=['Режим_работы'])
async def my_open_sait(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 10:00 до 18:00c\nВ ВЫХОДНЫЕ Я ОТДЫХАЮ\nно могу ответить)))))')

# @dp.message_handler(commands=['Предварительная_информация'])
async def my_info_sait(message : types.Message):
    await bot.send_message(message.from_user.id, 'Маркетолог, программист - Ваш выбор!\nДанные бот написан на Python!\nКаждую неделю, я что то добавляю! ')
    
# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands=['Написать_мне)'])
async def mysms_tomy(message : types.Message):
    callback_query_id = message.from_user.id
    await bot.send_message(message.from_user.id, 'Прошу Вас сообрать все мысли в одном сообщении!\nБот отправит мне увидомление о вашем сообщении\n****** https://t.me/MYsmsTomY *****')
    await message.reply('Обратите внимание на то, что нужно нажать на ссылку!')
    user_input = input('')
    user_input.bot.send_message(chat_id=my_chat_id, text=message.text)
  
# @dp.message_handler(content_type = 'text')
# async def send_msg(message: types.Message):
#     await bot.send_message(message.my_chat_id, message.text,reply_markup = markup)


def register_handlers_client (dp : Dispatcher):
    dp.register_message_handler(mysms_tomy, commands=['Связаться'])
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(my_open_sait, commands=['Режим_работы'])
    dp.register_message_handler(my_info_sait, commands=['Предварительная_информация'])
    dp.register_message_handler(pizza_menu_command, commands=['Мои_сертификаты'])
    # dp.register_message_handler(send_msg, content_types=['Связаться'])
    