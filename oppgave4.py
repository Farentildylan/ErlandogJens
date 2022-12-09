import csv
import matplotlib.pyplot as plt

filnavn = "Skilsmisser og ekteskap.csv"

class SortertData:
    def __init__(self, filnavn):
        self.filnavn = filnavn
        self.yverdierekteskap = []
        self.yverdierskilsmisse = []
        self.xverdier = []
        self.nyxverdier = []

        with open(self.filnavn, encoding="utf-8-sig") as fil:
            filinnhold = csv.reader(fil, delimiter=";")
            for _filinnhold in filinnhold: 
                if _filinnhold[0] == "Inngåtte ekteskap":
                    _filinnhold.pop(0)
                    self.yverdierekteskap = _filinnhold
                elif _filinnhold[0] == "Skilsmisser":
                    _filinnhold.pop(0)
                    self.yverdierskilsmisse = _filinnhold
                elif _filinnhold[0] == "statistikkvariabel":
                    _filinnhold.pop(0)
                    self.xverdier = _filinnhold
    
    def konverter(self):
        self.xverdier = [int(x) for x in self.xverdier]
        self.nyxverdier = self.xverdier
        self.xverdier = [x - 2 for x in self.xverdier]
        self.nyxverdier = [x + 2 for x in self.nyxverdier]
        self.yverdierekteskap = [int(x) for x in self.yverdierekteskap]
        self.yverdierskilsmisse = [int(x) for x in self.yverdierskilsmisse]
    
    def skrivUt(self):
        plt.bar(self.xverdier, self.yverdierekteskap, width=4)
        plt.bar(self.nyxverdier, self.yverdierskilsmisse, width=4)
        plt.xlabel("Antall år")
        plt.ylabel("Skilsmisser og Inngåttekteskap")
        plt.legend(["Ingåtte ekteskap","Skilsmisser"])
        plt.show()
        
sortertData = SortertData(filnavn)
sortertData.konverter()
sortertData.skrivUt()