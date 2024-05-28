import math

try:
    wybor = input("""Wybierz figurę:
1 - kwadrat
2 - prostokąt
3 - równoleglobok (znane boki i wysokość)
4 - romb
5 - trójkąt
6 - trójkąt równoboczny
7 - trapez
8 - koło
Wpisz tutaj: """)
    if wybor == "1":
        a = float(input("Podaj długość boku a: "))
        if a <= 0 :
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego kwadratu to: {a ** 2}")
    elif wybor == "2":
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        if a <= 0 or b <= 0:
            print("Błędne dane wejsciowe")
        else:
            print(f"Pole tego prostokąta to: {a * b}")
    elif wybor == "3":
        a = float(input("Podaj długość boku a: "))
        h = float(input("Podaj długość wysokosci h: "))
        if a <= 0 or h <= 0:
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego równoległoboku to: {a * h}")
    elif wybor == "4":
        e = float(input("Podaj długość przekątnej e: "))
        f = float(input("Podaj długość przekątnej f: "))
        if e <= 0 or f <= 0:
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego rombu to: {e * f / 2}")
    elif wybor == "5":
        a = float(input("Podaj długość boku a: "))
        h = float(input("Podaj długość wysokosci h opuszczonej na bok a: "))
        if a <= 0 or h <= 0:
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego trójkąta to: {a * h / 2}")
    elif wybor == "6":
        a = float(input("Podaj długość boku a: "))
        if a <= 0:
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego trójkąta to: {a ** 2 * math.sqrt(3) / 4} (około {round(a ** 2 * math.sqrt(3) / 4, 2)})")
    elif wybor == "7":
        a = float(input("Podaj długość krótszej podstawy: "))
        b = float(input("Podaj długość dłuszej podstawy: "))
        h = float(input("Podaj długość wysokosci h: "))
        if a <= 0 or b <= 0 or h <= 0:
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego trapezu to {(a + b) * h / 2}")
    elif wybor == "8":
        r = float(input("Podaj długość promienia: "))
        if r <= 0:
            print("Błędne dane wejściowe")
        else:
            print(f"Pole tego koła to: {math.pi * r ** 2} (około {round(math.pi * r ** 2, 2)})")
    else:
        print("Błędny wybór, spróbuj jeszcze raz!")
except(ValueError):
    print("Błędny typ danych!")
    
    