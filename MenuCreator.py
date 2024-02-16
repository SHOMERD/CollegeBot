# coding=utf-8 

import math
import telebot
from tbot import current_time


class Menu():
    
    def __init__(self, bot, call, pages, section, page, tree, parent):
        self.bot = bot
        self.call = call
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id
        self.section = section
        self.pages = pages
        self.number_in_sqare = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        self.buttons_text = self.pages[1]
        self.buttons_callback = self.pages[0]
        self.generated_buttons = []
        self.next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        self.bot = bot
        self.page = page
        self.tree = tree
        self.parent = parent
        
        self.recursion_button = False
        self.personality = {'Stud': 'Студента\Родителя', 
                            'Sotr':'Сотрудника\Преподавателя', 
                            'Abitur':'Абитуриента\Родителя абитуриента'}
    
    def sliding_window_listing(self, menu_page, menu, right_border = 6, left_border = 0):
        
        """"""

        for i in range(self.page):
            menu_page.append(menu[left_border:right_border])
            right_border += 6
            left_border += 6
    
    def create_buttons(self, menu):
        for text, callback in zip(self.buttons_text, self.buttons_callback):

            # ВНИМАНИЕ, ЕСЛИ ТЕКСТ КОЛЛБЕКА > 64 БАЙТ ТО ВЫДАСТ ОШИБКУ
            # ЛУЧШЕ ИСПОЛЬЗОВАТЬ АНГЛИЙСКИЕ СИМВОЛЫ, ТАК КАК ОНИ ИСПОЛЬЗУЮТ 1 БАЙТ НА СИМВОЛ
            # В ТО ВРЕМЯ КАК РУССКИЕ ПО 2 БАЙТА НА СИМВОЛ
            

            gggg = f'{self.parent}_{callback}' if self.parent == self.section else f'{self.parent}_{self.section}_{callback}'
            
            
            # расскоментируй строку с принтом если надо проверить коллбек, тип данных коллбека, вес коллбека
            # print(gggg, type(gggg), len(gggg.encode("utf8")), len(self.identity.encode("utf8")), len(callback.encode("utf8")))
            menu.append(telebot.types.InlineKeyboardButton(text, callback_data=gggg))
    
    def create_pages(self, min_page, max_page, menu_page):
        
        menu_buttons_pages_generated = [v for i,v in enumerate(menu_page[self.page-1]) if i <= 5]
        
        shablon = f'{self.section}' if self.parent == self.section else f'{self.parent}{self.tree}{self.section}'
        
        if self.page == min_page:
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{shablon}``{self.page + 1}'))    
        elif self.page == max_page:
            
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{shablon}``{self.page - 1}'))
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data=f'{shablon}``{min_page}'))
        else:
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{shablon}``{self.page + 1}'))
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{shablon}``{self.page - 1}'))
            
                    
        menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))

    def add_buttons_to_keyboard(self, menu_buttons_pages_generated):
        for i in menu_buttons_pages_generated:
            
            self.next_menu.add(i)
        
    def choose_description(self):
        if self.personality.get(self.section) != None:
            self.recursion_button = True
        
        if self.recursion_button:
            text = f'Меню для {self.personality.get(self.parent)}' if self.personality.get(self.parent) != None else ''
        else:
            text = ''
        return text

    def pager(self):
        
        menu = self.create_buttons(list())
        
        menu_len = len(menu)
        max_page = math.ceil(menu_len / 6)
        min_page = 1
        
        menu_page = self.sliding_window_listing(list(), menu, right_border=6, left_border=0)

        menu_buttons_pages_generated = self.create_pages(min_page, max_page, menu_page)

        self.add_buttons_to_keyboard(menu_buttons_pages_generated)
        
        return self.next_menu        

    def bot_menu_pager(self): 
        
        text = self.choose_descriptions()

        menu = self.pager()
        
        self.bot.edit_message_text(f'{text}\nСтраница номер: {self.number_in_sqare[self.page-1]}',
                              self.chat_id,
                              self.message_id,
                              reply_markup=menu)

    