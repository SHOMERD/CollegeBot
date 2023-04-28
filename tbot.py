# coding=utf-8 
from datetime import datetime, timedelta
import telebot

bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

now = datetime.now() + timedelta(hours=4)
current_time = now.strftime("%H:%M:%S") 






