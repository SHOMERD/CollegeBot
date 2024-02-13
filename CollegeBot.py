# coding=utf-8 

from SectionChooser import SectionChooser
from studmenpages import Menu
from tbot import bot, page_names, additional_buttons_data
from tbot import current_time
import telebot



@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud_page1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="Sotr_page1")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur_page1")
    
    markup.add(button_studRod, button_abitr, button_sotr, )
    
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    
    
    
@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    if call.data == 'mainmenu': # Главное меню
        
        bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Вернулся в Главное меню'.format(current_time(), call.from_user.id, call.from_user.first_name, call.from_user.last_name,call.from_user.username))
        
        mainmenu = telebot.types.InlineKeyboardMarkup(row_width = 1)
        
        button_studRod = telebot.types.InlineKeyboardButton(text='Студент\Родитель', callback_data='Stud_page1')
        button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник\Преподаватель', callback_data='Sotr_page1')
        button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент\Родитель абитуриента', callback_data='Abitur_page1')
        
        mainmenu.add(button_studRod, button_abitr,button_sotr)
        
        bot.edit_message_text("Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?", call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    print(call.data)    
    if '_page' in call.data:
        print(1, call.data[:-6])
        page = int(call.data[-1])
        identity = call.data[:-6]
        menuг = Menu(bot, call, page_names.get(identity), identity, page)
           
        menuг.bot_menu_pager()
    elif '_menu' in call.data:
        pass
    elif 'Stud_' in call.data or 'Sotr_' in call.data or 'Abitur_' in call.data:
        identity = call.data[:4]
        names = (page_names.get(identity))[0]
        callback_number = 0
        additional_buttons = additional_buttons_data.get(identity)
        
        for i in names:
            if call.data[5:] == i:
                print('found')
                break
            callback_number +=1
            print('not found, trying again')
         
        additional_button_array = additional_buttons[callback_number]
        additional_button_bool = additional_button_array[0] # [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
        additional_button_data = additional_button_array[1:]
        
        print(call.data[5:], callback_number, additional_button_array, additional_button_bool, additional_button_data)
        section = SectionChooser(bot, call, identity, callback_number, additional_button_data, additional_button_bool)
        section.section_selector()
    


bot.polling(none_stop=True)
