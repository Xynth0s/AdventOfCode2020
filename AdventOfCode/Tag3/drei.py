import os


x = -3

counter = 0
datei = open(os.path.join(os.path.dirname(__file__), 'lis.txt'), 'r')


for zeile in datei:

    zeile = zeile.strip()
    print(zeile)
    x += 3
    if x > 30:
        x = x - 31

    if zeile[x] == '#':
        counter += 1

print(counter)
