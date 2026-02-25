import re

print("RedStar Corporation | discord - green_tea_bag | version: 1.0 | 116 строк кода")
print("Добро пожаловать в программу для изменения версии сохранения Майнера PyMinerCMD!")
print("Может нестабильно работать при переносе с новой версии в старую")
print("Выберите с какой версии вы хотите взять сохранение:\n")
print("1 - 1.0")
print("2 - 1.1")
print("3 - 1.2")
print("4 - 1.3 до 1.5.3")
print("5 - 2.0")

money = 0
mined = 0
shop = {"VIP":False}

try:
    UserAnswer = int(input("\n> "))
except Exception:
    print("Вы ввели что-то не так")

if UserAnswer == 1:
    print("\nВведите код денег.")
    UserAnswer = input("\n> ")
    money = int((int(UserAnswer)-8)/16)
    print("\nВведите код циклов.")
    UserAnswer = input("\n> ")
    mined = int((int(UserAnswer)-12)/16)

elif UserAnswer == 2:
    print("\nВведите код денег.")
    UserAnswer = input("\n> ")
    money = (int((int(UserAnswer)-8)/16))/10
    print("\nВведите код циклов.")
    UserAnswer = input("\n> ")
    mined = int((int(UserAnswer)-12)/16)

elif UserAnswer == 3:
    print("\nВведите код сохранения.")
    UserAnswer = input("\n> ")
    decode = re.findall(r"\d+", UserAnswer)
    money = (int((int(decode[0])-8)/16))/10
    mined = int((int(decode[1])-12)/16)
    print("\nУспешно загружено.")

elif UserAnswer == 4:
    print("\n> Введите код сохранения.")
    UserAnswer = input("\n> ")
    try:
        decode = re.findall(r"\d+", UserAnswer)
        money = (int((int(decode[0])-8)/16))/10
        mined = int((int(decode[1])-12)/16)
        print("\n> Успешно загружено.")
    except Exception:
        print("\n> Вы ввели код неверно и действие было отменено.")

elif UserAnswer == 5:
    print("\nsystem> Введите код сохранения.")
    UserAnswer = input("\n> ")
    try:
        decode = re.findall(r"\d+", UserAnswer)
        money = (int((int(decode[0])-8)/16))/10
        mined = int((int(decode[1])-12)/16)
        shop["VIP"] = bool(decode[2])
        print("\nsystem> Успешно загружено.")
    except Exception:
        print("\nsystem> Вы ввели код неверно и действие было отменено.")

print(f"\nsystem> Количество заработанных денег: {money} PMC.")
print(f"system> Количество запущенных циклов: {mined} раз.")
if mined != 0:
    MinedToMoney = int(((money/mined)*100)/20)
    print(f"system> Процент Денег/Циклов: {MinedToMoney}%.")
print(f"system> Приобретённые товары: VIP - {shop['VIP']}.")

print("\nЕсли всё сделано верно, то теперь будет загрузка на желаемую версию, поэтому выберите версию на которую вы хотите записать сохранение:")
print("1 - 1.0")
print("2 - 1.1")
print("3 - 1.2")
print("4 - 1.3 до 1.5.3")
print("5 - 2.0")

try:
    UserAnswer = int(input("\n> "))
except Exception:
    print("Вы ввели что-то не так")

if UserAnswer == 1:
    saved_money = (money * 16) + 8
    saved_mined = (mined * 16) + 12
    print(f"\nsystem> Код денег: {saved_money}  |  Код циклов: {saved_mined}")

elif UserAnswer == 2:
    saved_money = int(((money * 10) * 16) + 8)
    saved_mined = int((mined * 16) + 12)
    print(f"\nsystem> Код денег: {saved_money}  |  Код циклов: {saved_mined}")

elif UserAnswer == 3:
    saved_money = int(((money * 10) * 16) + 8)
    saved_mined = int((mined * 16) + 12)
    code = f"SMy_{saved_money}-PMC-SMd_{saved_mined}"
    print("\nsystem> Код вашего сохранения:", code)

elif UserAnswer == 4:
    saved_money = int(((money * 10) * 16) + 8)
    saved_mined = int((mined * 16) + 12)
    code = f"SMy_{saved_money}-PMC-SMd_{saved_mined}"
    print("\nsystem> Код вашего сохранения:", code)

elif UserAnswer == 5:
    saved_money = int(((money * 10) * 16) + 8)
    saved_mined = int((mined * 16) + 12)
    code = f"SMy_{saved_money}-PMC-SMd_{saved_mined}_SS-{int(shop['VIP'])}"
    print("\nsystem> Код вашего сохранения:", code)

input("\nНадеюсь сохранение было перенесено успешно! Теперь вы можете скопировать сохранение и выйти!\n> ")