from tkinter import *
root = Tk()
root.title('Веб-Антисресс')
root.geometry('320x560')
root.iconbitmap(default='pics/Tea.ico')

Label(text='Тут разные виджеты\nНапример это текст', font=('mono', 15), foreground="#00AA00").pack()

def click_1(): print('Нажата кнопка <1>')
def click_2(): print('Нажата кнопка <2>')
def click_3(): print('Нажата кнопка <3>')

Button(text='А это кнопка', command=click_1).pack(fill=X)
Button(text='И это кнопка', command=click_2).pack(fill=X)
Button(text='Потыкай нас)', command=click_3).pack(fill=X)

Tea = PhotoImage(file='pics/Tea.png').subsample(4, 4)
Label(image=Tea).pack()

Entry().pack(fill=X)
Entry().pack(fill=X)
Checkbutton(text='Вам нравится код?').pack()

mode = IntVar()
Radiobutton(text='Кнопка 1', variable=mode, value=1).pack(anchor=NW)
Radiobutton(text='Кнопка 2', variable=mode, value=2).pack(anchor=N)
Radiobutton(text='Кнопка 3', variable=mode, value=3).pack(anchor=NE)

Listbox(listvariable=(Variable(value=['А это', 'Что-то вроде', 'Списка'])), height=4).pack()
Scale(orient=HORIZONTAL).pack()
Scale().pack()

root.mainloop()