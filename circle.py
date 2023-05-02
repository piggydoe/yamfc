import tkinter as tk
from tkinter import *
import os
import json
import fade

r = tk.Tk()
r.wm_attributes("-topmost", True)
r.wm_attributes("-disabled", True)
r.wm_attributes("-transparentcolor", "SystemButtonFace")
r.configure(background="SystemButtonFace")
r.overrideredirect(True)
r.lift()
try:
    with open("config/circle.json") as f:
        NORMAL = json.load(f)
        WIDTH = NORMAL['size']
        HEIGHT =  NORMAL['size']
except:
    print("No circle.json found, using default")
    WIDTH = 400
    HEIGHT = 400

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def create_circle(x, y, r, canvas): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, outline ='white', width=1)

def create(sizex, sizey):
    width = sizex
    height = sizey
    w = Canvas(r, width=width, height=height)
    create_circle(width / 2, height / 2, width / 2 - 2, w)
    w.pack()
    center(r)
    r.mainloop()

logo = f"""
                                            __  _____    __  _______________
                                            \ \/ /   |  /  |/  / ____/ ____/
                                             \  / /| | / /|_/ / /_  / /     
                                             / / ___ |/ /  / / __/ / /___   
                                            /_/_/  |_/_/  /_/_/    \____/   
                                                Yet another fov circle
                                        Close This Window To Close FOV Circle
                                                      FOV: {WIDTH}
"""
os.system("title Snowie's FOV Circle")
print(fade.greenblue(logo))
create(WIDTH, HEIGHT)           
