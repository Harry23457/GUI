from tkinter import *
from tkinter import messagebox

mainwindow=Tk()
mainwindow.title("Tic Tac Toe")

turn=1
result=""

def win():
    global result
    if (b1.cget("text")==b2.cget("Text")==b3.cget("text")) and b1.cget("text")!="":
        result=f"player {"1" if b1.cget("text")== "x" else "2"}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()

    elif (b4.cget("text")==b5.cget("Text")==b6.cget("text")) and b4.cget("text")!="":
        result=f"player {"1" if b4.cget("text")== "x" else "2"}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()
    
    elif (b7.cget("text")==b9.cget("Text")==b9.cget("text")) and b7.cget("text")!="":
        result=f"player{"1" if b7.cget("text")== "x" else "2"}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()

    elif (b1.cget("text")==b4.cget("Text")==b7.cget("text")) and b1.cget("text")!="":
        result=f"player {"1" if b1.cget("text")== "x" else "2"}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()

    elif (b2.cget("text")==b5.cget("Text")==b8.cget("text")) and b2.cget("text")!="":
        result=f"player {"1" if b2.cget("text")== "x" else "2"}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()

    elif (b3.cget("text")==b6.cget("Text")==b9.cget("text")) and b3.cget("text")!="":
        result=f"player {'1' if b3.cget("text")== "x" else '2'}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()

    elif (b1.cget("text")==b5.cget("Text")==b9.cget("text")) and b1.cget("text")!="":
        result=f"player{'1' if b1.cget("text")== "x" else '2'}Wins"
        messagebox.showinfo("Result",result)
        mainwindow.destroy()

def b1Click():
    global turn
    myText=b1.cget("text")
    if myText == "":
        if turn ==1:
            b1.configure(text="x")
            turn=2
        else:
            b1.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

def b2Click():
    global turn
    myText=b2.cget("text")
    if myText == "":
        if turn ==1:
            b2.configure(text="x")
            turn=2
        else:
            b2.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

             
def b3Click():
    global turn
    myText=b3.cget("text")
    if myText == "":
        if turn ==1:
            b3.configure(text="x")
            turn=2
        else:
            b3.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

def b4Click():
    global turn
    myText=b4.cget("text")
    if myText == "":
        if turn ==1:
            b4.configure(text="x")
            turn=2
        else:
            b4.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()  

def b5Click():
    global turn
    myText=b5.cget("text")
    if myText == "":
        if turn ==1:
            b5.configure(text="x")
            turn=2
        else:
            b5.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

def b6Click():
    global turn
    myText=b6.cget("text")
    if myText == "":
        if turn ==1:
            b6.configure(text="x")
            turn=2
        else:
            b6.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

def b7Click():
    global turn
    myText=b7.cget("text")
    if myText == "":
        if turn ==1:
            b7.configure(text="x")
            turn=2
        else:
            b7.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

def b8Click():
    global turn
    myText=b8.cget("text")
    if myText == "":
        if turn ==1:
            b8.configure(text="x")
            turn=2
        else:
            b8.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()

def b9Click():
    global turn
    myText=b9.cget("text")
    if myText == "":
        if turn ==1:
            b6.configure(text="x")
            turn=2
        else:
            b9.configure(text="O")
            turn=1
            Lbl.configure(txt="player" + str(turn) + "Turn")
            win()


b1=Button(mainwindow,text="",width=5,command=b1Click)
b1.gris(row=0,column=0,padx=4,pady=5)


b2=Button(mainwindow,text="",width=5,command=b2Click)
b2.gris(row=0,column=0,padx=4,pady=5)


b3=Button(mainwindow,text="",width=5,command=b3Click)
b3.gris(row=0,column=0,padx=4,pady=5)


b4=Button(mainwindow,text="",width=5,command=b4Click)
b4.gris(row=0,column=0,padx=4,pady=5)


b5=Button(mainwindow,text="",width=5,command=b5Click)
b5.gris(row=0,column=0,padx=4,pady=5)

b6=Button(mainwindow,text="",width=5,command=b6Click)
b6.gris(row=0,column=0,padx=4,pady=5)

b7=Button(mainwindow,text="",width=5,command=b7Click)
b7.gris(row=0,column=0,padx=4,pady=5)

b8=Button(mainwindow,text="",width=5,command=b8Click)
b8.gris(row=0,column=0,padx=4,pady=5)

b9=Button(mainwindow,text="",width=5,command=b9Click)
b9.gris(row=0,column=0,padx=4,pady=5)

Lbl=Label(mainwindow,text="Player 1 turn")
Lbl.grid(row=3,column=1,padx=10,pad=10)

mainwindow.mainloop()