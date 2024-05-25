import matplotlib.pyplot as plt
import math

def plot_function():
    # Pobieranie wzoru funkcji od użytkownika
    function_formula = input("Podaj wzór funkcji (pamiętaj o znakach składni Pythona!): ")
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    a = int(input("Podaj początek dziedziny funkcji: "))
    b = int(input("Podaj koniec dziedziny funkcji (większe niż poprzednia!): "))
    if '/x' in function_formula or "/ x" in function_formula:
        for x in range(a, -1):
            x1.append(x)
            y1.append(eval(function_formula))
        for x in range(1, b):
            x2.append(x)
            y2.append(eval(function_formula))
    else:
        for x in range(a, b):
            x1.append(x)
            y1.append(eval(function_formula))
    
    # Rysowanie wykresu
    plt.plot(x1, y1, color = "blue")
    plt.plot(x2, y2, color = "blue")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres funkcji: y = ' + function_formula)
    plt.grid(True)
    plt.show()
try:
    plot_function()
except ZeroDivisionError:
    print("Pamiętaj, że nie można dzielić przez 0!")
except SyntaxError:
    print("Nieprawidłowy wzór funkcji! Pamiętaj żeby używać składni Pythona (*, **, / itd.)")
except ValueError:
    print("Nieprawidłowe dane wejściowe!")

