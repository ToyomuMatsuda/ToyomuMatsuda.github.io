# We want to simulate the one-dimensional random differential equation $dX_t/dt = B(X_t) - m [X_t - w_t]$, where $B$ is two-sided Brownian motion.
# This SDE is called the Alessandro-Beatrice-Bertotti-Montorsi (ABBM) model.

import matplotlib.pyplot as plt
from fbm import FBM
import numpy as np

def process(w, time_step):
    X = np.zeros(len(w)) #solution of dX_t = (1 + L_t(X_t))**(-alpha) dB_t
    def B(x):
        
    for i in range(1, len(B)):
        X[i] = X[i-1] + B(X[i-1]) 
        # for j in range(0, STEP):
        #     if abs(j - level) <= 1:
        #         L[i][j] = L[i-1][j] + delta**(1)
        #     else:
        #         L[i][j] = L[i-1][j]
        for j in range(0, STEP):
            if X[i-1] < m + j*delta and X[i] > m + j*delta:
                L[i][j] = L[i-1][j] + X[i] - X[i-1]
            else:
                L[i][j] = L[i-1][j]
    return X, L

H = 0.5
T = 100
STEP= 4000
alpha = 6.0

B = FBM(n=STEP, hurst=H, length=T)
B_sample = B.fbm()
B_times = B.times()
X_sample, L_sample = process(B_sample, alpha)
X0_sample, L0_sample = process(B_sample, 0)

fig, (ax_1, ax_2) = plt.subplots(1, 2)
fig.set_size_inches(12, 6)
#fig.suptitle('H = {hurst}'.format(hurst=H))
ax_1.plot(B_times, X_sample)
ax_2.plot(B_times, X0_sample)

#plt.savefig('local_time_with_H={hurst}.pdf'.format(hurst=str(H)))
plt.show()
