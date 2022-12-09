import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "Skilsmisser og ekteskap.csv"

yverdierekteskap = []
yverdierskilsmisse = []
xverdier = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    for _filinnhold in filinnhold: 
        if _filinnhold[0] == "Inngåtte ekteskap":
            yverdierekteskap.append(_filinnhold[1], _filinnhold[len(_filinnhold)])
        elif _filinnhold[0] == "Skilsmisser":
            yverdierskilsmisse.append(_filinnhold[1], _filinnhold[len(_filinnhold)])
        else:
            xverdier.append(_filinnhold[1], _filinnhold[len(_filinnhold)])

"""
    for i in filinnhold:
        fil_linjer.append(i)

    xverdier = np.arange(1902,2022)
    yverdierekteskap = fil_linjer[2]
    yverdierekteskap.pop(0)
    yverdierskilsmisse = fil_linjer[3]
    yverdierekteskap.pop(0)

"""

plt.bar(xverdier + 0.2, yverdierekteskap, width=0.5)
plt.bar(xverdier - 0.2, yverdierskilsmisse, width=0.5)
plt.show()