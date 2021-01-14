# 6 of 10 application - Winter Holidays Challenge 2021

# Napisz program, który w wybranej lokalizacji odczyta wszystkie pliki graficzne 
# (w określonych formatach, np. jpg, png, bmp itp.), następnie zmniejszy ich rozdzielczość o 50% 
# i zapisze je w podkatalogu “smaller” z odpowiednimi nazwami. 
# Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami. 

# Propozycja rozszerzenia: Oblicz ile miejsca na dysku można oszczędzić po kompresji 
# (odczytaj rozmiar plików w pierwotnym folderze oraz "smaller" i porównaj obie wartości - bezwzględnie i w %)

from PIL import Image
import glob
import os

folder = "winter-holidays-challenge/images"
os.chdir(folder)

new_folder = "smaller"

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
