from tkinter import *
from tkinter import ttk
from tkinter import Tk
e=Tk()
e.geometry("300x300")
e.config(bg="red")

l1=Label(e,text="Pizza ordering website")
l1.grid(row=0,column=1)


pizza1=StringVar()
pizza2=["Pepperoni","magerita","Ham and pinapple","meat feast","Salad"]
box=ttk.Combobox(e,textvariable=pizza1,values=pizza2)
box.grid(row=1,column=1)

pizza3=StringVar()
pizza4=["Lemonade","Cola","Fanta","Water","Nothing"]
box2=ttk.Combobox(e,textvariable=pizza3,values=pizza4)
box2.grid(row=2 ,column=1)

pizza5=StringVar()
pizza6=["Small","Medium","Large","Extra large"]
box3=ttk.Combobox(e,textvariable=pizza5,values=pizza6)
box3.grid(row=3,column=1)


def ordered():
    pizza=pizza1.get()
    drink=pizza3.get()
    size=pizza5.get()
    l1=Label(e,text=f"You ordered a {size} {pizza} and a {drink} drink")
    l1.grid(row=5,column=1)


b1=Button(e,text="place order",command=ordered)
b1.grid(row=4,column=1)






























mainloop()