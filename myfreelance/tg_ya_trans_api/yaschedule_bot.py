import requests

YANDEX_TRANSPORT_API_KEY = '0fc89cc2-b4d4-4ee5-9e2e-a403760c330e'

request = f'''
    https://api.rasp.yandex.net/v3.0/schedule/ ?
      apikey={YANDEX_TRANSPORT_API_KEY}
    & station=<код станции>
    & [lang=<язык>]
    & [format=<формат>]
    & [date=<дата>]
    & [transport_types=<тип транспорта>]
    & [event=<прибытие или отправление>]
    & [system=<система кодирования для параметра station>]
    & [show_systems=<коды в ответе>]
    & [direction=<направление>]
    & [result_timezone=<часовой пояс>]
'''
