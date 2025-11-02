from tkinter import*
root=Tk()
root.title("currency converter")
def convert():
    euro=int(e.get())*1.14
    dollars=int(e.get())*1.31
    danishkrone=int(e.get())*8.51 
    t1.delete("1.0",END)
    t2.delete("1.0",END)
    t3.delete("1.0",END)
    t1.insert(END,euro)
    t2.insert(END,dollars)
    t3.insert(END,danishkrone)
w1=Label(root,text="Enter british pound")
w1.grid(row=0,column=0)
e=Entry(root,width=20)
e.grid(row=0,column=1)
b=Button(root,text="convert",command=convert)
b.grid(row=0,column=2)
l1=Label(root,text="Euro")
l1.grid(row=1,column=0)
l2=Label(root,text="Dollar")
l2.grid(row=1,column=1)
l3=Label(root,text="Dansish krone")
l3.grid(row=1,column=2)

t1=Text(root,width=20,height=1)
t1.grid(row=2,column=0)

t2=Text(root,width=20,height=1)
t2.grid(row=2,column=1)

t3=Text(root,width=20,height=1)
t3.grid(row=2,column=2)








mainloop()