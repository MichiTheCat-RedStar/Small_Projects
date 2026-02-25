import time
from random import randint
import re
import base64 

money = 0
mined = 0
cheats = False
shop = {"VIP":False, "CFS":False}
FireMoney = 0
FireMiner = False  # В будущем будет изменено

UserAnswer = ""

print("RedStar Corporation | discord - green_tea_bag | version: 2.3 | 357 строк кода")
print("\nsystem> Добро пожаловать в PyMinerCMD!")
print('system> Начнисе с "help" для помощи.')

# Внешний Античит (защита компилирвоанного кода или от внешних сохранений)
if (money or mined != 0) or (shop["VIP"]) or (shop["CFS"]) or (FireMoney != 0) or (FireMiner != False):
    exit()
if mined != 0:
    if (MinedToMoney := int(((money/mined)*100)/20)) > 203:
        exit()

# Mine
def Mine(Counts):
    global money
    global mined
    global FireMiner
    global FireMoney
    for i in range(Counts):
        TempNow = 0
        print("\nsystem/mine> Идёт поиск свободных циклов...")
        fat = bool(randint(0,1))
        if not fat:
            Temp = randint(3, 123)
        else:
            Temp = randint(1440, 5255)
        time.sleep(randint(5, 35)/10)
        print("system/mine> Цикл найден.")
        print("system/mine> Начинается вычисление...\n")
        time.sleep(randint(1, 15)/10)
        start = time.time()
        if not fat:
            while TempNow != Temp:
                print(f"system/mine> Решается... [{TempNow}/{Temp}]")
                TempNow += 1
                if not shop["VIP"]:
                    time.sleep(randint(10, 200)/100)
                else:
                    time.sleep(randint(5, 100)/100)
        else:
            while TempNow != Temp:
                print(f"system/mine> Решается... [{TempNow}/{Temp}]")
                TempNow += 1
                if not shop["VIP"]:
                    time.sleep(randint(5, 150)/1000)
                else:
                    time.sleep(randint(5, 75)/1000)
        finish = time.time()
        if not fat:
            if not shop["CFS"]:
                cash = randint(1, 50)/10
            else:
                cash = randint(25, 50)/10
        else:
            if not shop["CFS"]:
                cash = randint(25, 405)/10
            else:
                cash = randint(175, 405)/10
        money += cash
        mined += 1
        OutTime = finish - start
        print(f"\nsystem/mine> Цикл выполнен! Заработано: {cash} PMC за {int(OutTime)} секунд")
        if FireMiner == True:
            FireMoney += 0.5
            print("system/mine> Добавлено 0.5 FireMoney на счёт")

# Shop
#def Shop(position, price, currency, one_time_purchase, how_many):
#    global shop
#    global money
#    global FireMiner
#    global FireMoney                         # Задел под будущее

if (money or mined != 0) or (shop["VIP"]) or (shop["CFS"]) or (FireMoney != 0) or (FireMiner != False):
    cheats = True

