# coding=utf-8 

import telebot
from typing import NoReturn
from SectionChooser import SectionChooser
from MenuCreator import Menu
from tbot import bot, page_names, additional_buttons_data, recursion_menu
from tbot import current_time




@bot.message_handler(commands=['start'])
def start(message) -> NoReturn:
    
    #bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud``1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="Sotr``1")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur``1")
    
    markup.add(button_studRod, button_abitr, button_sotr, )
    
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    return
    
def mainmenu(call) -> NoReturn:
    mainmenu = telebot.types.InlineKeyboardMarkup(row_width = 1)
        
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент\Родитель', callback_data='Stud``1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник\Преподаватель', callback_data='Sotr``1')
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент\Родитель абитуриента', callback_data='Abitur``1')
        
    mainmenu.add(button_studRod, button_abitr,button_sotr)
        
    bot.edit_message_text("Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?", call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    return

def get_tree(tree, call_data) -> str:
    for i in call_data[:-1]:
        tree = tree + i
    return tree

def set_recursive_menu(bot, section, call, page, tree, parent_recursive) -> NoReturn:
        
    print('рекурсивное меню')
    
    recursed_menu = Menu(bot, call, recursion_menu.get(section), section, page, tree, parent_recursive)
    recursed_menu.bot_menu_pager()
    

def set_regular_menu(bot, section, call, page, tree, parent) -> NoReturn:
    print('обычное меню')

    recursed_menu = Menu(bot, call, page_names.get(parent), section, page, tree, parent)
    recursed_menu.bot_menu_pager()
    

def recursive_buttons(bot, section, call, tree, parent_recursive, parent) -> NoReturn:
    callbacks: tuple = (recursion_menu.get(parent_recursive))[0]
    
    if section in callbacks:
        callback_index: int = callbacks.index(section)
        callback_name: str = callbacks[callback_index]
            
        
        callback_number: int = 0   
        additional_buttons: tuple = additional_buttons_data.get(parent_recursive)
        print('содержание кнопок рекурсивных---', section, sep='\n')
        for i in callbacks:
            print(i, callback_name)
            if callback_name == i:
                
                break
            callback_number +=1
            
        additional_button_array: tuple = additional_buttons[callback_number]
        additional_button_bool: bool = additional_button_array[0] 
        additional_button_data = additional_button_array[1:] # tuples or string
        section = SectionChooser(bot, call, parent, section, callback_number, additional_button_data, tree, parent_recursive, additional_button_bool)
        section.section_selector()
        return

def set_buttons(bot, section, call, tree, parent) -> NoReturn:
    callbacks: tuple = (page_names.get(parent))[0]
    
    
    if section in callbacks:
        
        callback_index: int = callbacks.index(section)
        callback_name: str = callbacks[callback_index]
        
        callback_number: int = 0   
        additional_buttons: tuple = additional_buttons_data.get(parent)
        print('содержание кнопок---', call.data, section, sep='\n')
        for i in callbacks:
            print(i, callback_name)
            if callback_name == i:
                
                break
            callback_number +=1
            
        additional_button_array: tuple = additional_buttons[callback_number]
        additional_button_bool: bool = additional_button_array[0] 
        additional_button_data = additional_button_array[1:] # tuples or string
        section = SectionChooser(bot, call, parent, section, callback_number, additional_button_data, tree, additional_button=additional_button_bool)
        section.section_selector()
        return

@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    if call.data == 'mainmenu': # Главное меню
        mainmenu(call)
    print(type(call.message.chat.id), type(call.message.message_id))    
    
    call_data: str = call.data
    call_data: list = call_data.split('_')
    parsed: list = (call_data[-1]).split('``')
    section, page = parsed if len(parsed)>1 else [parsed[0],'1'] # все str
    page: int = int(page)
    print(call.data)
    
    parent: str = call_data.pop(0) if len(call_data) > 1 else section
    tree: str = get_tree('_', call_data)
    parent_recursive: str = parent if len(call_data) < 2 else call_data[-2]
    
    if section in recursion_menu.keys():    
        set_recursive_menu(bot, section, call, page, tree, parent_recursive)
        
    elif section in page_names.keys():
        set_regular_menu(bot, section, call, page, tree, parent)
        
    elif recursion_menu.get(parent_recursive) is not None:
        if section in recursion_menu.get(parent_recursive)[0]:
            recursive_buttons(bot, section, call, tree, parent_recursive, parent)
            
    elif page_names.get(parent) != None:
        if section in (page_names.get(parent))[0]:
            print('d')
            set_buttons(bot, section, call, tree, parent)
            
            

    
    


bot.polling(none_stop=True)
