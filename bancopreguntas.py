import csv

with open('resurce/preguntas2.csv', encoding="utf8") as csvfile:
    preguntas = csv.DictReader(csvfile, delimiter=",")
    for row in preguntas:
            print(row)