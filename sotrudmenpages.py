# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

class sotrud_menu():
    
    def elif_sotrudmenupage(call):

        def menu_page1(call): # страница меню сотрудника 1
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot 
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Расписание занятий', callback_data="raspis_zanyat")
            button_2 = telebot.types.InlineKeyboardButton('Расписание звонков', callback_data="raspis_zvonkov")
            button_3 = telebot.types.InlineKeyboardButton('Мероприятия', callback_data="events")
            button_4 = telebot.types.InlineKeyboardButton('Дополнительное образование', callback_data="dopolnitel_obr")
            button_5 = telebot.types.InlineKeyboardButton('Получить ведомость', callback_data="vedomost")
            button_6 = telebot.types.InlineKeyboardButton('Доступ в ЭлЖур', callback_data="dostupElJur")
            
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Sotr_page2')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6, page_next, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Сотрудника\Преподавателя\nСтраница номер: 1️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)    
        def menu_page2(call): # страница меню сотрудника 2
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot 
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Технические сложности', callback_data="Tech_diff")
            button_2 = telebot.types.InlineKeyboardButton('Опубликовать пост', callback_data="post")
            button_3 = telebot.types.InlineKeyboardButton('Куратору групп', callback_data="kuratoru")
            button_4 = telebot.types.InlineKeyboardButton('Учебные планы', callback_data="plans")
            button_5 = telebot.types.InlineKeyboardButton('Электронная библиотека', callback_data="electr_lib")
            button_6 = telebot.types.InlineKeyboardButton('Связаться со студентом', callback_data="message_student")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Sotr_page1')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Sotr_page3')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6, page_back,page_next, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Сотрудника\Преподавателя\nСтраница номер: 2️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page3(call): # страница меню сотрудника 3
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot 
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Сложности со студентами', callback_data="student_diff")
            button_2 = telebot.types.InlineKeyboardButton('Трудоустройство/оплата', callback_data="trud")
            button_3 = telebot.types.InlineKeyboardButton('Пропускной режим', callback_data="propusk")
            button_4 = telebot.types.InlineKeyboardButton('Реквизиты колледжа', callback_data="rekvisit")
            button_5 = telebot.types.InlineKeyboardButton('Другой вопрос', callback_data="other_question")
            button_6 = telebot.types.InlineKeyboardButton('Наш сайт и социальные сети', callback_data="links_sotr")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Sotr_page2')
            page_1 = telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data='Sotr_page1')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6, page_1, page_back, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Сотрудника\Преподавателя\nСтраница номер: 3️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        
        
        # словарь заменяющий длинную цепь if,elif,elif,elif
        Sotrud_page = {'Sotr_page1':menu_page1,
                     'Sotr_page2':menu_page2,
                     'Sotr_page3':menu_page3,
                     }       
        
        if call.data in Sotrud_page:
            Sotrud_page[call.data](call)



