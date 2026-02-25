from tkinter import *
root = Tk()
root.title('Создать записку')
root.geometry('255x70+500+300')
root.resizable(False, False)
root.iconbitmap(default='pics/Tea.ico')

def Save():
    try:
        file = open(f'files/{Name.get()}.txt', 'w', encoding='UTF-8')
        file.write(Insert.get())
        file.close()
    except Exception:
        Status.config(text='Ошибка!', bg='red')
    else:
        Status.config(text='Сохранено!', bg='green')
    root.after(1000, lambda: Status.config(text='...', bg='gray'))

Label(text='Название записки:').grid(row=0, column=0, sticky=NSEW)
Label(text='Содержимое записки:').grid(row=1, column=0, sticky=NSEW)
Name = Entry()
Name.grid(row=0, column=1, sticky=NSEW)
Insert = Entry()
Insert.grid(row=1, column=1, sticky=NSEW)
Button(text='Сохранить', command=Save).grid(row=2, column=1, sticky=NSEW)
Status = Label(text='...', bg='gray')
Status.grid(row=2, column=0, sticky=NSEW)

root.mainloop()