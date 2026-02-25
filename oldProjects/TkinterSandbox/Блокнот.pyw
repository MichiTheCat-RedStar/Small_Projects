from tkinter import *
root = Tk()
root.title('Блокнот')
root.geometry('280x340')
root.resizable(False, False)
root.iconbitmap(default='pics/Tea.ico')

def Delete(): txt.delete('1.0', 'end')
def Save():
    file = open('files/Блокнот.txt', 'w', encoding='UTF-8')
    file.write(txt.get('1.0', 'end'))
    file.close()

main_menu = Menu()
file_menu = Menu()
file_menu = Menu(tearoff=0)
file_menu.add_command(label="Отчистить", command=Delete)
file_menu.add_command(label="Сохранить", command=Save)
main_menu.add_cascade(label="Файл", menu=file_menu)
root.config(menu=main_menu)

txt = Text(wrap='word', width=32, height=21)
txt.grid(row=0, column=0, sticky=NSEW)

scrl = Scrollbar(orient='vertical', command=txt.yview)
scrl.grid(row=0, column=1, sticky=NSEW)
txt['yscrollcommand'] = scrl.set

root.mainloop()