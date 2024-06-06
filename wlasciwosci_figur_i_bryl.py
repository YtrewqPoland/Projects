import math

try:
    print("Witaj w kalkulatorze pól figur i objętości brył!")
    wyb = input("Wybierz co chcesz policzyć (1 - pole, 2 - objętość): ")
    if wyb == "1":
        wybor = input("""Wybierz figurę:
    1 - kwadrat
    2 - prostokąt
    3 - równoleglobok 
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
    elif wyb == "2":
        wybor = input("""Wybierz bryłę:
    1 - sześcian
    2 - prostopadłościan
    3 - ostrosłup
    4 - graniastosłup o podstawie trójkąta
    5 - walec
    6 - stożek
    7 - kula
    Wpisz tutaj: """)
        if wybor == "1":
            a = float(input("Podaj długość boku a: "))
            if a <= 0 :
                print("Błędne dane wejściowe")
            else:
                print(f"Objętość tego sześcianu to: {a ** 3}")
        elif wybor == "2":
            a = float(input("Podaj długość jednego boku: "))
            b = float(input("Podaj długość drugiego boku: "))
            h = float(input("Podaj długość wysokosci: "))
            if a <= 0 or b <= 0 or h <= 0:
                print("Błędne dane wejściowe")
            else:
                print(f"Objętość tego prostopadłościanu to {a * b * h}")
        elif wybor == "3":
            a = float(input("Podaj długość boku trójkąta: "))
            h1 = float(input("Podaj długość wysokości podstawy opuszczonej na powyższy bok: "))
            h2 = float(input("Podaj długość wysokosci bryły: "))
            if a <= 0 or h1 <= 0 or h2 <= 0:
                print("Błędne dane wejściowe")
            else:
                print(f"Objętość tego ostrosłupa to {1/3 * a * h1 / 2 * h2}")
        elif wybor == "4":
            a = float(input("Podaj długość boku trójkąta: "))
            h1 = float(input("Podaj długość wysokości podstawy opuszczonej na powyższy bok: "))
            h2 = float(input("Podaj długość wysokosci bryły: "))
            if a <= 0 or h1 <= 0 or h2 <= 0:
                print("Błędne dane wejściowe")
            else:
                print(f"Objętość tego graniastosłupa to {a * h1 / 2 * h2}")
        elif wybor == "5":
            r = float(input("Podaj długość promienia podstawy: "))
            h = float(input("Podaj długość wysokości tego walca: "))
            if r <= 0 or h <= 0:
                print("Błędne dane wejściowe")
            else:
                print(f"Objętość tego walca to: {math.pi * r ** 2 * h} (około {round(math.pi * r ** 2 * h, 2)})")
        elif wybor == "6":
            r = float(input("Podaj długość promienia: "))
            h = float(input("Podaj długość wysokości tego stożka: "))
            if r <= 0 or h <= 0:
                print("Błędne dane wejściowe")
            else:
                print(f"Objętość tego stożka to: {1/3 * math.pi * r ** 2 * h} (około {round(1/3 * math.pi * r ** 2 * h)})")
        elif wybor == "7":
            r = float(input("Podaj długość promienia kuli: "))
            if r <= 0:
                print("Błędne dane wejściowe!")
            else:
                print(f"Objętość tej kuli to: {4/3 * math.pi * r ** 3} (około {round(4/3 * math.pi * r ** 3, 2)})")
        else:
            print("Błędny wybór, spróbuj jeszcze raz!")
    else:
        print("Błędny wybór, spróbuj jeszcze raz!")
except(ValueError):
    print("Błędny typ danych!")
    
    