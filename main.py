import streamlit as st

# Finite Difference Method
import numpy as np
from scipy.sparse import diags
from tqdm import tqdm


K_R = 2.596 # (J/s*m*C) thermal conductivity of rock
U = 12000 # (J/s*m^2*C) heat transfer coefficient between rock and water
A = 10**3*10**3 # (m^2) area for heat transfer between rock and water
m = 1.446*10**3 # (kg/s) mass flowrate of water
rho_W = 1000 # kg/m^3 density of water
c_W = 4184 # (J/kg*C) heat capacity of water
rho_R = 2650 # (kg/m^3) density of rock
c_R = 1050 # (J/kg*K) heat capacity of rock

t_final =  100 # (years) maximum amount of time
L = 40 # (m) maximum length of rock

T_W0 = 40 # (deg. C) initial water temperature
T_R0 = 300 # (deg. C) final rock temperature


t_final = 31536000 * t_final # time in seconds
dt = t_final/100
dx = L/100

w = m * c_W / U / A
kappa = K_R / rho_R / c_R
h = -U * A / K_R * (w / (w + 1/2))
s = kappa * dt / dx**2


# Backwards Euler Implicit Method
t_array = np.arange(0, t_final+dt, dt)
x_array = np.arange(0, L+dx, dx)

len_t = len(t_array)
len_x = len(x_array)

T = np.zeros([len_t, len_x]) # temperature matrix

# initial boundary condition
T[0,:] = T_R0 - T_W0


# backward implicit
for t in tqdm(range(0, len_t-1)):
    A = diags([-s, 1+2*s, -s], [-1, 0, 1], shape=(len_x, len_x)).toarray()
    B = T[t,:]
    
    # boundary condition on left side
    A[0,0] = A[0,0] - s * (1 + h*dx)
    
    # boundary condition on right side
    A[-1,-1] = A[-1,-1] - s
    
    T[t+1,:] = np.linalg.solve(A,B)

# add initial temperature of water
T = T + T_W0

import matplotlib.pyplot as plt
from ipywidgets import interact

@interact(t_=(0,t_final/31536000,t_final/31536000/1000))
def plot(t_):
    time = int(t_*31536000/t_final*(len_t-1))
    plt.plot(
        x_array,
        T[time,:]
    )
    plt.ylim(T_W0,T_R0)
    plt.show()
