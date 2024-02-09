# coding=utf-8 

import math
import telebot
from tbot import bot
from tbot import current_time

class MenuPages():
    def __init__(self, buttons, identity = 'student'):
        self.buttons = buttons
        self.generated_buttons = []
        self.next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        self.identity = identity

    def generator_buttons(self):
        for v in self.buttons:
            return telebot.types.InlineKeyboardButton(v, callback_data=v)
         
    
    def pager(self, page = 1):
        menu = list(self.generator_buttons() for i in range(len(self.buttons)))
        menu_len = len(menu)
        max_page = math.ceil(menu_len // 6)
        min_page = 1
        menu_buttons_generated = list()
        for i, v in enumerate(menu):
            menu_buttons_generated.append(menu.pop(i))
            if i == 5:
                
                if page == min_page:
                    menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{self.identity}_page{page + 1}'))
                    break
                elif page == max_page:
                    menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{self.identity}_page{page - 1}'))
                    menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data=f'{self.identity}_page{min_page}'))
                    break
                else:
                    menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{self.identity}_page{page + 1}'))
                    menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{self.identity}_page{page + 1}'))
                    break
                    
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        for i in menu_buttons_generated:
            self.next_menu.add(i)
        return self.next_menu
        



class student_menu():
    
    def __init__(self, bot, call):
        self.bot = bot
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id
        self.pages = ('Получить справку',
                    'Отсрочка от армии',
                    'Расписание занятий',
                    'Расписание звонков',
                    'Оплатить обучение',
                    'Узнать задолженность (финансовую)',
                    'Узнать долги/пересдать сессию',
                    'Заочное обучение',
                    'Практика',
                    'Афиша мероприятий',
                    'Внеучебные траектории и клубы',
                    'Дополнительное образование',
                    'Второй диплом',
                    'Учебные планы',
                    'Электронная библиотека',
                    'Связаться с преподавателем',
                    'Доступ в ЭлЖур',
                    'Транспортная карта',
                    'Список сотрудников',
                    'Консультация психолога',
                    'Самоуправление',
                    'Потерял/нашел вещь',
                    'Правила внутреннего распорядка',
                    'Пропускной режим',
                    'Скидки и виды поощрений',
                    'Другой вопрос',
                    'Связаться с администрацией',
                    'Наш сайт и социальные сети'
                    )
        self.number_in_sqare = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')

    
    def bot_menu_pager(self, page = 1): 
            
        menu = MenuPages(self.pages)
        page_buttons = menu.pager(page)
        bot.edit_message_text(f'Меню для Студента/Родителя\nСтраница номер: {self.number_in_sqare[page-1]} ',
                              self.chat_id,
                              self.message_id,
                              reply_markup=page_buttons)

    def elif_studmenupage(call):

            
        
        def menu_page2(call):  # страница меню студента 2
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Узнать долги/пересдать сессию', callback_data="dolg_not_money")
            button_2 = telebot.types.InlineKeyboardButton('Заочное обучение', callback_data="distance")
            button_3 = telebot.types.InlineKeyboardButton('Практика', callback_data="practice")
            button_4 = telebot.types.InlineKeyboardButton('Афиша мероприятий', callback_data="afisha")
            button_5 = telebot.types.InlineKeyboardButton('Внеучебные траектории и клубы', callback_data="clubs")
            button_6 = telebot.types.InlineKeyboardButton('Дополнительное образование', callback_data="dop_obrazov1")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page1')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page3')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6, page_back,page_next, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 2️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        
        def menu_page3(call):  # страница меню студента 3
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Второй диплом', callback_data="dop_obrazov2")
            button_2 = telebot.types.InlineKeyboardButton('Учебные планы', callback_data="study_plans")
            button_3 = telebot.types.InlineKeyboardButton('Электронная библиотека', callback_data="el_library")
            button_4 = telebot.types.InlineKeyboardButton('Связаться с преподавателем', callback_data="message_teacher")
            button_5 = telebot.types.InlineKeyboardButton('Доступ в ЭлЖур', callback_data="el_jur")
            button_6 = telebot.types.InlineKeyboardButton('Транспортная карта', callback_data="transport_card")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page2')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page4')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4,button_5,button_6,  page_back,page_next, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 3️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        
        def menu_page4(call):  # страница меню студента 4
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Список сотрудников', callback_data="employee")
            button_2 = telebot.types.InlineKeyboardButton('Консультация психолога', callback_data="psixolog")
            button_3 = telebot.types.InlineKeyboardButton('Самоуправление', callback_data="self_control")
            button_4 = telebot.types.InlineKeyboardButton('Потерял/нашел вещь', callback_data="find_or_lost")
            button_5 = telebot.types.InlineKeyboardButton('Правила внутреннего распорядка', callback_data="rules")
            button_6 = telebot.types.InlineKeyboardButton('Пропускной режим', callback_data="kpp")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page3')
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Stud_page5')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_4, button_3,button_5,button_6, page_back,page_next, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 4️⃣', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page5(call):  # страница меню студента 5
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Скидки и виды поощрений', callback_data="sales")
            button_2 = telebot.types.InlineKeyboardButton('Другой вопрос', callback_data="different_q")
            button_3 = telebot.types.InlineKeyboardButton('Связаться с администрацией', callback_data="message_admin")
            button_4 = telebot.types.InlineKeyboardButton('Наш сайт и социальные сети', callback_data="links")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Stud_page4')
            page_1 = telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data='Stud_page1')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4, page_back,page_1, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Студента\Родителя\nСтраница номер: 5️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        
        
        # словарь заменяющий длинную цепь if,elif,elif,elif
        stud_page = {'Stud_page1':menu_page1,
                     'Stud_page2':menu_page2,
                     'Stud_page3':menu_page3,
                     'Stud_page4':menu_page4,
                     'Stud_page5':menu_page5
                     }       
        
        if call.data in stud_page:
            
            stud_page[call.data](call)
            bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Открыл страницу <{}> меню Студента/Родителя'.format(current_time(), call.from_user.id, call.from_user.first_name, call.from_user.last_name,call.from_user.username, call.data))
            
            
        



