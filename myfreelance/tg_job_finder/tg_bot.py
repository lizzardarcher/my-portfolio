import asyncio
from time import sleep
import datetime
import json
import traceback
import logging
import threading

from pyrogram import Client, compose, idle, filters
from pyrogram.handlers import MessageHandler

import utils.djangoORM
from tg_job_finder.models import *

logging.basicConfig(level=logging.WARNING)

settings = Settings.objects.get(pk=1)
api_id = settings.api_id
api_hash = settings.api_hash
name = str(api_id) + api_hash
phone = settings.phone
session = settings.session
chats = [str(x.link).split('/')[-1] for x in TgChat.objects.all()]
auto_reply_message = settings.auto_reply_message
auto_reply_delay = settings.auto_reply_delay
common_message = settings.common_message
common_message_delay = settings.common_message_delay

print(chats)
# client = Client(name=str(session))
# client = Client(name=name, api_id=api_id, api_hash=api_hash, phone_number=phone, device_model="iPhone 11 Pro",
#             system_version="14.7.1", app_version="8.5", lang_code="en")


app = Client(name=name + '2')


@app.on_message(filters.chat(chats))
async def auto_reply(client, message):
    # print(message.id)
    message = str(message.text)
    alw1level = [x.word for x in AllowedWord1Level.objects.all()]
    alw2level = [x.word for x in AllowedWord2Level.objects.all()]
    disw = [x.word for x in DisallowedWord.objects.all()]
    exclw = [x.word for x in ExcludeWord.objects.all()]
    # print(alw1level, alw2level, disw, exclw, sep="\n")
    flag = True
    flag_next_2 = False
    flag_next_3 = False
    msg = message.lower().split()
    for word in msg:
        if word in exclw:
            msg.remove(word)

    for dis in disw:
        for word in msg:
            if dis == word:
                flag = False

    if flag:
        for a1l in alw1level:
            for word in msg:
                if a1l == word:
                    print(message)
                    flag_next_2 = True

    # if flag_next_2:
    #     for a2l in alw2level:
    #         for word in msg:
    #             if a2l == word:
    #                 flag_next_3 = True
    #
    # if flag_next_3:
    #     print(message)


app.run()
