import math
import telebot
from text_parser import get_text

class SectionChooser():

    def __init__(self, bot, call, parent, section, number, additional_button_data, address_tree, recursive_parent=None, additional_button=False):
        
        """"""
        
        # полученные переменные при создании экземпляра класса
        self.bot = bot
        self.call = call
        self.page_numbers = number
        self.additional_data = additional_button_data
        self.additional_bool = additional_button
        self.tree = address_tree
        self.parent = parent
        self.recursive_parent = recursive_parent
        self.section = section
        self.number = number
        
        # дополнительные переменные полученные из предыдущих переменных
        self.back_page = math.ceil((number+1)/6)
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id
        self.text = get_text(number, self.parent if self.recursive_parent == None else self.recursive_parent)
        self.url = list()
        self.text_url = list()
        if isinstance(self.additional_data[0], tuple):
            for i in self.additional_data:
                
                self.url.append(i[1]) # ИЗМЕНИТЬ ПРОВЕРКУ НА ТИП ДАННЫХ, ИНАЧЕ ПРИ НЕПРАВИЛЬНО ВВЕДЕНЫХ ДАННЫХ
                                      # ВСЕ ПОЙДЕТ ПО ПИЗДЕ
                self.text_url.append(i[0])
        else:
            self.url = self.additional_data[1]
            self.text_url = self.additional_data[0]
        
    def get_menu_buttons(self, menu_buttons_generated):
        
        """"""

        if self.additional_bool and not isinstance(self.text_url, list) and not isinstance(self.url, list):
            
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(self.text_url, url=self.url))
        else:
            for text, url in zip(self.text_url, self.url):
                
                menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text, url=url))
        return menu_buttons_generated

    def add_buttons(self, menu_buttons_generated, next_menu):
        
        """"""
        
        for i in menu_buttons_generated:

            next_menu.add(i)
        return next_menu
        
    def create_buttons(self):
        
        """"""

        next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
        menu_buttons_generated = self.get_menu_buttons(list())
        coun = (self.tree).count('')
        call_back_data = f"{self.parent}``{self.back_page}" if self.parent == self.tree[1:] else f"{self.parent}{self.tree}``{self.back_page}"
        
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data=call_back_data)) 
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        
        next_menu = self.add_buttons(menu_buttons_generated, next_menu) 
        
        return next_menu
        
    def section_selector(self):
        
        """"""

        self.bot.edit_message_text(
                                    self.text,
                                    self.chat_id,
                                    self.message_id,
                                    reply_markup=self.create_buttons()
                                    )