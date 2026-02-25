from tkinter import *
root = Tk()
root.title('Пример окна')
root.geometry('240x240')
root.resizable(False, False)
root.iconbitmap(default='pics/Tea.ico')

# А тут код, чтобы каждый раз не создавать всю основную инфу с нуля

root.mainloop()