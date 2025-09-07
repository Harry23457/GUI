from tkinter import*
root=Tk()
root.title("weight converter")
w1=Label(root,text="Enter the weight in kg")
w1.grid(row=0,column=0)
e=Entry(root,width=20)
e.grid(row=0,column=1)
b=Button(root,text="convert")
b.grid(row=0,column=2)
l1=Label(root,text="Gram")
l1.grid(row=1,column=0)
l2=Label(root,text="Pounds")
l2.grid(row=1,column=1)
l3=Label(root,text="Ounce")
l3.grid(row=1,column=2)


mainloop()