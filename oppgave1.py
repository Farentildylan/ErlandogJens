import csv
import matplotlib.pyplot as plt

class CSV_sorted:
  def __init__(self, file):
    self.file = file
    self.aarstall = []
    self.befolkning = []
    with open(self.file, encoding="utf-8-sig") as fil:
      self.file_content = csv.reader(fil, delimiter=";")

      self.headers = next(self.file_content)

      for rad in self.file_content:
        self.aarstall.append(int(rad[0]))
        self.befolkning.append(int(rad[1]))

  def plot(self):
    plt.plot(self.aarstall, self.befolkning)
    plt.ticklabel_format(axis='y', style='plain')
    plt.xlabel(self.headers[0])
    plt.ylabel(self.headers[1])
    plt.title("Befolkning")

    