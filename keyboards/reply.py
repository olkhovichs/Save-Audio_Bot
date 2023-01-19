from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

def start():
    button_audio = KeyboardButton('Скачать аудиосообщения от пользователя')
    buton_photo = KeyboardButton('Распознать лицо на фото')
    markup_reply = ReplyKeyboardMarkup().row(button_audio, buton_photo)
    return markup_reply
