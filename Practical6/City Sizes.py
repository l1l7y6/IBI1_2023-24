import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
uk_cities=[0.56,0.62,0.04,9.7]#store the population sizes for the uk in a list
ch_cities=[0.58,8.4,29.9,22.2]#store the population sizes for the China in a list
print(uk_cities)
print(ch_cities)
#print two lists of sorted value for the populations of the lists
uk_labels = ['Edinburgh','Glasgow','Stirling','London'] 
#input the names of UK cities
ch_labels = ['Haining', 'Hangzhou', 'Shanghai' ,'Beijing'] 
#input the names of China cities
index = np.arange(4)
plt.figure()
plt.bar(index, uk_cities, 0.6, yerr = 0)
#Draw a bar chart where index is the x-axis position of the bar,
#uk_cities is the height of the bar,
#0.6 is the width of the bar
#yerr = 0 means that there is no y-axis error
plt.xticks(index, uk_labels) 
#Set the tick label on the x-axis so that it shows the name of the UK city
plt.title("city size of population")
#set the title of the chart
plt.show()
#Use the same steps to create a chart of Chinese citites
plt.figure()#Create a new graph again, ready to draw a second bar chart
plt.bar(index, ch_cities, 0.6, yerr = 0)
plt.xticks(index, ch_labels)
plt.title("city size of population")
plt.show()

plt.clf()

#I'd like to use one chart to show all the data