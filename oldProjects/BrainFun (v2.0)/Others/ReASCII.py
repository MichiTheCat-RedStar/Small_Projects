File = open("ASCII.txt", "w", encoding="UTF-8")
num = 32
while num < 127:
    File.write(f"[{num}]\t<-->\t[ {chr(num)} ]\n")
    print(f"[{num}]\t<-->\t[ {chr(num)} ]\n")
    num += 1
File.close()
File = open("ASCII+.txt", "w", encoding="UTF-8")
num = 16
while not (num > 32767):
    File.write(f"[{num}]\t<-->\t[ {chr(num)} ]\t\t[{num+1}]\t<-->\t[ {chr(num+1)} ]\n")
    num += 2
File.close()