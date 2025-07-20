from tkinter import *
from tkinter.ttk import *
root=Tk()
#proggress bar
progress=Progressbar(root,orient=HORIZONTAL,length=100,mode=("determinate"))
progress.pack(pady=20)
button1=Button(root,text="Start")
button1.pack(pady=10)










mainloop()
