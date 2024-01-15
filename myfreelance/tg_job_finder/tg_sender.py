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
auto_reply_delay= settings.auto_reply_delay
common_message = settings.common_message
common_message_delay = settings.common_message_delay


async def auto_sender():
    async with Client(name=name) as app:
        while True:
            for chat in chats:
                try:
                    await app.send_message(chat_id=chat, text=common_message)
                    await asyncio.sleep(13.7)
                except Exception as e:
                    print(traceback.format_exc())
            await asyncio.sleep(common_message_delay*60)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(auto_sender())
    loop.run_forever()
