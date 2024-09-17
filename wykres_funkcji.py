import matplotlib.pyplot as plt
import math
import numpy as np

def plot_function():
    # Pobieranie wzoru funkcji od użytkownika
    function_formula = input("Podaj wzór funkcji (pamiętaj o znakach składni Pythona!): ")
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    a = int(input("Podaj początek dziedziny funkcji: "))
    b = int(input("Podaj koniec dziedziny funkcji (większe niż poprzednia!): "))
    if a >= b:
        print("Nieprawidłowa dziedzina funkcji.")
    else:
        if '/x' in function_formula or "/ x" in function_formula:
                x = np.arange(a, 0, 0.01)
                y = eval(function_formula)
                plt.plot(x, y, color = "blue")
                x = np.arange(0.01, b + 0.01, 0.01)
                y = eval(function_formula)
                plt.plot(x, y, color = "blue")
        else:
                x = np.arange(a, b + 0.01, 0.01)
                y = eval(function_formula)
                plt.plot(x, y, color = "blue")

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Wykres funkcji: y = ' + function_formula)
        plt.grid(True)
        plt.axhline(y=0, color='black', linestyle='solid')
        plt.axvline(x=0, color='black', linestyle='solid')
        plt.show()

plot_function()
try:
    plot_function()
except ZeroDivisionError:
    print("Błąd, pamiętaj, że nie można dzielić przez 0!")
except SyntaxError:
    print("Nieprawidłowy wzór funkcji! Pamiętaj żeby używać składni Pythona (*, **, / itd.)")
except (ValueError, NameError):
    print("Nieprawidłowe dane wejściowe!")

