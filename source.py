#import bibliotek
import matplotlib as plt
import numpy as np
import math
import tkinter as tk
import datetime as dt
#Funkcje do tkintera
#wybór aplikacji
global app
app = 0
def wykres_app():
    global app
    app = 1
    okno.destroy()

#pobieranie danych do wykresu
global count
count = 1
def wart_wykres():
     global count
     count = pol_tekst.get()
     pol_tekst2 = tk.Entry(okno_1, width=30)
     pol_tekst2.grid(row=2, column=0)
     return count

def plot_function(count, compartments, function_formula):
    if count > 0 and count < 5:
        for i in range(count):
            if i == 0:
                 colorc = "blue"
            if i == 1:
                 colorc = "black"
            if i == 2:
                 colorc = "red"
            if i == 3:
                 colorc = "green"
            if i == 4:
                 colorc = "yellow"
            compartments = int(input("Z ilu przedziałów składa się funkcja?: "))
            for j in range(compartments):
                if j > 5:
                    print("Zbyt duża liczba przedziałów!")
                # Pobieranie wzoru funkcji od użytkownika
                function_formula = input("Podaj wzór funkcji (pamiętaj o znakach składni Pythona!): ")
                x1 = []
                x2 = []
                y1 = []
                y2 = []
                a = int(input("Podaj początek dziedziny funkcji: "))
                b = int(input("Podaj koniec dziedziny funkcji (większe niż poprzednia!): "))
                c = a
                d = b
                if a >= b:
                    print("Nieprawidłowa dziedzina funkcji.")
                else:
                    if '/x' in function_formula or "/ x" in function_formula:
                            x = np.arange(a, 0, 0.01)
                            y = eval(function_formula)
                            plt.plot(x, y, color = colorc)
                            x = np.arange(0.01, b + 0.01, 0.01)
                            y = eval(function_formula)
                            plt.plot(x, y, color = colorc)
                    else:
                            x = np.arange(a, b + 0.01, 0.01)
                            y = eval(function_formula)
                            plt.plot(x, y, color = colorc)
            x = c
            plt.scatter(x, eval(function_formula), s = 50, facecolor = colorc)
            x = d
            plt.scatter(x, eval(function_formula), s = 50, facecolor = colorc)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)
            plt.axhline(y=0, color='black', linestyle='solid')
            plt.axvline(x=0, color='black', linestyle='solid')
        plt.show()
    else:
         print("Błąd!")

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Strona główna")
okno.geometry("400x300+100+100")

#tworzenie tekstu i przycisków głównego menu
date = tk.Label(okno, text=f"Jest {dt.datetime.now()}",)
date.grid(row = 0, column = 0)
quit_button=tk.Button(okno, text="Wyjście", command=okno.destroy)
quit_button.grid(row = 1, column = 0)
second_button = tk.Button(okno, text="Drugi przycisk", command=wykres_app)
second_button.grid(row = 1, column = 1)
okno.mainloop()
if app == 1:
    okno_1 = tk.Tk()
    okno_1.title("Rysowanie wykresu funkcji")
    okno_1.geometry("400x300+100+100")

    pol_tekst = tk.Entry(okno_1, width=30)
    pol_tekst.grid(row=1, column=0)
    input_button1=tk.Button(okno_1, text="Potwierdź", command=wart_wykres)
    input_button1.grid(row = 1, column = 1)
    print(count)
    plot_function(count, 0, 0)
    okno_1.mainloop()
    
    
    





