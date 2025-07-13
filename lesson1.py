from tkinter import *
root=Tk()
#window dimensions
root.geometry("250x250")
#label widget
label=Label(root,text="username")
label.place(x=40,y=40)
passlabel=Label(root,text="password")
passlabel.place(x=40,y=80)
#entrywidget
userentry=Entry(root,width=20)
userentry.place(x=40,y=60)
passentry=Entry(root,show="*",width=20)
passentry.place(x=40,y=100)
#buttonwidget
button1=Button(root,text="Login")
button1.place(x=60,y=140)










































mainloop()













