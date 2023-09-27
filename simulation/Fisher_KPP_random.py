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
writer = Writer(fps=50, metadata=dict(artist='Me'), bitrate=1800)
#Setting for the figure
plt.figure(figsize=(15, 10))
plt.rcParams.update({'font.size': 16})

#Setting for the parameters
n = 500  # space [0, n] in integer
l = 1  # intensity of the noise $\xi$
speed = 2  # coefficient in front of Laplacian
t_number = 1500  # number of steps in time
T = 1000  # simulation in time [0, T]
x = np.linspace(0, n, n+1)  # space
t_set = np.linspace(0, T, t_number)  # time
V = l*(np.random.uniform(-0.5, 0.5, n+1) ) #=$\xi$, uniform dist
# = np.random.normal(0, 1, n+1)  # =$\xi$, Gaussian dist


#Setting for the initial data
u_0 = [0]*(n+1)
for i in range(0, n//2):
    u_0[i] = 1


def pam(u, t):
    v = [0]*(n+1)
    v[0] = speed*(u[1] - u[0]) + V[0]*u[0]*(1-u[0])
    v[n] = speed*(u[n-1] - u[n]) + V[n]*u[n]*(1-u[n])
    for i in range(1, n):
        v[i] = speed*(u[i+1] + u[i-1] - 2*u[i]) + V[i]*u[i]*(1-u[i])
    return v


#Solve PAM

u = odeint(pam, u_0, t_set)


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


anim.save('kpp_random_env_unif.mp4', writer=writer)
# for i in range(t_number):
#     plt.clf()
#     y = np.array(u[i])
#     plt.plot(x, y)
#     plt.savefig('tmp_{:04d}.png'.format(i))
