"""Simple Telegram Bot example"""

import os
import re
import random
import telebot
from threading import Timer
from config import stickers_id


def send_random_sticker():
    rand_int = random.randint(0, len(stickers_id))
    random_sticker_id = stickers_id[rand_int]
    bot.send_sticker(chat_id, random_sticker_id)

def newTimer():
    global t
    t = Timer(3600.0, send_random_sticker)
newTimer()


## production 
BOT_TOKEN = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']

###### test bot
# BOT_TOKEN = "574632910:AAFWAN7buAcQe7MNsmu2VnQGCtFYJJh0Ewc"
# chat_id = 76016759

# initiat bot
bot = telebot.TeleBot(BOT_TOKEN)

# sticker for "наверное"
file_id = "CAACAgIAAx0CZ7OvuQACP45ij2-WhDPJX8fDzzizrxzz7iXV4AAC2hAAAuZ4kEoD72yHqENwoSQE"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Скажи триста")


## TODO: refactor with pattern matching with python 3.10
# one word check
@bot.message_handler(func=lambda m: len(m.text.split()) > 0) #, regexp="[^А-Яа-яa0-9]+")
def reply_one_word(message):
    # print('reset timer and start again')
    t.cancel()
    newTimer()
    t.start()
    # print("\n timer started")
    text = message.text + " "
    text_clean = re.sub('[^А-Яа-яa0-9]+', ' ', text)
    
    # bot replies
    # if any(val in text_clean.lower().split() for val in ["триста", "300"]):
    #     bot.reply_to(message, "отсоси у тракториста")
    
    if text_clean.lower().split()[-1] in ["триста", "300"]:
        bot.reply_to(message, "отсоси у тракториста")

    elif text_clean.lower().split()[-1] in ["да", "дa"]:
        bot.reply_to(message, "пизда")

    elif text_clean.lower().split()[-1] in ["нет", "нeт", "net"]:
        bot.reply_to(message, "пидора ответ")

    elif "наверно" in text_clean.lower().split() :
        bot.send_sticker(chat_id, file_id)
        # bot.reply_to(message, bot.send_sticker(chat_id, file_id))

    elif text_clean.lower().split()[-1] in ["получилось", 
                                            "получилась", 
                                            "случилось",
                                            "приключилось"
                                            ]:
        bot.reply_to(message, "рубаха в жопу засучилась")

    elif "сука" in text_clean.lower().split()[-1]:
        bot.reply_to(message, "хуюка")
    
    elif "где" in text_clean.lower().split()[-1]:
        bot.reply_to(message, "в пизде")

    elif text_clean.lower().split()[-1] in ["получается", 
                                            "кончается", 
                                            "начинается",
                                            "встречается",
                                            "продолжается",
                                            "повышается",
                                            "рассыпается",
                                            "закрывается",
                                            "сражается",
                                            "ошибается",
                                            "считается",
                                            "испугается"
                                            ]:
        bot.reply_to(message, "... и хуй стоит, и голова качается!")
    
    elif "мне" in ' '.join(text_clean.lower().split()[-1]):
            bot.reply_to(message, "... у тебя рука в говне")
        
    elif "питоне" in text_clean.lower():
        bot.reply_to(message, "петухоне...")

    elif "спасибо" in text_clean.lower():
        bot.reply_to(message, "спасибое")

    elif text_clean.lower().split()[-1] in ["пидор", "педик", "петух", "гей"]:
        bot.reply_to(message, "сам педик!")

    elif "юдин" in text_clean.lower().split():
        bot.reply_to(message, "Хуюдин")

    elif "светов" in text_clean.lower().split():
        bot.reply_to(message, "Хуетов")

    elif "кац" in text_clean.lower().split():
        bot.reply_to(message, "Хуяц")

    elif "шульман" in text_clean.lower().split():
        bot.reply_to(message, "Правильно говорить Хуюльман!")

    elif text_clean.lower().split()[-1] in ["ага", 
                                            "война"]:
        bot.reply_to(message, "хуйна")
    
    # check if there are more than one word in message 
    if len(text_clean.split()) > 1:
        if "дай мне" == ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "... у тебя рука в говне")
        
        elif "будь другом" == ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "насри кругом!")

        elif "у вас" == ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "А у нас в Японии три врача в пизду глядели -ничего не поняли")




# # set up timer for messages
# @bot.message_handler(func=lambda m: True)
# def send_refresh(message):
#     # print('reset timer and start again')
#     t.cancel()
#     newTimer()
#     t.start()
#     # print("\n timer started")

if __name__ == '__main__':
    bot.polling()