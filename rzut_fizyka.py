import math
import matplotlib.pyplot as plt
#stała grawitacji
G = 9.81

def rzut_poziomy():
#dane
    vo = float(input("Podaj początkową szybkość ciała (w m/s): "))
    if vo <= 0:
        return "Błędne dane wejściowe!"
    h = float(input("Podaj początkową wysokoś, z której zostało wyrzucone ciało (w metrach): "))
    if h <= 0:
        return "Błędne dane wejściowe!"
    t = math.sqrt(2 * h / G)
    z = vo * math.sqrt(2 * h / G)
    wykres = input("""Wybierz rodzaj wykresu, który chcesz otrzymać:
1. Zasięg - Czas
2. Wysokość - Czas
3. Zasięg - Wysokość
4. Wypisz dane dotyczące rzutu
Wpisz tutaj: """)
#wykres zasięgu od czasu
    if wykres == "1":
        x = [0, 1/8 * t, 1/4 * t, 3/8 * t, 1/2 * t, 5/8 * t, 3/4 * t, 7/8 * t, t]
        y = [0, vo * 1/8 * t, vo * 1/4 * t, vo * 3/8 * t, vo * 1/2 * t, vo * 5/8 * t, vo * 3/4 * t, vo * 7/8 * t, z]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("Czas (s)")
        ax.set_ylabel("Zasięg (m)")
        ax.set_title(f"""Wykres zależności zasięgu rzutu od czasu. 
Dane: V pocz.: {vo} m/s, h pocz.: {h} m, czas spadania: ok. {round(t, 2)} s, zasięg rzutu: ok. {round(z, 2)} m)""")
        plt.show()
#wykres wysokości od czasu
    elif wykres == "2":
        x = [0, 1/8 * t, 1/4 * t, 3/8 * t, 1/2 * t, 5/8 * t, 3/4 * t, 7/8 * t, t]
        y = [h, h - G * (1/8 * t) ** 2 / 2, h - G * (1/4 * t) ** 2 / 2, h - G * (3/8 * t) ** 2 / 2, h - G * (1/2 * t) ** 2 / 2, h - G * (5/8 * t) ** 2 / 2, h - G * (3/4 * t) ** 2 / 2, h - G * (7/8 * t) ** 2 / 2, 0]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("Czas (s)")
        ax.set_ylabel("Wysokość (m)")
        ax.set_title(f"""Wykres zależności wysokości od czasu
Dane: V pocz.: {vo} m/s, h pocz.: {h} m, czas spadania: ok. {round(t, 2)} s, zasięg rzutu: ok. {round(z, 2)} m""")
        plt.show()
#wykres zasięgu rzutu od wysokości
    elif wykres == "3":
        x = [0, 1/8 * z, 1/4 * z, 3/8 * z, 1/2 * z, 5/8 * z, 3/4 * z, 7/8 * z, z]
        t1 = 1/8 * z / vo; t2 = 1/4 * z / vo; t3 = 3/8 * z / vo; t4 = 1/2 * z / vo; t5 = 5/8 * z / vo; t6 = 3/4 * z / vo; t7 = 7/8 * z / vo
        y = [h, h - G * t1 ** 2 / 2, h - G * t2 ** 2 / 2, h - G * t3 ** 2 / 2 , h - G * t4 ** 2 / 2, h - G * t5 ** 2 / 2, h - G * t6 ** 2 / 2, h - G * t7 ** 2 / 2, 0]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("Zasięg (m)")
        ax.set_ylabel("Wysokość (m)")
        ax.set_title(f"""Wykres zależności zasięgu rzutu od wysokości
Dane: V pocz.: {vo} m/s, h pocz.: {h} m, czas spadania: ok. {round(t, 2)} s, zasięg rzutu: ok. {round(z, 2)} m""")
        plt.show()
#wypisanie danych
    elif wykres == "4":
        print(f"""Dane:
Szybkość początkowa: {vo} m/s 
Wysokość początkowa: {h} m
Czas spadania: {t} s (ok. {round(t, 2)} s)
Zasięg rzutu: {z} m (ok. {round(z, 2)} m)""")
    else:
        return("Błędny wybór!")
    return "Zakończono działanie programu"

try:
    print(rzut_poziomy())
except ValueError:
    print("Błędne dane wejściowe!")