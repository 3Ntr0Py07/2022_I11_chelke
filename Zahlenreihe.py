'Rechner für Zahlenfolgen'

#Aktualisirung:
#c:\users\entropy\appdata\local\programs\python\python310\python.exe
#C:\Users\chelke\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe

from tkinter import *
from tkinter import ttk
from time import *
import sys
from numpy import *
from tabulate import tabulate
import re
import matplotlib.pyplot as plt
import colorama
import keyboard
import subprocess as sub
import random
import pandas as pd
import os
import platform

colorama.init()

#cpid = sub.Popen(['cmd'],start_new_session=True,shell=True).pid

Formel = 'a(n-1) + a(n-2)'
Forig = 'a(n-1) + a(n-2)'
Abbr = [2,1]
aorig = [2,1]
canc = False

'''
class cancelThreat(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name = 'Thread1')
    def run(self):
        global canc
        print('Start Thread')
        while not canc:
            if keyboard.is_pressed('space'):
                print('\rpressed')
                os.system('start cmd')
                canc = True
            else:
                os.system('start cmd')
                #os.system('pause')
                #sys.stdout.flush()
        print('Thread end')
        os.system('start cmd')


'''

'''
def startt():
    try:
        if t1.isAlive():
            return t1
        t1 = cancelThreat()
        t1.start()
    except:
        t1 = cancelThreat()
        t1.start()
    return t1
'''

class Error(Exception):
    pass


class VError(Error):
    pass


class bcolors:
    HEADER = '\033[95m'
    TITLE = '\033[51m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    pass


def clear():
    x = dos()
    if x == 'Linux' or x == 'Darwin':
        os.system('clear')
    elif x == 'Windows':
        os.system('cls')
    else:
        print(f'{bcolors.FAIL}Your Operation System is not Supported for this Function yet{bcolors.ENDC}')

def dos():
    return platform.system()


def restart():
    print(f'{bcolors.OKBLUE}Rebooting{bcolors.ENDC}')
    clear()
    sleep(1)
    os.execv(sys.executable, ['python'] + sys.argv)

'''
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
'''


def keytool():
    clear()
    x = random.randint(0,1)
    if x == 1:
        print('Die Tür ist offen.')
    else:
    print('Die Tür ist geschlossen')


def diagram(boo,n):
    if boo = False:
        clear()
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
            print(f'{bcolors.OKCYAN}Loading Diagramm{bcolors.ENDC}')
    else:
        print(f'{bcolors.OKCYAN}Loading{bcolors.ENDC}')
    for i in range(1,n+1):
        xarr = xarr + [i]
        yarr = yarr + [a(i)]
        j = (i)/n
        sys.stdout.write('\r')
        sys.stdout.write("|%-40s| %d%%" % ('█'*int(40*j), 100*j))
        sys.stdout.flush()
        if keyboard.is_pressed('esc'):
            return
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
    clear()
    global Formel,Forig,Abbr,aorig
    print('Die aktuelle Vorschrift ist: a = ' + Formel + ' a(n < ' + str(Abbr[0]) +') = '+ str(Abbr[1]) +'\nWollen sie diese ändern oder auf Standart zurücksetzen?\nEingabe y/n, ja/nein oder reset')
    while True:   
        yn = input().lower()
        if yn == 'n' or yn == 'nein':
            return
        elif yn == 'y' or yn == 'ja':
            print('''Geben sie ihre Vorschrift ein.
Operatoren: 
    Multiplikation -> *
    Division -> /
    Addition -> +
    Subtraktion -> -
    Quadratwurzel-> sqrt()
    Potenzen
    m-te Wurzel aus x -> x**(1/m)
    Sinus/Cosinus/Tangens -> cos()/sin()/tan()
    Arcussinus usw. -> arcsin() usw.
    Natürlicher Logarithmus -> log()
    Logarithmus Basis 2/10 -> log2()/log10()
    n-te wert von a -> a(n)
Konstanten:
    Eulersche Zahl e -> e
    π -> pi
    Euler-Mascheroni-Konstante (γ)-> euler_gamma
    Falls Eine andere Konstante benötigt wird, kann entweder der Zahlwert eingegeben werden oder auf Anfrage diese hinzugefügt werden.''')
            while True:
                Formel = input('a(n) = ')
                if Formel.lower() == 'quit':
                    break
                abr = input('Geben sie einen Konstanten Anfangswert an\nWenn n < Wert 1 , dann ist a Wert 2\nEingabeformat: Wert1,Wert2\n')
                Abbr = abr.split(',')
                kor = int(input('Geben sie den 5. Wert ein, damit die Formel auf Korrektheit geprüft werden kann.\n'))
                try:
                    if a(5) == kor:
                        print('Die Anwendungen wurden jetzt auf ihre Formel angepasst, es kann allerdings bei Tabellen zu Grafikfehlern kommen.')
                        return
                    else:
                        print(f'{bcolors.WARNING}Irgendetwas scheint in ihren Angaben nicht übereinzustimmen, bitte überprüfen sie Formel und 5. Wert. Errechnet für a(5) wurde: {bcolors.ENDC}' + str(a(5)) + f'.{bcolors.WARNING}\nWiederholen sie dann die korrigierte Eingabe.{bcolors.ENDC}\nFalls sie die Formel doch nicht ändern wollen schreiben sie Quit.')
                        Formel = Forig
                        Abbr = aorig
                except Exception as _err:
                    print(f'{bcolors.FAIL}Ihre Formel scheint mathematisch nicht korrekt zu sein. Überprüfen sie die Syntax und versuchen sie erneut.{bcolors.ENDC}')
                    print("Error Message:")
                    print(str(_err))
                
        elif yn.lower() == 'reset':
            Formel = Forig
            Abbr = aorig
            print(f'{bcolors.OKGREEN}Vorschrift zurückgesetzt{bcolors.ENDC}')
            return
        else:
            print(f"{bcolors.FAIL}Die Eingabe entspricht nicht y,n,ja oder nein{bcolors.ENDC}")


