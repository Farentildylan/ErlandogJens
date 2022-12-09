import json
import matplotlib.pyplot as plt
import numpy as np

class Sorted_data:
    def __init__(self, file):
        self.file = file
        with open(self.file, encoding="utf-8") as f:
            self.data = json.load(f)
        self.years = list(self.data["dataset"]["dimension"]["Tid"]["category"]["label"].values())
        self.status = list(self.data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"].values())
        self.values = self.data["dataset"]["value"]
        self.values_split = [self.values[x:x+len(self.years)] for x in range(0, len(self.values), len(self.years))]

    def plot(self):
        for i in range(0, len(data_sorted.status)):
            plt.tight_layout()
            plt.subplot(2, 3, i+1)
            plt.ticklabel_format(axis='y', style='plain')
            plt.xticks(np.arange(0, 42, step=5), rotation = 300)
            plt.plot(self.years, self.values_split[i])
            plt.title(self.status[i])


data_sorted = Sorted_data("sivilstand.json")
data_sorted.plot()

plt.subplot(2, 3, 6)
plt.plot([1,2,3,4,5],[1,4,5,6,7])


plt.show()


