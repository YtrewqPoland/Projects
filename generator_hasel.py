import random

znaki = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '@', '#', '$', '%', '^', '&', '*','+', '-', '=', '|', ';', ':', '"', "'", '<', '>', '/', '?']
try:
    ilosc = int(input("Ile znaków ma mieć hasło?: "))
    if ilosc < 1:
        print("Nieprawidłowa ilość znaków!")
    else:
        if ilosc > 81:
            print("Stworzenie takiego hasła jest niemożliwe, gdyż będzie miało powtarzające się znaki 2 razy.")
        else:
            if ilosc < 8:
                print("Pamiętaj, że silne hasło powinno zawierać przynajmniej 8 znaków!")
            haslo = []
            i = 0
            while i < ilosc:
                a = random.randrange(0, 81)
                if znaki[a] not in haslo:
                    haslo.append(znaki[a])
                    i+=1
            haslo = "".join(haslo)
            print(f"Twoje nowo wygenerowane hasło to: {haslo}")
except ValueError:
    print("Błędne dane wejściowe!")
    
