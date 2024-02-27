from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from tg_ya_trans_api.utils import djangoORM
from tg_ya_trans_api.models import Airport


def start_markup(*args, **kwargs):
    markup = InlineKeyboardMarkup()
    airports = Airport.objects.all()
    for airport in airports:
        markup.add(InlineKeyboardButton(text=f"✈ {airport.airport}", callback_data=f"start:station:{airport.iata}"))
    return markup


def shift_type(*args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("☀ День", callback_data=f"start:type:day"))
    markup.add(InlineKeyboardButton("🌙 Ночь", callback_data=f"start:type:night"))
    markup.add(InlineKeyboardButton("🕛 Сутки", callback_data=f"start:type:24"))
    return markup


def direction_type(*args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🛬 Прилёт", callback_data=f"start:dir:arrival"))
    markup.add(InlineKeyboardButton("🛫 Вылет", callback_data=f"start:dir:departure"))
    return markup
