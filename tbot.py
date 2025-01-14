# coding=utf-8 
import os
import json
import telebot
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time


page_names = {
              'Stud': (
                        ( # callbacks
                            "spravka",
                            "otsrochka",
                            "rasp zanyat",
                            "rasp zvon",
                            "oplata",
                            "dolg(money)",
                            "dolg(NotMoney)",
                            "distance",
                            "practice",
                            "afisha",
                            "clubs",
                            "dopObrazov1",
                            "dopObrazov2",
                            "studyPlans",
                            "elibrary",
                            "messageTeacher",
                            "eljur",
                            "transportCard",
                            "employee",
                            "psixolog",
                            "selfControl",
                            "find/lost",
                            "rules",
                            "kpp",
                            "sales",
                            "different",
                            "messageAdmin",
                            "links"
                        ),
                        ( # текст для кнопок
                            'Получить справку',
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
                    ),
              'Sotr': (
                        ( # callbacks
                            'raspis_zanyat',
                            'raspis_zvonkov',
                            'events',
                            'dopolnitel_obr',
                            'vedomost',
                            'dostupElJur',
                            'Tech_diff',
                            'post',
                            'kuratoru',
                            'plans',
                            'electr_lib',
                            'message_student',
                            'student_diff',
                            'trud',
                            'propusk',
                            'rekvisit',
                            'other_question',
                            'links_sotr'

                        ),
                        (   # текст кнопок
                            'Расписание занятий',
                            'Расписание звонков',
                            'Мероприятия',
                            'Дополнительное образование',
                            'Получить ведомость',
                            'Доступ в ЭлЖур',
                            'Технические сложности',
                            'Опубликовать пост',
                            'Куратору групп',
                            'Учебные планы',
                            'Электронная библиотека',
                            'Связаться со студентом',
                            'Сложности со студентами',
                            'Трудоустройство/оплата',
                            'Пропускной режим',
                            'Реквизиты колледжа',
                            'Другой вопрос',
                            'Наш сайт и социальные сети'
                        )
                    ),
              'Abitur': (
                            ( # callbacks
                                'about',
                                'specials', 
                                'docum',
                                'kakPostup',
                                'cost',
                                'exams',
                                'dopDegree',
                                'clubsAbitur',
                                'license1',
                                'partnership',
                                'affisha',
                                'kuratori',
                                'way',
                                'transac',
                                'links1'
                            ),
                            (
                                'О колледже',
                                'Специальности',
                                'Документы для поступления',
                                'Как поступить?',
                                'Стоимость обучения и скидки',
                                'Вступительные испытания',
                                'Дополнительное образование',
                                'Внеучебные траектории и клубы',
                                'Лицензия и аккредитация',
                                'Партнеры колледжа',
                                'Афиша мероприятий',
                                'Кураторы и наставники',
                                'Как добраться?',
                                'Оплатить обучение',
                                'Наш сайт и социальные сети'
                            )
                    )}



recursion_menu = {'specials':(
                                (
                                'spec1',
                                'spec2',
                                'spec3',
                                'spec4',
                                'spec5',
                                'spec6',
                                'spec7',
                                'spec8',
                                'spec9',
                                'spec10',
                                'spec11',
                                'spec12',
                                'spec13'
                                ),
                                (
                                'Дизайн (по отраслям)',
                                'Реклама',
                                'Информационные системы и программирование',
                                'Юриспруденция',
                                'Правоохранительная деятельность',
                                'Операционная деятельность в логистике',
                                'Экономика и бухгалтерский учет',
                                'Коммерция',
                                'Финансы',
                                'Социально-культурная деятельность',
                                'Народное художественное творчество',
                                'Коррекционная педагогика в нач. образовании',
                                'Специальное дошкольное образование'
                                )
                            )
                }

additional_buttons_data = {'Stud':(
                                    (1, 'Заказать справку','https://opencollege-nsk.ru/live/#extract'),
                                    (1, 'Заказать справку','https://opencollege-nsk.ru/live/#extract'),
                                    (1, 'Посмотреть расписание','https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748'),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (1, 'Перейти в Instudy','https://opencollege-nsk.ru/instudy'),
                                    (0, '',''),
                                    (1, 'Афиша мероприятий','https://docs.google.com/spreadsheets/d/1BD8GIu3mFyJaGab3cUBPxwgwu6J3KseI/edit?usp=drivesdk&ouid=114275661080998669061&rtpof=true&sd=true'),
                                    (1,
                                        ('Узнать подробнее','https://opencollege-nsk.ru/live/extracurricular/?group=creation'),
                                        ('Вступить в траекторию','https://forms.gle/BLf9EBoycc8EagQx5')
                                        ),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/education/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/education/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/sveden/education/eduop/'),
                                    (1, 'Зайти в библиотеку','http://www.iprbookshop.ru/'),
                                    (1, 'Зайти в ЭлЖур','https://opencollege-nsk.eljur.ru/authorize'),
                                    (1, 'Зайти в  ЭлЖур','https://opencollege-nsk.eljur.ru/authorize'),
                                    (1, 'Транспортная карта','https://t-karta.ru/novosibirsk/student'),
                                    (1, 'Все сотрудники','https://opencollege-nsk.ru/college/structure/'),
                                    (0, '',''),
                                    (1, 'Подробнее о совете','https://opencollege-nsk.ru/live/association/'),
                                    (0, '',''),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/live/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/live'),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    ),
                           'Sotr':(
                                    (1, 'Посмотреть','https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748'),
                                    (0, '',''),
                                    (1, 'Афиша мероприятий','https://docs.google.com/spreadsheets/d/1BD8GIu3mFyJaGab3cUBPxwgwu6J3KseI/edit?usp=drivesdk&ouid=114275661080998669061&rtpof=true&sd=true'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/education/'),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (1, 'Список кураторов и наставников','https://docs.google.com/spreadsheets/d/1b6Lz7k3KT8uDlekmWQZ30HxZ_5jeEll3ERz5uw4bs4M/edit?usp=drivesdk'),
                                    (0, '',''),
                                    (1, 'Зайти в  библиотеку','http://www.iprbookshop.ru/'),
                                    (1,  
                                        ('Зайти в  ЭлЖур','https://opencollege-nsk.eljur.ru/authorize'),
                                        ('Список кураторов','https://docs.google.com/spreadsheets/d/1b6Lz7k3KT8uDlekmWQZ30HxZ_5jeEll3ERz5uw4bs4M/edit?usp=drivesdk')),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '','')
                                    ),
                           'Abitur':(
                                    (1, 'Подробнее на сайте','https://opencollege-nsk.ru'),
                                    (0, '',''),
                                    (0, '',''),
                                    (1, 'Записаться на прием','https://opencollege-nsk.ru/enrollee/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/enrollee/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/enrollee/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/education/'),
                                    (1, 
                                        ('Узнать подробнее','https://opencollege-nsk.ru/live/extracurricular/?group=creation'),
                                        ('Студенчкский совет','https://opencollege-nsk.ru/live/association/')),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/college/'),
                                    (1, 'Перейти на сайт','https://opencollege-nsk.ru/college/partners/'),
                                    (1, 'Перейти в канал','https://t.me/opencollege2023'),
                                    (1, 'Список кураторов и наставников','https://docs.google.com/spreadsheets/d/1b6Lz7k3KT8uDlekmWQZ30HxZ_5jeEll3ERz5uw4bs4M/edit?usp=drivesdk'),
                                    (0, '',''),
                                    (0, '',''),
                                    (0, '',''),
                                    ),
                           'specials':(
                                    (1, 
                                        ('На сайт','https://opencollege-nsk.ru/speciality/'),
                                        ('Видео про Дизайн','https://youtu.be/_1DTn-nMuAU')),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/'),
                                    (1, 'На сайт','https://opencollege-nsk.ru/speciality/')
                                      )}

