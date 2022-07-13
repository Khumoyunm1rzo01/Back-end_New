
import pyttsx3
from pyttsx3 import engine

while True:
        matn = input("Введите слово или предложение: ")

        pyttsx3.speak(matn)

        engine = pyttsx3.init()
        engine.save_to_file(matn, "d://Алисахон.mp3")
        engine.runAndWait()

  


