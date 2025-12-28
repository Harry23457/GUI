from tkinter import *
from tkinter import ttk
from tkinter import Tk
e=Tk()
e.geometry("150x150")
e.config(bg="red")

l1=Label(e,text="Pizza ordering website")
l1.grid(row=0,column=1)


pizza1=StringVar()
pizza2=["Pepperoni","magerita","Ham and pinapple","meat feast","Salad"]
box=ttk.Combobox(e,textvariable=pizza1,values=pizza2)
box.grid(row=2,column=1)


pizza3=["1","2","3","4","5","6","7","8","9","10"]
box2=ttk.combobox(e,textvariable=pizza1,values=pizza3)
box2.grid(row=2,column=1)






























mainloop()