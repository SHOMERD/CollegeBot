# coding=utf-8 
from datetime import datetime, timedelta
import telebot

bot = telebot.TeleBot("")

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time






