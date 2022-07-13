from tkinter import Tk,Text,Button
import pyttsx3

app = Tk()
app.title("tts")
app.configure(bg="gray")
app.geometry("540x540")

Matn = Text(app,bg='white')
print(Matn.keys())
Matn.configure(width=66,height=30)
Matn.pack(pady=1)
def Run():
	matn = Matn.get(1.0, "end")
	pyttsx3.speak(matn)

play = Button(app,bg="blue",text="Boshlash",width=66,height=10,fg="white",command=Run)
play.pack(pady=2)
app.mainloop()