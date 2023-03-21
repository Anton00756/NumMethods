# Решение задачи Коши (Вариант 11)
import numpy as np


def derivative(x, y):
    return 2 * (x ** 2 - x * y) / (x ** 2 + 1)


def exact_solution(x):
    return 2 / 3 * (x ** 3 + 1) / (x ** 2 + 1)


def Euler(table: list, start_y, h):
    y = [start_y]
    for x_value in table[0][1:]:
        y.append(y[-1] + h * derivative(x_value, y[-1]))
    table.append(y)


def Euler_Cauchy(table: list, start_y, h):
    x = table[0]
    y = [start_y]
    for index in range(len(x) - 1):
        predictor = y[-1] + h * derivative(x[index], y[-1])
        y.append(y[-1] + h / 2 * (derivative(x[index], y[-1]) + derivative(x[index + 1], predictor)))
    table.append(y)


def Runge_Kutta(table: list, start_y, h):
    y = [start_y]
    for x_value in table[0]:
        k_1 = h * derivative(x_value, y[-1])
        k_2 = h * derivative(x_value + h / 2, y[-1] + k_1 / 2)
        k_3 = h * derivative(x_value + h / 2, y[-1] + k_2 / 2)
        k_4 = h * derivative(x_value + h, y[-1] + k_3)
        y.append(y[-1] + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6)
    table.append(y)


def inaccuracy(vector_1, vector_2):
    return max(abs(vector_1[i] - vector_2[i]) for i in range(1, len(vector_1)))


start_x, finish_x = 1, 2
h = 0.1
start_y = 2/3

table = [list(np.arange(start_x, finish_x + h, h))]
table.append([exact_solution(value) for value in table[0]])
Euler(table, start_y, h)
Euler_Cauchy(table, start_y, h)
Runge_Kutta(table, start_y, h)

string_matrix = [[str(round(float(element), 7)) for element in row] for row in table]
string_matrix[0].insert(0, 'x:')
string_matrix[1].insert(0, 'y-точ.:')
string_matrix[2].insert(0, 'y-Эйл.:')
string_matrix[3].insert(0, 'y-Э-К:')
string_matrix[4].insert(0, 'y-Р-К:')
lens = [max(map(len, col)) for col in zip(*string_matrix)]
fmt = '\t\t'.join(f'{{:{length}}}' for length in lens)
print_table = [fmt.format(*row) for row in string_matrix]
print('\n'.join(print_table))

print(f'\nПогрешность метода Эйлера: {inaccuracy(table[1], table[2])}')
print(f'Погрешность метода Эйлера-Коши: {inaccuracy(table[1], table[3])}')
print(f'Погрешность метода Рунге-Кутта: {inaccuracy(table[1], table[4])}')
