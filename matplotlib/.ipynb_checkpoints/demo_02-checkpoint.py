import matplotlib.pylab as plt
years =[2005,2006,2007,2008,2009,2010,2011,2012,2014,2014]
kohli =[423,342,564,457,543,987,235,652,435,234]
rohit =[456,234,875,345,786,345,766,344,654,655]
dhawan = [765,346,977,666,777,345,764,235,666,879]
plt.plot(years,kohli,label="Kohli",linestyle="--",color="red")
plt.plot(years,rohit,label="Rohit",linewidth=3,color="green")
plt.plot(years,dhawan,label="dhawan",linestyle="-.",color="blue")
plt.legend()
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Comparision of India Top 3")
plt.style.use("ggplot")
plt.show()