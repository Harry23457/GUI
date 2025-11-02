from tkinter import*
window=Tk()
window.geometry("200x200")


w4=Scrollbar(window)
w4.pack(side=RIGHT,fill=Y)

list3=Listbox(window,yscrollcommand=w4.set)
list3.pack()
w4.config(command=list3.yview)

for i in range(41):


    list3.insert(END,str(i)+"Duck")









mainloop()