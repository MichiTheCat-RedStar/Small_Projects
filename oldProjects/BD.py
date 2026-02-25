from random import randint
import time
number = 0
while True:
    number += 1
    print(randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1))
    time.sleep(0.05)
    if number == 500:
        print("\n× Ваша база данных загружена,переход к следующей...\n")
        number = 0
    elif number%10 == 0:
        print(f"    [{number}]")