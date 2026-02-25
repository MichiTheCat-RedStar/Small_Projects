import time
from random import randint
import re

money = 0
mined = 0
cheats = False
shop = {"VIP":False}

print("RedStar Corporation | discord - green_tea_bag | version: 2 | 196 строк кода")
print("\nsystem> Добро пожаловать в PyMinerCMD!")
print('system> Начнисе с "help" для помощи.')

if (money or mined != 0) or (shop["VIP"]):
    exit()

def Mine(Counts):
    global money
    global mined
    for i in range(Counts):
        TempNow = 0
        print("\nsystem> Идёт поиск свободных циклов...")
        fat = randint(0,1)
        if fat == 0:
            Temp = randint(3, 123)
        else:
            Temp = randint(1440, 5255)
        time.sleep(randint(5, 35)/10)
        print("system> Цикл найден.")
        print("system> Начинается вычисление...\n")
        time.sleep(randint(1, 15)/10)
        start = time.time()
        if fat == 0:
            while TempNow != Temp:
                print(f"system> Решается... [{TempNow}/{Temp}]")
                TempNow += 1
                if not shop["VIP"]:
                    time.sleep(randint(10, 200)/100)
                else:
                    time.sleep(randint(5, 100)/100)
        else:
            while TempNow != Temp:
                print(f"system> Решается... [{TempNow}/{Temp}]")
                TempNow += 1
                if not shop["VIP"]:
                    time.sleep(randint(5, 150)/1000)
                else:
                    time.sleep(randint(5, 75)/1000)
        finish = time.time()
        if fat == 0:
            cash = randint(1, 50)/10
        else:
            cash = randint(25, 405)/10
        money += cash
        mined += 1
        OutTime = finish - start
        print(f"\nsystem> Цикл выполнен! Заработано: {cash} PMC за {int(OutTime)} секунд")

if (money or mined != 0) or (shop["VIP"]):
    cheats = True

