from tkinter import *

window = Tk()
window.geometry("300x300")

def from_pounds():
    euros = float(e2_value.get()) * 1.06
    yens = float(e2_value.get()) * 2.21
    dollers = float(e2_value.get()) * 3.65

    t1.delete("1.0", END)
    t1.insert(END, euros)

    t2.delete("1.0", END)
    t2.insert(END, yens)

    t3.delete("1.0", END)
    t3.insert(END, dollers)

e1 = Label(window, text="Enter the amount in Pounds")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='Euros')
e4 = Label(window, text='Yens')
e5 = Label(window, text='Dollers')

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

b1 = Button(window, text="Convert", command=from_pounds)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()
