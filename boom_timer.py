import tkinter as tkr

from python_imagesearch.imagesearch import imagesearch
from datetime import datetime

lenguage = 0
seconds = 44

root = tkr.Tk()
root.geometry("+0+0")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", 0.01)
root.resizable(0, 0)

timer_display = tkr.Label(root, font=('Trebuchet MS', 30, 'bold'), bg='black')
timer_display.pack()

now = datetime.now()
dt_string = now.strftime("[%d/%m/%Y %H:%M:%S]")

if lenguage != 0:
    print(dt_string,"- Таймер бомбы.")
    print(dt_string,"- Используйте в игре режим - в окне/или в развёрнутом окне.")
else:
    print(dt_string,"- Bomb timer started.")
    print(dt_string,"- Use window/or in the max window.")
    
def countdown(time):
    if time > 0:
        mins, secs = divmod(time, 60)

        def color_change(t_time):
            if t_time > 10:
                return 'green'
            elif 7 <= t_time <= 10:
                return 'yellow'
            elif t_time < 7:
                return 'red'

        timer_display.config(text="{:02d}:{:02d}s.".format(mins, secs),
                             fg=color_change(time)), root.after(1000, countdown, time - 1)
    else:
        root.wm_attributes('-alpha', 0.01)
        search_image()


def start_countdown():
    root.wm_attributes('-alpha', 0.7)
    countdown(seconds)

def search_image():
    if lenguage == 0:
        pos = imagesearch("./en/1.png")
        pos1 = imagesearch("./en/2.png")
        if pos[0] & pos1[0] != -1:
            start_countdown()
        else:
            root.after(100, search_image)
            
    if lenguage == 1:
        pos2 = imagesearch("./ru/1.png")
        pos3 = imagesearch("./ru/2.png")
        if pos2[0] & pos3[0] != -1:
            start_countdown()
        else:
            root.after(100, search_image)

root.after(100, search_image)
root.mainloop()
