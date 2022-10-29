from tkinter import *
from tkinter.font import BOLD


def button_clicked():
    miles = input.get()

    label3.config(text=round(int(miles)*1.609))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text="", font=("Arial", 18))
label.grid(column=0, row=0)

input = Entry(width=20)
input.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Arial", 18))
label1.grid(column=2, row=0)


label2 = Label(text="is equal to", font=("Arial", 18))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Arial", 18, BOLD))
label3.grid(column=1, row=1)

label4 = Label(text="KM", font=("Arial", 18))
label4.grid(column=2, row=1)

label5 = Label(text="", font=("Arial", 18))
label5.grid(column=0, row=3)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

label6 = Label(text="", font=("Arial", 18))
label6.grid(column=2, row=3)

window.mainloop()