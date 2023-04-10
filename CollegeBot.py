# coding=utf-8 

from studmenu import student
from studmenpages import student_menu
from abiturmenu import abitur
from abiturpages import abitur_menu
import telebot

bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")


@bot.message_handler(commands=['start'])
def start(message):
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud_page1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="test2")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur_page1")
    markup.add(button_studRod, button_abitr, button_sotr, )
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    
@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    if call.data == 'mainmenu': # Главное меню
        mainmenu = telebot.types.InlineKeyboardMarkup(row_width = 1)
        button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud_page1')
        button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="test3")
        button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur_page1")
        mainmenu.add(button_studRod, button_abitr,button_sotr, )
        bot.edit_message_text("Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?", call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "Stud_page1": # Первая страница меню студента\родителя
        student_menu.menu_page1(call)
    elif call.data == "Stud_page2": # вторая страница меню студента\родителя
        student_menu.menu_page2(call)
    elif call.data == "Stud_page3": # третья страница студента\родителя
        student_menu.menu_page3(call)
    elif call.data == "Stud_page4": # четвертая страница студента\родителя
        student_menu.menu_page4(call)
    elif call.data == "Stud_page5": # пятая страница студента\родителя
        student_menu.menu_page5(call)


    elif call.data == "Abitur_page1": # Первая страница меню Абитуриентa или Родителя абитуриента
        abitur_menu.menu_page1(call)
    elif call.data == "Abitur_page2": # вторая страница меню Абитуриентa или Родителя абитуриента
        abitur_menu.menu_page2(call)
    elif call.data == "Abitur_page3": # третья страница меню Абитуриентa или Родителя абитуриента
        abitur_menu.menu_page3(call)


    elif call.data == "spravka": # Получить справку
        student.first_str_1(call)
    elif call.data == "otsrochka": # Получить отсрочку
        student.first_str_2(call)
    elif call.data == "rasp zanyat": # Расписание занятий
        student.first_str_3(call)
    elif call.data == "rasp zvon": # Расписание звонков
        student.first_str_4(call)
    elif call.data == "message_admin": # Связаться с администрацией
        student.first_str_5(call)
    elif call.data == "oplata": # Оплата
        student.first_str_6(call)
    elif call.data == "dolg_money": # Финансовая задолжность
        student.first_str_7(call)
    elif call.data == "dolg_not_money": # Узнать долги/пересдать сессию
        student.first_str_8(call)
    elif call.data == "distance": # Заочка
        student.first_str_9(call)
    elif call.data == "practice": # Практика
        student.first_str_10(call)
    elif call.data == "afisha": # Афиша
        student.first_str_11(call)
    elif call.data == "clubs": # Клубы
        student.first_str_12(call)
    elif call.data == "dop_obrazov1": # Дополнительное образование или второй диплом
        student.first_str_13(call)
    elif call.data == "dop_obrazov2": # Дополнительное образование или второй диплом
        student.first_str_14(call)
    elif call.data == "study_plans": # Учебные планы
        student.first_str_15(call)
    elif call.data == "el_library": # Электронная библиотека
        student.first_str_16(call)
    elif call.data == "message_teacher": # Связаться с преподавателем
        student.first_str_17(call)
    elif call.data == "el_jur": # ЭлЖур
        student.first_str_18(call)
    elif call.data == "transport_card": # Транспортная карта
        student.first_str_19(call)
    elif call.data == "employers": # Сотрудники
        student.first_str_20(call)
    elif call.data == "psixolog": # Консультация психолога
        student.first_str_21(call)
    elif call.data == "self_control": # Самоконтроль
        student.first_str_22(call)
    elif call.data == "find_or_lost": # Потерял\нашел вещь
        student.first_str_23(call)
    elif call.data == "rules": # Правила внутреннего распорядка
        student.first_str_24(call)
    elif call.data == "kpp": # Пропускной режим
        student.first_str_25(call)
    elif call.data == "sales": # Скидки и виды поощрений
        student.first_str_26(call)
    elif call.data == "different_q": # Другой вопрос
        student.first_str_27(call)
    elif call.data == "links": # Ссылки
        student.first_str_28(call)
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