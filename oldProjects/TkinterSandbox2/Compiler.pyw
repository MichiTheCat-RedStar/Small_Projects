from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Компилятор python (небезопасный!)')
root.geometry('610x310')
root.resizable(False, False)
root.iconbitmap(default='pics/Tea.ico')

glb = False
result = None
def compil():
    global glb
    _ = txt.get('1.0', 'end')
    if glb: _ = f'global result\n{_}'
    try:
        exec(_)
        lbl.config(text=(str(result)))
    except Exception:
        lbl.config(text='Ошибка!')

def save():
    file = open('files/CompilerSave.txt', 'w', encoding='UTF-8')
    file.write(txt.get('1.0', 'end'))
    file.close()
    file = open('files/CompilerSave.py', 'w', encoding='UTF-8')
    file.write(txt.get('1.0', 'end'))
    file.close()

def clear():
    global result
    result = None
    txt.delete('1.0', 'end')
    lbl.config(text='')

def wrap_func():
    if txt['wrap'] == WORD:
        txt.config(wrap=CHAR)
    else: txt.config(wrap=WORD)

def glb_func():
    global glb
    glb = not glb

def info():
    messagebox.showinfo('Инфо', f'result = {result}\nсимволы = {(len(txt.get('1.0', 'end')))-1}')

root.option_add("*tearOff", FALSE)
main_menu = Menu()
settings = Menu()
settings.add_checkbutton(label='Перенос по символам', command=wrap_func)
settings.add_checkbutton(label='Встроенный global', command=glb_func)
settings.add_cascade(label='Очистить всё', command=clear)
settings.add_cascade(label='Сохранить', command=save)
main_menu.add_cascade(label='Настройки', menu=settings)
main_menu.add_cascade(label='Инфо', command=info)
root.config(menu=main_menu)

txt = Text(height=19, width=40, wrap=WORD)
txt.grid(row=0, column=0, rowspan=2, sticky=NSEW)
lbl = Label(height=18, width=40, wraplength=280, justify=LEFT,bg="#CECECE", anchor=NW)
lbl.grid(row=0, column=1, sticky=NSEW)
Button(text='Скомпилировать', command=compil).grid(row=1, column=1, sticky=NSEW)
root.config(bg='black')
txt.insert('1.0', '# Выводится будут данные из переменной {result} после её объявления через {global} (либо это можно изменить в настройка):\n\nglobal result\nresult = 2')

root.mainloop()