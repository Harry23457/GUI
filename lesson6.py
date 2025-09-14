from tkinter import*
root=Tk()
root.title("weight converter")
def convert():
    gr=int(e.get())*1000
    pounds=int(e.get())*2.204
    ounces=int(e.get())*35.27
    t1.delete("1.0",END)
    t2.delete("1.0",END)
    t3.delete("1.0",END)
    t1.insert(END,gr)
    t2.insert(END,pounds)
    t3.insert(END,ounces)
w1=Label(root,text="Enter the weight in kg")
w1.grid(row=0,column=0)
e=Entry(root,width=20)
e.grid(row=0,column=1)
b=Button(root,text="convert",command=convert)
b.grid(row=0,column=2)
l1=Label(root,text="Gram")
l1.grid(row=1,column=0)
l2=Label(root,text="Pounds")
l2.grid(row=1,column=1)
l3=Label(root,text="Ounce")
l3.grid(row=1,column=2)

t1=Text(root,width=20,height=1)
t1.grid(row=2,column=0)

t2=Text(root,width=20,height=1)
t2.grid(row=2,column=1)

t3=Text(root,width=20,height=1)
t3.grid(row=2,column=2)








mainloop()