from random import randint
from time import sleep
from os import system

print("Добро пожаловать в BrainFunPlus!\n")

PreOutput = ""          # +PreOutput при выводах ("." и ":")
Output = ""             # Вывод текста
MemorySize = 32         # Количество ячеек памяти
Memory = []             # Все ячейки памяти
MemoryIndexMax = 256    # Максимальное значение ячейки
MemoryStep = 0          # Выбранная сейчас ячейка
GlobalValue = 0         # Глобальная переменная ("$" и "#")
Code = ""               # Код пользователя (обрабатывается ниже)
CodeStep = 0            # Выбранный символ кода
WhileList = []          # Сохраняемая информация для циклов
StepMode = False        # Пошаговый режим

if (input("Включить настройки? (Y/N): ")).upper() == "Y":
    if (input("\nСтавить пробелы между символами в [Вывод]? (Y/N): ")).upper() == "Y": PreOutput = " "
    if (input("Включить пошаговый режим? (Y/N): ")).upper() == "Y": StepMode = True
    try: MemorySize = int(input("Введите количество ячеек памяти (По умолчанию 32): "))
    except Exception: pass
    try: MemoryIndexMax = int(input("Введите максимальное значение ячейки памяти (По умолчанию 256): "))
    except Exception: pass
print()

for i in range(MemorySize): Memory.append(0)
Code = list(input("Вставьте свой код:\n"))

ErrSteps = 0
try:
    while True:

        if Code[CodeStep] == ">": MemoryStep += 1
        elif Code[CodeStep] == "<": MemoryStep -= 1
        elif Code[CodeStep] == "+": Memory[MemoryStep] += 1
        elif Code[CodeStep] == "-": Memory[MemoryStep] -= 1
        elif Code[CodeStep] == "$": GlobalValue = Memory[MemoryStep]
        elif Code[CodeStep] == "#": Memory[MemoryStep] = GlobalValue; GlobalValue = 0
        elif Code[CodeStep] == ".": Output += str(Memory[MemoryStep])+PreOutput
        elif Code[CodeStep] == ",": Memory[MemoryStep] = int(input(f"[({CodeStep}); (,); (int)]: "))
        elif Code[CodeStep] == ":": Output += chr(Memory[MemoryStep])+PreOutput
        elif Code[CodeStep] == ";": Memory[MemoryStep] = ord(input(f"[({CodeStep}); (;); (str)]: "))
        elif Code[CodeStep] == "r": Memory[MemoryStep] = randint(0, 1)
        elif Code[CodeStep] == "R": Memory[MemoryStep] = randint(0, MemoryIndexMax)
        elif Code[CodeStep] == "s": sleep(0.25)
        elif Code[CodeStep] == "«": MemoryStep = 0
        elif Code[CodeStep] == "»": MemoryStep = MemorySize-1
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

        MemoryStep = MemoryStep % MemorySize
        Memory[MemoryStep] = Memory[MemoryStep] % MemoryIndexMax
        CodeStep += 1
        ErrSteps += 1
        if ErrSteps > 10000:
            if input("Пройдено более 10000 шагов, возможно это бесконечный цикл; выйти? (Y/N): ").upper() == "Y": 
                break
    
except IndexError:
    pass

OutMemory = ""
for i in Memory: OutMemory += str(f"{i} ")
print("\n[Память]:", OutMemory, "\n[Глобальная переменная]:", GlobalValue, "\n[Сделано шагов]:", ErrSteps, "\n[Вывод]:", Output)
input("\nНажмите [Enter]\n")