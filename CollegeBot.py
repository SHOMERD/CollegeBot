# coding=utf-8 

import telebot
from typing import NoReturn
from SectionChooser import SectionChooser
from MenuCreator import Menu
from tbot import bot, page_names, additional_buttons_data, recursion_menu
from tbot import info




@bot.message_handler(commands=['start'])
def start(message) -> NoReturn:
    
    #bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='aab``1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="aaE``1")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="aaZ``1")
    
    markup.add(button_studRod, button_abitr, button_sotr, )
    
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    return
    

# def get_tree(tree, call_data) -> str:
#     for i in call_data[:-1]:
#         tree = tree + i
#     return tree

# def set_recursive_menu(bot, section, call, page, tree, parent_recursive) -> NoReturn:
        
    
    
#     recursed_menu = Menu(bot, call, recursion_menu.get(section), section, page, tree, parent_recursive)
#     recursed_menu.bot_menu_pager()
    

# def set_regular_menu(bot, section, call, page, tree, parent) -> NoReturn:
    

#     recursed_menu = Menu(bot, call, page_names.get(parent), section, page, tree, parent)
#     recursed_menu.bot_menu_pager()
    

# def recursive_buttons(bot, section, call, tree, parent_recursive, parent) -> NoReturn:
#     callbacks: tuple = (recursion_menu.get(parent_recursive))[0]
    
#     if section in callbacks:
#         callback_index: int = callbacks.index(section)
#         callback_name: str = callbacks[callback_index]
            
        
#         callback_number: int = 0   
#         additional_buttons: tuple = additional_buttons_data.get(parent_recursive)
        
#         for i in callbacks:
            
#             if callback_name == i:
                
#                 break
#             callback_number +=1
            
#         additional_button_array: tuple = additional_buttons[callback_number]
#         additional_button_bool: bool = additional_button_array[0] 
#         additional_button_data = additional_button_array[1:] # tuples or string
#         section = SectionChooser(bot, call, parent, section, callback_number, additional_button_data, tree, parent_recursive, additional_button_bool)
#         section.section_selector()
#         return

# def set_buttons(bot, section, call, tree, parent) -> NoReturn:
#     callbacks: tuple = (page_names.get(parent))[0]
    
    
#     if section in callbacks:
        
#         callback_index: int = callbacks.index(section)
#         callback_name: str = callbacks[callback_index]
        
#         callback_number: int = 0   
#         additional_buttons: tuple = additional_buttons_data.get(parent)
#         for i in callbacks:
#             if callback_name == i:
                
#                 break
#             callback_number +=1
            
#         additional_button_array: tuple = additional_buttons[callback_number]
#         additional_button_bool: bool = additional_button_array[0] 
#         additional_button_data = additional_button_array[1:] # tuples or string
#         section = SectionChooser(bot, call, parent, section, callback_number, additional_button_data, tree, additional_button=additional_button_bool)
#         section.section_selector()
#         return



@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    call_data: str = call.data
    if '``' in call_data:
        wanted_page = (call_data.split('``'))[-1]
        call_data = (call_data.split('``'))[0]
    print(call_data)
    all_info = info(call_data)
    

    recursed_menu = Menu(bot, call, all_info, wanted_page)
    recursed_menu.bot_menu_pager()



bot.polling(none_stop=True)
