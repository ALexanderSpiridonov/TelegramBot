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

# one word check
@bot.message_handler(func=lambda m: len(m.text.split()) > 0) #, regexp="[^А-Яа-яa0-9]+")
def reply_one_word(message):
    text = message.text + " "
    text_clean = re.sub('[^А-Яа-яa0-9]+', ' ', text)
    
    # bot replies
    if any(val in text_clean.lower().split() for val in ["триста", "300"]):
        bot.reply_to(message, "отсоси у тракториста")

    elif text_clean.lower().split()[-1] in ["да", "дa"]:
        bot.reply_to(message, "пизда")

    elif text_clean.lower().split()[-1] in ["нет", "нeт", "net"]:
        bot.reply_to(message, "пидора ответ")

    elif "наверно" in text_clean.lower().split() :
        bot.reply_to(message, bot.send_sticker(chat_id, file_id))

    elif "получилось" in text_clean.lower().split()[-1]:
        bot.reply_to(message, "рубаха в жопу засучилась")

    elif "получается" in text_clean.lower().split()[-1]:
        bot.reply_to(message, "... и хуй стоит, и голова качается!")
    
    elif "мне" in ' '.join(text_clean.lower().split()[-1]):
            bot.reply_to(message, "... у тебя рука в говне")
        
    elif "питоне" in text_clean.lower():
        bot.reply_to(message, "петухоне...")

    elif "пидор" in ' '.join(text_clean.lower().split()[-1]):
        bot.reply_to(message, "сам ты пидор")

    elif "юдин" in ' '.join(text_clean.lower()):
        bot.reply_to(message, "Хуюдин")

    elif "шульман" in ' '.join(text_clean.lower()):
        bot.reply_to(message, "Правильно говорить Хуюльман!")

    elif "ага" in ' '.join(text_clean.lower().split()[-1]):
        bot.reply_to(message, "хуйна")
    

    # check if there are more than one word in message 
    if len(text_clean.split()) > 1:
        if "дай мне" in ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "... у тебя рука в говне")
        
        elif "будь другом" in ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "насри кругом!")
    
bot.polling()