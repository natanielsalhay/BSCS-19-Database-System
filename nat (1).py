import tkinter as tk
from tkinter import *

master = tk.Tk()

master.geometry("1350x700+0+0")
master.title("nataniel")
master.configure(background = 'turquoise4')
master.resizable(False,False)

#########################################  frame  #####################
Tops = Frame(master, bg='turquoise1', bd=5, pady=5, relief=RIDGE)
Tops.pack(side=TOP, fill =X)
lblTitle = Label (Tops, font=('Times New Roman', 60, 'bold'),text = "Student Information System", bd=5, bg= 'turquoise1', fg='black', justify=CENTER)
lblTitle.pack (side = TOP)

add = Frame(master, bg='turquoise2', bd=5, pady=5, relief=RIDGE)
add.pack(side=LEFT, fill =BOTH)
add_lbl = Label (add, font=('Times New Roman', 30, 'bold','italic'),text = "Add Information", bd=5, bg= 'turquoise2', fg='black', justify=CENTER)
add_lbl.pack (side = TOP)

rem = Frame(master, bg='turquoise2', bd=5, pady=5, relief=RIDGE)
rem.pack(side=LEFT, fill =BOTH)


alllist = Frame(master, bg='turquoise2', bd=5, pady=5, relief=RIDGE)
alllist.pack(side=RIGHT, fill =X)

addname = Label(add, text = "Name:", font = ('times new roman', 12), bg="turquoise2")
addname.pack(side=TOP, fill=X)
entryname = Entry(add, width = 40, font = ('times new roman',12,'bold'))
entryname.pack(side=TOP)

addid = Label(add, text = "Student ID:", font = ('times new roman', 12), bg="turquoise2")
addid.pack(side=TOP, fill=X)
entryid = Entry(add, width = 40, font = ('times new roman',12,'bold'))
entryid.pack(side=TOP)

addsection = Label(add, text = "Year and Section:", font = ('times new roman', 12), bg="turquoise2")
addsection.pack(side=TOP, fill=X)
entrysection = Entry(add, width = 40, font = ('times new roman',12,'bold'))
entrysection.pack(side=TOP)

addgender = Label(add, text = "Gender", font = ('times new roman', 12), bg="turquoise2")
addgender.pack(side=TOP, fill=X)
entrygender = Entry(add, width = 40, font = ('times new roman',12,'bold'))
entrygender.pack(side=TOP)

addaddress = Label(add, text = "Address:", font = ('times new roman', 12), bg="turquoise2")
addaddress.pack(side=TOP, fill=X)
entryaddress = Entry(add, width = 40, font = ('times new roman',12,'bold'))
entryaddress.pack(side=TOP)

rem_lbl = Label (rem, font=('Times New Roman', 30, 'bold','italic'),text = "Remove Information", bd=5, bg= 'turquoise2', fg='black', justify=CENTER)
rem_lbl.pack (side = TOP)

rem_lbl = Label(rem, text = "Enter id number to remove", font = ('times new roman', 12), bg="turquoise2")
rem_lbl.pack(side=TOP, fill=X)

entry_rem = Entry(rem, width = 40, font = ('times new roman',12,'bold'))
entry_rem.pack(side=TOP)

btn_remove = Button (rem, padx = 20, pady = 3, fg="black", bg = "indianred1", font=('times new roman',10,"bold"), width=10, text='Remove')
btn_remove.pack (side=BOTTOM)

btn_done = Button (add, padx = 20, pady = 3, fg="black", bg = "green2", font=('times new roman',10,"bold"), width=10, text='Done')
btn_done.pack (side=BOTTOM)

btn_discard = Button (add, padx = 20, pady = 3, fg="black", bg = "MediumPurple1", font=('times new roman',10,"bold"), width=10, text='Discard')
btn_discard.pack (side=BOTTOM)

master.mainloop()
