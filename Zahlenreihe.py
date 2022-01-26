#Rechner für Fibonacci Reihe
from tkinter import * 
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popup(msg,ttl,y,x):
    popup = Tk()
    popup.wm_title(ttl)
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.config(width=20)
    label.pack(side="top", fill="x", pady=20)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def menu():
    print('''Menü 
    1: Diagramm
    2: Tabelle
    3: Tabelle & Diagramm
    4: Vorschrift
    5: Zahlwert''')
    try:
        m = int(input())
    except:
        popup('Eingabe ist kein ganzzahlieger Wert von 1 bis 5','Fehler',0,0)

menu()