import math

program_on = True

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
    while program_on:
        wybor = input("""Wybierz figurę:
1 - kwadrat
2 - prostokąt
3 - równoleglobok (znane boki i/lub wysokość)
4 - trójkąt
Wpisz tutaj: """)
        if wybor == "1":
            a = float(input("Podaj długość boku a: "))
            kw = Kwadrat(a)
            print(f"Pole: {kw.pole()}")
            print(f"Przekatna: {kw.przekatna()}")
            print(f"Obwód: {kw.obwod()}")
            break
        if wybor == "2":
            a = float(input("Podaj długość boku a: "))
            b = float(input("Podaj długość boku b: "))
            pr = Prostokat(a, b)
            print(f"Pole: {pr.pole()}")
            print(f"Przekatna: {pr.przekatna()}")
            print(f"Obwód: {pr.obwod()}")
            break
        if wybor == "3":
            a = float(input("Podaj długość boku a: "))
            b = float(input("Podaj długość boku b: "))
            h = float(input("Podaj długość wysokosci h: "))
            row = Rownoleglobok_abh(a, b, h)
            print(f"Pole: {row.pole()}")
            print(f"Obwód: {row.obwod()}")
        if wybor == "4":
            pass
        else:
            print("Błędny wybór, spróbuj jeszcze raz!")
except(ValueError):
    print("Błędny typ danych!")
    
    