while True:

    if (UserAnswer == "clear") and (money != 0) and (mined != 0):
        exit()

    UserAnswer = input("\nuser> ")

    # help
    if UserAnswer == "help":
        print("\nsystem> Все имеющиеся запросы:\n") # Не уносить
        print("help          Помощь по запросам")
        print("save          Сохранить прогресс в виде встаиваемого кода")
        print("load          Загрузить встраиваемый код (используйте только при наличии кода, иначе можно потерять весь прогресс)")
        print("exit          Закрыть PyMinerCMD")
        print("start         Запустить один цикл майнинга")
        print("morestart     Запустить выбранное вами количество циклов майнинга")
        print("info          Ваша статистика")
        print("changelog     Информация об обновлениях программы")
        print("shop          Выход в магазин с возможностью улучшения PyMinerCMD")
        print("clear         Очистить данные текущей сессии")
        print("bug           Вы можете написать о найденом баге здесь")
    
    # save
    elif (UserAnswer == "save") and (not cheats):
        saved_money = int(((money * 10) * 16) + 8)
        saved_mined = int((mined * 16) + 12)
        code = f"SMy_{saved_money}-PMC-SMd_{saved_mined}_SS-{int(shop['VIP'])}-{int(shop['CFS'])}" # SavedMoney_{SMy}-PythonMinerCoins-SavedMined_{SMd}_SavedShop-{VIP}-{CFS}
        if cheats:
            code = "DieSillyCheater"
            print("\nsystem> Читерить - плохо!")
        print("\nsystem> Код вашего сохранения:", base64.b64encode(code.encode('ascii')).decode('ascii'))
    elif (UserAnswer == "save") and (cheats):
        print("\nadmin> Читерам сохранение запрещено.")

    # load
    elif UserAnswer == "load":
        print("\nsystem/load> Введите код сохранения.")
        if (FireMoney != 0) or (FireMiner == True):
            print("system/load> FireMoney будет стёрт.")
        UserAnswer = input("\nuser> ")
        if (UserAnswer == "Add+100PMC_Now") and (cheats):
            money += 100
            print("\nadmin> +100 PMC")
        elif (UserAnswer == "Add+25Minde_Now") and (cheats):
            mined += 25
            print("\nadmin> +25 циклов")
        else:
            if UserAnswer == "U015XzgtUE1DLVNNZF8xMl9TUy0xLTE=":
                print("\nsystem/load> Предположитеьно что-то идёт не так.")
            # U015XzY0MDgtUE1DLVNNZF8yOF9TUy0wLTA= - SMy_6408-PMC-SMd_28_SS-0-0
            decodeBase = base64.b64decode(UserAnswer.encode('ascii')).decode('ascii')
            decodeTxt = re.findall(r"\D+", decodeBase)         # Почему-то работает неправильно
            if (decodeTxt[0] == "SMy_") and (decodeTxt[1] == "-PMC-SMd_") and (decodeTxt[2] == "_SS-") and (decodeTxt[3] == "-"):
                try:
                    decodeInt = re.findall(r"\d+", decodeBase)
                    money = (int((int(decodeInt[0])-8)/16))/10
                    mined = int((int(decodeInt[1])-12)/16)
                    shop["VIP"] = bool(int(decodeInt[2]))
                    shop["CFS"] = bool(int(decodeInt[3]))
                    print("\nsystem/load> Успешно загружено.")
                    FireMiner = False
                    FireMoney = 0
                except Exception:
                    print("\nsystem> Вы ввели код неверно и действие было отменено.")
                if (money == 0) and (mined == 0) and (shop["CFS"] == True) and (shop["VIP"] == True):
                    print("system> Предположитеьно что-то пошло так.")
                    shop = {"VIP":False, "CFS":False}
                if mined != 0:
                    if (MinedToMoney := int(((money/mined)*100)/20)) > 203:
                        exit()
            else:
                print("\nsystem> Вы ввели код неверно и действие было отменено.")

    # exit
    elif UserAnswer == "exit":
        exit()
    
    # start
    elif UserAnswer == "start":
        Mine(1)

    # morestart
    elif UserAnswer == "morestart":
        try:
            print("\nsystem/mine> Сколько циклов вы хотите?")
            UserAnswer = int(input("\nuser> "))
            Mine(UserAnswer)
            print("\nsystem/mine> Линейка циклов выполнена.")
        except Exception:
            print("\nsystem> Вы ввели число неверно и действие было отменено.")

    # info
    elif UserAnswer == "info":
        print(f"\nsystem> Количество заработанных денег: {money} PMC.")
        print(f"system> Количество запущенных циклов: {mined} раз.")
        if mined != 0:
            MinedToMoney = int(((money/mined)*100)/20)
            print(f"system> Процент Денег/Циклов: {MinedToMoney}%.")
        print(f"system> Приобретённые товары: VIP - {shop['VIP']}, CFS - {shop['CFS']}, FMM - {FireMiner}.")
        if FireMoney != 0:
            print(f"system> Количество FireMoney: {MinedToMoney}.")

    # update
    # Мне душно, вынесите это куда-то, пожалуйста
    # Бессмысленно занимает много места, но и в одну строку выглядело бы глупо, а отдельный файл - не вариант
    elif UserAnswer == "changelog":
        # Изменены:  Добавлены:  Исправлены:  
        print("\nsystem/changelog> Вот весь список обновлений:") # Не уносить
        print("\n-----= 2.3.2 =-----\n")
        print("Незначительное обновление")
        print("Изменены:")
        print("- Теперь показывает вызваную функцию в директори, если это имеет смысл")
        print("\n-----= 2.3 =-----\n")
        print("Обычное обновление")
        print("Изменены:")
        print("- Улучшен внешний античит ещё больше, а так же переделаны пара систем")
        print("Добавлены:")
        print("- Добавлен FireMoney, но пока он не такой, как планирвоалось и это будет в будущем изменено (загляните в shop)")
        print("- Добавлена команда Bug")
        print("\n-----= 2.2.2 =-----\n")
        print("Незначительное обновление")
        print("Добавлены: Улучшен внешний античит")
        print("\n-----= 2.2 =-----\n")
        print("Обычное обновление")
        print("Изменения: Изменён способ сохранения, таперь код более удобен для копирования и вставки, а так же немного исправлены ошибки во время загрузки")
        print("Добавлены: clear и немного защиты от читов")
        print("\n-----= 2.1.2 =-----\n")
        print("Очень незначительное обновление")
        print("Изменения: Изменена проверка загрузки")
        print("\n-----= 2.1 =-----\n")
        print("Незначительное обновление")
        print("Добавлены: Cycle Filtration System в магазине")
        print("Изменения: Сохранения были немного изменены, а так же немного оптимизирован код")
        print("Исправлены: Теперь при загрузке сохранения не будет ломаться магазин")
        print("\n-----= 2.0 =-----\n")
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

    # cheats
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

    # clear
    elif (UserAnswer == "clear"):
        money = 0
        mined = 0
        cheats = False
        shop = {"VIP":False, "CFS":False}
        FireMoney = 0
        FireMiner = False
        print("\nsystem> Данные были очищены.")

    # bug
    elif (UserAnswer == "bug"):
        print("\nsystem> Чтобы составить багрепорт, напишите сюда:")
        print("system> t.me/PMCMinerBugs")
        print("system> Пишите одним сообшением, давая как можно больше полезной информации о баге и тому, что к нему привело.")
        print("system> Так же вы сможете прикрепить видео/фото материалы к своей записи.")

    # shop
    elif (UserAnswer == "shop"):
        print("\nsystem/shop> Выберите одну из позиций:")
        print("VIP [140 PMC] Покупка VIP статуса, который ускорит работу")
        print("CFS [060 PMC] Покупка Cycle Filtration System - фильтрация поиска циклов, которая позволит находить более дорогие циклы")
        print("FM  [750 PMC] Покупка FireMoney в количестве одной штуки")
        print("FMM [003 FM ] Покупка майнера, который будет зарабатывать FireMoney вам")
        print("PMC [001 FM ] Покупка 10 PMC за 1 FM")
        UserAnswer = input("\nuser> ")
        
        #if UserAnswer == "VIP":
        #    Shop("VIP", 140, "PMC", True)
        #elif UserAnswer == "CFS":
        #    Shop("CFS", 60, "PMC", True)
        #elif UserAnswer == "FM":
        #    Shop("FM", 750, "PMC", False, 1)
        #elif UserAnswer == "FMM":
        #    Shop("FMM", 3, "FM", True)
        #elif UserAnswer == "PMC":
        #    Shop("PMC", 1, "FM", False, 10)

        if UserAnswer == "VIP": # VIP
            if not shop["VIP"]:
                if money >= 140:
                    money -= 140
                    shop["VIP"] = True
                    print("\nsystem> Вы успешно купили VIP статус.")
                else:
                    print("\nsystem> Вы слишком нищий для покупки этого и действие было отменено.")
            else:
                print("\nsystem> У вас уже есть VIP статус.")
        elif UserAnswer == "CFS": # CFS
            if not shop["CFS"]:
                if money >= 60:
                    money -= 60
                    shop["CFS"] = True
                    print("\nsystem> Вы успешно купили Cycle Filtration System.")
                else:
                    print("\nsystem> Вы слишком нищий для покупки этого и действие было отменено.")
            else:
                print("\nsystem> У вас уже есть Cycle Filtration System.")
        elif UserAnswer == "FMM": # FMM
            if not FireMiner:
                if FireMoney >= 3:
                    FireMoney -= 3
                    FireMiner = True
                    print("\nsystem> Вы успешно купили FireMoney Miner.")
                else:
                    print("\nsystem> Вы слишком нищий для покупки этого и действие было отменено.")
            else:
                print("\nsystem> У вас уже есть FireMoney Miner.")
        elif UserAnswer == "FM": # FM
            if money >= 750:
                money -= 750
                FireMoney += 1
                print("\nsystem> Вы успешно купили FireMoney.")
            else:
                print("\nsystem> Вы слишком нищий для покупки этого и действие было отменено.")
        elif UserAnswer == "PMC": # PMC
            if FireMoney >= 1:
                FireMoney -= 1
                money += 10
                print("\nsystem> Вы успешно купили 10 PMC.")
            else:
                print("\nsystem> Вы слишком нищий для покупки этого и действие было отменено.")
        else:
             print("\nsystem> Вы ввели ответ неверно и действие было отменено.")

    # wrong
    else:
        print(f'\nsystem> Допущена ошибка! "{UserAnswer}" не является встроенной командой. Попробуйте "help".')