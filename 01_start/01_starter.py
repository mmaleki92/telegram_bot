"""
Author: Morteza Maleki
github: Python More!
"""

import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(message, "Welcome to the menu example.")

@bot.message_handler(func=lambda message: True)
def handle_menu_selection(message):
    response = ''
    bot.reply_to(message, response)

bot.polling()
