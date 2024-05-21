import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#data
beta=0.3#Infection rate
gamma=0.05#Recovery rate
grid_size=(100,100)
time_steps=100

#Initialize the grid
population=np.zeros(grid_size,dtype=int)

#Initialize one infected individual randomly
outbreak=tuple(np.random.choice(range(100),2))
population[outbreak]=1

#Function to update the grid
def update_population(population):
    new_population=population.copy()
    infected_cells=np.argwhere(population==1)
    
    # nfection process and recovery
    for x,y in infected_cells:
        # Recovery
        if np.random.rand() < gamma:
            new_population[x,y] = 2
            
        # Infection
        for dx in range(-1,2):
            for dy in range(-1,2):
                if (dx, dy)!=(0,0):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<grid_size[0] and 0<=ny<grid_size[1]:
                        if new_population[nx,ny]==0 and np.random.rand()<beta:
                            new_population[nx,ny]=1
                            
    return new_population

#Function for animation
def animate(t):
    global population
    population=update_population(population)
    im.set_array(population)
    ax.set_title(f"Time step {t}")

fig,ax=plt.subplots(figsize=(6,4),dpi=150)
im=ax.imshow(population,cmap='viridis', vmin=0,vmax=2,interpolation='nearest')
plt.colorbar(im, ticks=[0,1,2],label='Status')

#Create animation
ani=FuncAnimation(fig,animate,frames=time_steps,interval=200,repeat=False)
plt.show()