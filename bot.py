import telebot
from parse import parse
from os.path import exists


TOKEN = '5565965300:AAFLvP7bCehp06PyWY8zNPUmTNAMGgINtjE'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Это бот, который показывает работу парсера")

@bot.message_handler(commands=['parse'])
def launch_parser(message):
    result=parse()
    for i in result.values():
        bot.send_message(message.chat.id, f'{list(i.values())[1]}-{list(i.values())[2]}')

@bot.message_handler(commands=['file'])
def send_file(message):
    chat_id = message.chat.id
    if exists('base.csv'):
        with open('base.csv') as f:
            bot.send_document(chat_id, f)
    else:
        bot.send_message(chat_id, 'Файл не сформирован. Используйте команду /parse для его формирования')

bot.polling()