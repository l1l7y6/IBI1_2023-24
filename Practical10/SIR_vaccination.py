import numpy as np  
import matplotlib.pyplot as plt  
  
N=10000  
beta=0.3  
gamma=0.05  
time_max=1000  # Maximum time steps  
  
# Initialize an empty list to store I_arr for each vaccination rate  
I_arr_list = []  
  
# Loop over different vaccination rates  
for r in range(0, 101, 10):  
    vaccination_rate = r / 100  # Convert percentage to a decimal  
    S = N * (1 - vaccination_rate)  # Adjust the initial number of susceptible individuals  
    I = 1  
    R = 0  
    I_arr = [I]  
  
    # SIR model simulation  
    for t in range(time_max):  
        dS=np.sum(np.random.choice(range(2),int(S*I/N+0.5),p=[1-beta,beta]))# Change in susceptible (not used directly here)  
        dR=np.sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))# Change in recovered
        dI=dS-dR # Change in infected  
  
        # Update S, I, R (approximating the derivatives with dt=1)  
        S-=dS
        I+=dI
        R+=dR 

        # Ensure no negative values and round to integers (optional)  
        S=max(0, int(S))
        S=min(S,10000)  
        I=max(0, int(I))
        I=min(I,10000)
        R=max(0, int(R))
        R=min(R,10000)
  
        # Append I to the current I_arr  
        I_arr.append(I)  
  
    # Add the I_arr for the current vaccination rate to the list  
    I_arr_list.append(I_arr)  
  
# Plot the SIR model with different vaccination rates  
plt.figure(figsize=(10, 6), dpi=100)  
for i, I_arr in enumerate(I_arr_list):  
    vaccination_rate = i * 10  # Get the vaccination rate from the loop index  
    plt.plot(range(time_max + 1), I_arr, label=f'{vaccination_rate}% Vaccination Rate')  
  
plt.xlabel('Time Steps')  
plt.ylabel('Number of Infected People')  
plt.title('SIR Model with Different Vaccination Rates')  
plt.legend()  
plt.grid(True)  # Add grid lines for better readability  
  
plt.show()  
plt.savefig("SIR_Model_Different_Vaccination_Rates.png")