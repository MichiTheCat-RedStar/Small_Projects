from random import randint

MemoryStep = 0 # Выбранная ячейка памяти от 0 до 31
Memory = [] # Ячейки памяти
for i in range(32):
    Memory.append(0)

CodeStep = 0 # Какой символ сейчас компилируется
Code = list(input("Вставьте код:\n\n"))
print("\n")

Stack = 0

try:
    while True:
  
        if Code[CodeStep] == ">":
            MemoryStep += 1
            if MemoryStep > (31):
                MemoryStep = 0
    
        elif Code[CodeStep] == "<":
            MemoryStep -= 1
            if MemoryStep < 0:
                MemoryStep = (31)
  
        elif Code[CodeStep] == ".":
            print(Memory[MemoryStep])
  
        elif Code[CodeStep] == "+":
            Memory[MemoryStep] += 1
            if Memory[MemoryStep] > 255:
                Memory[MemoryStep] = 0
    
        elif Code[CodeStep] == "-":
            Memory[MemoryStep] -= 1
            if Memory[MemoryStep] < 0:
                Memory[MemoryStep] = 255
    
        elif Code[CodeStep] == ",":
            Memory[MemoryStep] = int(input(f"[(,){CodeStep};(S){MemoryStep}]: "))
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
 
        CodeStep += 1
 
except IndexError:
    pass
 
OutMemory = ""
for i in Memory:
    OutMemory += str(f"{i} ")
print("\n\n[Memory]:", OutMemory)
print("[Stack]:", Stack)