"""
We want to simulate the one-dimensional random differential equation 
$dX_t/dt = B(X_t) - m X_t$, where $B$ is two-sided Brownian motion.
This SDE is called the Alessandro-Beatrice-Bertotti-Montorsi (ABBM) model.
"""

import matplotlib.pyplot as plt
from fbm import FBM
import numpy as np

def ABBM(B_max, B_step, B_value, m,  initial_condition, final_time, time_step, W, F):
    """
    Solve $dX_t = B(X_t) dt - m X_t dt + d W(t) + F$ by Euler method. 

    parameters
    ----------
    B_domain (float), B_step (int), B_value (array of size $2n+1$) 
        : model the function B. See the inside function $B$.
    m (float): drift coefficient
    initial_condition: initial condition $X_0$
    final_time: we simulate $X$ up to time $T$. 
    time_step: for the Euler scheme, time discretized as 0, T/n, 2T/n, \ldots, T.
    ----------
    """
    if len(B_value) != 2*B_step+1:
        raise ValueError("We must have len(B_value) = 2*n+1.")
    def B(x):
        """
        If $x \in [k B_max/B_step, (k+1) B_max/B_step)$, 
        we return B_value[k+B_step].
        If $x < - B_step$, return $B[0]$ and 
        if $x > B_step$, return $B[-1]$.
        """
        z = int(np.floor(B_step*x/B_max)) + B_step
        if z < 0:
            return B_value[0]
        elif z >= 2*B_step:
            return B_value[-1]
        else:
            return B_value[z]
    # X is the solution
    X = np.zeros(time_step)
    X[0] = initial_condition
    delta = final_time/time_step
    # Run the Euler scheme
    for i in range(1, time_step):
        X[i] = X[i-1] + (B(X[i-1]) - m*X[i-1] + F)*delta + W[i] - W[i-1] 
    return X, B(X[-1])

#parameters
H = 0.5
B_T = 20
B_STEP= 4000
X_T = 10
X_STEP = 4000
m = 0
F = 1


# Define B 
B_1 = FBM(n=B_STEP, hurst=H, length=B_T).fbm()
B_2 = FBM(n=B_STEP, hurst=H, length=B_T).fbm()
B_2 = B_2[::-1] #flop B_2
B = np.concatenate((B_2[:-1], B_1)) + np.random.normal(0, 1)

W = FBM(n=X_STEP, hurst=H, length=X_T).fbm()
W_0 = np.zeros(X_STEP)

# Obtain X
X, B_final = ABBM(B_T, B_STEP, B, m, 0, X_T, X_STEP, W, F)
X_0, B_final_0 = ABBM(B_T, B_STEP, B, m, 0, X_T, X_STEP, W_0, F)
X_times = np.linspace(0, X_T, X_STEP)

# Draw graph
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(12, 6)
#fig.suptitle('H = {hurst}'.format(hurst=H))
ax.plot(X_times, X_0)
# ax_2.plot(X_times, X)
# ax_3.plot(X_times, W[:-1])

#plt.savefig('local_time_with_H={hurst}.pdf'.format(hurst=str(H)))
plt.show()
