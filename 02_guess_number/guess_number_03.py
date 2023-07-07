"""
Author: Morteza Maleki
github: Python More!
"""

import random
import telebot

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

secret_number = random.randint(1, 100)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the number guessing game! Try to guess the secret number between 1 and 100.")

@bot.message_handler(func=lambda message: 'hint' in message.text.lower())
def send_hint(message):
    hint = "The secret number is between 1 and 100."
    bot.reply_to(message, hint)

@bot.message_handler(func=lambda message: 'guess' in message.text.lower())
def prompt_guess(message):
    prompt = "Enter your guess:"
    bot.reply_to(message, prompt)

@bot.message_handler(func=lambda message: True)
def guess_number(message):
    try:
        guess = int(message.text)
        if guess == secret_number:
            response = "Congratulations! You guessed the correct number."
        elif guess < secret_number:
            response = "Try a higher number."
        else:
            response = "Try a lower number."
    except ValueError:
        response = "Please enter a valid number."

    bot.reply_to(message, response)

bot.polling()
