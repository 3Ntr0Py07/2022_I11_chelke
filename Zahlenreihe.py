#Rechner für Fibonacci Reihe
from logging import root
from tkinter import *
from tkinter import ttk

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

def calc(x):
    if x < 2:
        return 1
    else:
        x = calc(x-1) + calc(x-2)
        return x


def zahl():
    print('Den wievielten Wert der Fibonaccireihe wollen sie sehen?')
    try:
        n = int(input())
    except:
        print('Der Wert darf nur eine Natürliche Zahl betragen')

def menu():
    running = True
    print('''Menü 
    1: Diagramm
    2: Tabelle
    3: Tabelle & Diagramm
    4: Vorschrift
    5: Zahlwert
    6: Schließen''')
    while running:
        try:
            m = int(input())
            if m < 1: raise VError
            if m > 6: raise VError
        except VError:
            popup('Die Eingabe muss zwischen 1 und 6 liegen','Value Error')
        except ValueError:
            popup('Eingabe muss eine Natürliche Zahl sein','Type Error')
        switch = {
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: quit()
        }

menu()
