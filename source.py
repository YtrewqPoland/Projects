#IMPORT
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
import datetime as dt
#------------------------------------------------------------------------------------------------------------------
#FUNKCJE
#aplikacja do rysowania wykresów funkcji
def wykres_app():
    okno.title("Rysowanie wykresu funkcji")
    okno.geometry("600x300+100+100")
    date.destroy()
    second_button.destroy()
    quit_button.destroy()
    third_button.destroy()
    global pol_tekst
    pol_tekst = tk.Entry(okno, width=30)
    pol_tekst.grid(row=1, column=1)
    global info
    info = tk.Label(okno, text="Podaj wzór funkcji (pamiętaj o znakach składni Pythona!): ")
    info.grid(row=1, column=0)
    global pol_tekst1
    pol_tekst1 = tk.Entry(okno, width=30)
    pol_tekst1.grid(row=2, column=1)
    global info1
    info1 = tk.Label(okno, text="Podaj początek dziedziny funkcji: ")
    info1.grid(row=2, column=0)
    global pol_tekst2
    pol_tekst2 = tk.Entry(okno, width=30)
    pol_tekst2.grid(row=3, column=1)
    global info2
    info2 = tk.Label(okno, text="Podaj koniec dziedziny funkcji: ")
    info2.grid(row=3, column=0)
    global input_button1
    input_button1=tk.Button(okno, text="Potwierdź", command=wart_wykres_formula)
    input_button1.grid(row = 4, column = 0)
    global quit_button1
    quit_button1 = tk.Button(okno, text="Wyjście", command=main_menu1)
    quit_button1.grid(row=4, column=1)

#pobieranie danych do wykresu
def wart_wykres_formula():
    global function_formula
    try:
        function_formula = pol_tekst.get()
        global a
        a = pol_tekst1.get()
        global b
        b = pol_tekst2.get()
        a = int(a)
        b = int(b)
        plot_function(function_formula, a, b)
    except ValueError as e:
        print(f"Blad!(Zle dane wejsciowe do wykresu funkcji ({e}) )")
    except ZeroDivisionError as e:
        print(f"Blad!(Zle dane wejsciowe do wykresu funkcji ({e}) )")
    except SyntaxError as e:
        print(f"Blad!(Zle wzor do wykresu funkcji ({e}) )")

#funkcja rysująca wykres
def plot_function(function_formula, a, b):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axhline(y=0, color='black', linestyle='solid')
    plt.axvline(x=0, color='black', linestyle='solid')
    x=a
    plt.scatter(x, eval(function_formula), s = 50, facecolor = "red")
    x=b
    plt.scatter(x, eval(function_formula), s = 50, facecolor = "red")
    if '/x' in function_formula or "/ x" in function_formula:
        x = np.arange(a, 0, 0.001)
        y = eval(function_formula)
        plt.plot(x, y, color = "red")
        x = np.arange(0.01, b + 0.01, 0.001)
        y = eval(function_formula)
        plt.plot(x, y, color = "red")
    else:
        x = np.arange(a, b + 0.01, 0.001)
        y = eval(function_formula)
        plt.plot(x, y, color = "red")
    plt.show()

#aplikacja do wyświetlania daty i godziny
def date_show_app():
    okno.title("Data i godzina")
    second_button.destroy()
    quit_button.destroy()
    third_button.destroy()
    date.grid(row=0, column=0)
    dtnow = dt.date.today()
    global info
    info = tk.Label(okno, text="Czas do:")
    info.grid(row=1, column=0)
    global info1
    datedate = dt.date(dtnow.year, 12, 24)
    info1 = tk.Label(okno, text=f"Świąt Bożego Narodzenia: {(datedate-dtnow).days} dni")
    info1.grid(row=2, column=0)
    global info2
    datedate = dt.date(2025, 6, 27)
    info2 = tk.Label(okno, text=f"Końca roku szkolnego: {(datedate-dtnow).days} dni")
    info2.grid(row=3, column=0)
    global quit_button1
    quit_button1 = tk.Button(okno, text="Wyjście", command=main_menu2)
    quit_button1.grid(row=4, column=0)
#główne menu
def main_menu():
    okno.title("Strona główna")
    okno.geometry("400x300+100+100")
    #tworzenie tekstu i przycisków głównego menu
    global date
    dtt = dt.datetime.now()
    if dtt.minute < 10:
        minute = f"0{dtt.minute}"
    else:
        minute = dtt.minute
    date_str = f"{dtt.hour}:{minute} || {dtt.day}.{dtt.month}.{dtt.year}"
    date = tk.Label(okno, text=date_str)
    date.grid(row=0, column=0, columnspan=3)
    global quit_button
    quit_button=tk.Button(okno, text="Wyjście", command=okno.destroy)
    quit_button.grid(row=1, column=2)
    global second_button
    second_button = tk.Button(okno, text="Rysowanie wykresów funkcji", command=wykres_app)
    second_button.grid(row=1, column=0)
    global third_button
    third_button = tk.Button(okno,text="Data i godzina", command=date_show_app)
    third_button.grid(row=1, column=1)

#menu po wykres_app
def main_menu1():
    pol_tekst.destroy()
    pol_tekst1.destroy()
    pol_tekst2.destroy()
    info.destroy()
    info1.destroy()
    info2.destroy()
    input_button1.destroy()
    quit_button1.destroy()
    main_menu()

#menu po date_show_app
def main_menu2():
    quit_button1.destroy()
    info.destroy()
    info1.destroy()
    info2.destroy()
    main_menu()
#-----------------------------------------------------------------------------------------------------------
global okno
okno = tk.Tk()
main_menu()
okno.mainloop()


    
    
    
    





