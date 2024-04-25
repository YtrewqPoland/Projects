def weryfikacja_pesel():
    pesel = list(input("Podaj pesel: "))
    rok_int = int(pesel[0] + pesel[1])
    if rok_int < 24:
        rok = "19" + pesel[0] + pesel[1] + " lub 20" + pesel[0] + pesel[1]
        miesiac = str(int(pesel[2] + pesel[3]) - 20)
    else:
        rok = "19" + pesel[0] + pesel[1]
        miesiac = str(pesel[2] + pesel[3])
    dzien = pesel[4] + pesel[5]
    data_urodzenia = dzien + "." + miesiac + "." + rok
    
    l_porz = str(pesel[6] + pesel[7] + pesel[8])
    
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
Cyfra kontrolna: {c_kontr}"""
    return(info)


print(weryfikacja_pesel())