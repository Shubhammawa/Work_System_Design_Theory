# Shubham Mawa
# 16IM10033
import numpy as np
from matplotlib import pyplot as plt
import math
import random



# Function for generation of the complete dataset
def data_generation(n,m,p0):                           
    d = []
    sig = math.sqrt(m*(1-m)/n)                                                                    # Array that will store the daily values
    for i in range(0,n):                                                                                 # n = No of days for which data is generated
        p = np.random.rand()                                                                        # probability that a number will be generated outside or inside the interval
        if(p<p0):                                                                                            # If probability less than threshold, generate a number inside the interval else outside the interval
            d.append(np.random.normal(m,sig)) # Inside interval
        else:
            p2 = np.random.rand()
            if(p2<0.5):
                d.append(random.uniform(m+3*sig,m+3.5*sig))   # Above the interval
            else:
                d.append(random.uniform(m-3.5*sig,m-3*sig))     # Below the interval
    D = np.array(d)
    result = [D,n,m]
    return(result)                 # Returning the array, array size and the mean value


# Function to update the mean and the interval when a point lying outside the interval is found
def update(D,t,n):
    sum = 0   
    for i in range(0,t+1):
        sum = sum + D[i]
    m_new = sum/(t+1)                        # New mean
    sig_new = math.sqrt(m_new*(1-m_new)/n)
    result = [m_new,sig_new]
    print(result)
    return result                            # Returning updated sigma and mean

# Function to generate the plots
def plot_generation(D,n,m):
    x = range(0,n)
    y = D
    sig = math.sqrt(m*(1-m)/n)
    plt.scatter(x,y, label = 'Sample data', color = 'r', marker = '*')
    plt.axhline(y=m+3*sig, color='b', linestyle='-')
    plt.axhline(y=m-3*sig, color='b', linestyle='-')
    plt.axhline(y=m,color='k',linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('p^')
    plt.title('Work Sampling')
    plt.legend()
    plt.show()


#Function to check if any point is lying outside the 3 sigma interval    
def check(D,n,m):
    i = 0
    sig = math.sqrt(m*(1-m)/n)
    flag = 0
    while(i<n):
        if (flag == 0):                                     # For plotting the initial data generated
            plot_generation(D,n,m)
            flag = 1
        print(m,sig,i)
        if(D[i]<m-3*sig or D[i] > m+3*sig):   # Check: If point outside interval, calls function update
            new = update(D,i,n)
            if(m==new[0]):
                D[i] = m
            else:    
                m = new[0]
                sig = new[1]
            print(m,m+3*sig,m-3*sig,D[i])
            i = 0
            plot_generation(D,n,m)             # Generates the new plot after the update
        else:
            i = i+1
    return 0

data = data_generation(20,0.5,.9)            # Calling the data_generation function with values n = 20, mean = 0.5, and p0(threshold probability = 0.9)
check(data[0],data[1],data[2])
