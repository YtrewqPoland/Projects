import random

znaki = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '@', '#', '$', '%', '^', '&', '*','+', '-', '=', '|', ';', ':', '"', "'", '<', '>', '/', '?']
try:
    ilosc = int(input("Ile znaków ma mieć hasło?: "))
    haslo = []
    i = 0
    while i < ilosc:
        haslo.append(znaki[random.randrange(0, 81)])
        i += 1
    haslo = "".join(haslo)
    print(f"Twoje nowo wygenerowane hasło to: {haslo}")
except ValueError:
    print("Błędny wybór!")
    
