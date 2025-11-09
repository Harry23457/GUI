from tkinter import *
from tkinter.messagebox import * 
import random

number=random.randint(1,20)

def neww():
    name=e1.get()
    showinfo("Welcome","well "+name+" im think of a number 1-20 can you guess it?")
    f1.pack_forget()
    f2.pack()

def game():
    guess=int(e2.get())
    if guess==number:
        showinfo("Anwser","You guessed it correctly")
        exit()
    elif guess<number:
        showinfo("Anwser","Your guess it to low")
    else:
        showinfo("Anwser","Your anwser is to high")


w=Tk()
w.geometry("220x100")

f1=Frame(w)
f1.pack()

l1=Label(f1,text="Welcome to the game")
l1.pack()

l2=Label(f1,text="Whats your name?")
l2.pack()

e1=Entry(f1)
e1.pack()

b1=Button(f1,text="OK",command=neww)
b1.pack()

f2=Frame(w)
l3=Label(f2,text="Guess:")
l3.pack()
e2=Entry(f2)
e2.pack()
b2=Button(f2,text="Guess",command=game)
b2.pack()








mainloop()