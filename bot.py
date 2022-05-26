import re
import telebot
from config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)
chat_id = -1001739829177
file_id = "AQAD2hAAAuZ4kEpy"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Скажи триста")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text + " "
    text_clean = re.sub('[^А-Яа-яa0-9]+', ' ', text)
    if "триста" in text_clean.lower().split():
        bot.reply_to(message, "отсоси у тракториса")
    elif text_clean.lower().split()[-1] in ["да", "дa"]:
        bot.reply_to(message, "пизда")
    elif text_clean.lower().split()[-1] in ["нет", "нeт", "net"]:
        bot.reply_to(message, "пидора ответ")
    elif text_clean.lower().split() in ["наверно"]:
        bot.reply_to(message, "наверное!")
        bot.reply_to(message, bot.send_sticker(chat_id, file_id))
        
bot.polling()