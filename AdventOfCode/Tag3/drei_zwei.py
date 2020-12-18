import os

counter = 0
datei = open(os.path.join(os.path.dirname(__file__), 'lis.txt'), 'r')
liste = datei.readlines()
datei.close()
# print(liste)
x = 0
y = 0

while y < len(liste)-1:
    x += 3
    y += 1
    x = x % 31
    if liste[y][x] == '#':
        counter += 1
print(counter)

counter02 = 0
x = 0
y = 0
while y < len(liste)-1:
    x += 1
    y += 1
    x = x % 31
    if liste[y][x] == '#':
        counter02 += 1
print(counter02)


counter03 = 0
x = 0
y = 0
while y < len(liste)-1:
    x += 5
    y += 1
    x = x % 31
    if liste[y][x] == '#':
        counter03 += 1
print(counter03)


counter04 = 0
x = 0
y = 0
while y < len(liste)-1:
    x += 7
    y += 1
    x = x % 31
    if liste[y][x] == '#':
        counter04 += 1
print(counter04)


counter05 = 0
x = 0
y = 0
while y < len(liste)-1:
    x += 1
    y += 2
    x = x % 31
    if liste[y][x] == '#':
        counter05 += 1
print(counter05)

print(counter*counter02*counter03*counter04*counter05)
