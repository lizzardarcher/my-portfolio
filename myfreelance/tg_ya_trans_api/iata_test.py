# from utils import djangoORM
# from tg_ya_trans_api.models import IATA_ICAO
#
#
# import csv
# iata_list = list()
#
# with open('iata-icao.csv', newline='', mode='r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         iata_list.append((row))
#
# for i in iata_list:
#
#     country_code = i[0]
#     region_name = i[1]
#     iata = i[2]
#     icao = i[3]
#     airport = i[4]
#     print(country_code, region_name, iata, icao, airport, sep=' || ')
#     IATA_ICAO.objects.create(country_code=country_code, region_name=region_name, iata=iata, airport=airport, icao=icao)
#

l = []
with open('airports.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        l.append(i.replace('\n', ''))

with open('airports.txt', 'w') as file:
    for i in l:
        file.writelines(i.lower())
        file.writelines('\n')