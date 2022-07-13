import pyttsx3
import os
import random
import webbrowser
import time
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *
# раздел глобальных переменных

text = ''
r = sr.Recognizer()
engine = pyttsx3.init()
adress = ''
j = 0
task_number = 0
ndel = ['Алиса', 'Ализа','Aся','ладно', 'не могла бы ты','пожалуйста']

commnds = ["привет", "открой файл", "выключи комп", "выруби компьютер", "пока", "покажи файл","покажи список команд",
"открой vk", "открой браузер", "включи vk", "открой интернет", "открой youtube", "включи", "включи музон", "вруби музыку", "щчисти файл",
"открой стату","покажи статистику","открой музыку","переведи", "планы", "на будущее", "что планируется"]

# раздел описания функций комманд

def pri_com(): # выводит на экран историю запросов
    z = {}
    mas = []
    mas2 = []
    mas3 = []
    mas4 = []
    file = open('commands.txt', 'r', encoding = 'UTF-8')
    k = file.readlines()
    for i in range(len(k)):
        line = str(k[i].replace('\n','').strip())
        mas.append(line)
    file.close()
    for i in range(len(mas)):
        x = mas[i]
        if x in z:
            z[x] += 1
        if not(x in z):
            b = {x : 1}
            z.update(b)
        if not(x in mas2):
            mas2.append(x)
    for i in mas2:
        mas3.append(z[i])
    for i in range(1, len(mas3)+1):
        mas4.append(str(i)+') ')
        List = pd.DataFrame({
            'command': mas2,
            'count': mas3
        }, index = mas4)
        List.index.name = '№'
        print(List)

def plans():
    global engine
    plans = ''''''
    "Моя задача заключается в том, что в будущем я хочу помочь моему владельцу ХУМОЮНМИРЗО чтобы углубить его знании, и ещё в помощи в управлении системой умного дома."
    "На данный момент ведётся работа над виртуальной частью программного обеспечения."
    "Так же ведётся работа по оптимизации всех существующих в коде фукций."
    "В дальнейщем планируется работа над технической частью проекта."
    "Она будет состоять из создания эллементов умного дома с помощью микроконтроллеров Arduino."
    "В конечном итоге виртуальная и техническая части проекта будут объеденены."
    "Моя конечная цель будет достигнута. Но при этом не буду остановливаться Ха ха ха."
    ''''''
    engine.say(plans)

def clear_analis(): # очистка файла с историей запросов
    global engine
    file = open('commands.txt', 'w', encoding = 'UTF-8')
    file.close()
    engine.say('файл аналитики очищен!')

def add_file(x):
    file = open('commands.txt', 'a', encoding = 'UTF-8')
    if x != '':
        file.write(x='\n')
    file.close()
def comparison(x): # осуществляет поиск самой подходящей под запрос функции
    commands = [], j = [], add_file = []
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(x, commands[i])
        if (k > 50)&(k > j):
            ans = commands[i]
            j = k
    if (ans != 'пока')&(ans != 'привет'):
        add_file(ans)
    return(str(ans))

def web_search(): # осуществляет поиск в интернете по запросу (adress)
    global adress
    webbrowser.open('https://yandex.ru/{yandex:searchPath}?text=%s&{yandex:referralID}')

def check_searching(): # проверяет нужно ли искать в интернете
    global text, wifi_name, add_file
    global adress
    global web_search
    if 'найди' in text:
        add_file('найди')
        adress = text.replace('найди', '').strip()
        text = text.replace(adress, '').strip()
        web_search()
        text = ''
    elif 'найти' in text:
        add_file('найди')
        adress = text.replace('найти', '').strip()
        text = text.replace(adress, '').strip()
        web_search()
        text = ''
    adress = ''

def clear_task(): #удаляет ключевые слова
    global text, ndel
    for z in ndel:
        text = text.replace(z,'').strip()
        text = text.replace(' ',' ').strip()

def hello(): # Функция приветствия
    global engine
    z = ["Рада вас снова слушать!", 'Что вам угодно?', 'Привет. Чем-нибудь помочь?']
    x = random.choice(z)
    engine.say(x)

def quit(): # функция выхода из программы
    global engine
    x = ['наденуюсь мы скоро увидемся!', 'рада была помочь', 'всегда к вашим услугам']
    engine.say(random.choice(x))
    engine.runAndWait()
    engine.stop()
    os.system('cls')
    exit(0)

