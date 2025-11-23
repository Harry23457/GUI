from tkinter import *
from tkinter.filedialog import *

def additem():
    item=e.get()
    l.insert(END,item)

def deleteitem():
    index=l.curselection()
    print(index)
    if index :
        index=index[::-1]
        for i in index:
            l.delete (i)


def savelist():
    f=asksaveasfile()
    if f :
        for item in l.get(0,END):
            print (item,file=f)
        l.delete(0,END)

def openlist():
    p=askopenfile()
    if p :
        l.delete(0,END)
        items=p.readlines()
        for item in items:
            l.insert(END,item.strip())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            
window=Tk()
window.geometry("400x500")

a=Button(window,text="Add",command=additem)
a.pack()


e=Entry(window)
e.pack(pady=10)

d=Button(window,text="Delete",command=deleteitem)
d.pack(pady=10)

l=Listbox(window,selectmode="multiple")
l.pack()

s=Button(window,text="save",command=savelist)
s.pack()

o=Button(window,text="open",command=openlist)
o.pack()








mainloop()