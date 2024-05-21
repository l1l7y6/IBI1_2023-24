#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#data
N=10000#total population  
S=9999#initial number of susceptible individuals  
I=1  #initial number of infected individuals  
R=0  #initial number of recovered individuals  
beta=0.3 #rate of infection  
gamma = 0.05 #Recovery rate

time_max=1000
dt=1

#Arrays to store the values of S, I, R
S_arr = [S]
I_arr = [I]
R_arr = [R]

for t in range(time_max):
    dS=-np.sum(np.random.choice(range(2),int(S*I/N+0.5),p=[1-beta,beta]))
    dR=np.sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))
    dI=-dS-dR

    S+=dS
    I+=dI
    R+=dR

 # Ensure no negative values and round to integers (optional)  
    S=max(0, int(S))
    S=min(S,10000)  
    I=max(0, int(I))
    I=min(I,10000)
    R=max(0, int(R))
    R=min(R,10000)

    #Append SIR to the arrays
    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)

# Time array  
time = np.arange(time_max + 1) * dt  
  
#Plot the SIR model using Matplotlib  
plt.figure(figsize=(8, 4), dpi=140)  
plt.plot(time, S_arr, label='Susceptible')  
plt.plot(time, I_arr, label='Infected')  
plt.plot(time, R_arr, label='Recovered')  
plt.xlabel('Time')  
plt.ylabel('Number of People')  
plt.title('SIR Model')  
plt.legend()  
plt.show()  
  
plt.savefig("<SIR.png>",type="png")  #Save the figure