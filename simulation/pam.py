"""
This module simulates the 1D parabolic Anderson model
$\\partial_t u = \\Delta u + u \\xi$ in the discrete spatial setting.
The output is an mp4 file of the simulation.
Since the space is discrete, solving the PAM is solving a high-dimensional ODE with random input $\\xi$.
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # necessary to solve ODE.
#For animation, check https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c.
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
plt.style.use('seaborn-pastel')

#Save mp4 file
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#Setting for the figure
plt.figure(figsize=(15, 10))
plt.rcParams.update({'font.size': 16})

#Setting for the parameters
n = 500  # space [0, n] in integer
l = 1  # intensity of the noise $\xi$
speed = 1  # coefficient in front of Laplacian
# kappa(t) = kappa_slope*t + kappa_initial; for time dependent diffusion
kappa_slope = 0.05
kappa_initial = 1
t_number = 1000  # number of steps in time
T = 1000  # simulation in time [0, T]
x = np.linspace(0, n, n+1)  # space
t_set = np.linspace(0, T, t_number)  # time
#V = l*(np.random.rand(n+1)  ) #=$\xi$, uniform dist
V = np.random.normal(0, 3, n+1)  # =$\xi$, Gaussian dist

#Setting for the initial data
u_0 = [0]*(n+1)
u_0[n//2] = 1


def pam(u, t):
    v = [0]*(n+1)
    v[0] = speed*(u[1] - u[0]) + V[0]*u[0]
    v[n] = speed*(u[n-1] - u[n]) + V[n]*u[n]
    for i in range(1, n):
        v[i] = speed*(u[i+1] + u[i-1] - 2*u[i]) + V[i]*u[i]
    return v

def kappa(t):
    return kappa_slope*t + kappa_initial

def pam_time_dependent_diffusion(u, t):
    v = [0]*(n+1)
    v[0] = kappa(t)*(u[1] - u[0]) + V[0]*u[0]
    v[n] = kappa(t)*(u[n-1] - u[n]) + V[n]*u[n]
    for i in range(1, n):
        v[i] = kappa(t)*(u[i+1] + u[i-1] - 2*u[i]) + V[i]*u[i]
    return v

def u_function(u):
    return (1 + u)**(-0.5)

def pam_u_in_front_of_laplacian(u, t):
    v = [0]*(n+1)
    v[0] = u_function(u[0])*(u[1] - u[0]) + V[0]*u[0]
    v[n] = u_function(u[n])*(u[n-1] - u[n]) + V[n]*u[n]
    for i in range(1, n):
        v[i] = u_function(u[i])*(u[i+1] + u[i-1] - 2*u[i]) + V[i]*u[i]
    return v

def pam_u_in_front_of_noise(u, t):
    """
    Return speed*Laplacian u + u_function(u)*u*V, i.e. the right-hand side of the PAM.
    """
    v = [0]*(n+1)
    v[0] = speed*(u[1] - u[0]) + u[0]*V[0]*u_function(u[0])
    v[n] = speed*(u[n-1] - u[n]) + u[n]*V[n]*u_function(u[n])
    for i in range(1, n):
        v[i] = speed*(u[i+1] + u[i-1] - 2*u[i]) + u[i]*V[i]*u_function(u[i])
    return v

#Solve PAM

#u = odeint(pam, u_0, t_set)
#u = odeint(pam_time_dependent_diffusion, u_0, t_set)
#u = odeint(pam_u_in_front_of_laplacian, u_0, t_set)
u = odeint(pam_u_in_front_of_noise, u_0, t_set)


fig = plt.figure()
ax = plt.axes(xlim=(0, n))
line, = ax.plot([], [])
ax.set_yticklabels([])


def init():
    line.set_data([], [])
    return line,


def animate(i):
    m = max(u[i])
    plt.title('maximum={maximum}'.format(maximum=m))
    ax.set_ylim([0, m*1.1])
    line.set_data(x, u[i])
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=t_number, interval=100, blit=True)


anim.save('pam_u_in_front_of_noise_new.mp4', writer=writer)
# for i in range(t_number):
#     plt.clf()
#     y = np.array(u[i])
#     plt.plot(x, y)
#     plt.savefig('tmp_{:04d}.png'.format(i))
