import traceback

from tg_ya_trans_api.utils import djangoORM

import asyncio
import logging

import requests
import json
from telebot import TeleBot
import telebot
from datetime import date, timedelta
import datetime

from telebot.types import CallbackQuery, ReplyKeyboardRemove
from telebot_calendar import Calendar, CallbackData, RUSSIAN_LANGUAGE

from tg_ya_trans_api.models import TelegramScheduleUser as User
from tg_ya_trans_api.utils.access import key
from tg_ya_trans_api.utils import kb

YANDEX_TRANSPORT_API_KEY = '0fc89cc2-b4d4-4ee5-9e2e-a403760c330e'

bot = TeleBot(token=key)
calendar = Calendar(language=RUSSIAN_LANGUAGE)
calendar_1_callback = CallbackData("calendar_1", "action", "year", "month", "day")


# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

def get_schedule(station, direction, selected_date, selected_shift_type, bot, message):
    station_code = station
    lang = ''
    json_response = 'json'
    date_1 = selected_date
    date_2 = datetime.datetime.strptime(selected_date, '%Y-%m-%d') + datetime.timedelta(days=1)
    transport_type = 'plane'
    event = direction  # departure / arrival
    system = 'iata'
    raw_data = []
    ru_cities = []
    schedule_pool = []
    event_type = -1
    if event == 'arrival': event_type = 0

    with open('airports.txt', 'r') as file:
        lines = file.readlines()
        for i in lines:
            ru_cities.append(i.replace('\n', ''))

    day_start = datetime.datetime.strptime('09:00', "%H:%M").time()
    day_end = datetime.datetime.strptime('20:00', "%H:%M").time()
    day_end_departure = datetime.datetime.strptime('23:00', "%H:%M").time()
    day_end_total = datetime.datetime.strptime('23:59', "%H:%M").time()
    day_start_total = datetime.datetime.strptime('00:00', "%H:%M").time()
    night_end_departure = datetime.datetime.strptime('12:00', "%H:%M").time()

    query_1 = (f'https://api.rasp.yandex.net/v3.0/schedule/?'
               f'apikey={YANDEX_TRANSPORT_API_KEY}'
               f'&station={station_code}'
               f'&lang={lang}'
               f'&format={json_response}'
               f'&date={date_1}'
               f'&transport_types={transport_type}'
               f'&event={event}'
               f'&system={system}'
               f'&show_systems=yandex')

    query_2 = (f'https://api.rasp.yandex.net/v3.0/schedule/?'
               f'apikey={YANDEX_TRANSPORT_API_KEY}'
               f'&station={station_code}'
               f'&lang={lang}'
               f'&format={json_response}'
               f'&date={date_2}'
               f'&transport_types={transport_type}'
               f'&event={event}'
               f'&system={system}'
               f'&show_systems=yandex')

    if selected_shift_type == 'night':

        #  Запрос на текущую дату
        r_1 = requests.get(query_1).json()
        j_1 = json.dumps(r_1, indent=8)
        for i in json.loads(j_1)['schedule']:
            _from = i['thread']['title'].split(' — ')[event_type].lower()
            fl_time = str(i[event]).split('T')[-1].split('+')[0][:5]
            fl_time = datetime.datetime.strptime(fl_time, "%H:%M").time()
            if _from not in ru_cities:
                if day_end < fl_time < day_end_total:
                    schedule_pool.append(i)

        #  Запрос на следующую дату
        r_2 = requests.get(query_2).json()
        j_2 = json.dumps(r_2, indent=8)
        for i in json.loads(j_2)['schedule']:
            _from = i['thread']['title'].split(' — ')[event_type].lower()
            fl_time = str(i[event]).split('T')[-1].split('+')[0][:5]
            fl_time = datetime.datetime.strptime(fl_time, "%H:%M").time()
            if _from not in ru_cities:
                if day_start_total < fl_time < night_end_departure:
                    schedule_pool.append(i)

        for i in schedule_pool:
            _from = i['thread']['title'].split(' — ')[event_type].lower()
            fl_time = str(i[event]).split('T')[-1].split('+')[0][:5]
            fl_time = datetime.datetime.strptime(fl_time, "%H:%M").time()

            if direction == 'arrival':
                if day_end < fl_time < day_end_total or day_start_total < fl_time < day_end:

                    try:
                        if raw_data[-1] != (i[event], _from):
                            raw_data.append((i[event], _from, i['thread']['number']))
                    except:
                        raw_data.append((i[event], _from, i['thread']['number']))

            elif direction == 'departure':
                if day_end < fl_time < day_end_total or day_start_total < fl_time < night_end_departure:
                    try:
                        if raw_data[-1] != (i[event], _from):
                            raw_data.append((i[event], _from, i['thread']['number']))
                    except:
                        raw_data.append((i[event], _from, i['thread']['number']))

    if selected_shift_type != 'night':

        #  Запрос на текущую дату
        r_1 = requests.get(query_1).json()
        j_1 = json.dumps(r_1, indent=8)
        for i in json.loads(j_1)['schedule']:
            _from = i['thread']['title'].split(' — ')[event_type].lower()
            if _from not in ru_cities:
                schedule_pool.append(i)

        for i in schedule_pool:
            _from = i['thread']['title'].split(' — ')[event_type].lower()
            if _from not in ru_cities:
                print(i[event], i['thread']['title'])
                fl_time = str(i[event]).split('T')[-1].split('+')[0][:5]
                if selected_shift_type == 'day':

                    fl_time = datetime.datetime.strptime(fl_time, "%H:%M").time()

                    if direction == 'arrival':
                        if day_start < fl_time < day_end:
                            try:
                                if raw_data[-1] != (i[event], _from):
                                    raw_data.append((i[event], _from, i['thread']['number']))
                            except:
                                raw_data.append((i[event], _from, i['thread']['number']))

                    elif direction == 'departure':
                        if day_start < fl_time < day_end_departure:
                            try:
                                if raw_data[-1] != (i[event], _from):
                                    raw_data.append((i[event], _from, i['thread']['number']))
                            except:
                                raw_data.append((i[event], _from, i['thread']['number']))

                elif selected_shift_type == '24':
                    try:
                        if raw_data[-1] != (i[event], _from):
                            raw_data.append((i[event], _from, i['thread']['number']))
                    except:
                        print(traceback.format_exc())
                        raw_data.append((i[event], _from, i['thread']['number']))
    raw_data = sorted(raw_data)
    count = 1
    for data in raw_data:
        tm = '<code>' + str(data[0]).split('T')[0] + ' ' + str(data[0]).split('T')[-1].split('+')[0][:5] + '</code>'
        fl = str(data[2])
        ds = '<i>' + str(data[1]).capitalize() + '</i>'
        text = str(count) + ') ' + tm + ' | ' + fl + ' | ' + ds
        bot.send_message(message.chat.id, text=text, parse_mode='HTML')
        count += 1
    bot.send_message(message.chat.id, text='Начать поиск заново /start')
    for sh in schedule_pool:
        print(sh)


