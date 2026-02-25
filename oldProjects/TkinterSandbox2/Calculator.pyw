from tkinter import *
root = Tk()
root.title('Калькулятор')
root.geometry('240x65')
root.resizable(True, False)
root.iconbitmap(default='pics/Tea.ico')

def Calculate():
    inp = Ins.get()
    error = False
    for char in inp:
        if char in '1234567890+-*/() .': pass
        else: error = True
    if error == True:
        Out.config(text='Недопустимые символы!')
    else:
        try: inp=eval(inp)
        except Exception: Out.config(text='Ошибка!')
        else: Out.config(text=inp)

Out = Label(text='Тут будет ответ...', bg="#C0C0C0")
Out.pack(fill=X)
Ins = Entry(bg="#EBEBEB")
Ins.pack(fill=X)
Button(text='Посчитать', bg="#C0C0C0", command=Calculate).pack(fill=BOTH)

root.mainloop()