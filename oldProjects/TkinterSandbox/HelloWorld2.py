from tkinter import *
root = Tk()
root.title('Just HW!')
root.geometry('160x80')
root.resizable(False, False)
root.iconbitmap(default='pics/Tea.ico')
Label(text='Hello World!').pack(ipady=40)   # Стоит объяснить, что я не задаю переменную для Label, так как не вижу в этом смысла, ведь не использую её в коде в дальнейшем
root.mainloop()