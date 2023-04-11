# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

class student_menu():
    def elif_studmenupage(call):

        def menu_page1(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('Получить справку', callback_data="spravka")
            button_2 = telebot.types.InlineKeyboardButton('Отсрочка от армии', callback_data="otsrochka")
            button_3 = telebot.types.InlineKeyboardButton('Расписание занятий', callback_data="rasp zanyat")
            button_4 = telebot.types.InlineKeyboardButton('Расписание звонков', callback_data="rasp zvon")
            button_5 = telebot.types.InlineKeyboardButton('Оплатить обучение', callback_data="oplata")
            button_6 = telebot.types.InlineKeyboardButton('Узнать задолженность (финансовую)', callback_data="dolg_money")
            
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page2')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6, page_next, back)
           
            bot.edit_message_text('Меню для Студента/Родителя\nСтраница номер: 1️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)    
        def menu_page2(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
            button_1 = telebot.types.InlineKeyboardButton('Узнать долги/пересдать сессию', callback_data="dolg_not_money")
            button_2 = telebot.types.InlineKeyboardButton('Заочное обучение', callback_data="distance")
            button_3 = telebot.types.InlineKeyboardButton('Практика', callback_data="practice")
            button_4 = telebot.types.InlineKeyboardButton('Афиша мероприятий', callback_data="afisha")
            button_5 = telebot.types.InlineKeyboardButton('Внеучебные траектории и клубы', callback_data="clubs")
            button_6 = telebot.types.InlineKeyboardButton('Дополнительное образование', callback_data="dop_obrazov1")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page1')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page3')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6,page_next, page_back, back)
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 2️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page3(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
            button_1 = telebot.types.InlineKeyboardButton('Второй диплом', callback_data="dop_obrazov2")
            button_2 = telebot.types.InlineKeyboardButton('Учебные планы', callback_data="study_plans")
            button_3 = telebot.types.InlineKeyboardButton('Электронная библиотека', callback_data="el_library")
            button_4 = telebot.types.InlineKeyboardButton('Связаться с преподавателем', callback_data="message_teacher")
            button_5 = telebot.types.InlineKeyboardButton('Доступ в ЭлЖур', callback_data="el_jur")
            button_6 = telebot.types.InlineKeyboardButton('Транспортная карта', callback_data="transport_card")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page2')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page4')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6, page_next, page_back, back)
            
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 3️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page4(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
            button_1 = telebot.types.InlineKeyboardButton('Список сотрудников', callback_data="employers")
            button_2 = telebot.types.InlineKeyboardButton('Консультация психолога', callback_data="psixolog")
            button_3 = telebot.types.InlineKeyboardButton('Самоуправление', callback_data="self_control")
            button_4 = telebot.types.InlineKeyboardButton('Потерял/нашел вещь', callback_data="find_or_lost")
            button_5 = telebot.types.InlineKeyboardButton('Правила внутреннего распорядка', callback_data="rules")
            button_6 = telebot.types.InlineKeyboardButton('Пропускной режим', callback_data="kpp")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page3')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page5')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_4, button_3,button_5,button_6,page_next, page_back, back)
            
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 4️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page5(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('Скидки и виды поощрений', callback_data="sales")
            button_2 = telebot.types.InlineKeyboardButton('Другой вопрос', callback_data="different_q")
            button_3 = telebot.types.InlineKeyboardButton('Связаться с администрацией', callback_data="message_admin")
            button_4 = telebot.types.InlineKeyboardButton('Наш сайт и социальные сети', callback_data="links")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page4')
            page_1 = telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data='Stud_page1')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4, page_back,page_1, back)
            
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 5️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        
        stud_page = {'Stud_page1':menu_page1,
                     'Stud_page2':menu_page2,
                     'Stud_page3':menu_page3,
                     'Stud_page4':menu_page4,
                     'Stud_page5':menu_page5
                     }       
        
        if call.data in stud_page:
            stud_page[call.data](call)
            
            
        



