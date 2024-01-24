import csv
import pandas

dati = open("Azbesta_mekletaji.csv",encoding="utf-8")
csv_dati = csv.reader(dati)
rindas = list(csv_dati)

print(rindas[58])