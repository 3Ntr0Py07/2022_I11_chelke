'Rechner für Zahlenfolgen'

#Aktualisirung:
#c:\users\entropy\appdata\local\programs\python\python310\python.exe
#C:\Users\chelke\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe

from tkinter import *
import matplotlib.pyplot as plt
#Einblendung des Graphen
from time import *
#Pausen/Wartezeiten
import sys
import os
#Kommunikation mit der Konsole
from numpy import *
#Bibliothek für viele mathematische Funktionen
from tabulate import tabulate
#Formatierung Tabellen für Text-Ausgabe
import colorama
#Farbige Schrift in Windows Konsole
import keyboard
#Tastatureingabe direkt
import subprocess as sub
#Für Neustarts
import random
#Zufallszahlen
import platform
#Information zum Betriebssystem

colorama.init()

Formel = 'a(n-1) + a(n-2)'
Forig = 'a(n-1) + a(n-2)'
Abbr = [2,1]
Aorig = [2,1]
#Definition der Formel


class Error(Exception):
    pass


class VError(Error):
    pass
#Eigene Fehlerklassen


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
    BROWN = '\033[31m'
    pass
#Klasse Farbcodes basierend auf Ansi-Escape-Sequenzen 


def clear():
    x = platform.system()
    if x == 'Linux' or x == 'Darwin':
        os.system('clear')
    elif x == 'Windows':
        os.system('cls')
    else:
        print(f'{bcolors.FAIL}Your Operation System is not Supported for this Function yet{bcolors.ENDC}')
#Refresh der Konsole, So dass immer nur ein Menü sichtbar ist


def restart():
    clear()
    print(f'{bcolors.OKBLUE}Rebooting{bcolors.ENDC}')
    sub.Popen(['python3'] + sys.argv)
    sys.exit()
#Neustartfunktion, nur für Wartung vorgesehen


def keytool():
    clear()
    x = random.randint(0,1)
    if x == 1:
        print(f'{bcolors.BROWN}Die Tür ist offen.{bcolors.ENDC}')
    else:
        print(f'{bcolors.BROWN}Die Tür ist geschlossen{bcolors.ENDC}')
#Ein kleines Easteregg


def diagram(boo,n):
    if boo == False:
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
    print(f'{bcolors.OKCYAN}Done{bcolors.ENDC}')
    plt.show()
#Ausgabe eines Graphen mit optionaler Tabelle (Aufruf der Tabelle nur über dnt()), Pop-Up


def vorschrift():
    clear()
    global Formel,Forig,Abbr,Aorig
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
                        Abbr = Aorig
                except Exception as _err:
                    print(f'{bcolors.FAIL}Ihre Formel scheint mathematisch nicht korrekt zu sein. Überprüfen sie die Syntax und versuchen sie erneut.{bcolors.ENDC}')
                    print("Error Message:")
                    print(str(_err))
                
        elif yn.lower() == 'reset':
            Formel = Forig
            Abbr = Aorig
            print(f'{bcolors.OKGREEN}Vorschrift zurückgesetzt{bcolors.ENDC}')
            return
        else:
            print(f"{bcolors.FAIL}Die Eingabe entspricht nicht y,n,ja oder nein{bcolors.ENDC}")
#Ausgabe der Funktionsforschrift, sowie Optionale Bearbeitung und Zürücksetzung auf Standard


def ptz(a,b):
    x = float_power(a,b)
    if abs(x-floor(x))<1e-6:
        trunc(x)
    return x
#Verkürzung der Potenzfunktion -> Einfachere eingabe in vorschrift()


def a(n):
    if n < int(Abbr[0]):
        return int(Abbr[1])
    else:
        n = eval(Formel)
        return n
#Rekursive Funktion für Berechnung der Zahlenreihe 


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
    print(f'{bcolors.OKCYAN}Done{bcolors.ENDC}')
    print('\n' +df)
#Ausgabe einer Tabelle als Text


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
        print('Der erste Wert der Zahlenreihe ist '+ str(a(n)))
    else:
        print(f'Der ' + str(n) + '-te Wert der Zahlenreihe ist '+ str(a(n)))
#Ausgabe einer einzelnen Zahl innerhalb der Reihe


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
#Funktion zur Weiterleitung an diagram() mit Tabelle


def menu():
    switch = {
        1: diagram,
        2: table,
        3: dnt,
        4: zahl,
        5: vorschrift,
        6: sys.exit,
        7: restart,
        42: keytool
    }
    _isFirst = True
    while True:
        if (not _isFirst):
            clear()
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
        os.system("pause")
        _isFirst = False
#Ein Menü um alle Funktionen aufzurufen 


if (__name__ == "__main__"):
    clear()
    print(f'{bcolors.HEADER}Ein Rechner für Zahlenfolgen{bcolors.ENDC}')
    print('Alle gemessenen Angaben oder Emfehlungen beziehen sich auf die Fibonacci-Folge\n')
    menu()
#Ausführung des Programms
