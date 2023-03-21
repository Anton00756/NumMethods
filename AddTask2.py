# Вычисление определённого интеграла (Вариант 11)
import math
import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return 1 / (x ** 3 + 64)


def rectangle_method(x, h):
    return sum(h * function(x_value) for x_value in x[:-1])


def trapezoid_method(x, h):
    return h / 2 * (function(x[0]) + function(x[-1]) + 2 * sum(function(x[1:-1])))


def simpson_method(x, h):
    return h / 3 * (function(x[0]) + function(x[-1]) + 4 * sum(function(x[i]) for i in range(1, len(x), 2)) +
                    2 * sum(function(x[i]) for i in range(2, len(x) - 1, 2)))


def graphic(start_x, finish_x, h, method=''):
    if method == '':
        return
    plt.figure(figsize=(10, 5))
    x_values = np.arange(start_x, finish_x + 0.01, 0.01)
    plt.plot(x_values, function(x_values), label=r'$y(x)$')
    h_x = np.arange(start_x, finish_x + h, h)
    x = []
    y = []
    if method == 'r':
        for i in range(len(h_x) - 1):
            x += [h_x[i], h_x[i], h_x[i + 1], h_x[i + 1]]
            y_value = function(h_x[i])
            y += [0, y_value, y_value, 0]
    elif method == 't':
        for i in range(len(h_x) - 1):
            x += [h_x[i], h_x[i], h_x[i + 1]]
            y += [0, function(h_x[i]), function(h_x[i + 1])]
        x.append(h_x[-1])
        y.append(0)
    elif method == 's':
        points_x, points_y = [], []
        for index in range(1, len(h_x), 2):
            points_x.append(h_x[index])
            points_y.append(function(h_x[index]))
            poly = np.poly1d([])
            local_x = h_x[index - 1: index + 2]
            for i in range(len(local_x)):
                poly += function(local_x[i]) * math.prod(np.poly1d([1, -local_x[j]]) / (local_x[i] - local_x[j])
                                                         for j in range(len(local_x)) if j != i)
            lagrange_x = list(np.arange(local_x[0], local_x[-1] + 0.01, 0.01))
            x += lagrange_x
            y += list(poly(lagrange_x))
        plt.plot(points_x, points_y, 'ro')
    plt.plot(x, y, label=f'$h={h}$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()


def refine_value(full_value, half_value, p):
    return half_value + (half_value - full_value) / (2 ** p - 1)


start_x = -2
finish_x = 2
h_1 = 1
h_2 = 0.5
rec_1 = rectangle_method(np.arange(start_x, finish_x + h_1, h_1), h_1)
rec_2 = rectangle_method(np.arange(start_x, finish_x + h_2, h_2), h_2)
trap_1 = trapezoid_method(np.arange(start_x, finish_x + h_1, h_1), h_1)
trap_2 = trapezoid_method(np.arange(start_x, finish_x + h_2, h_2), h_2)
sim_1 = simpson_method(np.arange(start_x, finish_x + h_1, h_1), h_1)
sim_2 = simpson_method(np.arange(start_x, finish_x + h_2, h_2), h_2)

print("\n\t\tМетод прямоугольников:")
print(f'Значение при h = {h_1}: {rec_1}')
print(f'Значение при h = {h_2}: {rec_2}')
print(f'Уточнённое значение: {refine_value(rec_1, rec_2, 1)}')
print("\n\t\tМетод трапеций:")
print(f'Значение при h = {h_1}: {trap_1}')
print(f'Значение при h = {h_2}: {trap_2}')
print(f'Уточнённое значение: {refine_value(trap_1, trap_2, 2)}')
print("\n\t\tМетод Симпсона:")
print(f'Значение при h = {h_1}: {sim_1}')
print(f'Значение при h = {h_2}: {sim_2}')
print(f'Уточнённое значение: {refine_value(sim_1, sim_2, 4)}')

graphic(start_x, finish_x, h_1, 's')  # r, t, s

