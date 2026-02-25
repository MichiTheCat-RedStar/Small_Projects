from time import sleep

UserInventory = []
AutoSave = 0

def PT(text="", speed=1, enter=False):      # PT - print text
    print(text); sleep(speed); (input("Нажмите [Enter]\n")) if enter else None

def UI(text="", key_item=None):             # UI - user interaction
    global UserInventory
    while True:
        print(text, "\nВаш инвентарь:", UserInventory)
        if (input("Что вы используете? > ").lower() == key_item): break
        else: print("Попробуйте другой предмет...\n")

def UC(text="", choice=[]):                 # UC - user choice
    while True:
        print(text)
        _ = input("Что вы хотите сделать? > ").lower()
        if _ in choice: return _; break
        else: print("Попробуйте другой вариант...\n")

def Save():
    global AutoSave
    AutoSave += 1
    file = open("StorySaveFile.michi", "w")
    file.write(str(AutoSave))
    file.close()

def Load():
    global AutoSave
    try:
        file = open("StorySaveFile.michi")
        AutoSave = file.read()
        file.close()
    except FileNotFoundError:
        AutoSave = 0
    try:
        AutoSave = int(AutoSave)
    except Exception:
        AutoSave = 0

# --- Игровая Часть ---

if input("Загрузить игру? Y/N > ").upper() in ["Y", "YES", "Д", "ДА"]: Load()

if AutoSave == 0:
    PT("\nВы нашли топор")
    PT("+Топор")
    UserInventory.append("топор")
    PT(f"Ваш инвентарь теперь: {UserInventory}")
    PT("Сломайте дверь топором\n")
    UI("Перед вами дверь, что вы примените?", "топор")
    PT("\nХорошо, неплохо", 2)
    PT("Давайте представим, что вы на развилке?\n")
    _=UC("Куда вы хотите пойти?\n> Прямо\n> Направо", ["прямо", "направо"])
    if _ == "прямо":
        PT("Вы пошли прямо и умерли")
    elif _ == "направо":
        PT("Вы пошли направо и выжили")
        PT("Вот вам ничего")
        UserInventory.append("ничего")
    PT("\nВы рады игре?")
    PT("В любом случае это неважно", enter=True)
    Save()
if AutoSave == 1:
    PT("\nВы либо дошли до конца, либо загрузились уже отсюда")
    PT("Я дам вам скипнуть))", enter=True)