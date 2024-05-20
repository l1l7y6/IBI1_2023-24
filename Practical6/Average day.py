import matplotlib.pyplot as plt # type: ignore
timedict={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'music':1}
#store the data to the dictionary
timedict['other']= 24 - sum(timedict.values())
#calculate the time of "other" and create a key to store the value
print(timedict) #output the dictionary
print(timedict['sleeping'])
#choose sleeping activity to print
plt.figure()#Create a new drawing
plt.pie(timedict.values(), labels= timedict.keys()) 
#Draw a pie chart where time.values() is a list of values for time and time.keys() is a list of corresponding labels
plt.show()#show the figure
plt.clf()#Clear the current drawing in preparation for the next drawing