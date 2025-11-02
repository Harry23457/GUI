from tkinter import *
from tkinter.messagebox import*


window=Tk()
window.geometry("200x200")

showinfo("information","Today is tuesday")


showerror("Error message","you have been hacked")

showwarning("Warning","Its raining")

print(askquestion("Question","Is it Tuesday?"))

print(askokcancel("Question","Is it wensday?"))

print(askyesno("Question","would you like to continue?"))

print(askretrycancel("Question","cant open file"))






mainloop()