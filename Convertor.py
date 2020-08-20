from tkinter import *
import math
conv = Tk()
def convert():
    if(e1.get() == ""):
        return
    value1 = -1
    e2.delete(0,END)
    if(e1.get().find(".")):
        value1 = float(e1.get())
    else:
        value1 = int(e1.get())
    if(select.get()=="km"):
        if(select1.get()=="km"):
            e2.insert(0,value1)
        elif(select1.get()=="m"):
            e2.insert(0,value1*1000)
        elif(select1.get()=="dm"):
            e2.insert(0,value1 * 10000)
        elif (select1.get()== "cm"):
            e2.insert(0,value1 * 100000)
        elif (select1.get()== "mm"):
            e2.insert(0,value1 * 1000000)
        elif (select1.get() == "μm"):
            e2.insert(0,value1 * 1000000000)
        elif (select1.get() == "nm"):
            e2.insert(0,value1 * 1000000000000)
        elif (select1.get() == "pm"):
            e2.insert(0,value1 * 1000000000000000)
        elif (select1.get() == "mile"):
            e2.insert(0,value1 * 0.621371)
        elif (select1.get() == "yd"):
            e2.insert(0,value1 * 1093.613)
        elif (select1.get() == "ft"):
            e2.insert(0,value1 * 3280.838)
        elif (select1.get() == "in"):
            e2.insert(0,value1 * 39370.06)
    elif(select.get() == "m"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.001)
        elif (select1.get() == "m"):
            e2.insert(0, value1)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 10)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 100)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 1000)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 1000000)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * 1000000000)
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * 1000000000000)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.000621)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 1.093)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 3.280)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 39.370)
    if (select.get() == "dm"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.0001)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.1)
        elif (select1.get() == "dm"):
            e2.insert(0, value1)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 10)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 100)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 100000)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * 100000000)
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * 100000000000)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * .0000621)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.1093)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 0.328)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 3.936)
    if (select.get() == "cm"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.00001)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.01)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 0.1)
        elif (select1.get() == "cm"):
            e2.insert(0, value1)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 10)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 10000)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * 10000000)
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * 10000000000)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.00000621)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.0109)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 0.0328)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 0.393)
    if (select.get() == "mm"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.000001)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.001)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 0.01)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 0.1)
        elif (select1.get() == "mm"):
            e2.insert(0, value1)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 1000)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * 1000000)
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * 1000000000)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.000000621)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.00109)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 0.00328)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 0.0393)
    if (select.get() == "μm"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.000000001)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.000001)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 0.00001)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 0.0001)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 0.001)
        elif (select1.get() == "μm"):
            e2.insert(0, value1)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * 1000)
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * 1000000)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.00000000621)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.00000109)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 0.00000328)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 0.0000393)
    if (select.get() == "nm"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.000000000001)
        elif (select1.get() == "m"):
            e2.insert(0, value1*0.000000001)
        elif (select1.get() == "dm"):
            e2.insert(0, value1*0.00000001)
        elif (select1.get() == "cm"):
            e2.insert(0, value1*0.0000001)
        elif (select1.get() == "mm"):
            e2.insert(0, value1*0.000001)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 0.001)
        elif (select1.get() == "nm"):
            e2.insert(0, value1)
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * 1000)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.000000000000621)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.00000000109)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 0.00000000328)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 0.0000000393)
    if (select.get() == "pm"):
        if (select1.get() == "km"):
            e2.insert(0, value1*math.pow(1,-15))
        elif (select1.get() == "m"):
            e2.insert(0, value1*math.pow(1,-12))
        elif (select1.get() == "dm"):
            e2.insert(0, value1*math.pow(1,-11))
        elif (select1.get() == "cm"):
            e2.insert(0, value1*math.pow(1,-10))
        elif (select1.get() == "mm"):
            e2.insert(0, value1*math.pow(1,-9))
        elif (select1.get() == "μm"):
            e2.insert(0, value1*math.pow(1,-6))
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * 0.001)
        elif (select1.get() == "pm"):
            e2.insert(0, value1)
        elif (select1.get() == "mile"):
            e2.insert(0, value1 *math.pow(6.21,-16))
        elif (select1.get() == "yd"):
            e2.insert(0, value1*math.pow(1.09,-12))
        elif (select1.get() == "ft"):
            e2.insert(0, value1*math.pow(3.28,-12))
        elif (select1.get() == "in"):
            e2.insert(0, value1*math.pow(3.93,-11))
    if (select.get() == "mile"):
        if (select1.get() == "km"):
            e2.insert(0, value1*1.609)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 1609.34)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 16093.4)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 160934)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * math.pow(1.609,6))
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * math.pow(1.609,9))
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * math.pow(1.609,12))
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * math.pow(1.609,15))
        elif (select1.get() == "mile"):
            e2.insert(0, value1)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 1760)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 5280)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 63360)
    if (select.get() == "yd"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.0009144)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.9144)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 9.144)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 91.44)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 914.4)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 914400)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * math.pow(9.144,8))
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * math.pow(9.144,11))
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.000568)
        elif (select1.get() == "yd"):
            e2.insert(0, value1)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 3)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 36)
    if (select.get() == "ft"):
        if (select1.get() == "km"):
            e2.insert(0, value1*0.000304)
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.3048)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 3.048)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 30.48)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 304.8)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 304800)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * math.pow(3.048,8))
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * math.pow(3.048,11))
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * 0.000189)
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.333)
        elif (select1.get() == "ft"):
            e2.insert(0, value1)
        elif (select1.get() == "in"):
            e2.insert(0, value1 * 12)
    if (select.get() == "in"):
        if (select1.get() == "km"):
            e2.insert(0, value1*math.pow(2.540,-5))
        elif (select1.get() == "m"):
            e2.insert(0, value1 * 0.0254)
        elif (select1.get() == "dm"):
            e2.insert(0, value1 * 0.254)
        elif (select1.get() == "cm"):
            e2.insert(0, value1 * 2.54)
        elif (select1.get() == "mm"):
            e2.insert(0, value1 * 25.4)
        elif (select1.get() == "μm"):
            e2.insert(0, value1 * 25400)
        elif (select1.get() == "nm"):
            e2.insert(0, value1 * math.pow(2.54,7))
        elif (select1.get() == "pm"):
            e2.insert(0, value1 * math.pow(2.54,10))
        elif (select1.get() == "mile"):
            e2.insert(0, value1 * math.pow(1.57,-5))
        elif (select1.get() == "yd"):
            e2.insert(0, value1 * 0.0277)
        elif (select1.get() == "ft"):
            e2.insert(0, value1 * 0.0833)
        elif (select1.get() == "in"):
            e2.insert(0, value1)
