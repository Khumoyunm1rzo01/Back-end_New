from tkinter import *
from tkinter import font
from tkinter.ttk import *
from time import *

root = Tk()
root.title('Soat')

def soat():
    string = strftime("%H:%M:%S %p ")
    label.config(text=string)
    label.after(1000, soat)

label =Label (root, font=('ds-digital', 100), background="black", foreground="cyan")
label.pack(anchor="center")

soat()
root.mainloop()