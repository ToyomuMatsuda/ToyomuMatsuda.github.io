# We want to consider $dX_t = \xi(dt, X_t)$, where $\xi$ is the space-time white noise. 
# Of course such equation does not make sense, and we want to consider the mollified eq
# $dX_t = c_N \sum_{k=1}^N f_k(X_t) dB_t^k$, where $(f_k)$ is an orthonormal basis 
# and $(B^k)$ are independent Brownian motions. 
# Can we choose $c_N$ so that you get the limit? 
import matplotlib.pyplot as plt
from fbm import FBM
import numpy as np




def process(B, alpha):
    X = np.zeros(len(B)) #solution of dX_t = (1 + L_t(X_t))**(-alpha) dB_t
    L = np.zeros((len(B), STEP)) #local time of X.
    m = min(B)
    M = max(B)
    delta = (M - m + 1)/STEP
    for i in range(1, len(B)):
        level = int((X[i-1] - m)/delta)
        X[i] = X[i-1] + (1 + L[i-1][level])**(-alpha)*(B[i]-B[i-1])
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


def process_with_drift(B, alpha):
    X = np.zeros(len(B)) #solution of dX_t = (1 + L_t(X_t))**(-alpha) dB_t
    L = np.zeros((len(B), STEP)) #local time of X.
    delta = 10*T/STEP
    for i in range(1, len(B)):
        level = int((X[i-1] + 5*T)/delta)
        X[i] = X[i-1] + T/STEP + (1 + L[i-1][level])**(-alpha)*(B[i]-B[i-1])
        # for j in range(0, STEP):
        #     if abs(j - level) <= 1:
        #         L[i][j] = L[i-1][j] + delta**(1)
        #     else:
        #         L[i][j] = L[i-1][j]
        for j in range(0, STEP):
            if X[i-1] < -5*T  + j*delta and X[i] > -5*T + j*delta:
                L[i][j] = L[i-1][j] + X[i] - X[i-1]
            else:
                L[i][j] = L[i-1][j]
    return X, L


def process_ornstein(B, alpha):
    X = np.zeros(len(B)) #solution of dX_t = (1 + L_t(X_t))**(-alpha) dB_t
    L = np.zeros((len(B), STEP)) #local time of X.
    delta = 10*T/STEP
    for i in range(1, len(B)):
        level = int((X[i-1] + 5*T)/delta)
        X[i] = X[i-1] - X[i-1]**3*T/STEP + (1 + L[i-1][level])**(-alpha)*(B[i]-B[i-1])
        # for j in range(0, STEP):
        #     if abs(j - level) <= 1:
        #         L[i][j] = L[i-1][j] + delta**(1)
        #     else:
        #         L[i][j] = L[i-1][j]
        for j in range(0, STEP):
            if X[i-1] < -5*T  + j*delta and X[i] > -5*T + j*delta:
                L[i][j] = L[i-1][j] + X[i] - X[i-1]
            else:
                L[i][j] = L[i-1][j]
    return X, L

def process_local_time_drift(B, alpha):
    X = np.zeros(len(B)) #solution of dX_t = (1 + L_t(X_t))**(-alpha) dB_t
    L = np.zeros((len(B), STEP)) #local time of X.
    m = -10*T
    M = 10*T
    delta = (M - m)/STEP
    for i in range(1, len(B)):
        print(max(L[i-1]))
        level = int((X[i-1] - m)/delta)
        X[i] = X[i-1] +  max([L[i-1][level], 1])**alpha*T/STEP + (B[i]-B[i-1])
        # for j in range(0, STEP):
        #     if abs(j - level) <= 1:
        #         L[i][j] = L[i-1][j] + delta**(1)
        #     else:
        #         L[i][j] = L[i-1][j]
        for j in range(0, STEP):
            if X[i-1] < m  + j*delta and X[i] > m + j*delta:
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
