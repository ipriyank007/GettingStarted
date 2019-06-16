from tkinter import *

root = Tk()
root.geometry('240x180')
root.title("My Window")
mylabel1 = Label(root, text="First Name")
mylabel1.grid(row=0, column=0)
fname = Entry(root)
fname.grid(row=0, column=1)

mylabel2 = Label(root, text="Last Name")
mylabel2.grid(row=1, column=0)
lname = Entry(root)
lname.grid(row=1, column=1)



def myfunction():
    first = fname.get()
    last = lname.get()
    result = Label(root, text=first+' '+last)
    result.grid(row=3, column=0)
gender=0
options = Radiobutton(root, textvariable= gender, command=myfunction)
options.grid(row=2, column=1)
options = Radiobutton(root, textvariable= gender, command=myfunction)
options.grid(row=2, column=2)
submit = Button(root, text="Submit", command=myfunction)
submit.grid(row=2, column=0)
root.mainloop()

