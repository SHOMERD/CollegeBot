# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

class sotrud():
    
    def elif_sotr():

        def first_str_1(call): # Расписание занятий
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Посмотреть', url='https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748') # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2,button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Посмотреть актуальное расписание занятий можно по ссылке: https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748

Согласовать свое расписание, внести по нему предложения, предупредить о незапланированной ситуации, назначить и согласовать время пересдачи, уточнить возможности аудиторного фонда, попросить маркер и губку можно в кабинете 261. 

Контакты:

Заведующая учебной частью - Лидия Егоровна Пикулина.

Кабинет 261. 
Тел.: 8 (383) 363-63-63, доб.: 1006
E-mail: pikulina-le@opencollege-nsk.ru


Заместитель директора по учебно-методической работе - Юлия Андреевна Хохлова

Кабинет 263. 
Тел.: 8 (383) 363-63-63, доб.: 1005
E-mail: hohlova-ya@opencollege-nsk.ru 
ТГ: @uliahohlova

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_2(call): # Расписание звонков
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        




