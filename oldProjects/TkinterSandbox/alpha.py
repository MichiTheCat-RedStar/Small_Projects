from tkinter import *
root = Tk()
root.title('Alpha Chanel')
root.geometry('160x140+600+300')
root.iconbitmap(default='pics/Tea.ico')
root.attributes("-alpha", 0.5)  # Ключевая функция этого теста
Label(text='Тут я пробую настройку альфаканала для окна... Вот вы можете прочитать этот текст? Альфа канал прозрачности не так сильно понижен, чтобы вы не могли... Хотя кто-то ведь не может... Вы кто-то?)', wraplength=160).pack()
root.mainloop()