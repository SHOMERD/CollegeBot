import math
from typing import Any
import telebot
from text_parser import get_text

class SectionChooser():

    def __init__(self, bot: Any, call: Any, parent: str, section: str, number: int, additional_button_data: Any, address_tree: str, recursive_parent=None, additional_button=False):
        
        """"""
        
        # полученные переменные при создании экземпляра класса
        self.bot: Any = bot
        self.call: Any = call
        self.page_numbers: int = number
        self.additional_data = additional_button_data
        self.additional_bool: bool = additional_button
        self.tree: str = address_tree
        self.parent: str = parent
        self.recursive_parent: Any = recursive_parent
        self.section: str = section
        self.number: int = number
        
        # дополнительные переменные полученные из предыдущих переменных
        self.back_page: int = math.ceil((number+1)/6)
        self.chat_id: int = call.message.chat.id
        self.message_id: int = call.message.message_id
        
        self.text: str = get_text(number, self.parent if self.recursive_parent == None else self.recursive_parent)
        
        self.url: list = list()
        self.text_url: list = list()
        if isinstance(self.additional_data[0], tuple):
            for i in self.additional_data:
                
                self.url.append(i[1]) # ИЗМЕНИТЬ ПРОВЕРКУ НА ТИП ДАННЫХ, ИНАЧЕ ПРИ НЕПРАВИЛЬНО ВВЕДЕНЫХ ДАННЫХ
                                      # ВСЕ ПОЙДЕТ ПО ПИЗДЕ
                self.text_url.append(i[0])
        else:
            self.url: str = self.additional_data[1]
            self.text_url: str = self.additional_data[0]
        
    def get_menu_buttons(self, menu_buttons_generated: list) -> list:
        
        """
        Функция добавляет дополнительные кнопки для раздела если они имеются, все кнопки - кнопки-ссылки
        """

        if self.additional_bool and not isinstance(self.text_url, list) and not isinstance(self.url, list):
            
            menu_buttons_generated.append(telebot.types.InlineKeyboardButton(self.text_url, url=self.url))
        else:
            for text, url in zip(self.text_url, self.url):
                
                menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text, url=url))
        return menu_buttons_generated

    def add_buttons(self, menu_buttons_generated: list, next_menu: Any) -> Any:
        
        """
        Функция добавляет созданные ранее кнопки, хранящиеся в листе, в экземпляр клавиатуры
        """
        
        for i in menu_buttons_generated:

            next_menu.add(i)
        return next_menu
        
    def create_buttons(self) -> Any:
        
        """
        Функция создает клавиатуру с кнопками управления страницами, возвращает объект клавиатуры
        """

        next_menu: Any = telebot.types.InlineKeyboardMarkup(row_width=1)
        
        menu_buttons_generated: list = self.get_menu_buttons(list())
        
        call_back_data: str = f"{self.parent}``{self.back_page}" if len(self.tree)==1 else f"{self.parent}{self.tree}``{self.back_page}"
        
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data=call_back_data)) 
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        
        next_menu: Any = self.add_buttons(menu_buttons_generated, next_menu) 
        
        return next_menu
        
    def section_selector(self):
        
        """
        Редактирует сообщение, тем самым "открывает" раздел, меняет текст сообщения, добавляет кнопки
        возврата в прошлое меню и глав меню
        """

        self.bot.edit_message_text(
                                    self.text,
                                    self.chat_id,
                                    self.message_id,
                                    reply_markup=self.create_buttons()
                                    )