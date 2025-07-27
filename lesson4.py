from tkinter import *
root=Tk()
root.geometry("250x250")
header=Label(root,text="ice cream",font=("times new roman",25,"normal"),bg="light blue")
header.pack()
#frames
f1=Frame(root,bg="pink")
f1.pack(pady=25)
f2=Frame(root,bg="yellow")
f2.pack(pady=25)

#button
b1=Button(f1,text="choclate",bg="Brown")
b1.grid(row=0,column=0)
b2=Button(f1,text="strawberry",bg="pink")
b2.grid(row=0,column=1)
b3=Button(f1,text="Vanilla",bg="yellow")
b3.grid(row=0,column=2)













mainloop()