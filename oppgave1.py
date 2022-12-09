import csv
import matplotlib.pyplot as plt

class CSV_sorted:
  #Vi lager to lister for x- og yverdier
  def __init__(self, file):
    self.file = file
    self.aarstall = []
    self.befolkning = []
    #Her leser vi filen og i self.headers linjen fjerner vi overskriftene.
    #Dat trenger vi kun å jobbe med rene tall
    with open(self.file, encoding="utf-8-sig") as fil:
      self.file_content = csv.reader(fil, delimiter=";")

      self.headers = next(self.file_content)
      #Denne linjen tar verdiene fra filen og legger dem inn i x- og yverdi listene våre
      #I programmet er de kalt aarstall og befolkning
      for rad in self.file_content:
        self.aarstall.append(int(rad[0]))
        self.befolkning.append(int(rad[1]))
  #Her printes grafen ut som et linjediagram
  def plot(self):
    plt.plot(self.aarstall, self.befolkning)
    plt.ticklabel_format(axis='y', style='plain')
    plt.xlabel(self.headers[0])
    plt.ylabel(self.headers[1])
    plt.title("Befolkning")

    