from tkinter import *

from tkinter.filedialog import *


def save():
    t=asksaveasfile()

def openfile():
    f=askopenfile(filetypes=[("Text Document","*.txt"),("Python Files","*.py")])
    if f is not None:
        g=f.read()
        print(g)



window=Tk()
window.geometry("400x300")

s=Button(window,text="save",command=save)
s.pack()

o=Button(window,text="open",command=openfile)
o.pack()







mainloop()
