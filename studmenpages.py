# coding=utf-8 

import math
import telebot
from tbot import current_time


class Menu():
    
    def __init__(self, bot, call, pages, identity, page):
        self.bot = bot
        self.call = call
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id
        self.identity = identity
        self.pages = pages
        self.number_in_sqare = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        self.buttons_text = self.pages[1]
        self.buttons_callback = self.pages[0]
        self.generated_buttons = []
        self.next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        self.bot = bot
        self.page = page
        
    def pager(self):
        print(self.pages[1])
        menu = list()
        for text, callback in zip(self.buttons_text, self.buttons_callback):

            # ВНИМАНИЕ, ЕСЛИ ТЕКСТ КОЛЛБЕКА > 64 БАЙТ ТО ВЫДАСТ ОШИБКУ
            # ЛУЧШЕ ИСПОЛЬЗОВАТЬ АНГЛИЙСКИЕ СИМВОЛЫ, ТАК КАК ОНИ ИСПОЛЬЗУЮТ 1 БАЙТ НА СИМВОЛ
            # В ТО ВРЕМЯ КАК РУССКИЕ ПО 2 БАЙТА НА СИМВОЛ

            gggg = self.identity+'_'+callback 
            # расскоментируй строку с принтом если надо проверить коллбек, тип данных коллбека,
            # вес маркера идентификации (self.identity), и вес коллбека
            # print(gggg, type(gggg), len(gggg.encode("utf8")), len(self.identity.encode("utf8")), len(callback.encode("utf8")))
            menu.append(telebot.types.InlineKeyboardButton(text, callback_data=gggg))
        
        
        
        menu_len = len(menu)
        max_page = math.ceil(menu_len / 6)
        min_page = 1
        right_border = 6
        left_border = 0
        menu_page = []
        page = self.page
        for i in range(self.page):
            menu_page.append(menu[left_border:right_border])
            right_border += 6
            left_border += 6
                
        
        
        menu_buttons_generated = [v for i,v in enumerate(menu_page[self.page-1]) if i <= 5]
        
        if self.page == min_page:
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{self.identity}_page{self.page + 1}'))    
        elif self.page == max_page:
            
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{self.identity}_page{self.page - 1}'))
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data=f'{self.identity}_page{min_page}'))
        else:
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{self.identity}_page{self.page + 1}'))
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{self.identity}_page{self.page - 1}'))
            
                    
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        for i in menu_buttons_generated:
            
            self.next_menu.add(i)
        
        return self.next_menu        

    def bot_menu_pager(self): 
        
        personality = {'Stud': 'Студента\Родителя', 'Sotr':'Сотрудника\Преподавателя', 'Abitur':'Абитуриента\Родителя абитуриента'}
        
        menu = self.pager()
        
        self.bot.edit_message_text(f'Меню для {personality.get(self.identity)}\nСтраница номер: {self.number_in_sqare[self.page-1]}',
                              self.chat_id,
                              self.message_id,
                              reply_markup=menu)

    def menu_recurtion(self):
        pass