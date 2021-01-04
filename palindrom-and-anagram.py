# to jest 1 z 10 zadań w ramach FerieChallange2021 

# Napisz program, który prosi użytkownika o podanie dowolnego napisu. 
# Następnie program wyświetla na ekranie to słowo wspak (od prawej do lewej) 
# i wyświetla komunikat czy to wyrażenie jest palindromem 
# (czyli czytane wspak daje do samo wyrażenie np. “ala”, “Kobyła ma mały bok” 
# (inne przykłady: http://www.palindromy.pl/pal_kr.php). 
# Podczas sprawdzania ignoruj wielkość liter oraz znaki niebędące literami. 
# Następnie wywołaj dowolną stronę internetową, która pokaże anagramy oraz słowa utworzone po usunięciu liter, 
# np. https://poocoo.pl/scrabble-slowa-z-liter/hardcoder 

# Propozycja rozszerzenia: samodzielnie wyszukaj anagramy i słowa utworzone po usunięciu liter z podanego słowa, 
# na przykład wykorzystując słownik wspomniany na stronie https://anagramy.wybornie.com/ 

import re
import time
import webbrowser

word = input("Podaj słowo lub zdanie: ").lower().replace(" ", "")
word = re.sub("[^a-z żółćąężśń]", "", word)
inverted_word = "".join(reversed(word)).lower().replace(" ", "")
print("Twoje wyrażenie wspak to: " + inverted_word)

if word == inverted_word:
    print("Twoje wyrażenie to palindrom!")
    time.sleep(3)
    webbrowser.open("https://poocoo.pl/scrabble-slowa-z-liter/" + word)
else:
    print("Twoje wyrażenie nie jest palindromem.")