import matplotlib.pyplot as plt
years = [2010,2012,2013,2014,2015,2016,2017,2018,2019]
numbers = [5,7,13,10,20,22,17,16.5,27]

plt.bar(years,numbers)
plt.xlabel("Years")
plt.ylabel("Number of passengers (x1000)")
plt.xticks(years)
plt.yticks(numbers)
plt.show()