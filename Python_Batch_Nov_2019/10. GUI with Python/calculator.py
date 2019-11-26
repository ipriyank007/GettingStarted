from tkinter import *

root = Tk()
root.title('Addition')
root.geometry('240x240')

Label(root, text='First No.').grid(row=0, column=0)
num1 = Entry(root)
num1.grid(row=0, column=1)
Label(root, text='Second No.').grid(row=1, column=0)
num2 = Entry(root)
num2.grid(row=1, column=1)

def addition():
    n1 = num1.get()
    n2 = num2.get()
    result = int(n1) + int(n2)

    Label(root, text='Result: ' + str(result)).grid(row=2, column=1)

    # Label(root, text=f'Result: {result}').grid(row=2, column=1)

btn = Button(root, text='Add', command=addition)
btn.grid(row=2, column=0)

root.mainloop()
