"""
Author: Morteza Maleki
github: Python More!
"""

import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    # Create the menu options
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(types.KeyboardButton('Option 1'))
    menu.add(types.KeyboardButton('Option 2'))
    menu.add(types.KeyboardButton('Option 3'))

    # Send the menu to the user
    bot.reply_to(message, "Welcome to the menu example.", reply_markup=menu)

@bot.message_handler(func=lambda message: True)
def handle_menu_selection(message):
    response = ''
    bot.reply_to(message, response)

bot.polling()
