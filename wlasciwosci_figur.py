import math

class Kwadrat:
    def __init__(self, a):
        self.a = a
    def pole(self):
        return self.a ** 2
    def przekatna(self):
        return self.a * math.sqrt(2)
    def obwod(self):
        return 4 * self.a
        
class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def pole(self):
        return self.a * self.b
    def przekatna(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)
    def obwod(self):
        return 2 * self.a + 2 * self.b
    
class Rownoleglobok_abh:
    def __init__(self, a, b, h): 
        self.a = a
        self.b = b
        self.h = h
    def pole(self):
        return self.a * self.h
    def obwod(self):
        return 2 * self.a + 2 * self.h

class Rownoleglobok_ef:
    def __init__(self, e, f):
        self.e = e
        self.f = f
    def pole(self):
        return self.e * self.f / 2
class Trojkat:
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def pole(self):
        return self.a * self.h / 2
class Kolo:
    def __init__(self, r):
        self.r = r
    def pole(self):
        return math.pi * self.r ** 2
    def obwod(self):
        return 2 * math.pi * self.r
try:           
    wybor = input("""Wybierz figurę:
1 - kwadrat
2 - prostokąt
3 - równoleglobok (znane boki i wysokość)
4 - równoległobok, w którym znamy tylko przekątne
5 - romb
6 - trójkąt
Wpisz tutaj: """)
    if wybor == "1":
        a = float(input("Podaj długość boku a: "))
        kw = Kwadrat(a)
        print("Dane: ")
        print(f"Pole: {kw.pole()}")
        print(f"Przekatna: {kw.przekatna()}")
        print(f"Obwód: {kw.obwod()}")
    elif wybor == "2":
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        pr = Prostokat(a, b)
        print("Dane: ")
        print(f"Pole: {pr.pole()}")
        print(f"Przekatna: {pr.przekatna()}")
        print(f"Obwód: {pr.obwod()}")
    elif wybor == "3":
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        h = float(input("Podaj długość wysokosci h: "))
        row = Rownoleglobok_abh(a, b, h)
        print("Dane: ")
        print(f"Pole: {row.pole()}")
        print(f"Obwód: {row.obwod()}")
    elif wybor == "4":
        e = float(input("Podaj długość przekątnej e: "))
        f = float(input("Podaj długość przekątnej f: "))
        rowe = Rownoleglobok_ef(e, f)
        print("Dane: ")
        print(f"Pole: {rowe.pole()}")
    elif wybor == "5":
        pass
    elif wybor == "6":
        a = float(input("Podaj długość boku a: "))
        h = float(input("Podaj długość wysokosci h: "))
        tr = Trojkat(a, h)
        print("Dane: ")
        print(f"Pole: {tr.pole()}")
    else:
        print("Błędny wybór, spróbuj jeszcze raz!")
except(ValueError):
    print("Błędny typ danych!")
    
    