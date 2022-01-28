'Rechner für Fibonacci Reihe'

#Aktualisirung:
#c:\users\entropy\appdata\local\programs\python\python310\python.exe

from logging import exception, root
from tkinter import *
from tkinter import ttk
from time import sleep
import sys
from numpy import *
import matplotlib
from tabulate import tabulate
import keyboard

class Error(Exception):
    pass

class VError(Error):
    pass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    pass

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

'''
def popup(msg,ttl,xw,yw):
    root = Tk()
    root.wm_title(ttl)
    label = ttk.Label(root, text=msg, font=NORM_FONT)
    hs = label.winfo_screenheight()
    y = hs*0.1*yw
    h = (hs/2)-(y/2)
    ws = label.winfo_screenwidth()
    x = ws*0.2*xw
    w = (ws/2)-(x/2)
    root.geometry('%dx%d+%d+%d' % (x, y, w ,h ))
    label.place(relx = 0.5, rely = 0.35, anchor = 'center')
    B1 = ttk.Button(root, text="Okay", command = root.destroy)
    B1.place(relx = 0.5, rely = 0.7, anchor = 'center')
    root.attributes('-topmost', True)
    root.mainloop()
'''

def kill():
    quit()

def calc(x):
    if x < 2:
        return 1
    else:
        x = calc(x-1) + calc(x-2)
        return x


def table():
    xarr = ['Element Nr.']
    yarr = ['Wert']
    print('Wie lang soll die Tabelle sein?\nBeginn ist immer Element 1.\nEmpfohlenes Maximum:40')
    while True:
        try:
            n = int(input())
            break
        except:
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    for i in range(1,n+1):
        xarr = xarr + [str(i)]
        yarr = yarr + [str(calc(i))]
        j = (i)/n
        sys.stdout.write('\r')
        sys.stdout.write("[%-40s] %d%%" % ('❚'*int(40*j), 100*j))
        sys.stdout.flush()
        sleep(0.25)
    print('\n')
    tabl = [xarr] + [yarr]
    print(str(tabl)+ '\n' + str(xarr)+ '\n' +str(yarr))
    df = tabulate(tabl,headers= [],tablefmt='fancy_grid')
    print(df)

def zahl():
    print('Den wievielten Wert der Fibonacci-Folge wollen sie sehen?')
    while True:
        try:
            n = int(input())
            break
        except:
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    if n == 1:
        print('Der erste Wert der Fibonacci-Folge ist '+ str(calc(n)))
    else:
        print('Der ' + str(n) + '-te Wert der Fibonacci-Folge ist '+ str(calc(n)))

def menu():
    switch = {
        1: '',
        2: table,
        3: '',
        4: '',
        5: zahl,
        6: quit
    }
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
            switch[m]()
        except VError:
            #popup('Die Eingabe muss zwischen 1 und 6 liegen','Value Error',1,1)
            print(f"{bcolors.FAIL}Die Eingabe muss zwischen 1 und 6 liegen{bcolors.ENDC}")
        except ValueError:
            #popup('Eingabe muss eine Natürliche Zahl sein','Type Error',1,1)
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
        

menu()
