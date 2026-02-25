from random import randint
from time import sleep

MemoryStep = 0 # Выбранная ячейка памяти от 0 до {MemoryCount}
Memory = [] # Ячейки памяти    

if input("Открыть дополнительные настрйоки? (Y/N): ").upper() == "Y":
    try:
        MemoryCount = int(input("Задайте количество ячеек (обычно 32): ")) # Количество ячеек
    except ValueError:
        MemoryCount = 32
    try:
        Out = int(input("Каким числом заполнить ячейки? (обычно 0): "))
    except ValueError:
        Out = 0
    MemoryCount -= 1
    try:
        MaxMemory = int(input("Введите максимум данных в ячейке (обычно 255): "))
    except ValueError:
        MaxMemory = 255
else:
    MemoryCount = 31
    Out = 0
    MaxMemory = 255

for i in range(MemoryCount):
    Memory.append(0)
StepMode = False
if input("Включить пошаговый режим? (Y/N): ").upper() == "Y":
    StepMode = True
PreOut = ""
if input("Добавить разделение символов для [Вывод]? (Y/N): ").upper() == "Y":
    PreOut = " "

CodeStep = 0 # Какой символ сейчас компилируется
if input("\nЗагрузить код из SaveFile.txt? (Y/N): ").upper() == "Y":
    try:
        File = open("SaveFile.txt", "r", encoding="UTF-8")
        Code = File.read()
        print(Code)
        File.close()
    except FileNotFoundError:
        File = open("SaveFile.txt", "w", encoding="UTF-8")
        if input("\nФайл не найден и будет создан новый; Сохранить в него код? (Y/N): ").upper() == "Y":
            Code = (input("\nВставьте код:\n\n"))
            File.write(Code)
        else:
            Code = (input("\nВставьте код:\n\n"))
        File.close()
else:
    Code = (input("\nВставьте код:\n\n"))
    if input("\nСохранить в SaveFile.txt? (Y/N): ").upper() == "Y":
        File = open("SaveFile.txt", "w", encoding="UTF-8")
        File.write(Code)
        File.close()
Code = list(Code)
print("\n")

OutMemory = ""
Out = ""
Stack = 0
StepOn = 0
ErrWhile = 0


