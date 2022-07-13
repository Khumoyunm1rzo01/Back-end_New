import pyttsx3
from tkinter import Tk,Text,Button

app = Tk()
app.title("Моя Говорящая Ассистентка ;)")
app.configure(bg="gray")
app.geometry("540x540")

Matn = Text(app,bg='white')

print(Matn.keys())
Matn.configure(width=110,height=35)
Matn.pack(pady=1)
def Run():
	matn = Matn.get(0.1, "end")
	pyttsx3.speak(matn)


play = Button(app,bg="blue",text="НАЧАТЬ ЧИТАТЬ ЛЕКЦИЮ!!!",width=40,height=3,fg="white",command=Run)
play.pack(pady=2)
engine = pyttsx3.init()
engine.save_to_file(Matn, 'd://Ассистентка.mp3')
engine.runAndWait()
app.mainloop()