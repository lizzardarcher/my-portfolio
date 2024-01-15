from pyrogram import Client

api_id = 27618579
api_hash = '2bde502799414029ff5e63be8b9529e8'
name = str(api_id) + api_hash
phone = '+79080409710'

client = Client(name=name, api_id=api_id, api_hash=api_hash, phone_number=phone, device_model="iPhone 11 Pro",
                system_version="14.7.1", app_version="8.5", lang_code="en")
client.start()
client.stop()
