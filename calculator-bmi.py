# 4 of 10 application - Winter Holidays Challenge 2021

# Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI 
# (https://en.wikipedia.org/wiki/Body_mass_index) oraz informuje użytkownika, w jakim jest zakresie. 
# Zakresy można wpisać “z palca” (ale może nieco mądrzej niż ciągiem if-elif-else dla każdego zakresu! 😉 ) 
# albo odczytać z dowolnego API, np. https://rapidapi.com/navii/api/bmi-calculator . 
# Następnie program losuje jedną z aktywności fizycznych oraz czas jej wykonania, np. bieganie przez 30 minut. 
# Czas nie może być dłuższy niż podany przez użytkownika (maksymalny czas, który można poświęcić na ćwiczenia). 
# Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI (na przykład osoba z niedowagą nie powinna ćwiczyć 
# mniej niż osoba o wadze normalnej - ustal pewien minimalny czas; ale już osoba z nadwagą powinna ćwiczyć dłużej 
# - ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum). 
# Utwórz w ten sposób plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.

# Propozycja rozszerzenia: przygotuj urozmaicony plan treningowy uwzględniający maksymalny czas wpisany przez 
# użytkownika - kilka aktywności fizycznych ma wypełniać całą dzienną ilość czasu, mają zajmować jakąs ustaloną 
# minimalną długość (np. 10 minut) oraz nie mogą się powtarzać jednego dnia.

import random
import calendar

print("Kalkulator BMI")
print()

height = input("Podaj swój wzrost w metrach: ")
weight = input("Podaj swoją wagę w kilogramach: ")
free_time = int(input("Podaj ile czasu w minutach możesz poświecić na ćwiczenia: "))

bmi = float(weight) / float(height) ** 2

sports = ["bieganie", "jazdę na rowerze", "pływanie", "podnoszenie ciężarów", "skakanie na skakance", 
        "jazdę na rolkach", "zumbę", "pilates", "granie w tenisa", "maszerowanie"]

multiplier = 1
activity = random.choice(sports)

print("Twoje BMI wynosi: {:.2f}".format(bmi))

if bmi < 18.5:
    print("Masz niedowagę! Zacznij więcej jeść.")
elif bmi > 18.5 and bmi < 24.9:
    print("Twoja waga jest w normie. Trzymaj tak dalej!")
elif bmi > 25 and bmi < 29.9:
    activity_time = random.randint(20, free_time +1)
    print("Masz nadwagę! Odżywiaj się zdrowiej!")
    print(f"Zacznij ćwiczyć {activity} przez {activity_time} minut codziennie.")
elif bmi > 30:
    activity_time = random.randint(30, free_time +1)
    print("Jesteś otyły! Musisz przejść na ścisłą dietę.")
    print(f"Zacznij ćwiczyć {activity} przez {activity_time} minut codziennie.")

# save training plan to file txt:

with open('training_plan.txt', 'w') as f:
    f.write('Training Plan: \n')
    
    for i in range(7):
        training = random.choice(sports)
        time = random.randint(activity_time, free_time +1)
        f.write(f"{calendar.day_name[i]}: {training} - {time} minut \n")