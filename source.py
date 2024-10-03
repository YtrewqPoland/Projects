#import bibliotek
import matplotlib.pyplot as plt
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
def wart_wykres_formula():
     global function_formula
     function_formula = pol_tekst.get()
     global a
     a = pol_tekst1.get()
     global b
     b = pol_tekst2.get()
     a = int(a)
     b = int(b)
     plot_function(function_formula, a, b)
     return function_formula

def plot_function(function_formula, a, b):
            if '/x' in function_formula or "/ x" in function_formula:
                    x = np.arange(a, 0, 0.01)
                    y = eval(function_formula)
                    plt.plot(x, y, color = "red")
                    x = np.arange(0.01, b + 0.01, 0.01)
                    y = eval(function_formula)
                    plt.plot(x, y, color = "red")
            else:
                    x = np.arange(a, b + 0.01, 0.01)
                    y = eval(function_formula)
                    plt.plot(x, y, color = "red")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)
            plt.axhline(y=0, color='black', linestyle='solid')
            plt.axvline(x=0, color='black', linestyle='solid')
            plt.show()


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
    okno_1.geometry("800x300+100+100")
    pol_tekst = tk.Entry(okno_1, width=30)
    pol_tekst.grid(row=1, column=1)
    info = tk.Label(okno_1, text="Podaj wzór funkcji (pamiętaj o znakach składni Pythona!): ")
    info.grid(row=1, column=0)
    pol_tekst1 = tk.Entry(okno_1, width=30)
    pol_tekst1.grid(row=2, column=1)
    info1 = tk.Label(okno_1, text="Podaj początek dziedziny funkcji: ")
    info1.grid(row=2, column=0)
    pol_tekst2 = tk.Entry(okno_1, width=30)
    pol_tekst2.grid(row=3, column=1)
    info2 = tk.Label(okno_1, text="Podaj koniec dziedziny funkcji: ")
    info2.grid(row=3, column=0)
    input_button1=tk.Button(okno_1, text="Potwierdź", command=wart_wykres_formula)
    input_button1.grid(row = 4, column = 0, columnspan=2)
    okno_1.mainloop()
    
    
    
    





