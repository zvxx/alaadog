import telebot

import requests

bot = telebot.TeleBot("6101233775:AAG3gIndRflLusMmajpYCxyEQY_SDsWB5RA")

# Define the inline keyboard

keyboard = telebot.types.InlineKeyboardMarkup()

url_button2 = telebot.types.InlineKeyboardButton(text='المبرمج', url='https://HH_KK.t.me')

keyboard.add(url_button2)

@bot.message_handler(commands=['start'])

def start_command(message):

    bot.reply_to(message, "اسئلني اي شيء و سأرد عليك .", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)

def chat(message):

    text = message.text

    r = requests.get(f"https://gptzaid.zaidbot.repl.co/1/text={text}").text

    bot.reply_to(message , r)

bot.polling()
