#import a few python libraries that will help in this assignment
import os
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
os.chdir("../Practical7")
os.getcwd()#Get current working directory
os.listdir()#List all files and directories in the current working directory
#Change the working directory to the directory where the data file is located
dalys_data=pd.read_csv(".//dalys-rate-from-all-causes.csv")
#import the CSV file to the DataFrame
print(dalys_data.head(5))
#see the beginning 5 lines of the data frame
dalys_data.info()#Print basic information about the data
print(dalys_data.describe())#Overview of display statistics
print(dalys_data.iloc[0:3])#Show the first three lines
print(dalys_data.iloc[0:10:2,0:5])
#In this line I randomly modified and came up with the law

#above is about some scripts
#below is the code that complete the task
selected_rows=dalys_data.iloc[0:100:10, 3]
print(selected_rows)
# Displaying every 10th row's DALYs value up to the 100th row

Afghanistan_row=[] 
# Use Booleans to find all rows correspounding to Afghanistan
for i in dalys_data.loc[:,"Entity"]:  
    if i=="Afghanistan": 
        Afghanistan_row.append(True) 
    else:
        Afghanistan_row.append(False)  
print(dalys_data.loc[Afghanistan_row,"DALYs"])  

#compute the mean DALYs in China
china_data = dalys_data[dalys_data['Entity'] == 'China']
china_mean = china_data['DALYs'].mean()
print("Mean DALYs for China:",np.mean(china_mean))

# Commenting on the 2019 DALYs compared to the mean
china_2019_dalys = china_data[china_data['Year'] == 2019]['DALYs'].iloc[0]
if china_2019_dalys > china_mean:
    print("The DALYs in China in 2019 is bigger than the mean.")
elif china_2019_dalys < china_mean:
    print("The DALYs in China in 2019 is smaller than the mean.")
else:
    print("The DALYs in China in 2019 is equal to the mean.")

# Plotting DALYs over time for China
plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Over Time in China')
plt.xticks(rotation=-90)
plt.show()


#code that answers the question in File quesiton.txt

# Filter for data from the year 2019
dalys_2019 = dalys_data[dalys_data['Year']==2019]

# Create a boxplot of DALYs across all countries in 2019
dalys_2019.boxplot(column='DALYs', by='Entity')
plt.title('Boxplot of DALYs by Country in 2019')
plt.suptitle('')  # Suppresses the automatic "Boxplot grouped by Entity" subtitle
plt.show()
plt.clf()
#I found that there are too many countries in the list so if you want to see them you need to zoom in on the chart, looking at the output directly sucks!