from tkinter import *

root = Tk()
root.title('My Window')
root.geometry('640x480')

#pack : put element in center of first emplty row it finds.
#Label(root, text="Hello, Tkinter here!").pack()

#grid : put element in the respective row and column.
#Label(root, text="Hello, Tkinter here!").grid(row=0, column=0)

#place: put at exact position from x and y axis given in pixel
Label(root, text="Hello, Tkinter here!").place(x=100, y=100)

root.mainloop()


