import re
import telebot
from config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

# {
# "width":512,
# "height":394,
# "emoji":"\ud83e\udd14",
# "set_name":"omgitiscooleststickersintheworld",
# "is_animated":false,
# "is_video":false,
# "thumb":{
#           "file_id":"AAMCAgADHQJns6-5AAI_jmKPb5aEM8lfx8PPOLOvHPPuJdXgAALaEAAC5niQSgPvbIeoQ3ChAQAHbQADJAQ",
#           "file_unique_id":"AQAD2hAAAuZ4kEpy",
#           "file_size":10766,"width":320,"height":246},
#           "file_id":"CAACAgIAAx0CZ7OvuQACP45ij2-WhDPJX8fDzzizrxzz7iXV4AAC2hAAAuZ4kEoD72yHqENwoSQE",
#           "file_unique_id":"AgAD2hAAAuZ4kEo",
#           "file_size":16910
#           }
# }}]}
chat_id = -1001739829177
file_id = "CAACAgIAAx0CZ7OvuQACP45ij2-WhDPJX8fDzzizrxzz7iXV4AAC2hAAAuZ4kEoD72yHqENwoSQE"

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
    elif "наверно" in text_clean.lower().split() :
        bot.send_sticker(chat_id, file_id)
        
bot.polling()