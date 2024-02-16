# coding=utf-8 


from SectionChooser import SectionChooser
from MenuCreator import Menu
from tbot import bot, page_names, additional_buttons_data, recursion_menu
from tbot import current_time
import telebot



@bot.message_handler(commands=['start'])
def start(message):
    
    #bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud``1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="Sotr``1")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur``1")
    
    markup.add(button_studRod, button_abitr, button_sotr, )
    
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    
def mainmenu(call):
    mainmenu = telebot.types.InlineKeyboardMarkup(row_width = 1)
        
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент\Родитель', callback_data='Stud``1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник\Преподаватель', callback_data='Sotr``1')
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент\Родитель абитуриента', callback_data='Abitur``1')
        
    mainmenu.add(button_studRod, button_abitr,button_sotr)
        
    bot.edit_message_text("Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?", call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    return

def get_tree(tree, call_data):
    for i in call_data[:-1]:
        tree = tree + i
    return tree

def set_recursive_menu(section, call, page, tree, parent_recursive):
        
    print('рекурсивное меню')
    recursed_menu = Menu(bot, call, recursion_menu.get(section), section, page, tree, parent_recursive)
    recursed_menu.bot_menu_pager()

def set_regular_menu(section, call, page, tree, parent):
    print('обычное меню')

    recursed_menu = Menu(bot, call, page_names.get(parent), section, page, tree, parent)
    recursed_menu.bot_menu_pager()

def recursive_buttons(bot,call, parent_recursive):
    callbacks = (recursion_menu.get(parent_recursive))[0]
            
    if section in callbacks:
        callback_index = callbacks.index(section)
        callback_name = callbacks[callback_index]
            
        names = recursion_menu.get(parent_recursive) 
        callback_number = 0   
        additional_buttons = additional_buttons_data.get(parent_recursive)
        print('содержание кнопок---', call.data, section, sep='\n')
        for i in names[0]:
            print(i, callback_name)
            if callback_name == i:
                
                break
            callback_number +=1
            
        additional_button_array = additional_buttons[callback_number]
        additional_button_bool = additional_button_array[0] # [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
        additional_button_data = additional_button_array[1:]
        section = SectionChooser(bot, call, parent_recursive, section, callback_number, additional_button_data, tree, additional_button_bool)
        section.section_selector()
def set_buttons(parent, call, tree):
    callbacks = (page_names.get(parent))[0]

    if section in callbacks:
        callback_index = callbacks.index(section)
        callback_name = callbacks[callback_index]
        names = (page_names.get(parent)) 
        callback_number = 0   
        additional_buttons = additional_buttons_data.get(parent)
        print('содержание кнопок---', call.data, section, sep='\n')
        for i in names[0]:
            print(i, callback_name)
            if callback_name == i:
                
                break
            callback_number +=1
            
        additional_button_array = additional_buttons[callback_number]
        additional_button_bool = additional_button_array[0] # [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
        additional_button_data = additional_button_array[1:]
        section = SectionChooser(bot, call, parent, section, callback_number, additional_button_data, tree, additional_button_bool)
        section.section_selector()

@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    if call.data == 'mainmenu': # Главное меню
        
        mainmenu(call)
        return
    
    call_data=call.data
    
    call_data = call_data.split('_')
    parsed = (call_data[-1]).split('``')
    section, page = parsed if len(parsed)>1 else [parsed[0],1]
    page = int(page)
    tree = get_tree('_', call_data)
    
    parent = call_data.pop(0) if len(call_data) > 1 else section

    parent_recursive = parent if len(call_data) < 2 else call_data[-2]
    
    if section in recursion_menu.keys():    
        set_recursive_menu(section, call, page, tree, parent_recursive)
        return
    
    if section in page_names.keys():
        set_regular_menu(section, call, page, tree, parent)
        return

    if recursion_menu.get(parent_recursive) is not None:
        if section in recursion_menu.get(parent_recursive)[0]:
            recursive_buttons(section, page, tree)
            return
    
            
    
    if page_names.get(parent) is not None:
        if section in (page_names.get(parent))[0]:
            print('d')
            set_buttons(section, page, tree)
            
            return

    

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #if '_recmenu' in call.data:
        
    #    page = int(call.data[-1])
    #    identity = ((call.data).split('_'))[1] 
    #    print('меню рекурсии---', call.data, identity, sep='\n')
    #    menuг = Menu(bot, call, recursion_menu.get(identity), identity, page)
    #    menuг.bot_menu_pager()
    #    return    
    #elif '_page' in call.data:
    #    print('страницы меню---', call.data, sep='\n')
    #    page = int(call.data[-1])
    #    identity = ((call.data).split('_'))[0] 
        
    #    menuг = Menu(bot, call, page_names.get(identity), identity, page)
    #    menuг.bot_menu_pager()
    #    return
    
    
    #for recursion in recursion_menu.keys():
    #    if recursion in call.data:
            
    #        identity = ((call.data).split('_'))[0] #if menu in call.data else ((call.data).split('_'))[1]
    #        callback_name = ((call.data).split('_'))[1]
    #        names = (recursion_menu.get(identity))[0]
    #        callback_number = 0   
    #        additional_buttons = additional_buttons_data.get(identity)
    #        print('содержание кнопок рекурсии---', call.data, identity, sep='\n')
    #        for i in names:
    #            print(i, callback_name)
    #            if callback_name == i:
                
    #                break
    #            callback_number +=1
            
    #        additional_button_array = additional_buttons[callback_number]
    #        additional_button_bool = additional_button_array[0] # [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
    #        additional_button_data = additional_button_array[1:]
    #        recursion = 1 
    #        #print(recursion, callback_name, callback_number, additional_button_array, additional_button_bool, additional_button_data)
    #        section = SectionChooser(bot, call, identity, callback_number, additional_button_data, additional_button_bool, 1)
    #        section.section_selector()
    #        return
    
    #for menu in page_names.keys():    
    #    print(menu)
    #    if menu in call.data:
            
    #        identity = ((call.data).split('_'))[0] #if menu in call.data else ((call.data).split('_'))[1]
    #        callback_name = ((call.data).split('_'))[1]
    #        names = (page_names.get(identity))[0] 
    #        callback_number = 0   
    #        additional_buttons = additional_buttons_data.get(identity)
    #        print('содержание кнопок---', call.data, identity, sep='\n')
    #        for i in names:
    #            print(i, callback_name)
    #            if callback_name == i:
                
    #                break
    #            callback_number +=1
            
    #        additional_button_array = additional_buttons[callback_number]
    #        additional_button_bool = additional_button_array[0] # [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
    #        additional_button_data = additional_button_array[1:]
    #        recursion = 0
    #        #print(recursion, callback_name, callback_number, additional_button_array, additional_button_bool, additional_button_data)
    #        section = SectionChooser(bot, call, identity, callback_number, additional_button_data, additional_button_bool)
    #        section.section_selector()
    #        return
        
    


bot.polling(none_stop=True)
