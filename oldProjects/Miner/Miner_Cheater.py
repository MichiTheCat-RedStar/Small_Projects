'''Читерилка для майнера 2.2'''

import base64
print("Добро пожаловать в Miner2.2 trainer")
print("")
saved_money = int(input("сколько денег: "))*10*16+8 #деньги
saved_mined = int(input("сколько циклов: "))*16+12 #циклы 
vip = input("vip (0/1): ") #випка
cfs = input("cfs (0/1): ")#фильтрация циклов
code = f"SMy_{saved_money}-PMC-SMd_{saved_mined}_SS-{vip}-{cfs}"# создание кода сохранения
print("загрузи в майнер: ", base64.b64encode(code.encode('ascii')).decode('ascii'))#кодирование кода сохранения
