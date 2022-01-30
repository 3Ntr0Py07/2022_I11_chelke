'Rechner für Fibonacci Reihe'

#Aktualisirung:
#c:\users\entropy\appdata\local\programs\python\python310\python.exe

from logging import exception, root
from tkinter import *
from tkinter import ttk
from time import *
import sys
from xmlrpc.client import boolean
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.axes
from tabulate import tabulate
import keyboard
import re
from Zahlenreihe import *

Formel = 'a(n-1) + a(n-2)'
Forig = 'a(n-1) + a(n-2)'
Abbr = [2,1]
aorig = [2,1]

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


class Reprinter:
    def __init__(self):
        self.text = ''

    def moveup(self, lines):
        for _ in range(lines):
            sys.stdout.write("\x1b[A")

    def reprint(self, text):
        # Clear previous text by overwritig non-spaces with spaces
        self.moveup(self.text.count("\n"))
        sys.stdout.write(re.sub(r"[^\s]", " ", self.text))

        # Print new text
        lines = min(self.text.count("\n"), text.count("\n"))
        self.moveup(lines)
        sys.stdout.write(text)
        self.text = text

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()


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


def diagram(boo,n):
    form = ''
    xarr = [0]
    yarr = [0]
    yn = ''
    if not boo:
        print('Wiegroß soll das Diagramm sein (X-Achse)?\nBeginn ist immer Element 1.\nEmpfohlenes Maximum:40 (89,9 Sekunden Auf Intel I7 9.Gen)')
        try:
            n = int(input())
        except:
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    print('Sollen die Punkte verbunden werden? Eingabe: y/n bzw. ja/nein')
    while True:
        yn = input()
        yn = yn.lower()
        if yn == 'y' or yn == 'ja':
            form = '-'
            break
        elif yn == 'n' or yn == 'nein':
            form = 'D'
            break
        else:
            print(f"{bcolors.FAIL}Die Eingabe entspricht nicht y,n,ja oder nein{bcolors.ENDC}")
    if boo:
            print('Loading Diagramm')
    else:
        print('Loading')
    for i in range(1,n+1):
        xarr= xarr + [i]
        yarr= yarr + [a(i)]
        j = (i)/n
        sys.stdout.write('\r')
        sys.stdout.write("[%-40s] %d%%" % ('❚'*int(40*j), 100*j))
        sys.stdout.flush()
    print()
    xpoints = array(xarr)
    ypoints = array(yarr)
    tabl = xarr,yarr
    plt.plot(xpoints,ypoints,form)
    plt.axis([-n*0.1,n+0.1*n,-yarr[-1]*0.01,yarr[-1]+0.1*n])
    plt.grid(True)
    if boo:
        plt.table(cellText=tabl, cellColours=None, cellLoc='right', colWidths=None, rowLabels=['Wert Nr.','Wert'], rowColours=None, rowLoc='center', colLabels=None, colColours=None, colLoc='center', loc='top', bbox=None, edges='closed')
    plt.show()
    
def vorschrift():
    global Formel,Forig,Abbr,aorig
    print('Die aktuelle Vorschrift ist: a = ' + Formel + '\nWollen sie diese ändern?\nEingabe y/n oder ja/nein')
    yn = input().lower()
    if yn == 'n' or yn == 'nein':
        return
    else:
        print('''Eingabe der Formel in Form des Terms der a entspricht.
Operatoren: 
    Multiplikation -> *
    Division -> /
    Addition -> +
    Subtraktion -> -
    Quadratwurzel-> sqrt()
    n-te Wurzel aus x -> x**(1/n)
    Sinus/Cosinus/Tangens -> cos()/sin()/tan()
    Arcussinus usw. -> arcsin() usw.
    Natürlicher Logarithmus -> log()
    Logarithmus Basis 2/10 -> log2()/log10()
    n-te wert von a -> a(n)''')
        while True:
            Formel = input()
            if Formel.lower() == 'quit':
                return
            abr = input('Geben sie einen Konstanten Anfangswert an\nWenn n < Wert 1 , dann ist a Wert 2\nEingabeformat: Wert1,Wert2')
            Abbr = abr.split()
            kor = int(input('Geben sie den 5. Wert ein, damit die Formel auf Korrektheit geprüft werden kann.\n'))
            if a(5) == kor:
                print('Die Anwendungen wurden jetzt auf ihre Formel angepasst, es kann allerdings bei Tabellen zu Grafikfehlern kommen.')
                return
            else:
                print(f'{bcolors.WARNING}Irgendetwas scheint in ihren Angaben nicht übereinzustimmen, bitte überprüfen sie Formel und 5. Wert. Errechnet für a(5) wurde: {bcolors.ENDC}' + str(a(5)) + '.{bcolors.WARNING}\nWiederholen sie dann die korrigierte Eingabe.{bcolors.ENDC}\nFalls sie die Formel doch nicht ändern wollen schreiben sie Quit.')
                Formel = Forig
                Abbr = aorig

