from tkinter import *

root = Tk()
root.title('Registeration Form')
root.geometry('240x180')

Label(root, text='Name').grid(row=0, column=0)
name = Entry(root)
name.grid(row=0, column=1)
Label(root, text="Email").grid(row=1, column=0)
email = Entry(root)
email.grid(row=1, column=1)
Label(root, text="Password").grid(row=2, column=0)
password = Entry(root, show='\u2022') #or *
password.grid(row=2, column=1)

def submit_form():
    nm = name.get()
    em = email.get()
    passwd = password.get()
    print(nm)

btn = Button(root, text="Submit", command=submit_form)
btn.grid(row=3)

root.mainloop()