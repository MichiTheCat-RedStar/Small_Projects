File = open("ASCII.txt", "w", encoding="UTF-8")
num = 32
while num < 127:
    File.write(f"[{num}]\t<-->\t[ {chr(num)} ]\n")
    print(f"[{num}]\t<-->\t[ {chr(num)} ]\n")
    num += 1
File.close()