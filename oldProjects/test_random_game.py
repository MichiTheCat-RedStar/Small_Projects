from random import randint
print("TRG - игра сделаная на python, где вы можете убивать врагов... Удачной игры!")
achievements = []
while True:
    money = 0
    hp = 10
    hpb = 1
    dead = 0
    allde = 0
    armor = "нет"
    sword = "нет"
    while hp > 0:
        if dead == 1:
            achievements.append("Первый враг")
        elif dead == 13:
            achievements.append("13 тел")
        if (armor == "есть") and (sword == "есть") and ("Фулл сет брони" not in achievements):
            achievements.append("Фулл сет брони")
        if (hpb == 25) and ("Коллекционер" not in achievements):
            achievements.append("Коллекционер")
        if (allde == 666) and ("Челоаек из ада" not in achievements):
            achievements.append("Человек из ада")
        sore = randint(0, 10)
        if sore != 0:
            c = randint(0, 5)
            ehp = randint(1, 10)
            if hp <= 5:
                ehp = randint(1, 5)
            elif hp > 5 and hpb > 3:
                ehp = randint(10, 20)
            elif hp > 10 and hpb > 5:
                ehp = randint(10, 20)
            print()
            print(f"На вас напал противник с {ehp} здоровья, вы можете атаковать его (A), использовать одну из {hpb} бутылок с лечебным зельем (H) или посмотреть инвентарь (I) [чтобы посмотреть ачивки, нажмите (D)]")
            while ehp > 0 and hp > 0:
                txt = input("Ваш выбор: ")
                if txt == "A":
                    pd = randint(0, 3)
                    if sword == "Нет":
                        ed = randint(0, 3)
                    else:
                        ed = randint(1, 4)
                    allde += ed
                    hp -= pd
                    ehp -= ed
                    print(f"Вы получили {pd} урона, противник получил {ed} урона, ваше здоровье - {hp}, здоровье врага - {ehp}")
                    if ehp <= 0:
                        dead += 1
                        hos = randint(0, 8)
                        if hos > 1:
                            hpb += c
                            print(f"Вы победили противника, из него выпало {c} лечебных зелий, текущее количество - {hpb}")   
                        elif hos == 1 and sword == "нет":
                            print("Вы победили противника, из него выпал меч. Подобрать? (Y)/(N)")
                            ups = input("Ваш выбор: ")
                            if ups == "Y":
                                sword = "есть"
                                print("Вы подобрали меч")
                            else:
                                print("Вы не подобрали меч")
                        elif hos == 0 and armor == "нет":
                            print("Вы победили противника, из него выпаа броня. Подобрать? (Y)/(N)")
                            upa = input("Ваш выбор: ")
                            if upa == "Y":
                                armor = "есть"
                                print("Вы подобрали броню")
                            else:
                                print("Вы не подобрали броню")
                        elif (hos == 0 and armor == "есть") or (hos == 1 and sword == "есть"):
                            print(f"Вы победили противника, из него выпало {c} монет, текущее количество - {c}")
                            money += c
                elif txt == "H" and hpb > 0:
                    b = randint(1, 3)
                    hp += b
                    if hp > 10 and armor == "нет":
                        hp = 10
                    if hp > 20 and armor == "есть":
                        hp = 20
                    hpb -= 1
                    print(f"Вы использовали зелье лечения и восстановили {b} здоровья, текущее количество зелий - {hpb}, ваше зддоровье - {hp}")
                elif txt == "I":
                    print(f"Броня: {armor}   Меч: {sword}")
                    print("Деньги: ", money)
                elif txt == "D":
                    print("Достижения: ", achievements)
        else:
            pr = randint(2, 8)
            sumbt = randint(1, 5)
            print()
            print(f"Вы встретили торговца, он предлагает вам {sumbt} лечебных зелий за {pr} монет, у вас есть {money} монет и {hpb} зелий. Купить? (Y)/(N)")
            buy = input("Ваш выбор: ")
            if buy == "Y" and money >= pr:
                money -= pr
                hpb += sumbt
                print(f"Вы купили зелья, текущее количество зелий - {hpb}, монет - {money}")
            elif buy == "N":
                print("Вы прошли мимо")
            elif buy == "Y" and money < pr:
                print("Торговец ушёл от вас, увидев, что у вас нет денег")
    print()
    print(f"Вы проиграли и забрали с собой {dead} врагов и нанесли {allde} урона")
    print("Начать заново? (Y)/(N)")
    rest = input("Ваш выбор: ")
    if rest == "N":
        break