import os


datei = open(os.path.join(os.path.dirname(__file__), 'lis.txt'), 'r')
liste = []
for zeile in datei:
    liste.append(int(zeile))
datei.close()
i = 0
j = i + 1
k = j + 1
b = False
for i in range(len(liste)):
    if b:
        break
    for j in range(len(liste)):
        if b:
            break
        for k in range(len(liste)):

            ergebnis = int(liste[i]) + int(liste[j]) + int(liste[k])
            if ergebnis == 2020:
                b = True
                # print(int(liste[i]))
                # print(int(liste[j]))
                # print(int(liste[k]))
                print(ergebnis)
                print(int(liste[i]) * int(liste[j]) * int(liste[k]))
                break
