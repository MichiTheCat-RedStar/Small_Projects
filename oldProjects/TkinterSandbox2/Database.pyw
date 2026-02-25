from tkinter import *
from tkinter import ttk
root = Tk()
root.title('База данных')
root.geometry('420x280')
root.resizable(True, True)
root.iconbitmap(default='pics/Tea.ico')

tree = ttk.Treeview(columns=('name', 'phone', 'profesion'), show='headings')
tree.pack(fill=BOTH)
tree.heading('name', text='ФИО')
tree.heading('phone', text='Номер телефона')
tree.heading('profesion', text='Должность')

tree.insert('', END, values=('Карлик Иван Павлович', '-71730496907', 'Охраник'))
tree.insert('', END, values=('Ну Немножко Пирамид', 'Отсутствует', 'Археолог'))
tree.insert('', END, values=('Этот Жаренный Морж', '+3086665557721', 'Повар'))
tree.insert('', END, values=('Молочный Рог Древности', '=7352031#8', 'Носитель носков'))
tree.insert('', END, values=('Фея Вкусного Пироженного', 'плюс(83487593645)', 'Уволен же?'))

# Мне вообще лень в этом разбираться обширнее, простите)

root.mainloop()