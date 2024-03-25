# coding=utf-8 

import math
from typing import Any, NoReturn
import telebot
from tbot import current_time


class Menu():
    
    def __init__(self, bot, call, info, wanted_page):
        self.bot: Any = bot
        self.call: Any = call
        self.chat_id: int = call.message.chat.id
        self.message_id: int = call.message.message_id
        
        self.number_in_sqare: tuple = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        
        
        self.generated_buttons: list = list()
        self.next_menu: Any = telebot.types.InlineKeyboardMarkup(row_width=1)
        self.page: int = int(wanted_page)
        
        self.info = info
        self.parent = info.parent
        self.callbacks = info.callbacks
        self.names = info.names
        
        
    
    def sliding_window_listing(self, menu_page: list, menu: list, right_border: int = 6, left_border: int = 0) -> list:
        
        """
        Функция которая скользит по списку с помощью так называемого способа "Скользящего окна", для 
        более подробной информации используйте гугл, задать границы можно при передаче аргументов
        """

        for _ in range(self.page):
            menu_page.append(menu[left_border:right_border])
            right_border += 6
            left_border += 6
        return menu_page
    
    def create_buttons(self, menu: list) -> list:

        """
        Функция итерирует список с текстами для кнопок и список с их коллбеками, после создает экземпляр кнопки
        и добавляет его к списку по которому можно будет итерировать способом скользящего окна

        Возвращает  список кнопок
        """

        for text, callback in zip(self.names, self.callbacks):
            menu.append(telebot.types.InlineKeyboardButton(text, callback_data=callback+'``1'))
        return menu

    def control_buttons(self,menu_buttons_pages_generated: list, min_page: int, max_page: int, shablon: str) -> tuple:
        
        """
        Функция добавляет кнопки управления страницами и кнопку возврата в глав меню
        """

        left = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{shablon}``{self.page - 1}')
        right = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{shablon}``{self.page + 1}')
        begining = telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data=f'{shablon}``{min_page}')

        if self.page == min_page:

            menu_buttons_pages_generated.append(right)    
        elif self.page == max_page:
            
            menu_buttons_pages_generated.append(left)
            menu_buttons_pages_generated.append(begining)
        else:
            menu_buttons_pages_generated.append(right)
            menu_buttons_pages_generated.append(left)
            
                    
        menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='aaa``1'))
        return menu_buttons_pages_generated

    def create_pages(self, min_page: int, max_page: int, menu_page: list) -> tuple:
        
        """
        Функция генерирует, именно генерирует, 6 кнопок для нужной страницы, и дополнительные кнопки меню 
        для управления, такие как перелистывание страниц и возврат в меню и добавляет это все в лист

        Возвращает список кнопок для страницы с определенным номером, который определяется благодаря числу элементов.
        Так что страницы по сути генерируются сами, просто добавьте больше кнопок в список и страницы сами появятся
        """
        shablon = self.info.callback
        
        menu_buttons_pages_generated: list = [v for i,v in enumerate(menu_page[self.page-1]) if i <= 5]
        menu_buttons_pages_generated: tuple = self.control_buttons(menu_buttons_pages_generated, min_page, max_page, shablon)
            
        return menu_buttons_pages_generated

    def add_buttons_to_keyboard(self, menu_buttons_pages_generated: list, next_menu: Any):

        """
        Функция добавляет кнопки созданной страницы в клавиатуру

        """
        
        for i in menu_buttons_pages_generated:
            
            next_menu.add(i)
        return next_menu
        

    def pager(self) -> Any:
        
        """
        Функция которая создает "страницу" кнопок, выясняет максимальную возможную страницу, минимально возможную и тд.

        Возвращает клавиатуру с набором нужных кнопок
        """

        menu = self.create_buttons(list())
        
        menu_len = len(menu)
        max_page = math.ceil(menu_len / 6)
        min_page = 1
        
        menu_page = self.sliding_window_listing(list(), menu, right_border=6, left_border=0)

        menu_buttons_pages_generated = self.create_pages(min_page, max_page, menu_page)

        next_menu = self.add_buttons_to_keyboard(menu_buttons_pages_generated, self.next_menu)
        
        return next_menu        

    def bot_menu_pager(self) -> NoReturn: 
        
        """
        Функция создает страницу из кнопок в сообщении
        """
        

        text = self.info.text

        menu = self.pager()
        
        self.bot.edit_message_text(f'{text}\nСтраница номер: {self.number_in_sqare[self.page-1]}',
                              self.chat_id,
                              self.message_id,
                              reply_markup=menu)
        
    