import numpy as np
import math
import matplotlib.pyplot as plt

V = 3

A1 = 2553
E1 = 34000

A2 = 2.1*10**9
E2 = 7.7 * 10**4

A3 = 8.4*10**9
E3 = 5.2*10**4

A4 = 9.45*10**4
E4 = 3.75*10**4

Q1 = 62540
Q2 = 10**6
Q4 = 1.08*10**6

R = 8.31

K_t = 700
T_vh = 40
ro = 1180
C_t = 1200
T_t = 8

C1_vh = 0.55 
C2_vh = 0.35
C5_vh = 0.10
T_max = 60

def math_model(F=6.5):

    k1 = lambda TT: A1 * np.exp((-E1) / (R * TT))
    k2 = lambda TT: A2 * np.exp((-E2) / (R * TT))
    k3 = lambda TT: A3 * np.exp((-E3) / (R * TT))
    k4 = lambda TT: A4 * np.exp((-E4) / (R * TT))

    d_C3 = lambda C1,C2,C3,C6,t : k1(t)*C1*C2-k4(t)*C3*C6
    d_C1 = lambda C1,C2,t: -k1(t)*C1*C2-k2(t)*C1*C2
    d_C2 = lambda C1,C2,C3,C6,t: -k1(t)*C1*C2-k2(t)*C1*C2+k4(t)*C3*C6
    d_C6 = lambda C4,C5,C3,C6,t: k3(t)*C4*C5-k4(t)*C3*C6
    d_C4 = lambda C1,C2,C4,C5,t: k2(t)*C1*C2-k3(t)*C4*C5
    d_C5 = lambda C3,C6,C4,C5,t: k4(t)*C3*C6-k3(t)*C4*C5

    d_T = lambda d_C1,d_C2,d_C3,d_C6,T: k1(T)*d_C1*d_C2*Q1*V + k2(T)*d_C1*d_C2*Q2*V+k4(T)*d_C3*d_C6*Q4*V-K_t*F(T-T_t)

    T_h = [T_vh]

def main():
    pass

if __name__ == '__main__':
    main()