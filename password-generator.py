# 7 of 10 application - Winter Holidays Challenge 2021

# Napisz program do generowania losowych haseł o zadanej przez użytkownika długości. 
# Hasło musi spełniać zadane warunki np. co najmniej jedna liczba, co najmniej po jednej dużej i małej literze. 
# Warto skorzystać z modułów string i secrets.

# Propozycja rozszerzenia: Po wygenerowaniu hasła skopiuj je do schowka systemowego

import random
import string
from pyperclip import copy

LETTERS = string.ascii_letters
NUMS = string.digits
SPECJAL = string.punctuation
POSSIBLE_SYMBOLS = LETTERS + NUMS + SPECJAL

while True:
    try:
        len_password = int(input("Enter password length: "))
        if len_password < 8:
            raise Exception("Your password is too short. Try again.")
        break
    except Exception as e:
        print(e)

password = ''.join(random.sample(POSSIBLE_SYMBOLS, len_password))

print(f"Your generated passoword is: {password}")
copy(password)

