from tkinter import *
root=Tk()
import calendar

root.title("calendar")
l1=Label(root,text="Calendar",font=("times new roman",40,"normal"),bg="light blue")
l1.pack()

l2=Label(root,text="Enter here",font=("times new roman",20,"normal"))
l2.pack(pady=15)

e=Entry(root,width=20)
e.pack(pady=15)

c=Button(text="Submit",bg="red")
c.pack(pady=2)

exit=Button(text="Exit",bg="red")
exit.pack(pady=5)










mainloop()