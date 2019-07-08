from tkinter import *

root = Tk()

root.title('My Calculator')
root.geometry('640x480')

val1 = Label(root, text='Value 1:')
val1.grid(row=0, column=0)
ent1 = Entry(root)
ent1.grid(row=0, column=1)
val2 = Label(root, text='Value 2:')
val2.grid(row=1, column=0)
ent2 = Entry(root)
ent2.grid(row=1, column=1)


def addition():
    try:
        a = int(ent1.get())
        b = int(ent2.get())
    except ValueError:
        result = Label(root, text="You can only enter numbers")
        result.grid(row = 3, column=0)
    
    result = Label(root, text="result = "+str(a+b))
    result.grid(row = 3, column=0)


def subtraction():
    try:
        a = int(ent1.get())
        b = int(ent2.get())
    except ValueError:
        result = Label(root, text="You can only enter numbers")
    
    result = Label(root, text="result = "+str(a-b))
    result.grid(row = 3, column=0)


def multiplication():
    try:
        a = int(ent1.get())
        b = int(ent2.get())
    except ValueError:
        result = Label(root, text="You can only enter numbers")
        result.grid(row = 3, column=0)
    
    result = Label(root, text="result = "+str(a*b))
    result.place(row=3, column=0)


def division():
    try:
        a = int(ent1.get())
        b = int(ent2.get())
    except ValueError:
        result = Label(root, text="You can only enter numbers")
        result.grid(row = 3, column=0)
    try:
        result = Label(root, text="result = "+str(a/b))
    except ZeroDivisionError:
        result = Label(root, text="Denominator cannot be zero")
    finally:
        result.grid(row=3, column=0)
        

add_btn = Button(root, text="+", command=addition)
add_btn.grid(row=2, column=0)
sub_btn = Button(root, text="-", command=subtraction)
sub_btn.grid(row=2, column=1)
mul_btn = Button(root, text="x", command=multiplication)
mul_btn.grid(row=2, column=2)
div_btn = Button(root, text="/", command=division)
div_btn.grid(row=2, column=3)

root.mainloop()
