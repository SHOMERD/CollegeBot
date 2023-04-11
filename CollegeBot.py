# coding=utf-8 

from studmenu import student
from studmenpages import student_menu
from abiturmenu import abitur
from abiturpages import abitur_menu
from sotrmenu import sotrud
from sotrudmenpages import sotrud_menu
import telebot

bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")


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
    


"""
        #bot.delete_message(call.message.chat.id, call.message.message_id)
        #bot.send_photo(chat_id = call.message.chat.id, photo= open('zvonki.png', 'rb'), reply_markup = next_menu)
        #bot.delete_message(call.message.chat.id, call.message.message_id)
        #bot.send_message(call.message.chat.id, '.')
        #if call.data == 'Stud_page1' or 'mainmenu':
           #bot.delete_message(call.message.chat.id, call.message.message_id)
           #bot.send_message(call.message.chat.id, '.')
        #bot.edit_message_media(chat_id = call.message.chat.id, message_id = call.message.message_id, media = telebot.types.InputMediaPhoto(open('zvonki.png', "rb")))
        #bot.edit_message_text("", call.message.chat.id, call.message.message_id,
                              #reply_markup=next_menu)
        """ 

bot.polling(none_stop=True)