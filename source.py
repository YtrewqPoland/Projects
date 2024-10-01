#import bibliotek
import matplotlib as plt
import numpy as np
import math
import tkinter as tk
import datetime as dt
import time

global app
app = 0
def wykres_app():
    global app
    app = 1
    okno.destroy()

def pobierz_tekst():
    wartosc = pol_tekst.get()
    print("Wpisałeś:", wartosc)
    okno_1.destroy()

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Strona główna")
okno.geometry("400x300+100+100")

#tworzenie tekstu i przycisków
date = tk.Label(okno, text=f"Jest {dt.datetime.now()}",)
date.grid(row = 0, column = 0)
quit_button=tk.Button(okno, text="Wyjście", command=okno.destroy)
quit_button.grid(row = 1, column = 0)
second_button = tk.Button(okno, text="Drugi przycisk", command=wykres_app)
second_button.grid(row = 1, column = 1)

# Uruchamianie głównej pętli aplikacji
okno.mainloop()
print(app)
if app == 1:
    okno_1 = tk.Tk()
    okno_1.title("Rysowanie wykresu funkcji")
    okno_1.geometry("400x300+100+100")
    date = tk.Label(okno_1, text=f"Jest {dt.datetime.now()}",)
    pol_tekst = tk.Entry(okno_1, width=30)
    wart = pol_tekst.get()
    pol_tekst.grid(row=1, column=0)
    date.grid(row=0, column=0)
    quit_button1=tk.Button(okno_1, text="Wyjście", command=pobierz_tekst)
    quit_button1.grid(row = 1, column = 0)
    okno_1.mainloop()
    print(wart)





