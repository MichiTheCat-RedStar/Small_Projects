from random import randint
from time import sleep

MemoryStep = 0
Memory = []
for i in range(32):
    Memory.append(0)

CodeStep = 0
Code = list(input("Вставьте код:\n\n"))
print("\n")

Out = ""
Stack = 0
StepOn = 0
ErrWhile = 0

try:
    while True:
  
        if Code[CodeStep] == ">":
            MemoryStep += 1
            if MemoryStep > 31:
                MemoryStep = 0
    
        elif Code[CodeStep] == "<":
            MemoryStep -= 1
            if MemoryStep < 0:
                MemoryStep = 31
  
        elif Code[CodeStep] == ".":
            print(Memory[MemoryStep])
            Out += str(Memory[MemoryStep])
  
        elif Code[CodeStep] == "+":
            Memory[MemoryStep] += 1
            if Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 0
    
        elif Code[CodeStep] == "-":
            Memory[MemoryStep] -= 1
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 255
    
        elif Code[CodeStep] == ",":
            Memory[MemoryStep] = int(input("[,]: "))
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
            elif Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 255

        elif Code[CodeStep] == ";":
            Memory[MemoryStep] = ord(input("[;]: "))
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
            elif Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 255
    
        elif Code[CodeStep] == "r":
            Memory[MemoryStep] = randint(0, 255)
  
        elif Code[CodeStep] == "$":
            Stack = Memory[MemoryStep]
   
        elif Code[CodeStep] == "#":
            Memory[MemoryStep] = Stack
            Stack = 0

        elif Code[CodeStep] == "*":
            Memory[MemoryStep] += Stack
            Stack = 0
            if Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 255

        elif Code[CodeStep] == "%":
            Memory[MemoryStep] -= Stack
            Stack = 0
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0

        elif Code[CodeStep] == "«":
            MemoryStep = 0

        elif Code[CodeStep] == "»":
            MemoryStep = 31

        elif Code[CodeStep] == ":":
            print(chr(Memory[MemoryStep]))
            Out += chr(Memory[MemoryStep])

        elif (Code[CodeStep] == "{") and (Memory[MemoryStep] > 0):
            MemoryStep -= 1
            if MemoryStep < 0:
                MemoryStep = 31

        elif (Code[CodeStep] == "}") and (Memory[MemoryStep] > 0):
            MemoryStep += 1
            if MemoryStep > 31:
                MemoryStep = 0
            
        elif Code[CodeStep] == "c":
            Memory[MemoryStep] = 0

        elif Code[CodeStep] == "C":
            for i in range(32):
                Memory[i] = 0

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
            elif Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 255

        elif (Code[CodeStep] == "[") and (Memory[MemoryStep] > 0):
            StepOn = CodeStep

        elif (Code[CodeStep] == "]") and (Memory[MemoryStep] > 0):
            CodeStep = StepOn

        elif Code[CodeStep] == "^":
            MemoryStep = Memory[MemoryStep]
            if MemoryStep > 31:
                MemoryStep = 0
            elif MemoryStep < 0:
                MemoryStep = 31

        elif Code[CodeStep] == "_":
            Memory[MemoryStep] -= 1
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 0
  
        elif Code[CodeStep] == "=":
            Memory[MemoryStep] += 1
            if Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 255

        elif (Code[CodeStep] == "~") and (Memory[MemoryStep] == Stack):
            MemoryStep += 1
            if MemoryStep > 31:
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
                if MemoryStep > 31:
                    MemoryStep = 0
            else:
                MemoryStep -= 1
                if MemoryStep < 0:
                    MemoryStep = 31

        elif Code[CodeStep] == "/":
            if Memory[MemoryStep] > 0:
                StepOn = CodeStep
            else:
                CodeStep += 1
                while Code[CodeStep] != "]":
                    CodeStep += 1

        elif Code[CodeStep] == "№":
            sleep(0.5)


        CodeStep += 1
        ErrWhile += 1
        if ErrWhile == 10001:
            if input("Пройдено более 10000 шагов, вероятно это бесконечный цикл; Остановить? (Y/N): ").upper() == "Y":
                break
 
except IndexError:
    pass
 
OutMemory = ""
for i in Memory:
    OutMemory += str(f"{i} ")
print("\n\n[Memory]:", OutMemory)
print("[Stack]:", Stack)
print("[GlobalSteps]:", ErrWhile)
print("[Вывод]:", Out)
input("\nНажмите Enter\n")