def kill():
    quit()


def a(n):
    if n < Abbr[0]:
        return Abbr[1]
    else:
        n = eval(Formel)
        return n


def tablec(n,boo):
    xarr = ['Wert Nr.']
    yarr = ['Wert']
    xarr2 = ['Wert Nr.']
    yarr2 = ['Wert']
    if boo:
        print('Loading Table')
    else:
        print('Loading')
    for i in range(1,n+1):
        if i >= 30:
            xarr2 = xarr2 + [str(i)]
            yarr2 = yarr2 + [str(a(i))]
        #elif i >=
        
        else:
            xarr = xarr + [str(i)]
            yarr = yarr + [str(a(i))]
        
        j = (i)/n
        sys.stdout.write('\r')
        sys.stdout.write("[%-40s] %d%%" % ('❚'*int(40*j), 100*j))
        sys.stdout.flush()
        sleep(0.25)
    return xarr,xarr2,yarr,yarr2


def table(boo,n):
    file = True
    try:
        f = open('time.txt','a')
    except:
        file = False
    if not boo:
        print('Wie lang soll die Tabelle sein?\nBeginn ist immer Element 1.\nEmpfohlenes Maximum:40 (89,9 Sekunden Auf Intel I7 9.Gen)')
        while True:
            try:
                n = int(input())
                break
            except:
                print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    a = perf_counter()
    xarr,xarr2,yarr,yarr2 = tablec(n,boo)
    b = perf_counter()
    if file:
        f.write(str(n) + ': ' + str(b-a))
    print('\n')
    tabl = [xarr] + [yarr]
    df = tabulate(tabl,headers= [],tablefmt='fancy_grid')
    if len(yarr2)>1:
        tabl2 = [xarr2] + [yarr2]
        df = df + '\n' + tabulate(tabl2,headers= [],tablefmt='fancy_grid')
    else:
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
        print('Der erste Wert der Fibonacci-Folge ist '+ str(a(n)))
    else:
        print('Der ' + str(n) + '-te Wert der Fibonacci-Folge ist '+ str(a(n)))


def dnt():
    print('Bis zum wievielten Wert soll Diagramm und Tabelle reichen?')
    while True:
        try:
            n = int(input())
            break
        except:
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    diagram(True,n)
    

def menu():
    switch = {
        1: diagram,
        2: table,
        3: dnt,
        4: zahl,
        5: vorschrift,
        6: kill
    }
    running = True
    """
    print('''   Menü 
    1: Diagramm
    2: Tabelle
    3: Tabelle & Diagramm
    4: Zahlwert
    5: Vorschrift
    6: Schließen''')
    """
    while running:
        try:
            m = int(input('''Menü \n1: Diagramm\n2: Tabelle\n3: Tabelle & Diagramm\n4: Vorschrift\n5: Zahlwert\n6: Schließen\n'''))
            if m < 1: raise VError
            if m > 6: raise VError
            if switch[m] == table or switch[m] == diagram:
                switch[m](False,0)
            else:
                switch[m]()
        except VError:
            #popup('Die Eingabe muss zwischen 1 und 6 liegen','Value Error',1,1)
            print(f"{bcolors.FAIL}Die Eingabe muss zwischen 1 und 6 liegen{bcolors.ENDC}")
        except ValueError:
            #popup('Eingabe muss eine Natürliche Zahl sein','Type Error',1,1)
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
        

menu()
