import matplotlib.pyplot as plt
import oppgave1
import oppgave2

plt.style.use("ggplot")
plt.grid()

#Kryss ut plot så spretter plot til neste oppgave opp. 

#Oppgave 1 plotter den første grafen
csv_data_sorted = oppgave1.CSV_sorted("Befolkning.csv")
csv_data_sorted.plot()
plt.show()

#Oppgave 2 plotter 5 grafer
json_data_sorted = oppgave2.Json_sorted("sivilstand.json")
json_data_sorted.plot()
plt.show()

#Oppgave 3 Putter plottet fra oppgave 1 inn i samme figur som oppgave 2
json_data_sorted.plot()
plt.subplot(2, 3, json_data_sorted.plot_amount+1)
csv_data_sorted.plot()
plt.show()


