import time
from random import randint
import re
import base64
import hashlib
from tkinter import *
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

version = "3.1 (rewrited)" # Версия проекта
print("RedStar Corporation | Discord - green_tea_bag | Telegram - t.me/RedStarEngineers | Version", version)

# show
def show(text):
    console.config(state=NORMAL)
    console.insert(END, "\n"+text+"\n")
    console.config(state=DISABLED)

# Кнопка ввода
def Input():
    UserAnswer = input_text.get("1.0", END+"-1c")
    print(f'\nsystem/terminal> Отправлено: "{UserAnswer}"')
    input_text.delete("1.0", END)
    show("user> "+UserAnswer)

    # UserAnswer
    UserAnswer = UserAnswer.lower()
    if UserAnswer == "":
        UserAnswer = ""
    elif UserAnswer == "help": # help
        show("system> Все имеющиеся запросы:\n- Пусто (пока что)") # Не уносить
    else:
        show(f'system> Допущена ошибка! "{UserAnswer}" не является встроенной командой. Попробуйте "help".')

# Tkinter (main)
print("\nsystem/terminal> Запуск окна")
main = Tk()
main.title("Miner "+version)
main.geometry("800x670")
main.resizable(False, False)
main.configure(bg="black")

# info
info = Label(text="\nRedStar Corporation | Discord - green_tea_bag | Telegram - t.me/RedStarEngineers | Version "+version+"\n", font=("Arial Black", 10), bg="black", fg="white")
info.pack()

# console
console_frame = Frame(master=main)
console = Text(console_frame, height=28, width=90, font=("Arial Black", 9), bg="#181818", fg="white", bd=5, state=DISABLED, wrap=WORD)
console.grid(column=0, row=0)

# scroll
scroll = Scrollbar(console_frame, command=console.yview)
scroll.grid(column=1, row=0, sticky="ns")
console.config(yscrollcommand=scroll.set)
console_frame.config(bg="black")
console_frame.pack(side=TOP)

# status
status = Label(text=f"\nMoney: {money} | Shop: {shop} | Others: {others}\n", font=("Arial Black", 10), bg="black", fg="white")
status.pack() # Текст выше будет переделан в будущем, чтобы там были красивые значения, а не то, что сейчас

# input
input = Frame(master=main)
input_text = Text(input, height=1, width=85, font=("Arial Black", 9), bg="#181818", fg="white", bd=5)
input_text.grid(column=0, row=0)
input_button = Button(input, height=1, width=5, font=("Arial Black", 9), bg="#181818", fg="white", bd=5, activebackground="black", text="ввод", command=Input)
input_button.grid(column=1, row=0)
input.config(bg="black")
input.pack(side=TOP)

# pressed
#pressed = Entry(main)
#pressed.pack()
#pressed.bind("<Return>", lambda event: Input())
#   Планировал заменить input_text на Entry, чтобы можно было не нажимая на кнопку ввода нажать Enter и ввести сообщение
#   Однако понял, что некоторые функции не работают с Entry как с тексом
#   А так как я проделал большую работу и ещё ничего не выкладывал в ТГ, то можно сказать, что я работаю без бэкапов

# Первые сообщения
print("\nsystem/terminal> Окно запущено")
console.config(state=NORMAL)
console.insert(END, "system> Добро пожаловать в PyMinerCMD!\n")
console.insert(END, 'system> Начнисе с "help" для помощи.\n')
console.config(state=DISABLED)

# mainloop
main.mainloop()
print("\nsystem/terminal> Окно было закрыто")