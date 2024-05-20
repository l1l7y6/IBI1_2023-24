#we can use while loop to calculate
#n=0.05
#if the outcome is smaller than 0.9
#n*=2
#if the outcome is bigger than 0.9, end the code
#also, use i to store the number of days I can have a holiday
n=0.05#density
i=0#days I can have a holiday
damn=0.9
while n<damn:
    i+=1
    n*=2#calculate the day
print("on day "+str(i+1)+" the cell density goes over 90%")
print("so I can have a "+str(i)+" days' holiday from the lab")
#the i starts at 0 is because if n is bigger than 0.9, the cells will die
#so one day in advance