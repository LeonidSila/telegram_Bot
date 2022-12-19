from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton#, ReplyKeyboardRemove


b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Предварительная_информация')
b3 = KeyboardButton('/Мои_сертификаты')
b4 = KeyboardButton('/Поделиться номером', request_contact=True)
b5 = KeyboardButton('/Отправить где я', request_location=True)
b6 = KeyboardButton('/Связаться')

# b7 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Hello", callback_data='www'))

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # one_time_keyboard=True - Одноразовасть клавиатуры
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client.add(b1).add(b2).insert(b3,b4,b5,b6) #№add добавляет с новой строчки, а insert с свободное место
# kb_client.row(b1, b2, b3) #Просто добавляет кнопки

kb_client.add(b1).add(b2).add(b3).row(b4,b5,b6)#.add(b7)
