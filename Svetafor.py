# import time
# rang = "Qizil"
# print("Qizil")
# while True:
#     if rang == "Qizil":
#         time.sleep(5)
#         rang = "Sariq"
#         print('')
#         time.sleep(1)
#         rang = "Yashil"
#         print('')
#     elif rang == "Yashil":
#         time.sleep(5)
#         rang = "Sariq"
#         print('')
#         time.sleep(1)
#         rang = "Qizil"
#         print("")


from tkinter import *



class TrafficLights:
    

    def __init__(self):
        

        window = Tk()
        window.title("Traffic Light")

        frame = Frame(window)
        frame.pack()

        self.color = StringVar()

        radio_red = Radiobutton(frame, text="Red", bg="red", variable=self.color, value="R", command=self.on_RadioChange)
        radio_red.grid(row=10, column=1)

        radio_yellow = Radiobutton(frame, text="Yellow", bg="yellow", variable=self.color, value="Y", command=self.on_RadioChange)               
        radio_yellow.grid(row = 10, column = 2)

        radio_green = Radiobutton(frame, text="Green", bg="green", variable=self.color, value="G", command=self.on_RadioChange)
        radio_green.grid(row = 10, column = 3)

        self.canvas = Canvas(window, width=450, height=300, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white")
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white")

        self.color.set('R')
        self.canvas.itemconfig(self.oval_red, fill="red")

        window.mainloop()

    def on_RadioChange(self):
        color = self.color.get()

        if color == 'R':
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'Y':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'G':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")


TrafficLights()




