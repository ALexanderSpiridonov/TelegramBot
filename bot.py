import re
import telebot
from config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Скажи триста")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text + " "
    text_clean = re.sub('[^А-Яа-яa0-9]+', ' ', text)
    if "триста" in text.lower().split():
        bot.reply_to(message, "отсоси у тракториса")
    elif text.lower().split()[-1] in ["да", "дa"]:
        bot.reply_to(message, "пизда")
    elif text.lower().split()[-1] in ["нет", "нeт", "net"]:
        bot.reply_to(message, "пидора ответ")
        
bot.polling()