try:
    while True:
  
        if Code[CodeStep] == ">":
            MemoryStep += 1
            if MemoryStep > (MemoryCount):
                MemoryStep = 0
    
        elif Code[CodeStep] == "<":
            MemoryStep -= 1
            if MemoryStep < 0:
                MemoryStep = (MemoryCount)
  
        elif Code[CodeStep] == ".":
            print(Memory[MemoryStep])
            Out += str(Memory[MemoryStep])+PreOut
  
        elif Code[CodeStep] == "+":
            Memory[MemoryStep] += 1
            if Memory[MemoryStep] > MaxMemory:
                Memory[MemoryStep] = 0
    
        elif Code[CodeStep] == "-":
            Memory[MemoryStep] -= 1
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = MaxMemory
    
        elif Code[CodeStep] == ",":
            Memory[MemoryStep] = int(input(f"[(,){CodeStep}; (S){MemoryStep}]: "))
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
            elif Memory[MemoryStep] > MaxMemory:
                Memory[MemoryStep] = MaxMemory

        elif Code[CodeStep] == ";":
            Memory[MemoryStep] = ord(input(f"[(;){CodeStep}; (S){MemoryStep}]: "))
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
            elif Memory[MemoryStep] > MaxMemory:
                Memory[MemoryStep] = MaxMemory
    
        elif Code[CodeStep] == "r":
            Memory[MemoryStep] = randint(0, MaxMemory)
  
        elif Code[CodeStep] == "$":
            Stack = Memory[MemoryStep]
   
        elif Code[CodeStep] == "#":
            Memory[MemoryStep] = Stack
            Stack = 0
            
        elif Code[CodeStep] == "*":
            Memory[MemoryStep] += Stack
            Stack = 0
            if Memory[MemoryStep] > MaxMemory:
                Memory[MemoryStep] = MaxMemory

        elif Code[CodeStep] == "%":
            Memory[MemoryStep] -= Stack
            Stack = 0
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0

        elif Code[CodeStep] == "«":
            MemoryStep = 0

        elif Code[CodeStep] == "»":
            MemoryStep = MemoryCount

        elif Code[CodeStep] == ":":
            print(chr(Memory[MemoryStep]))
            Out += chr(Memory[MemoryStep])+PreOut

        elif Code[CodeStep] == "C":
            for i in range(MemoryCount+1):
                MemoryStep = i
                Memory[MemoryStep] = 0
            MemoryStep = 0

        elif Code[CodeStep] == "c":
            Memory[MemoryStep] = 0

        elif (Code[CodeStep] == "{") and (Memory[MemoryStep] > 0):
            MemoryStep -= 1
            if MemoryStep < 0:
                MemoryStep = MaxMemory

        elif (Code[CodeStep] == "}") and (Memory[MemoryStep] > 0):
            MemoryStep += 1
            if MemoryStep > MaxMemory:
                MemoryStep = 0

        elif Code[CodeStep] == "|":
            break

        elif Code[CodeStep] == "(":
            Count = ""
            while Code[CodeStep] != ")":
                CodeStep += 1
                Count += str(Code[CodeStep])
                Count = Count.replace(")", "")
            Memory[MemoryStep] = int(Count)
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
            elif Memory[MemoryStep] > MaxMemory:
                Memory[MemoryStep] = MaxMemory

        elif (Code[CodeStep] == "[") and (Memory[MemoryStep] > 0):
            StepOn = CodeStep

        elif (Code[CodeStep] == "]") and (Memory[MemoryStep] > 0):
            CodeStep = StepOn

        elif Code[CodeStep] == "^":
            MemoryStep = (Memory[MemoryStep])-1

        elif Code[CodeStep] == "o":
            print(Out)
        
        elif Code[CodeStep] == "O":
            Out = ""

        elif Code[CodeStep] == "_":
            Memory[MemoryStep] -= 1
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
  
        elif Code[CodeStep] == "=":
            Memory[MemoryStep] += 1
            if Memory[MemoryStep] > MaxMemory:
                Memory[MemoryStep] = MaxMemory

        elif (Code[CodeStep] == "~") and (Memory[MemoryStep] == Stack):
            MemoryStep += 1
            if MemoryStep > MemoryCount:
                MemoryStep = 0

        elif Code[CodeStep] == "❛":
            Stack += 1
        
        elif Code[CodeStep] == "❜":
            Stack -= 1
            if Stack < 0:
                Stack = 0
        
        elif Code[CodeStep] == "@":
            CodeStep = Stack

        elif Code[CodeStep] == "'":
            CodeStep += 1
            while Code[CodeStep] != "'":
                CodeStep += 1
                
        elif (Code[CodeStep] == "!") and (Memory[MemoryStep] > 0):
            Memory[MemoryStep] = 0

        elif Code[CodeStep] == "?":
            if Memory[MemoryStep] == 0:
                MemoryStep += 1
                if MemoryStep > MemoryCount:
                    MemoryStep = 0
            else:
                MemoryStep -= 1
                if MemoryStep < 0:
                    MemoryStep = MemoryCount

        elif Code[CodeStep] == "/":
            if Memory[MemoryStep] > 0:
                StepOn = CodeStep
            else:
                CodeStep += 1
                while Code[CodeStep] != "]":
                    CodeStep += 1

        elif Code[CodeStep] == "№":
            sleep(0.5)
            

        if StepMode:
            for i in Memory:
                OutMemory += str(f"{i} ")
            print("\n[Memory]:", OutMemory)
            OutMemory = ""
            input(f"[MemoryStep]:({MemoryStep}); [Code]:({CodeStep}); [Step]:({Code[CodeStep]}); [GlobalSteps]:({ErrWhile}); нажмите Enter\n")
        CodeStep += 1
        ErrWhile += 1
        if ErrWhile == 5001:
            if input("Пройдено более 5000 шагов, вероятно это бесконечный цикл; Остановить? (Y/N): ").upper() == "Y":
                break
        elif ErrWhile == 10001:
            if input("Пройдено более 10000 шагов, вероятно это всё же бесконечный цикл; Остановить? (Y/N): ").upper() == "Y":
                break
        elif ErrWhile == 100001:
            if input("Пройдено более 100000 шагов, ну это точно бесконечный цикл; Остановить? (Y/N): ").upper() == "Y":
                break
 
except IndexError:
    pass
 
for i in Memory:
    OutMemory += str(f"{i} ")
print("\n\n[Memory]:", OutMemory)
print("[Stack]:", Stack)
print("[GlobalSteps]:", ErrWhile)
print("[Вывод]:", Out)
input("\nНажмите Enter\n")