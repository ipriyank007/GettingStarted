from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Registration form')
root.geometry('480x360')

def do_nothing():
    pass

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=do_nothing)
filemenu.add_command(label='Open', command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quit)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='help docs', command=do_nothing)
helpmenu.add_command(label='shortcuts', command=do_nothing)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

Label(root, text="Username").grid(row=0, column=0)
user_name = Entry(root)
user_name.grid(row=0, column=1)
Label(root, text="Email").grid(row=1, column=0)
user_email = Entry(root)
user_email.grid(row=1, column=1)
Label(root, text="Password").grid(row=2, column=0)
user_password = Entry(root, show='\u2022')
user_password.grid(row=2, column=1)
Label(root, text="Gender").grid(row=3, column=0)
gender_set = Canvas(root)
gender = IntVar()
Label(gender_set, text="Male").grid(row=0, column=0)
male = Radiobutton(gender_set, variable=gender, value=0)
male.grid(row=0, column=1)
Label(gender_set, text="Female").grid(row=1, column=0)
female = Radiobutton(gender_set, variable=gender, value=1)
female.grid(row=1, column=1)
gender_set.grid(row=3, column=1)

accept_value = IntVar()
accept_license = Checkbutton(root, variable=accept_value)
accept_license.grid(row=4, column=0)
Label(root, text="Accept our Terms and Conditions").grid(row=4, column=1)

def submit_form():
    user = user_name.get()
    email = user_email.get()
    gen = gender.get()
    accepted = accept_value.get() 
    if gen:
        user_gender = 'Female'
    else:
        user_gender = "Male"
    data_format = f'''
username: {user}
email: {email}
gender: {user_gender}
license: {accepted}

=============================
'''
    if accepted:
        with open('our_database.txt', 'a') as f:
            f.write(data_format)
    else:
        messagebox.showerror('Form not submitted', 'You must agree with our terms and condition to proceed!')

    if user == '':
        messagebox.showerror('Form not submitted', 'Username cannot be empty')

   

btn = Button(root, text="Submit", command=submit_form)
btn.grid(row=5)
root.mainloop()
