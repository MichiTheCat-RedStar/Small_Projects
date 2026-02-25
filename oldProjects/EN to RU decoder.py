RU = list("ё1234567890-=йцукенгшщзхъ\\фывапролджэячсмитьбю.Ё!\"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ, "); EN = list("`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? ")
while True: 
    translate = ""
    if input('\n1. Английская раскладка в русскую\n2. Русская раскладка в английскую\n> ') == '1':
        for char in input('> '): translate += str(RU[EN.index(char)])
    else:
        for char in input('> '): translate += str(EN[RU.index(char)])
    print('\n', translate)