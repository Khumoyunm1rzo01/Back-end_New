import time
a = int(input("Vaqtni kiriting: "))
def countdown(time_sec):
    while time_sec:
        global a
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("stop")
countdown(a)
input()