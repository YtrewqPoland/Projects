import matplotlib.pyplot as plt

def plot_function():
    # Pobieranie wzoru funkcji od użytkownika
    function_formula = input("Podaj wzór funkcji: ")
    xl = [] 
    y = []
    if '/' in function_formula:
        for x in range(-500, -1):
            xl.append(x)
            y.append(eval(function_formula))
        for x in range(1, 500):
            xl.append(x)
            y.append(eval(function_formula))
    else:
        for x in range(-500, 500):
            xl.append(x)
            y.append(eval(function_formula))
    
    # Rysowanie wykresu
    plt.plot(xl, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres funkcji: y = ' + function_formula)
    plt.grid(True)
    plt.show()

plot_function()