def clear_user(user):
    user.update(selected_station='', selected_date='', selected_shift_type='', selected_direction='', )


@bot.message_handler(commands=['start'])
def start(message):
    try:
        User.objects.create(telegram_id=message.from_user.id,
                            username=message.from_user.username,
                            first_name=message.from_user.first_name,
                            last_name=message.from_user.last_name)
    except:
        pass

    bot.send_message(message.chat.id, text='Добро пожаловать, бла-бла-бла выберите ваш международный аэропорт',
                     reply_markup=kb.start_markup())


@bot.callback_query_handler(func=lambda call: True)
def schedule_callback_query_handler(call):
    user = User.objects.filter(telegram_id=call.from_user.id)
    query = call.data.split(':')

    if 'start' in query:
        if 'station' in query:
            station = query[-1]

            # todo add station / iata reference
            if station == 'koltsovo':
                station = 'SVX'
            else:
                station = 'SVX'

            user.update(selected_station=station)
            now = datetime.datetime.now()  # Get the current date
            bot.send_message(chat_id=call.message.chat.id,
                             text="Selected date",
                             reply_markup=calendar.create_calendar(
                                 name=calendar_1_callback.prefix,
                                 year=now.year,
                                 month=now.month), )

        elif 'type' in query:

            if '24' in query:
                user.update(selected_shift_type='24')
                bot.send_message(chat_id=call.message.chat.id, text="Выборка за сутки",
                                 reply_markup=kb.direction_type())

            elif 'day' in query:
                user.update(selected_shift_type='day')
                bot.send_message(chat_id=call.message.chat.id, text="Выборка за дневную смену (9:00-20:00)")
                bot.send_message(chat_id=call.message.chat.id, text="Выберите направление",
                                 reply_markup=kb.direction_type())

            elif 'night' in query:
                user.update(selected_shift_type='night')
                bot.send_message(chat_id=call.message.chat.id, text="Выборка за ночную смену (20:00-9:00)")
                bot.send_message(chat_id=call.message.chat.id, text="Выберите направление",
                                 reply_markup=kb.direction_type())
        elif 'dir' in query:

            if 'arrival' in query:
                user.update(selected_direction='arrival')
                bot.send_message(chat_id=call.message.chat.id, text="Выбран Прилёт")
                get_schedule(
                    station=User.objects.get(pk=call.message.chat.id).selected_station,
                    direction=User.objects.get(pk=call.message.chat.id).selected_direction,
                    selected_date=User.objects.get(pk=call.message.chat.id).selected_date,
                    selected_shift_type=User.objects.get(pk=call.message.chat.id).selected_shift_type,
                    bot=bot,
                    message=call.message
                )

            elif 'departure' in query:
                user.update(selected_direction='departure')
                bot.send_message(chat_id=call.message.chat.id, text="Выбран Вылет")
                get_schedule(
                    station=User.objects.get(pk=call.message.chat.id).selected_station,
                    direction=User.objects.get(pk=call.message.chat.id).selected_direction,
                    selected_date=User.objects.get(pk=call.message.chat.id).selected_date,
                    selected_shift_type=User.objects.get(pk=call.message.chat.id).selected_shift_type,
                    bot=bot,
                    message=call.message
                )
    # Calendar
    name, action, year, month, day = call.data.split(calendar_1_callback.sep)
    selected_date = calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )
    if action == "DAY":
        bot.send_message(
            chat_id=call.from_user.id,
            text=f"Выбрана дата: {selected_date.strftime('%d.%m.%Y')}",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{calendar_1_callback}: Day: {selected_date.strftime('%d.%m.%Y')}")
        selected_date = selected_date.strftime('%Y-%m-%d')
        user.update(selected_date=selected_date)
        bot.send_message(chat_id=call.message.chat.id, text='Выберите тип выборки в соответствии с вашей сменой',
                         reply_markup=kb.shift_type())

    elif action == "CANCEL":
        bot.send_message(
            chat_id=call.from_user.id,
            text="Cancellation",
            reply_markup=ReplyKeyboardRemove(),
        )
        clear_user(user)
        print(f"{calendar_1_callback}: Cancellation")


bot.infinity_polling()
