import math
import matplotlib.pyplot as plt
import numpy

G = 9.81

def rzut_poziomy():
#dane
    vo = float(input("Podaj początkową szybkość ciała (w m/s): "))
    h = float(input("Podaj początkową wysokość ciała (w metrach): "))
    t = math.sqrt(2 * h / G)
    z = vo * math.sqrt(2 * h / G)
    dane = (f"""Dane:
Szybkość początkowa: {vo} m/s 
Wysokość początkowa: {h} m
Czas spadania: {t} s (ok. {round(t, 2)} s)
Zasięg rzutu: {z} m (ok. {round(z, 2)} m)""")
#wykres zasięgu od czasu
    plt.subplot(211)
    x = [0, 1/8 * t, 1/4 * t, 3/8 * t, 1/2 * t, 5/8 * t, 3/4 * t, 7/8 * t, t]
    y = [0, vo * 1/8 * t, vo * 1/4 * t, vo * 3/8 * t, vo * 1/2 * t, vo * 5/8 * t, vo * 3/4 * t, vo * 7/8 * t, z]
    plt.plot(x, y)
    plt.subplot(212)
#wykres wysokości od czasu
    x = [0, 1/8 * t, 1/4 * t, 3/8 * t, 1/2 * t, 5/8 * t, 3/4 * t, 7/8 * t, t]
    y = [h, G * (7/8 * t) ** 2 / 2, G * (3/4 * t) ** 2 / 2, G * (5/8 * t) ** 2 / 2, G * (1/2 * t) ** 2 / 2, G * (3/8 * t) ** 2 / 2, G * (1/4 * t) ** 2 / 2, G * (1/8 * t) ** 2 / 2, 0]
    plt.plot(x, y)
    plt.show()
    return dane

def rzut_ukosny():
    vo = float(input("Podaj początkową szybkość ciała (w m/s): "))
    a = float(input("Podaj miarę kąta pomiędzy podłożem a wektorem szybkości: "))
    h = vo ** 2 * math.pow(math.sin(a), 2) / 2 * G
    t = vo * math.sin(a) / G
    z = vo ** 2 *math.sin(2 * a) / G



print(rzut_poziomy())