# coding=utf-8 
from datetime import datetime, timedelta
import telebot

bot = telebot.TeleBot("6269939624:AAGAv4FO_FD5JvfRlSSWPiednZXPesUbZhU")

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time






