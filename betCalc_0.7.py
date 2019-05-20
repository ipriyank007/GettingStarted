from tkinter import *

root = Tk()


s_no = Label(root, text="S. No.")
s_no.grid(row=0, column=0)

bet_amt = Label(root, text="Betting Amount")
bet_amt.grid(row=0, column=1)

odd = Label(root, text="Odds")
odd.grid(row=0, column=2)

l1=l2=l3=l4=l5=l6=l7=l8=l9=l10=0
l_names = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
for i in range(10):
    l_names[i] = Label(root, text = i+1)
    l_names[i].grid(row=i+1, column=0)

e1=e2=e3=e4=e5=e6=e7=e8=e9=e10=0
e_names = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
for i in range(10):
    e_names[i]= Entry(root)
    e_names[i].grid(row=i+1, column=1)

o1=o2=o3=o4=o5=o6=o7=o8=o9=o10=0
odds = [o1,o2,o3,o4,o5,o6,o7,o8,o9,o10]

for i in range(10):
    odds[i] = Entry(root)
    odds[i].grid(row=i+1, column=2)


b1=b2=b3=b4=b5=b6=b7=b8=b9=b10=0
bets = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]

od1 = od2 = od3 = od4 = od5 = od6 = od7 = od8 = od9 = od10 = 0
ods = [od1, od2, od3, od4, od5, od6, od7, od8, od9, od10]

def docal():
    global e_names
    # e_names = list(map(int, e_names))
    global odds
    # odds = list(map(int, odds))
    global bets
    # bets = list(map(int, bets))
    global ods

    for i in range(10):
        bets[i] = e_names[i].get()
        if not bets[i] is '':
            bets[i] = float(bets[i])
        if bets[i] is '':
            bets[i] = 0.0

        ods[i] = odds[i].get()
        if not ods[i] is '':
            ods[i] = float(ods[i])
        if ods[i] is '':
            ods[i]= 0

    d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = d9 = d10 = 0
    dif = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

    sh1 = sh2 = sh3 = sh4 = sh5 = sh6 = sh7 = sh8 = sh9 = sh10 = 0
    showbet = [sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, sh9, sh10]

    zipped = zip(ods, bets, dif, showbet)

    sorted_list = sorted(zipped, key=lambda x: x[0])

    strip_sorted_list = list(map(list,zip(*sorted_list)))

    ods = strip_sorted_list[0]
    bets = strip_sorted_list[1]
    dif = strip_sorted_list[2]
    showbet = strip_sorted_list[3]

    max_value = max(bets)
    ind_max_ind = bets.index(max_value)
    total = max_value


    for i in range(0,ind_max_ind):
        if bets[i] == 0 and not ods[i] == 0:
            dif[i] = total/ods[i]
            total += dif[i]
            dif[i] = round(dif[i],3)
    for i in range(ind_max_ind, len(bets)):
        if bets[i] == 0 and not ods[i] == 0:
            dif[i] += total/ods[i]
            total += dif[i]
            dif[i] = round(dif[i], 3)



    for i in range(10):
        showbet[i] = Label(root, text=dif[i])
        showbet[i].grid(row=ods.index(ods[i])+1, column=3)
    showbets = Label(root, text=max(bets))
    showbets.grid(row=11, column=1)

    showPred = Label(root, text=sum(dif))
    showPred.grid(row=11, column=3)

    # count = 0
    #
    # while sum(dif)>1:
    #
    #     dif[count] =



calbutton = Button(root, text="Calculate", command = docal)
calbutton.grid(row=11, column=0)


root.mainloop()