def weryfikacja_pesel():
    pesel = list(input("Podaj pesel: "))
    if len(pesel) != 11 or int(pesel[0]) < 0 or int(pesel[1]) < 0 or int(pesel[2]) < 0 or int(pesel[3]) < 0 or int(pesel[4]) < 0 or int(pesel[5]) < 0 or int(pesel[6]) < 0 or int(pesel[7]) < 0 or int(pesel[8]) < 0 or int(pesel[9]) < 0 or int(pesel[10]) < 0:
        info = "Niepoprawny numer PESEL!"
    else:   
        miesiac_int = int(pesel[2] + pesel[3])
    # XX czy XXI wiek?
        if miesiac_int > 12:
            rok = "20" + pesel[0] + pesel[1]
            miesiac = str(int(pesel[2] + pesel[3]) - 20)
        else:
            rok = "19" + pesel[0] + pesel[1]
            miesiac = str(pesel[2] + pesel[3])
        dzien = pesel[4] + pesel[5]
        data_urodzenia = dzien + "." + miesiac + "." + rok
    #sprawdzenie liczby porządkowej
        l_porz = str(pesel[6] + pesel[7] + pesel[8])
    #sprawdzenie płci
        plec = pesel[9]
        if plec == "1" or plec == "3" or plec == "5" or plec == "7" or plec == "9":
            plec = "Mężczyzna"
        else:
            plec = "Kobieta"
    #wyliczanie cyfry kontrolnej
        waga = [1,3,7,9,1,3,7,9,1,3]
        suma = int(pesel[0]) * waga[0] + int(pesel[1]) * waga[1] + int(pesel[2]) * waga[2] + int(pesel[3]) * waga[3] + int(pesel[4]) * waga[4] + int(pesel[5]) * waga[5] + int(pesel[6]) * waga[6] + int(pesel[7]) * waga[7] + int(pesel[8])* waga[8] + int(pesel[9]) * waga[9]
        reszta = int(suma) % 10
        if reszta == 0:
            c_kontr = 0
        else:
            c_kontr = 10 - reszta
        
        if c_kontr != int(pesel[10]):
            info = "Niepoprawny numer PESEL!"
        else:
            info = f"""Twoje dane:
    Data urodzenia: {data_urodzenia}
    Liczba porządkowa: {l_porz}
    Płeć: {plec}
    Cyfra kontrolna: {c_kontr} (poprawna)"""
            
    return(info)


print(weryfikacja_pesel())