def kill():
    #os.system('taskkill /PID /F ' + str(cpid))
    quit()


def ptz(a,b):
    x = float_power(a,b)
    if abs(x-floor(x))<1e-6:
        trunc(x)
    return x
    


def a(n):
    if n < int(Abbr[0]):
        return int(Abbr[1])
    else:
        n = eval(Formel)
        return n


'''
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
        sys.stdout.write("|%-40s| %d%%" % ('█'*int(40*j), 100*j))
        sys.stdout.flush()
    return xarr,xarr2,yarr,yarr2
'''


def table(boo,n):
    clear()
    xarr = ['Wert']
    yarr = ['Wert Nr.']
    if not boo:
        print('Wie lang soll die Tabelle sein?\nBeginn ist immer Element 1.\nEmpfohlenes Maximum:40 (89,9 Sekunden Auf Intel I7 9.Gen)')
        while True:
            try:
                n = int(input())
                break
            except:
                print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    print(f'{bcolors.OKCYAN}Loading Table{bcolors.ENDC}')
    for i in range(1,n+1):
        xarr = xarr + [str(i)]
        yarr = yarr + [str(a(i))]
        j = (i)/n
        sys.stdout.write('\r')
        sys.stdout.write("|%-40s| %d%%" % ('█'*int(40*j), 100*j))
        sys.stdout.flush()
        if keyboard.is_pressed('esc'):
            return
    #fig, ax = plt.subplots()
    #fig.patch.set_visible(False)
    #ax.axis('off')
    #ax.axis('tight')
    tabl = [xarr,yarr]
    #df = pd.DataFrame(data = array(tabl),dtype = 'string')
    df = tabulate(tabl, tablefmt="fancy_grid")
    print('\n' +df)
    #ax = table(cellText=df.values, cellColours=None, cellLoc='right', colWidths=None, rowLabels=['Wert Nr.','Wert'], rowColours=None, rowLoc='center', colLabels=None, colColours=None, colLoc='center', loc='top', bbox=None, edges='closed')
    #ax.set_fontsize(14)
    #ax.setscale(2,2)
    #fig.tight_layout()
    #plt.show()    


def zahl():
    clear()
    print('Den wievielten Wert Zahlenreihe wollen sie sehen?')
    while True:
        try:
            n = int(input())
            break
        except:
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    if n == 1:
        print('Der erste Wert Zahlenreihe ist '+ str(a(n)))
    else:
        print(f'Der ' + str(n) + '-te Wert der Zahlenreihe ist '+ str(a(n)))


def dnt():
    clear()
    print('Bis zum wievielten Wert soll Diagramm und Tabelle reichen?')
    while True:
        try:
            n = int(input())
            break
        except:
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}")
    diagram(True,n)
    

def menu():
    clear()
    switch = {
        1: diagram,
        2: table,
        3: dnt,
        4: zahl,
        5: vorschrift,
        6: kill,
        7: restart,
        42: keytool
    }
    """
    print('''   Menü 
    1: Diagramm
    2: Tabelle
    3: Tabelle & Diagramm
    4: Zahlwert
    5: Vorschrift
    6: Schließen''')
    """
    while True:
        try:
            m = int(input('''Menü \n1: Diagramm\n2: Tabelle\n3: Tabelle & Diagramm\n4: Zahlwert\n5: Vorschrift\n6: Schließen\n'''))
            if m < 1: raise VError
            if m > 7 and m != 42: raise VError
            if switch[m] == table or switch[m] == diagram:
                switch[m](False,0)
            else:
                switch[m]()
        except VError:
            #popup('Die Eingabe muss zwischen 1 und 6 liegen','Value Error',1,1)
            print(f"{bcolors.FAIL}Die Eingabe muss zwischen 1 und 6 liegen{bcolors.ENDC}")
        except ValueError as err:
            #popup('Eingabe muss eine Natürliche Zahl sein','Type Error',1,1)
            print(f"{bcolors.FAIL}Eingabe muss eine natürliche Zahl \u2115 sein{bcolors.ENDC}\n" + str(err))
        
print(f'\n{bcolors.HEADER}Ein Rechner für Zahlenfolgen{bcolors.ENDC}')
print('Alle gemessenen Angaben oder Emfehlungen beziehen sich auf die Fibonacci-Folge\n')
menu()

