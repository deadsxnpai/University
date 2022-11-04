import matplotlib.pyplot as plt
import lr6 as gen
import pylab


def proc_conversion_C3(C3):
    C3_proc = ((C3 * 0.098) / 200) * 100
    return C3_proc


def proc_conversion_C1(C1):
    C1_proc = ((C1 * 0.072) / 200) * 100
    return C1_proc


def c1_calc(C1, delta_Z):
    c_calc = C1 + ((- 0.00526 * C1 - 0.00734 * C1) / 0.022) * delta_Z
    return c_calc


def c3_calc(C1, C3, delta_Z):
    c_calc = C3 + ((0.00526 * C1 - 0.00269 * C3) / 0.022) * delta_Z
    return c_calc


def calculating(iteration_Z, C_1):
    _Z = 0
    _delta_Z = 0.01
    if C_1 == 0:
        _C1 = 770
    else:
        _C1 = C_1
    _C3 = 0
    _Z_list = list()
    _C3_list = list()
    _C1_list = list()
    while _Z < iteration_Z:
        _C1_list.append(proc_conversion_C1(_C1))
        _C1 = c1_calc(_C1, _delta_Z)
        c3_max = c3_calc(_C1, _C3, _delta_Z)
        _C3 = c3_max
        _Z_list.append(_Z + _delta_Z)
        _Z += _delta_Z
        _C3_list.append(proc_conversion_C3(_C3))
    return proc_conversion_C3(_C3)


def show_C1_C3(C_1):
    _Z = 0
    _delta_Z = 0.01
    if C_1 == 0:
        _C1 = 770
    else:
        _C1 = C_1
    _C3 = 0
    _Z_list = list()
    _C3_list = list()
    _C1_list = list()
    while _Z < 50:
        _C1_list.append(proc_conversion_C1(_C1))
        _C1 = c1_calc(_C1, _delta_Z)
        c3_max = c3_calc(_C1, _C3, _delta_Z)
        _C3 = c3_max
        _Z_list.append(_Z + _delta_Z)
        _Z += _delta_Z
        _C3_list.append(proc_conversion_C3(_C3))
    return _Z_list, _C1_list, _C3_list


def show_C(C_1):
    _Z = 0
    _delta_Z = 0.01
    if C_1 == 0:
        _C1 = 770
    else:
        _C1 = C_1
    _C3 = 0
    _C3_list = list()
    while _Z < 3.42:
        _C1 = c1_calc(_C1, _delta_Z)
        c3_max = c3_calc(_C1, _C3, _delta_Z)
        _C3 = c3_max
        _Z += _delta_Z
    _C3 = proc_conversion_C3(_C3)
    return _C3


def check_c():
    arr = gen.gen(520)
    iteration = 0
    _Z = 0
    _delta_Z = 0.1
    _Z_list = list()
    _C1_list = list()
    _C3_list = list()
    while _Z < 50:
        _Z_list.append(_Z)
        if _Z >= 3.42:
            _C3_list.append(show_C(arr[iteration]))
        else:
            _C3_list.append(0)
        _C1_list.append(proc_conversion_C1(arr[iteration]))
        _Z += _delta_Z
        iteration += 1
    fig, axes = pylab.subplots(nrows=2, ncols=1, figsize=(12, 7))
    axes[0].plot(_Z_list, _C1_list, color="purple", label="C1")
    axes[1].plot(_Z_list, _C3_list, color="blue", label="C3")
    axes[0].set(xlabel="Z(с)", ylabel="Концентрация(%)")
    axes[1].set(xlabel="Z(с)", ylabel="Концентрация(%)")
    axes[0].legend()
    axes[1].legend()
    plt.show()


def golden_ratio(C_1):
    a0 = 0
    b0 = 50
    _Z, _C1, _C3 = show_C1_C3(C_1)
    fig, axes = pylab.subplots(nrows=1, ncols=2, figsize=(12, 5))
    axes[0].plot(_Z, _C1, color="purple", label="C1")
    axes[0].plot(_Z, _C3, color="blue", label="C3")
    axes[0].set(xlabel="Z(с)", ylabel="Концентрация(%)")
    axes[0].scatter(3.46, 10.31, color="purple")
    axes[0].legend()
    axes[1].plot(_Z, _C3, color="blue", label="C3")
    axes[1].set(xlabel="L(м)", ylabel="Концентрация(%)")
    axes[1].scatter(a0, 0, color="red")
    axes[1].scatter(b0, 0, color="black")
    x1 = a0 + 0.38 * (abs(b0 - a0))
    x2 = b0 - 0.38 * (abs(b0 - a0))
    while abs(b0 - a0) >= 0.04:
        if calculating(x1, C_1) > calculating(x2, C_1):
            b0 = x2
            x2 = x1
            x1 = a0 + 0.38 * (abs(b0 - a0))
            axes[1].scatter(x1, 0, color="red")
            axes[1].plot((x1, x1), (0, calculating(x1, C_1)), linewidth=0.55, color="black", linestyle='--')
            axes[1].scatter(x2, 0, color="black")
            axes[1].plot((x2, x2), (0, calculating(x2, C_1)), linewidth=0.55, color="black", linestyle='--')
        else:
            a0 = x1
            x1 = x2
            x2 = b0 - 0.38 * (abs(b0 - a0))
    L_Max = x1 if calculating(x1, C_1) > calculating(x2, C_1) else x2
    axes[1].scatter(L_Max, calculating(L_Max, C_1), color="purple")
    plt.text(L_Max + 0.3, calculating(L_Max, C_1), "C3_max")
    print("Максимальная концентрация C3:", calculating(L_Max, C_1), "%, достигается при длине трубы", L_Max, "метров(а)")
    axes[1].legend()
    plt.show()
    check_c()
    return L_Max, calculating(L_Max, C_1)


if __name__ == '__main__':
    golden_ratio(770)

