import requests
import telebot
from telebot import apihelper
from parse import parse
import pprint
import os
import json


TOKEN = '5565965300:AAFLvP7bCehp06PyWY8zNPUmTNAMGgINtjE'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Это бот, который показывает работу парсера")

@bot.message_handler(commands=['launch'])
def launch_parser(message):
    bot.reply_to(message, parse())

bot.polling()