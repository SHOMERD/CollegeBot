# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")


class abitur_menu():
    def elif_abitur(call):

        def menu_page1(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('О колледже', callback_data="about")
            button_2 = telebot.types.InlineKeyboardButton('Специальности', callback_data="specials")
            button_3 = telebot.types.InlineKeyboardButton('Документы для поступления', callback_data="docum")
            button_4 = telebot.types.InlineKeyboardButton('Как поступить?', callback_data="kak_postup")
            button_5 = telebot.types.InlineKeyboardButton('Стоимость обучения и скидки', callback_data="cost")
            
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Abitur_page2')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4,button_5, page_next, back)
           
            bot.edit_message_text('Меню для Абитуриента/Родителя абитуриента\nСтраница номер: 1️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu) 
        def menu_page2(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('Вступительные испытания', callback_data="exams")
            button_2 = telebot.types.InlineKeyboardButton('Дополнительное образование', callback_data="dop_degree")
            button_3 = telebot.types.InlineKeyboardButton('Внеучебные траектории и клубы', callback_data="clubs_abitur")
            button_4 = telebot.types.InlineKeyboardButton('Лицензия и аккредитация', callback_data="license1")
            button_5 = telebot.types.InlineKeyboardButton('Партнеры колледжа', callback_data="partnership")
            
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Abitur_page3')
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Abitur_page1')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4, button_5, page_back,page_next, back)
            
            bot.edit_message_text('Меню для Абитуриента/Родителя абитуриента\nСтраница номер: 2️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page3(call):
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('Афиша мероприятий', callback_data="affisha")
            button_2 = telebot.types.InlineKeyboardButton('Кураторы и наставники', callback_data="kuratori")
            button_3 = telebot.types.InlineKeyboardButton('Как добраться?', callback_data="way")
            button_4 = telebot.types.InlineKeyboardButton('Оплатить обучение', callback_data="transac")
            button_5 = telebot.types.InlineKeyboardButton('Наш сайт и социальные сети', callback_data="links1")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Abitur_page2')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1,button_2,button_3,button_4, button_5, page_back, back)
            
            bot.edit_message_text('Меню для Абитуриента/Родителя абитуриента\nСтраница номер: 3️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        abitur_page = {'Abitur_page1':menu_page1,
                     'Abitur_page2':menu_page2,
                     'Abitur_page3':menu_page3,
                     }       
        
        if call.data in abitur_page:
            abitur_page[call.data](call)



