from tkinter import *
root = Tk()
root.title('Кулькулятор')
root.geometry('255x140+500+300')
root.resizable(True, False)
root.iconbitmap(default='pics/Tea.ico')
root.attributes("-toolwindow", True)

def Click():
    user = User.get()
    try: user = eval(user)
    except: Out.config(text='Ошибка!')
    else: Out.config(text=user)

Out = Label(text='Тут будет ответ', bg="#84B97C")
Out.pack()
User = Entry(bg="#BCECB5")
User.pack(fill=X)
Button(text='Посчитать', command=Click, bg="#5E9156").pack(fill=X)
Label(text='"+" - сложение\t "-" - вычитание\n"*" - умножение\t "/" - деление\n"**" - степень\t "//" - деление без остатка\n"==" - сравнение\t "!=" - неравенство\n">" - больше\t "<" - меньше\n"%" - деление по модолю\n""', bg="#84B97C").pack(anchor=CENTER)

root.config(bg="#84B97C")

root.mainloop()