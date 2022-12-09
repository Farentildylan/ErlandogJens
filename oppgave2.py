import json
import matplotlib.pyplot as plt
import numpy as np

class Json_sorted:
    def __init__(self, file):
        #Henter fil og lager et objekt som har henter ut relevant data for plotting
        self.file = file
        with open(self.file, encoding="utf-8") as f:
            self.data = json.load(f)
        #Henter lables for de forksjellige verdiene
        self.years = list(self.data["dataset"]["dimension"]["Tid"]["category"]["label"].values())
        self.status = list(self.data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"].values())
        self.values = self.data["dataset"]["value"]
        #Lager en todimensjonal liste som splitt verdiene inn i tilhørende kategori
        self.values_split = [self.values[x:x+len(self.years)] for x in range(0, len(self.values), len(self.years))]
        self.plot_amount = 0

    def plot(self):
        #Setter antall plot til 0
        self.plot_amount = 0
        for i in range(0, len(self.status)):
            #Plotter hver datagrupppe som subplots i hovedfiguren
            self.plot_amount += 1
            plt.subplot(2, 3, i+1)
            plt.ticklabel_format(axis='y', style='plain')
            #Setter x ticks til hvert 5 år for mer oversiktlig plot
            plt.xticks(np.arange(0, 42, step=5), rotation = 300)
            plt.plot(self.years, self.values_split[i])
            plt.title(self.status[i])
            #Setter ylable og xlable ut ifra 
            plt.ylabel(self.data["dataset"]["dimension"]["ContentsCode"]["category"]["unit"]["Personer"]["base"] +" "+ self.data["dataset"]["dimension"]["ContentsCode"]["category"]["label"]["Personer"])
            plt.xlabel(self.data["dataset"]["dimension"]["Tid"]["label"])
        #setter mer plass mellom subplots 
        plt.tight_layout()

