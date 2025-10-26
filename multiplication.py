from tkinter import *
from tkinter.ttk import *
window=Tk()
#indow.geometry("200x200")

def result():
    n1=number.get()
    n2=multiples.get()
    finalanwser=""
    for i in range(1,n2+1):
        anwser=str(n1)+"x"+str(i)+"="+str(n1*i)+"\n"

        finalanwser=finalanwser+anwser

    l.config(text=finalanwser)


heading1=Label(window,text="Multiplication table")
heading1.grid(row=0,column=0,columnspan=2,pady=20,padx=20)
heading2=Label(window,text="Number")
heading2.grid(row=1,column=0,pady=20,padx=20)
number=IntVar()
box=Combobox(window,textvariable=number)
box.grid(row=1,column=1,padx=20,pady=20)
box["values"]=list(range(1,21))
number.set(1)
h3=Label(window,text="Range")
h3.grid(row=2,column=0,rowspan=3)
multiples=IntVar()
r10=Radiobutton(window,text=10,value=10,variable=multiples)
r10.grid(row=2,column=1)
r20=Radiobutton(window,text=20,value=20,variable=multiples)
r20.grid(row=3,column=1)
r30=Radiobutton(window,text=30,value=30,variable=multiples)
r30.grid(row=4,column=1)
multiples.set(10)
g=Button(window,text="Generate",command=result)
g.grid(row=5,column=0,columnspan=2,pady=20,padx=20)
l=Label(window)
l.grid(row=6,column=0,columnspan=2,pady=10,padx=10)







window.mainloop()
