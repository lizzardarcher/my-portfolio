from telebot import TeleBot

bot = TeleBot(token='<KEY>')



@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    if message.json['new_chat_participant']['is_bot'] == 123:
        bot.send_message(message.chat.id, 'всем чмоки в этом чатике')