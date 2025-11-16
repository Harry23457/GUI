from tkinter import *

window=Tk()
window.geometry("400x500")

a=Button(window,text="Add")
a.pack()

e=Entry(window)
e.pack(pady=10)

d=Button(window,text="Delete")
d.pack(pady=10)

l=Listbox(window)
l.pack()

s=Button(window,text="save")
s.pack()

o=Button(window,text="open")
o.pack()







mainloop()