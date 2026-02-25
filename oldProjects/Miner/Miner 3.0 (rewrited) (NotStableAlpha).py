import time
from random import randint
import re
import base64
import hashlib
from tkinter import *
from tkinter import ttk
# Тут должны быть только встроенные библиотеки

money = {    # Валюты
    "PMC": 0, # PythonMinerCoins - основная валюта
    "FM": 0 # FireMoney - несохраняемая валюта
}
shop = {    # Товары магазина
    "CF": False, # CycleFilter - исключает невыгодные циклы
    "SCS": False # SuccessfulCyclesSystem - исключает неудачные циклы
}
others = {    # Остальное
    "mined": 0 # Количество раз фарма
}

# Больше нет встроенного античита, так как код на то и open source, чтобы его мог поменять любой под себя)
# Автор кода: Discord - green_tea_bag | Telegram - t.me/RedStarEngineers

version = "3.0 (rewrited)" # Версия проекта
print("RedStar Corporation | Discord - green_tea_bag | Telegram - t.me/RedStarEngineers | Version", version)

# Tkinter (main)
print("\nsystem/terminal> Запуск окна")
main = Tk()
main.title("Miner "+version)
main.geometry("800x600")
main.resizable(False, False)
main.configure(bg="black")

# info
info = ttk.Label(text="RedStar Corporation | Discord - green_tea_bag | Telegram - t.me/RedStarEngineers | Version "+version, font=("Arial Black", 10))
info.pack()

main.mainloop()

print("\nsystem/terminal> Окно было закрыто")