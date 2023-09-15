from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread
# my colors
head_color = '#94D82D'
balck = '#666'
main_color = '#fff'

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('deactivate alarm :', selected.get())
    mixer.music.stop()

    
window = Tk()
window.title("Python alarm")
window.geometry("600x200")

custom_font = "Georgia 18 bold"

selected = IntVar()

frame_head = Frame(window, width=600, height=10, bg=head_color)
frame_head.grid( row =0, column=0)

frame_main = Frame(window, width=600, height=590, bg=main_color)
frame_main.grid(row=1,column=0)

my_icon = Image.open('ala.png')
my_icon = ImageTk.PhotoImage(my_icon)

alarm_icon = Label(frame_main,height=100, image=my_icon , bg= main_color)
alarm_icon.place(x=30, y=40)

header  = Label(frame_main, text="Alarm", height=1 ,font=("Verdana 20 bold"), bg=main_color )
header.place(x=250, y=10)

hour_lab  = Label(frame_main, text="hour", height=1 ,font=("Verdana 12 bold"), bg=main_color, fg=head_color )
hour_lab.place(x=180, y=60)

hour_lab  = Label(frame_main, text="minute", height=1 ,font=("Verdana 12 bold"), bg=main_color, fg=head_color )
hour_lab.place(x=250, y=60)

hour_lab  = Label(frame_main, text="seconds", height=1 ,font=("Verdana 12 bold"), bg=main_color, fg=head_color )
hour_lab.place(x=330, y=60)

hour_box = Combobox(frame_main, width=2, font=("Verdana 20"))
hour_box['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
hour_box.current(0)
hour_box.place(x=180,y=90)

min_box = Combobox(frame_main, width=2, font=("Verdana 20"))
min_box['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
min_box.current(0)
min_box.place(x=260,y=90)

sec_box = Combobox(frame_main, width=2, font=("Verdana 20"))
sec_box['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
sec_box.current(0)
sec_box.place(x=340,y=90)

btn = Radiobutton(frame_main, font=("Verdana 20"), value=1, text="Set Alarm", bg=balck, fg=head_color, command=activate_alarm, variable=selected)
btn.place(x=400, y=140)
#music player
def playsound():
    mixer.music.load("ala.wav")
    mixer.music.play()
    btn2 = Radiobutton(frame_main, font=("Verdana 20"), value=1, text="Close Alarm", bg=balck, fg=head_color, command=deactivate_alarm, variable=selected)
    btn2.place(x=200, y=140)
    selected.set(0)

def alarm():
    print("i am runing")
    while(True):
        check_val =1
        print (check_val)

        alarm_hour =hour_box.get()
        alarm_min = min_box.get()
        alarm_sec = sec_box.get()

        now = datetime.now()
        print (now)
        time_hour = now.strftime("%I")
        time_min = now.strftime("%M")
        time_sec = now.strftime("%S")
        

        if check_val == 1:
            if alarm_per == time_per:
                if alarm_hour == time_hour:
                    if alarm_min == time_min:
                        if alarm_sec == time_sec:
                            mixer.init()
                            playsound()
        sleep(1)
window.mainloop()