conv.geometry("768x650")
conv.title("Length Convertor")
conv.wm_iconbitmap("length_f3N_icon.ico")
Label(text="Length Convertor",font="comicsansms 32 bold",fg="orange").grid(column=21)
v1 = IntVar()
v2=IntVar()
select=StringVar(conv)
select.set("cm")
select1=StringVar(conv)
select1.set("cm")
e1 = Entry(textvariable=v1,width=10,borderwidth=7,relief=SUNKEN,font="lucida 25 bold",fg="blue")
e1.grid(row=7,column=20,pady=30,padx=5)
e2=Entry(textvariable=v2,width=10,borderwidth=7,relief=SUNKEN,font="lucida 25 bold",fg="blue")
e2.grid(row=7,column=24)
w = OptionMenu(conv, select, "km", "m", "dm","cm","mm","μm","nm","pm","mile","yd","ft","in")
w.grid(row=13,column=20)
w1 = OptionMenu(conv, select1, "km", "m", "dm","cm","mm","μm","nm","pm","mile","yd","ft","in")
w1.grid(row=13,column=24)
but = Button(text="Calculate",font="comicsansms 11 bold",borderwidth=7,relief=SUNKEN,bg="green",command=convert)
but.grid(row=20,column=21,pady=35,padx=14)
conv.mainloop()