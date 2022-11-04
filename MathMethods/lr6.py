import math
import matplotlib.pyplot as plt

l1 = 5 ** 8
l2 = 3 ** 15
M0 = 770
disp = 400
alfa0 = 0.09

N = 200
Ns = 10
z0 = 1
A1 = 1
A2 = 1



def M(z):
    return (1 / N) * sum(z)

def dispersion(z, M):
    sum = 0
    for zi in z:
        sum += (zi - M) ** 2
    return 1 / N * sum

def K(z, M):
    k = []
    for s in range(0, 20):
        sum = 0
        for i in range(0, len(z) - s):
            sum += (z[i] - M) * (z[i + s] - M)
        k.append((1 / (N - s)) * sum)
    return k

def process_generator(z, d):
    # генератор случайных процессов
    arr = []
    for k in range(0, len(z) - Ns):
        sum = 0
        for i in range(k, k + Ns):
            sum += z[i] * math.sqrt(disp / (d * alfa0)) \
                    * math.exp(-1 * alfa0 * (i - k)) + M0
        arr.append((1 / Ns) * sum)
    return arr

def number_generator(N):
        # генератор случайных чисел
        # конгруэнтный метод
    gen_values = []
    z = [z0]
    for i in range(0, N - 1):
        zi = (l1 * z[i]) % l2
        z.append(zi)
    for i in range(0, N):
        gen_values.append((z[i] / l2) - 0.5)
    return gen_values


def gen(N):
    arr = process_generator(number_generator(N), dispersion(number_generator(N), M(number_generator(N))))
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 7))
    axes[0].plot([i for i in range(N)], number_generator(N), color="purple")
    axes[1].plot([i for i in range(len(arr))], arr, color="blue")
    plt.subplots_adjust(wspace=0.5, hspace=0)
    plt.show()
    return arr




