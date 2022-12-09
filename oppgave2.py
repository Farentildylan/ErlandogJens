import json
import matplotlib.pyplot as plt
import numpy as np

class Json_sorted:
    def __init__(self, file):
        self.file = file
        with open(self.file, encoding="utf-8") as f:
            self.data = json.load(f)
        self.years = list(self.data["dataset"]["dimension"]["Tid"]["category"]["label"].values())
        self.status = list(self.data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"].values())
        self.values = self.data["dataset"]["value"]
        self.values_split = [self.values[x:x+len(self.years)] for x in range(0, len(self.values), len(self.years))]
        self.plot_amount = 0

    def plot(self):
        self.plot_amount = 0
        for i in range(0, len(self.status)):
            self.plot_amount += 1
            plt.subplot(2, 3, i+1)
            plt.ticklabel_format(axis='y', style='plain')
            plt.xticks(np.arange(0, 42, step=5), rotation = 300)
            plt.plot(self.years, self.values_split[i])
            plt.title(self.status[i])
            plt.ylabel(self.data["dataset"]["dimension"]["ContentsCode"]["category"]["unit"]["Personer"]["base"] +" "+ self.data["dataset"]["dimension"]["ContentsCode"]["category"]["label"]["Personer"])
            plt.xlabel(self.data["dataset"]["dimension"]["Tid"]["label"])
        plt.tight_layout()

