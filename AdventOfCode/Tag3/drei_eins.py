import os

counter = 0
datei = open(os.path.join(os.path.dirname(__file__), 'lis.txt'), 'r')
liste = datei.readlines()
datei.close()
print(liste)
x = 0
y = 0

while y < len(liste)-1:
    x += 3
    y += 1
    x = x % 31
    if liste[y][x] == '#':
        counter += 1
print(counter)
