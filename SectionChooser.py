import telebot
from text_parser import get_text

class SectionChooser():

    def __init__(self, bot, call, identity, number, additional_button=False):
        self.bot = bot
        self.additional_button = additional_button
        self.text = get_text(number)
        self.call = call
        self.identity = identity
        self.page_numbers = number

    def section(self, url, text_url):
        next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        menu_buttons_generated = list()
        if self.additional_button:
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton('', url=''))
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1"))
        #telebot.types.InlineKeyboardButton('Заказать справку', url="https://opencollege-nsk.ru/live/#extract")
            
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        next_menu.add()  
        return next_menu