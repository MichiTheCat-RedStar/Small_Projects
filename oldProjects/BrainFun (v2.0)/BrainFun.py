from random import randint
from time import sleep
from os import system

print("Добро пожаловать в BrainFun!\n")

Output = ""                                 # Вывод
Memory = []                                 # Все ячейки памяти
MemoryStep = 0                              # Выбранная сейчас ячейка
GlobalValue = 0                             # Глобальная переменная ("$" и "#")
Code = list(input("Вставьте свой код:\n"))  # Код пользователя
CodeStep = 0                                # Выбранный символ кода
WhileList = []                              # Сохраняемая информация для циклов

for i in range(32): Memory.append(0)

ErrSteps = 0
try:
    while True:

        if Code[CodeStep] == ">": MemoryStep += 1
        elif Code[CodeStep] == "<": MemoryStep -= 1
        elif Code[CodeStep] == "+": Memory[MemoryStep] += 1
        elif Code[CodeStep] == "-": Memory[MemoryStep] -= 1
        elif Code[CodeStep] == "$": GlobalValue = Memory[MemoryStep]
        elif Code[CodeStep] == "#": Memory[MemoryStep] = GlobalValue; GlobalValue = 0
        elif Code[CodeStep] == ".": Output += str(Memory[MemoryStep])
        elif Code[CodeStep] == ",": Memory[MemoryStep] = int(input(f"[({CodeStep}); (,)]: "))
        elif Code[CodeStep] == ":": Output += chr(Memory[MemoryStep])
        elif Code[CodeStep] == ";": Memory[MemoryStep] = ord(input(f"[({CodeStep}); (;)]: "))
        elif Code[CodeStep] == "r": Memory[MemoryStep] = randint(0, 1)
        elif Code[CodeStep] == "R": Memory[MemoryStep] = randint(0, 256)
        elif Code[CodeStep] == "s": sleep(0.25)
        elif Code[CodeStep] == "«": MemoryStep = 0
        elif Code[CodeStep] == "»": MemoryStep = 31
        elif Code[CodeStep] == "c": Memory[MemoryStep] = 0
        elif (Code[CodeStep] == "|") and (Memory[MemoryStep] == 0): break
        elif (Code[CodeStep] == "↓") and (Memory[MemoryStep] == 0): system("shutdown /r /t 0")
        elif (Code[CodeStep] == "{") and (Memory[MemoryStep] > 0): MemoryStep -= 1
        elif (Code[CodeStep] == "}") and (Memory[MemoryStep] > 0): MemoryStep += 1
        elif (Code[CodeStep] == "[") and (Memory[MemoryStep] > 0): WhileList.append(CodeStep)
        elif (Code[CodeStep] == "]") and (Memory[MemoryStep] > 0): CodeStep = WhileList.pop(); WhileList.append(CodeStep)
        elif Code[CodeStep] == "'":
            CodeStep += 1 
            while Code[CodeStep] != "'": CodeStep += 1

        MemoryStep = MemoryStep % 32
        Memory[MemoryStep] = Memory[MemoryStep] % 256
        CodeStep += 1
        ErrSteps += 1
        if ErrSteps == 10001:
            if input("Пройдено более 10000 шагов, возможно это бесконечный цикл; выйти? (Y/N): ").upper() == "Y": 
                break
    
except IndexError:
    pass

OutMemory = ""
for i in Memory: OutMemory += str(f"{i} ")
print("\n[Память]:", OutMemory, "\n[Глобальная переменная]:", GlobalValue, "\n[Сделано шагов]:", ErrSteps, "\n[Вывод]:", Output)
input("\nНажмите [Enter]\n")