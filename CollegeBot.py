# coding=utf-8 

from studmenu import student
from studmenpages import student_menu
from abiturmenu import abitur
from abiturpages import abitur_menu
from sotrmenu import sotrud
from sotrudmenpages import sotrud_menu
from tbot import bot
import telebot

#ssss


@bot.message_handler(commands=['start'])
def start(message):
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud_page1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="Sotr_page1")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur_page1")
    
    markup.add(button_studRod, button_abitr, button_sotr, )
    
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    
    
@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    if call.data == 'mainmenu': # Главное меню
        
        mainmenu = telebot.types.InlineKeyboardMarkup(row_width = 1)
        
        button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud_page1')
        button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="Sotr_page1")
        button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur_page1")
        
        mainmenu.add(button_studRod, button_abitr,button_sotr, )
        
        bot.edit_message_text("Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?", call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    
    student_menu.elif_studmenupage(call)
    
    abitur_menu.elif_abitur(call)
    
    sotrud_menu.elif_sotrudmenupage(call)
    
    student.elif_stud(call)
    
    abitur.abitur_bum(call)    
    
    sotrud.elif_sotr(call)


bot.polling(none_stop=True)