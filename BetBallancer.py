from tkinter import *

root = Tk()
root.geometry('640x480')
root.title("Betting Ballancer")
label1 = Label(root, text= "1")
label1.grid(row= 0, column = 0)

label2 = Label(root, text= "2")
label2.grid(row= 1, column = 0)

label3 = Label(root, text= "3")
label3.grid(row= 2, column = 0)

label4 = Label(root, text= "4")
label4.grid(row= 3, column = 0)

label5 = Label(root, text= "5")
label5.grid(row= 4, column = 0)

label6 = Label(root, text= "6")
label6.grid(row= 5, column = 0)

entry1 = Entry(root)
entry1.grid(row= 0, column = 1)


entry2 = Entry(root)
entry2.grid(row= 1, column = 1)

entry3 = Entry(root)
entry3.grid(row= 2, column = 1)


entry4 = Entry(root)
entry4.grid(row= 3, column = 1)

entry5 = Entry(root)
entry5.grid(row= 4, column = 1)

entry6 = Entry(root)
entry6.grid(row= 5, column = 1)

odds1 = Entry(root)
odds1.grid(row= 0, column = 2)


odds2 = Entry(root)
odds2.grid(row=1, column=2)

odds3 = Entry(root)
odds3.grid(row=2, column=2)

odds4 = Entry(root)
odds4.grid(row=3, column=2)

odds5 = Entry(root)
odds5.grid(row=4, column=2)

odds6 = Entry(root)
odds6.grid(row= 5, column = 2)

# submit = Button(root, text="Enter", width=15, command=lambda: valueGET(e1.get(), e2.get()))
# submit.grid(row=6,column=2)

def printvalues():
    principal = []
    large = 0
    largeodd = 0
    winamt = 0
    e1 = entry1.get()
    if not e1 is'':
        e1 = int(e1)
        if e1>large:
            large =e1
        principal.append(e1)
    e2 = entry2.get()
    if not e2 is '':
        e2 = int(e2)
        if e2>large:
            large =e2
        principal.append(e2)
    e3 = entry3.get()
    if not e3 is '':
        e3 = int(e3)
        if e3>large:
            large =e3
        principal.append(e3)
    e4 = entry4.get()
    if not e4 is '':
        e4 = int(e4)
        if e4>large:
            large =e4
        principal.append(e4)
    e5 = entry5.get()
    if not e5 is '':
        e5 = int(e5)
        if e5>large:
            large =e5
        principal.append(e5)
    e6 = entry6.get()
    if not e6 is '':
        e6 = int(e6)
        if e6>large:
            large =e6
        principal.append(e6)
    odds = []

    o1 = odds1.get()
    if not o1 is '':
        o1 = float(o1)
        if large == e1:
            largeodd = o1
        odds.append(o1)
    o2 = odds2.get()
    if not o2 is '':
        o2 = float(o2)
        if large == e2:
            largeodd = o2
        odds.append(o2)
    o3 = odds3.get()
    if not o3 is '':
        o3 = float(o3)
        if large == e3:
            largeodd = o3
        odds.append(o3)
    o4 = odds4.get()
    if not o4 is '':
        o4 = float(o4)
        if large == e4:
            largeodd = o4
        odds.append(o4)
    o5 = odds5.get()
    if not o5 is '':
        o5 = float(o5)
        if large == e5:
            largeodd = o5
        odds.append(o5)
    o6 = odds6.get()
    if not o6 is '':
        o6 = float(o6)
        if large == e6:
            largeodd = o6
        odds.append(o6)
    def customwin():
        winner = winnerentry.get()
        if winner is '1':
            winamt = o1*e1
            largeodd = o1
        if winner is '2':
            winamt = o2*e2
            largeodd = o2
        if winner is '3':
            winamt = o3*e3
            largeodd = o3
        if winner is '4':
            winamt = o4*e4
            largeodd = o4
        if winner is '5':
            winamt = o5*e5
            largeodd = o5
        if winner is '6':
            winamt = o6*e6
            largeodd = o6
        totalOutcome = Label(root, text = ((winamt - sum(principal))))
        totalOutcome.grid(row=7,column=2)
    custombutton = Button(root, text='Custom winner', command=customwin)
    custombutton.grid
     # = [e1, e2, e3, e4, e5, e6]
    # odds = [o1, o2, o3, o4, o5, o6]
    finalinvest = Label(root, text=sum(principal))
    finalinvest.grid(row=7, column=1)
    finalreturn = Label(root, text =(large*largeodd-sum(principal)) )
    def predictnow():
        prediction = []
        e1 = entry1.get()
        if e1 is '':
            e1 = sum(principal)/(float(o1)-1)
            # e1['text'] =float(e1)
            prelabel = Label(root, text = e1)
            prelabel.grid(row = 0,column = 4)
            prediction.append(e1)

        e2 = entry2.get()
        if e2 is '':

            e2 = sum(principal) / (float(o2) - 1)
            # e2['text'] = float(e2)
            prelabel1 = Label(root, text=e2)
            prelabel1.grid(row=1, column=4)
            prediction.append(e2)

        e3 = entry3.get()
        if e3 is '':

            e3 = sum(principal) / (float(o3) - 1)
            # e3['text'] = float(e3)
            prelabel2 = Label(root, text=e3)
            prelabel2.grid(row=2, column=4)
            prediction.append(e3)

        e4 = entry4.get()
        if e4 is '':

            e4 = sum(principal) / (float(o4) - 1)
            # e4['text'] = float(e4)
            prelabel3 = Label(root, text=e4)
            prelabel3.grid(row=3, column=4)
            prediction.append(e4)

        e5 = entry5.get()
        if e5 is '':

            e5 = sum(principal)/(float(o5)-1)
            # e5['text'] = float(e5)
            prediction.append(e5)
            prelabel4 = Label(root, text=e5)
            prelabel4.grid(row=4, column=4)

        e6 = entry6.get()
        if e6 is '':

            e6 = sum(principal) / (float(o6) - 1)
            # e6['text'] = float(e6)
            prelabel5 = Label(root, text=e6)
            prelabel5.grid(row=5, column=4)
            prediction.append(e6)
        # predictLabel = Label(root, text = )

    getPrediction = Button(root, text='Get Prediction', command = predictnow)
    getPrediction.grid(row=6, column=2)

submit2 = Button(root, text="GetValue",command= printvalues)
submit2.grid(row=6, column=1)
winnerentry = Entry(root)
winnerentry.grid(row=6, column=0)
root.mainloop()
