import matplotlib.pyplot as plt
import numpy as np
import math
def plot_function():
    count = int(input("Ile wzorów funkcji chcesz narysować?: "))
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
                        plt.plot(x, y, color = colorc)
                        x = np.arange(0.01, b + 0.01, 0.01)
                        y = eval(function_formula)
                        plt.plot(x, y, color = colorc)
                else:
                        x = np.arange(a, b + 0.01, 0.01)
                        y = eval(function_formula)
                        plt.plot(x, y, color = colorc)
                plt.title('Wykres funkcji: y = ' + function_formula)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.axhline(y=0, color='black', linestyle='solid')
        plt.axvline(x=0, color='black', linestyle='solid')
        plt.show()
    else:
         print("Błąd!")

try:
    plot_function()
except ZeroDivisionError:
    print("Błąd, pamiętaj, że nie można dzielić przez 0!")
except SyntaxError:
    print("Nieprawidłowy wzór funkcji! Pamiętaj żeby używać składni Pythona (*, **, / itd.)")
except (ValueError, NameError):
    print("Nieprawidłowe dane wejściowe!")