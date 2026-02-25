from tkinter import *
root = Tk()
root.title('Some Checkbuttons')
root.geometry('340x320')
root.resizable(False, False)
root.iconbitmap(default='pics/Tea.ico')

checked = 0
def click():
    global checked
    checked += 1
    print(f'Чекед {checked} раз!')
    checks.config(text=f'Чеков: {checked}')

for r in range(12):
    for c in range(12):
        Checkbutton(command=click).grid(column=c, row=r)

checks = Label(text='Чеков: 0')
checks.grid(row=12, column=0, columnspan=12)

root.mainloop()