while True:
    UserAnswer = input("\nuser> ")

    if UserAnswer == "help":
        print("\nsystem> Все имеющиеся запросы:\n")
        print("help          Помощь по запросам")
        print("save          Сохранить прогресс в виде встаиваемого кода")
        print("load          Загрузить встраиваемый код (используйте только при наличии кода, иначе можно потерять весь прогресс)")
        print("exit          Закрыть PyMinerCMD")
        print("start         Запустить один цикл майнинга")
        print("morestart     Запустить выбранное вами количество циклов майнинга")
        print("info          Ваша статистика")
        print("update        Информация об обновлениях программы")
        print("cheats        Включает читы, но отключает сохранения")
        print("shop          Выход в магазин с возможностью улучшения PyMinerCMD")
    
    elif (UserAnswer == "save") and (not cheats):
        saved_money = int(((money * 10) * 16) + 8)
        saved_mined = int((mined * 16) + 12)
        code = f"SMy_{saved_money}-PMC-SMd_{saved_mined}_SS-{int(shop['VIP'])}"
        if cheats:
            code = "DieSillyCheater"
        print("\nsystem> Код вашего сохранения:", code)
    elif (UserAnswer == "save") and (cheats):
        print("\nadmin> Читерам сохранение запрещено.")

    elif UserAnswer == "load":
        print("\nsystem> Введите код сохранения.")
        UserAnswer = input("\nuser> ")
        if (UserAnswer == "Add+100PMC_Now") and (cheats):
            money += 100
            print("\nadmin> +100 PMC")
        elif (UserAnswer == "Add+25Minde_Now") and (cheats):
            mined += 25
            print("\nadmin> +25 циклов")
        else:
            try:
                decode = re.findall(r"\d+", UserAnswer)
                money = (int((int(decode[0])-8)/16))/10
                mined = int((int(decode[1])-12)/16)
                shop["VIP"] = bool(decode[2])
                print("\nsystem> Успешно загружено.")
            except Exception:
                print("\nsystem> Вы ввели код неверно и действие было отменено.")

    elif UserAnswer == "exit":
        break
    
    elif UserAnswer == "start":
        Mine(1)

    elif UserAnswer == "morestart":
        try:
            print("\nsystem> Сколько циклов вы хотите?")
            UserAnswer = int(input("\nuser> "))
            Mine(UserAnswer)
            print("\nsystem> Линейка циклов выполнена.")
        except Exception:
            print("\nsystem> Вы ввели число неверно и действие было отменено.")

    elif UserAnswer == "info":
        print(f"\nsystem> Количество заработанных денег: {money} PMC.")
        print(f"system> Количество запущенных циклов: {mined} раз.")
        if mined != 0:
            MinedToMoney = int(((money/mined)*100)/20)
            print(f"system> Процент Денег/Циклов: {MinedToMoney}%.")
        print(f"system> Приобретённые товары: VIP - {shop['VIP']}.")

    # Мне душно, вынесите это куда-то, пожалуйста
    elif UserAnswer == "update":
        print("\nsystem> Вот весь список обновлений:")
        print("\n-----= 2 =-----\n")
        print("Значительное обновление")
        print("Добавлены: Был добавлен магазин, проработаено его сохранение и вывод в информацию, на базе чего в дальнейшем можно сделать много товаров без проблем с переписыванием всего кода")
        print("\n-----= 1.5.3 =-----\n")
        print("Очень незначительное обновление")
        print("Изменения: Немного оптимизирвоан код")
        print("\n-----= 1.5.2 =-----\n")
        print("Очень незначительное обновление")
        print("Добавлены: ---")
        print("\n-----= 1.5 =-----\n")
        print("Незначительное обновление")
        print("Добавлены: morestart из-за которого немного был изменён код")
        print("\n-----= 1.4 =-----\n")
        print("Незначительное обновление")
        print("Добавлены: Подтверждение включения читов и время выполнения одного цикла")
        print("Исправлены: Теперь при неправильном коде загрузки программа не закрывается, а отменяет действие")
        print("\n-----= 1.3 =-----\n")
        print("Незначительное обновление")
        print("Добавлены: Добавлены читы")
        print("\n-----= 1.2 =-----\n")
        print("Незначительное обновление")
        print("Изменения: Наконец-то изменена система сохранений до желаемого результата")
        print("\n-----= 1.1 =-----\n")
        print("Незначительное обновление")
        print("Добавлены: Теперь можно фармить большие кластеры данных")
        print("Изменения: info более правильно показывае проценты, система сохранений и ожидания была немного изменена")
        print("Исправвления: Исправлена ошибка сохранений, теперь вам не надо писать выдающие ошибку float значения")
        print("\n-----= 1.0 =-----\n")
        print("Программа была создана")
        print("Добавлены: help, save, load, start, info, exit, update")
        print("Планируется изменение системы сохранения, чтобы код нельзя было подделать")

    elif (UserAnswer == "cheats") and (not cheats):
        print("\nsystem> Вы уверены? [Y/N]")
        UserAnswer = input("\nuser> ")
        if UserAnswer == "Y":
            cheats = True
            print("\nadmin> Читы включены.")
        elif UserAnswer == "N":
            print("\nsystem> Читы не были включены.")
        else:
            print("\nsystem> Вы ввели ответ неверно и действие было отменено.")
    elif (UserAnswer == "cheats") and (cheats):
        print("\nadmin> Читы уже были включены ранее.")

    elif (UserAnswer == "shop"):
        print("\nsystem> Выберите одну из позиций:")
        print("VIP [115 PMC] Покупка VIP статуса, который ускорит работу")
        UserAnswer = input("\nuser> ")
        if UserAnswer == "VIP":
            if not shop["VIP"]:
                if money >= 115:
                    money -= 115
                    shop["VIP"] = True
                    print("\nsystem> Вы умпешно купили VIP статус.")
                else:
                    print("\nsystem> Вы слишком нищий для покупки этого и действие было отменено.")
            else:
                print("\nsystem> У вас уже есть VIP статус.")
        else:
             print("\nsystem> Вы ввели ответ неверно и действие было отменено.")

    else:
        print(f'\nsystem> Допущена ошибка! "{UserAnswer}" не является встроенной командой. Попробуйте "help".')