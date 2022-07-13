from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Humoyunmirzo Soati :) ')

def time():
    string = strftime("%H:%M:%S %p %D %Y")
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = ('Calibri', 45, 'bold'), background = 'yellow', foreground = 'red')
label.pack(anchor = 'center') 
time()
mainloop()
