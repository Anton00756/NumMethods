# Интерполяционный многочлен (Nг = Nc = 11)
import math

import numpy as np
import matplotlib.pyplot as plt


def get_F_Lagrange(x, y):
    result = np.poly1d([])
    for i in range(len(x)):
        result += y[i] * math.prod(np.poly1d([1, -x[j]]) / (x[i] - x[j]) for j in range(len(x)) if j != i)
    for i in range(len(x)):
        if round(result(x[i]), 10) != y[i]:
            print(f"Проверка: ❌ [{result(x[i])} != {y[i]}]")
            break
    else:
        print("Проверка: ✔")
    return result


class NewtonProcessor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.buffer = dict()

    def get_f(self, indexes):
        if len(indexes) == 1:
            return self.y[indexes[0] - 1]
        map_key = "".join(str(index) for index in indexes)
        if map_key in self.buffer.keys():
            return self.buffer.get(map_key)
        result = (self.get_f(indexes[1:]) - self.get_f(indexes[:-1])) / (self.x[indexes[-1] - 1] -
                                                                         self.x[indexes[0] - 1])
        self.buffer[map_key] = result
        return result

    def get_coefficient(self, number):
        return self.buffer.get("".join(str(index) for index in range(1, int(number) + 1)))

    def get_expression(self):
        self.get_f(np.arange(1, len(self.x) + 1, 1))
        result = np.poly1d([self.get_f([1])])
        result += sum(self.get_coefficient(i) * math.prod(np.poly1d([1, -self.x[j]]) for j in range(i - 1))
                      for i in range(2, len(self.x) + 1))
        return result


def get_F_Newton(x, y):
    return NewtonProcessor(x, y).get_expression()


x = [-2, -1, 0, 1, 2]
y = [11, 11, -1, 11, 11]
print("\t\tМногочлен Лагранжа:")
print("а) ", end='')
a_result_l = get_F_Lagrange(x[:-1], y[:-1])
print(f'{a_result_l}')
print("б) ", end='')
b_result_l = get_F_Lagrange(x[1:], y[1:])
print(f'{b_result_l}')
print("в) ", end='')
c_result_l = get_F_Lagrange(x, y)
print(f'{c_result_l}')

print("\n\t\tМногочлен Ньютона:")
print("а) \n", end='')
a_result_n = get_F_Newton(x[:-1], y[:-1])
print(f'{a_result_n}')
print("б) \n", end='')
b_result_n = get_F_Newton(x[1:], y[1:])
print(f'{b_result_n}')
print("в) \n", end='')
c_result_n = get_F_Newton(x, y)
print(f'{c_result_n}')

fig, (lagrange_plot, newton_plot) = plt.subplots(1, 2)
fig.set_size_inches(15, 5)
lagrange_plot.set_title("Многочлен Лагранжа")
lagrange_plot.plot(x, y, 'ro')
x_values = np.arange(x[0], x[-2] + 0.01, 0.01)
lagrange_plot.plot(x_values, a_result_l(x_values), label=r'$L_а$')
x_values = np.arange(x[1], x[-1] + 0.01, 0.01)
lagrange_plot.plot(x_values, b_result_l(x_values), label=r'$L_б$')
x_values = np.arange(x[0], x[-1] + 0.01, 0.01)
lagrange_plot.plot(x_values, c_result_l(x_values), label=r'$L_в$')
lagrange_plot.set_xlabel(r'$x$', fontsize=14)
lagrange_plot.set_ylabel(r'$f(x)$', fontsize=14)
lagrange_plot.grid(True)
lagrange_plot.legend(loc='best', fontsize=12)

newton_plot.set_title("Многочлен Ньютона")
newton_plot.plot(x, y, 'ro')
x_values = np.arange(x[0], x[-2] + 0.01, 0.01)
newton_plot.plot(x_values, a_result_n(x_values), label=r'$N_а$')
x_values = np.arange(x[1], x[-1] + 0.01, 0.01)
newton_plot.plot(x_values, b_result_n(x_values), label=r'$N_б$')
x_values = np.arange(x[0], x[-1] + 0.01, 0.01)
newton_plot.plot(x_values, c_result_n(x_values), label=r'$N_в$')
newton_plot.set_xlabel(r'$x$', fontsize=14)
newton_plot.set_ylabel(r'$f(x)$', fontsize=14)
newton_plot.grid(True)
newton_plot.legend(loc='best', fontsize=12)

plt.show()
