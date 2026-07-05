from RandLang import *

RandLang(''' # Тест последовательного выполнения используя del и разные переменные
a = True; print(0)
if a: b = True; del a; print(1)
if b: del a; del b; c = True; print(3)
if c: print(4)
if b: a = True; print(2)
''')
