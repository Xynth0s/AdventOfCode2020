import os


datei = open(os.path.join(os.path.dirname(__file__), 'lis.txt'), 'r')
#liste = []
# for zeile in datei:
#    liste.append(int(zeile))

liste = datei.readlines()
datei.close()

i = 0
j = i + 1
b = False
for i in range(len(liste)):
    if b:
        break
    for j in range(len(liste)):
        ergebnis = int(liste[i]) + int(liste[j])
        if ergebnis == 2020:
            b = True
            # print(int(liste[i]))
            # print(int(liste[j]))
            print(ergebnis)
            print(int(liste[i]) * int(liste[j]))
            break
