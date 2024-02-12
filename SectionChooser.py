import math
import telebot
from text_parser import get_text

class SectionChooser():

    def __init__(self, bot, call, identity, number, additional_button_data, additional_button=False):
        # полученные переменные при создании экземпляра класса
        self.bot = bot
        self.call = call
        self.identity = identity
        self.page_numbers = number
        self.additional_data = additional_button_data
        self.additional_bool = additional_button
        # дополнительные переменные полученные из предыдущих переменных
        self.back_page = math.ceil(number/6)
        print(self.back_page, number, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id
        self.text = get_text(number, self.identity)
        self.url = list()
        self.text_url = list()
        if type(self.additional_data) == 'tuple':
            for i in self.additional_data:
                self.url.append(i[1])
                self.text_url.append(i[0])
        else:
            self.url = self.additional_data[1]
            self.text_url = self.additional_data[0]
        

    def create_buttons(self):
        next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        menu_buttons_generated = list()
        if self.additional_bool and type(self.url) != 'tuple' and type(self.text_url) != 'tuple':
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(self.text_url, url=self.url))
        else:
            for text, url in zip(self.text_url, self.url):
                menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text, url=url))

        menu_buttons_generated.append(telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data=f"{self.identity}_page{self.back_page}"))
        
            
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        for i in menu_buttons_generated:

            next_menu.add(i) 
         
        return next_menu

    def section_selector(self):
        
        self.bot.edit_message_text(
                                    self.text,
                                    self.chat_id,
                                    self.message_id,
                                    reply_markup=self.create_buttons()
                                    )