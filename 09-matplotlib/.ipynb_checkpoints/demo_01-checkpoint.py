import matplotlib.pyplot as plt
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
kohli_runs = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

plt.plot(years,runs,color="orange",linestyle="--",label = "Sachin")
plt.plot(years,kohli_runs,color="blue",linestyle="-.",label="Kohli")
plt.plot(years,sehwag,color="red",label="Sehwag")
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Comparision")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()