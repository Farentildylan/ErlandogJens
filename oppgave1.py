import csv
import matplotlib.pyplot as plt

filnavn = "Befolkning.csv"

#Lager lister for x- og y-verdier
aarstall = []
befolkning = []

#Åpner filen og skriver ut y- og x-verdiene i par
with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  
  for rad in filinnhold:
    aarstall.append(int(rad[0]))
    befolkning.append(int(rad[1]))

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.xlabel("Antall År")
plt.ylabel("Befolkning")
plt.grid()
plt.show()