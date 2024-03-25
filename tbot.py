# coding=utf-8 
import os
import math
import json
import telebot
from datetime import datetime, timedelta
from dotenv import load_dotenv
from typing import Any, NoReturn

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time



class info():
    
    def __init__(self, callback: str):

        with open('settings.json', 'r') as file:
            data = json.load(file)
        
        self.callback = callback

        self.parent: str = data[callback]['Parent']
        self.text: str = data[callback]['Text']
        self.buttons: Any = data[callback]['Buttons']
        self.urlButtons = data[callback]['urlButtons']

        self.callbacks = tuple(data[callback]['Buttons'].keys()) if self.buttons is not None else None
        self.names = tuple(data[callback]['Buttons'].values()) if self.buttons is not None else None

        self.number = list(data[self.parent]['Buttons'].keys()).index(callback) if self.parent != None else 0
        self.page = math.ceil((self.number+1)/6)



