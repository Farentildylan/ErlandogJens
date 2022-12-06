import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "Skilsmisser og ekteskap.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    fil_linjer = []

    for i in filinnhold:
        fil_linjer.append(i)

    xverdier = np.arange(1902,2022)
    yverdierekteskap = fil_linjer[2]
    yverdierekteskap.pop(0)
    yverdierskilsmisse = fil_linjer[3]
    yverdierekteskap.pop(0)

class Gradtegener:
    def __init__(self, xverdier, yverdier):
        

plt.bar(xverdier + 0.2, yverdierekteskap, width=0.5)
plt.bar(xverdier - 0.2, yverdierskilsmisse, width=0.5)
plt.show()