import time
from random import randint

money = 0
mined = 0

print("RedStar Corporation | discord - green_tea_bag | version: 1.0")
print("\nsystem> Добро пожаловать в PyMinerCMD!")
print("system> Начнисе с help для помощи.")

while True:
    UserAnswer = input("\nuser> ")

    if UserAnswer == "help":
        print("\nsystem> Все имеющиеся запросы:\n")
        print("help      Помощь по запросам")
        print("save      Сохранить прогресс в виде встаиваемого кода")
        print("load      Загрузить встраиваемый код (используйте только при наличии кода, иначе можно потерять весь прогресс)")
        print("exit      Закрыть PyMinerCMD")
        print("start     Запустить один цикл майнинга")
        print("info      Ваша статистика")
        print("update    Информация об обновлениях программы")

    elif UserAnswer == "save":
        saved_money = (money * 16) + 8
        saved_mined = (mined * 16) + 12
        print(f"\nsystem> Код денег: {saved_money}  |  Код циклов: {saved_mined}")

    elif UserAnswer == "load":
        print("\nsystem> Введите код денег.")
        UserAnswer = input("\nuser> ")
        money = int((int(UserAnswer)-8)/16)
        print("\nsystem> Введите код циклов.")
        UserAnswer = input("\nuser> ")
        mined = int((int(UserAnswer)-12)/16)

    elif UserAnswer == "exit":
        break
    
    elif UserAnswer == "start":
        TempNow = 0
        print("\nsystem> Идёт поиск свободных циклов...")
        Temp = randint(3, 100)
        time.sleep(randint(5, 35)/10)
        print("system> Цикл найден.")
        print("system> Начинается вычисление...\n")
        time.sleep(randint(1, 10)/10)
        while TempNow != Temp:
            print(f"system> Решается... [{TempNow}/{Temp}]")
            TempNow += 1
            time.sleep(randint(1, 20)/10)
        cash = randint(1, 50)/10
        money += cash
        mined += 1
        print("\nsystem> Цикл выполнен! Заработано:", cash, "PMC")

    elif UserAnswer == "info":
        print(f"\nsystem> Количество заработанных денег: {money} PMC.")
        print(f"system> Количество запущенных циклов: {mined} раз.")
        if mined != 0:
            MinedToMoney = (mined/money)*100
            print(f"system> Процент Циклов/Денег: {MinedToMoney}%.")

    elif UserAnswer == "update":
        print("\nsystem> Вот весь список обновлений:")
        print("\n-----= 1.0 =-----\n")
        print("Программа была создана")
        print("Добавлены: help, save, load, start, info, exit, update")
        print("Планируется изменение системы сохранения, чтобы код нельзя было подделать")

    else:
        print(f'\nsystem> Допущена ошибка! "{UserAnswer}" не является встроенной командой. Попробуйте "help".')