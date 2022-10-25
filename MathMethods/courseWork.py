import pylab
import math
import numpy as np
import matplotlib.pyplot as plt

def lab_6():
    lam1 = 5 ** 12
    lam2 = 3 ** 11
    M0 = 15
    disp0 = 12
    alpha0 = -0.1
    N = 5000
    Ns = 10
    x = [1]
    xi = []
    for j in range(N):
        x.append(((lam1 * x[j]) % lam2))
        xi.append(x[j] / lam2 - 0.5)
    Mx = 1 / N * sum(xi)
    peremen = 0
    for j in range(N):
        peremen += (xi[j] - Mx) ** 2
    dispx = 1 / N * peremen
    z = []
    for k in range(1, N - 9):
        j = 0
        for i in np.arange(k, k + Ns):
            j += xi[i] * np.sqrt(disp0 / (dispx * -alpha0)) * np.exp(alpha0 * (i -k)) + M0
    z.append(1 / Ns * j)
    x1 = [i for i in range(N)]
    z1 = [i for i in range(N - 10)]
    return z1, z, z[0]

def math_model(F=5, v=0.01):     
    z1, Z_k, C1_vh = lab_6()
    A_1 = 10000
    E_1 = 156000
    A_2 = 20000
    E_2 = 166400
    A_3 = 50000
    E_3 = 177000
    A_4 = 500
    E_4 = 160000
    K_t = 2000
    T_t = 500
    V = 10
    T_vh = 1200
    Q_1 = 361000
    Q_2 = 950000
    Q_4 = 1520000   
    C_t = 1200
    p = 1.9
    R = 8.31
    C1_vh = (13 * p) / (100 * (16 / 1000))
    C3_vh = (15 * p) / (100 * (32 / 1000))
    C2_vh = (12 * p) / (100 * (17 / 1000))

    k1 = lambda TT: A_1 * np.exp((-E_1) / (R * TT))
    k2 = lambda TT: A_2 * np.exp((-E_2) / (R * TT))
    k3 = lambda TT: A_3 * np.exp((-E_3) / (R * TT))
    k4 = lambda TT: A_4 * np.exp((-E_4) / (R * TT))

    tau = v / V
    d_t = 1
    eps = 0.001

    d_C4 = lambda C1, C2, C3, C4, t: 2 * k1(t) * C1 * C2 * C3 + tau * (- C4)
    d_C1 = lambda C1, C2, C3, C5, t: -2 * k1(t) * C1 * C2 * C3 - k2(t) * C1 * C5 - 2 * k3(t) * C1 * C3 + tau * (C1_vh - C1)
    d_C2 = lambda C1, C2, C3, t: -2 * k1(t) * C1 * C2 * C3 - 4 * k4(t) * C2 * C3 + tau * (C2_vh - C2)
    d_C3 = lambda C1, C2, C3, t: -3 * k1(t) * C1 * C2 * C3 - k3(t) * C1 * C3 - 3 * k4(t) * C2 * C3 + tau * (C3_vh - C3)
    d_C5 = lambda C1, C2, C3, C5, t: 6 * k1(t) * C1 * C2 * C3 - k2(t) * C1 * C5 + 6 * k4(t) * C2 * C3 + tau * (-C5)
    d_T = lambda d_C1, d_C2, d_C3, d_C5, T: (((v / V) * (T_vh - T))/ (C_t*p)) - ((K_t * F) / (C_t * V * p)) * (T - T_t) + ((k1(T) * d_C1 * d_C2 * d_C3 * Q_1)) + ((k4(T) * d_C2 *d_C3 * Q_4)) - (k2(T) * d_C1 * d_C5 * Q_2)

    T_h = [T_vh]
    res_1 = Z_k
    res_2 = [C2_vh]
    res_3 = [C3_vh]
    res_4 = [0]
    res_5 = [0]
    Time = [0]
    count1 = -1
    print(F,v)
    while True:
        count1 += 1
        res_4.append(res_4[-1] + (d_C4(res_1[count1], res_2[-1], res_3[-1],res_4[-1], T_h[-1]) * d_t))
        res_2.append(res_2[-1] + (d_C2(res_1[count1], res_2[-1], res_3[-1], T_h[-1]) * d_t))
        res_1.append(res_1[-1] + (d_C1(res_1[-1], res_2[-1], res_3[-1], res_5[-1], T_h[-1]) * d_t))
        res_2.append(res_2[-1] + (d_C2(res_1[count1], res_2[-1], res_3[-1], T_h[-1]) * d_t))
        res_3.append(res_3[-1] + (d_C3(res_1[count1], res_2[-2], res_3[-1], T_h[-1]) * d_t))
        res_5.append(res_5[-1] + (d_C5(res_1[count1], res_2[-2], res_3[-2],res_5[-1], T_h [-1]) * d_t))
        T_h.append(T_h [-1] + d_T(res_1[count1], res_2[-2], res_3[-2], res_5[-2], T_h[-1])*d_t)
        print(T_h [-1])
        print(res_1[count1], res_2[-1], res_3[-1], res_4[-1], res_5[-1], T_h [-1])
        Time.append(Time[-1] + d_t)
        if count1 == res_1.index(res_1[-1]):
            return Time, z1, res_1, res_2, res_3, res_4, res_5

Time, z1, res_1, res_2, res_3, res_4, res_5 = math_model()
fig, axes = pylab.subplots(nrows=1, ncols=2, figsize=(12, 5))
axes[0].plot(z1, res_1, color='black')
axes[1].plot(Time, res_4, color='black')
axes[4].plot(Time, res_5, color='black')
print(res_4)
pylab.subplots_adjust(wspace=0.5, hspace=0)
pylab.show()
