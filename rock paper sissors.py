from tkinter import *
import tkinter.font as f
import random

pscore=0
cscore=0    
options=["rock","paper","scissors"]
def rps(pchoice):
    global pscore,cscore
    cchoice=random.choice(options)
    playerchoice.config(text=pchoice)
    computerchoice.config(text=cchoice)
    if pchoice==cchoice:
        text2.config(text="It was a tie")
    elif (pchoice==options[0] and cchoice==options[2])or(pchoice==options[1] and cchoice==options[0])or(pchoice==options[2] and cchoice==options[1]):
        text2.config(text="You win") 
        pscore += 1
    else:
        text2.config(text="You lose")
        cscore += 1



root=Tk()
root.title("Rock,Paper,Sissors")
headingfont=f.Font(family="Times new roman",size=25, weight=NORMAL)
texthd=Label(root,text="Rock,Paper,Scissors",font=headingfont,bg="green")
texthd.pack()
text2=Label(root,text="lets start the game...",font=headingfont,bg="green")
text2.pack()
text3=Label(root,text="options:",font=headingfont,bg="grey")
text3.pack()

b1=Button(text="rock",bg="grey",command=lambda:rps(options[0]))
b1.pack()
b2=Button(text="paper",bg="light pink",command=lambda:rps(options[1]))
b2.pack()
b3=Button(text="sissors",bg="Red",command=lambda:rps(options[2]))
b3.pack()

f1=Frame(root)
f1.pack()

yourchoice=Label(f1,text="you selected:")
yourchoice.grid(row=0,column=0)
playerchoice=Label(f1,text="")
playerchoice.grid(row=0,column=1)
compchoice=Label(f1,text="computer selected:")
compchoice.grid(row=1,column=0)
computerchoice=Label(f1,text="")
computerchoice.grid(row=1,column=1)

playerscore=Label(f1,text="your score:")
playerscore.grid(row=0,column=2)
computerscore=Label(f1,text="computerscore")
plscore=Label(f1,text="")
plscore.grid(row=0,column=3)
coscore=Label(f1,text="")
coscore.grid(row=1,column=3)





root.mainloop()
