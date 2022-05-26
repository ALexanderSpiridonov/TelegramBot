"""Simple Telegram Bot example"""

import os
import re
import telebot
# from config import BOT_TOKEN
BOT_TOKEN = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']
bot = telebot.TeleBot(BOT_TOKEN)

file_id = "CAACAgIAAx0CZ7OvuQACP45ij2-WhDPJX8fDzzizrxzz7iXV4AAC2hAAAuZ4kEoD72yHqENwoSQE"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Скажи триста")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text + " "
    text_clean = re.sub('[^А-Яа-яa0-9]+', ' ', text)
    if len(text_clean) > 0:
        if "триста" in text_clean.lower().split():
            bot.reply_to(message, "отсоси у тракториса")
        elif text_clean.lower().split()[-1] in ["да", "дa"]:
            bot.reply_to(message, "пизда")
        elif text_clean.lower().split()[-1] in ["нет", "нeт", "net"]:
            bot.reply_to(message, "пидора ответ")
        elif "наверно" in text_clean.lower().split() :
            bot.send_sticker(chat_id, file_id)
        
bot.polling()