def show_cmds(): # выводит на экран список доступных комманд
    my_com = ['привет', 'открой файл', 'выключи компьютер', 'пока', 'покажи список команд',
    'открой vk', 'открой интернет', 'открой youtube', 'включи музыку', 'очисти файл', 'покажи статистику', 'открой этот компьютер']
    for i in my_com:
        print(i)
    time.sleep(2)

def brows(): # открывает браузер
    webbrowser.open('https://google.com')

def ovk(): # открывает вк
    webbrowser.open('https://vk.com/feed')

def youtube(): # открывает ютуб
    webbrowser.open('https://www.youtube.com')

def shut(): # выключает компьютер
    global quit
    os.system('shutdown /s /f /t 10')
    quit()

def musik(): # включает музыку
    webbrowser.open('https://vk.com/audios296431501')

def check_translate():
    global text, tr
    tr = 0
    variants = ['переведи', 'перевести', 'переводить', 'перевод']
    for i in variants:
        if (i in text)&(tr == 0):
            word = text
            word = word.replace('переведи','').strip()
            word = word.replace('перевести','').strip()
            word = word.replace('переводить','').strip()
            word = word.replace('перевод','').strip()
            word = word.replace('слово','').strip()
            word = word.replace('слова','').strip()            
            webbrowser.open('https://www.google.com/search?q=google+translate&rlz=1C1GCEA_enUZ980UZ980&oq=go&aqs=chrome.0.0i131i433i512j46i131i199i433i465i512j69i57j0i131i433i512j0i433i512l3j0i512j0i433i512l2.4042j0j15&sourceid=chrome&ie=UTF-8={}'.format(word))
            tr =1
            text = ''

cmds = {
    'привет': hello,                    'выруби компьютер' : shut,
    'пока': quit,                       'покажи статистику' : pri_com,
    'открой браузер' : brows,           'включи vk' : ovk,
    'открой youtube' : youtube,         'вруби музыку' : musik,
    'открой стату' : pri_com,           'включи музон' : musik,
    'покажи файл' : pri_com,            'открой файл' : pri_com,
    'планы' : plans,                    'на будущее' : plans,
    'переведи' : check_translate,
}

# распознование

def talk():
    global text, clear_task
    text = ''
    with sr.Microphone                                                                                          () as sourse:
        print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse, phrase_time_limit=3)
        try:
            text = (r.recognize_google(audio, language="ru-Ru")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        os.system('cls')
        lb['text'] = text
        clear_task()

# выполнение команд
def cmd_exe():
    global cmds, engine, comparison, check_searching, task_number, text, lb
    check_translate()
    text = comparison(text)
    print(text)
    check_searching()
    if (text in cmds):
        if (text != 'привет') & (text != 'пока') & (text != 'покажи список команд'):
            k = ['секундочку', 'Сейчас сделаю', 'уже выполняю']
            engine.say(random.choice(k))
        cmds[text]()
    elif text == '':
        pass
    else:
        print('Команда не найдена!')
    task_number += 1
    if (task_number % 10 == 0):
        engine.say('У вас есть ещё задания?')
    engine.runAndWait
    engine.stop()

# исправляет цвет

print(Fore.YELLOW + '', end = '')
os.system('cls')

# основной бесконечный цикл

def main():
    global text, talk, cmd_exe, j
    try:
        talk()
        if text != '':
            cmd_exe()
            j = 0
    except(UnboundLocalError):
        pass
    except(TypeError):
        pass

# раздел создания интерфейса

root = Tk()
root.geometry('250x350')
root.configure(bg = 'gray22')
root.title('Aлиса')
root.resizable(False, False)

lb = Label(root, text = text)
lb.configure(bg = 'gray')
lb.place(x = 25, y = 25, height = 25, width = 200)

but1 = Button(root, text = 'Слушать', command = main)
but1.configure(bd = 1, font = ('Castellar', 25), bg = 'gray')
but1.place(x = 50, y = 160, height = 50, width = 150)

but2 = Button(root, text = 'Выход', command = quit)
but2.configure(bd = 1, font = ('Castellar', 25), bg = 'gray')
but2.place(x = 50, y = 220, height = 50, width = 150)

root.mainloop()

while True:
    main()
