#Rechner für Fibonacci Reihe
from logging import root
from tkinter import * 
from tkinter import ttk
import numpy

class Error(Exception):
    pass


class VError(Error):
    pass

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popup(msg,ttl):
    root = Tk()
    root.wm_title(ttl)
    label = ttk.Label(root, text=msg, font=NORM_FONT)
    hs = label.winfo_screenheight()
    y = hs*0.1
    h = (hs/2)-(y/2)
    ws = label.winfo_screenwidth()
    x = ws*0.2
    w = (ws/2)-(x/2)
    root.geometry('%dx%d+%d+%d' % (x, y, w ,h ))
    label.place(relx = 0.5, rely = 0.35, anchor = 'center')
    B1 = ttk.Button(root, text="Okay", command = root.destroy)
    B1.place(relx = 0.5, rely = 0.7, anchor = 'center')
    root.attributes('-topmost', True)
    root.mainloop()

def menu():
    print('''Menü 
    1: Diagramm
    2: Tabelle
    3: Tabelle & Diagramm
    4: Vorschrift
    5: Zahlwert''')
    while Running:
        try:
            m = int(input())
            if m < 1: raise VError
            if m > 5: raise VeError
        except VError:
            popup('Die Eingabe muss zwischen 1 und 5 liegen','Value Error')
        except ValueError:
            popup('Eingabe muss eine Natürliche Zahl sein','Type Error')

menu()