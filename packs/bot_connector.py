import telebot
from telebot import types

TOKEN = ""
PARSE_MODE = 'HTML'

bot = telebot.TeleBot(TOKEN, parse_mode=PARSE_MODE)
