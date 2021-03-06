"""Royzman replyes Telegram Bot example"""

import os
import re
import random
import telebot
from threading import Timer
from config import stickers_id, today_reply, putin_reply


def send_random_sticker():
    rand_int = random.randint(0, len(stickers_id)-1)
    random_sticker_id = stickers_id[rand_int]
    bot.send_sticker(chat_id, random_sticker_id)

def send_today_reply(chat_id):
    # print(len(today_reply))
    rand_int = random.randint(0, len(today_reply)-1)
    random_reply = today_reply[rand_int]
    bot.send_message(chat_id, random_reply)

def send_putin_reply():
    rand_int = random.randint(0, len(today_reply)-1)
    random_reply = putin_reply[rand_int]
    bot.send_message(chat_id, random_reply)

def timer_action():
    # send_today_reply(chat_id=chat_id)
    send_putin_reply()
    send_random_sticker()

def newTimer():
    global t
    t = Timer(3600.0, timer_action)
newTimer()


## production 
BOT_TOKEN = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']

# initiat bot
bot = telebot.TeleBot(BOT_TOKEN)

# # sticker for "наверное"
# file_id = "CAACAgIAAx0CZ7OvuQACP45ij2-WhDPJX8fDzzizrxzz7iXV4AAC2hAAAuZ4kEoD72yHqENwoSQE"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Скажи триста")

@bot.message_handler(commands=['хуй', 'sticker'])
def send_sticker(message):
    send_random_sticker()

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
    
    ####  bot replies
    if len(text_clean.split()) > 0:
        
        # if any(val in text_clean.lower().split() for val in ["триста", "300"]):
        #     bot.reply_to(message, "отсоси у тракториста")

        if text_clean.lower().split()[-1] in ["триста", "300", "зоо"]:
            bot.reply_to(message, "отсоси у тракториста")

        elif text_clean.lower().split()[-1] in ["aaa", "ааа"]:
            bot.reply_to(message, "хуйна")

        # elif text_clean.lower().split()[-1] in ["да", "дa"]:
        #     bot.reply_to(message, "пизда")

        elif "путин" in text_clean.lower().split():
            send_putin_reply()

        elif text_clean.lower().split()[-1] in ["нет", "нeт", "net"]:
            bot.reply_to(message, "пидора ответ")

        # elif "наверно" in text_clean.lower().split() :
        #     bot.send_sticker(chat_id, file_id)
        #     # bot.reply_to(message, bot.send_sticker(chat_id, file_id))

        elif text_clean.lower().split()[-1] in ["получилось", 
                                                "получилась", 
                                                "случилось",
                                                "приключилось"
                                                ]:
            bot.reply_to(message, "... рубаха в жопу засучилась")

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

        elif text_clean.lower().split()[-1] in ["ну"]:
            bot.reply_to(message, "хуй гну ...")
        
        elif "мне" in ' '.join(text_clean.lower().split()[-1]):
            bot.reply_to(message, "... у тебя рука в говне")
            
        elif "питоне" in text_clean.lower():
            bot.reply_to(message, "петухоне...")

        # elif text_clean.lower().split()[-1][-1] == "о":
        #     bot.reply_to(message, text_clean.lower().split()[-1] + "е")
        #     send_random_sticker()

        elif text_clean.lower().split()[-1] in ["пидор", "педик", "петух", "гей"]:
            bot.reply_to(message, f"сам {text_clean.lower().split()[-1]}!")

        elif "юдин" in text_clean.lower().split():
            bot.reply_to(message, "Хуюдин")

        elif "светов" in text_clean.lower().split():
            bot.reply_to(message, "Хуетов")

        elif "кац" in text_clean.lower().split():
            bot.reply_to(message, "Хуяц")

        elif "шульман" in text_clean.lower().split():
            bot.reply_to(message, "Правильно говорить Хуюльман!")

        elif text_clean.lower().split()[-1] in ["ага"]:
            bot.reply_to(message, "хуерга")

        elif text_clean.lower().split()[-1] in ["война"]:
            bot.reply_to(message, "хуйна")

        elif text_clean.lower().split()[-1] in ["мне"]:
            bot.reply_to(message, "... у тебя рука в говне")

        elif text_clean.lower().split()[-1] in ["ладно"]:
            bot.reply_to(message, "у тебя в трусах прохладно ...")

        if "сегодня" in text_clean.lower().split():
            send_today_reply(chat_id = message.chat.id)
        
    # check if there are more than one word in message 
    if len(text_clean.split()) > 1:
        # if "дай мне" == ' '.join(text_clean.lower().split()[-2:]):
        #     bot.reply_to(message, "... у тебя рука в говне")
        
        if "будь другом" == ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "насри кругом!")

        elif "у вас" == ' '.join(text_clean.lower().split()[-2:]):
            bot.reply_to(message, "А у нас в Японии три врача в пизду глядели - ничего не поняли")


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