from tkinter import *
from time import strftime
window=Tk()

label=Label(bg="orange",fg="white",text="hello")
label.pack()

def clock():
    tm=strftime("%H:%M:%S %Z")
    label.config(text=tm)
    label.after(1000,clock)

clock()










window.mainloop()