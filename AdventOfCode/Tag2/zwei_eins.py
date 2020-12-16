import os


datei = open(os.path.join(os.path.dirname(__file__), 'lis.txt'), 'r')

counter_1 = 0
counter_2 = 0
for zeile in datei:
    # print(zeile)
    pw = zeile.split(': ')
    passwort = pw[1].strip()

    buch = pw[0].split(' ')
    buchstabe = buch[1]
    minmax = buch[0].split('-')
    min = int(minmax[0])
    max = int(minmax[1])
    if min <= passwort.count(buchstabe) <= max:
        counter_1 += 1
    #print(passwort, buchstabe, min, max)
    if (passwort[min - 1] == buchstabe) != (passwort[max - 1] == buchstabe):
        counter_2 += 1

datei.close()

print(counter_1)
print(counter_2)
