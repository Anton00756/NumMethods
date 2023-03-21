# Метод наименьших квадратов (Nг = Nc = 11)
import math
import numpy as np
import matplotlib.pyplot as plt


def get_sum_x(x_list, degree):
    if not degree:
        return len(x_list)
    return sum(math.pow(x_value, degree) for x_value in x_list)


def get_a_by_Gauss(matrix_size, big_matrix):
    for main_index in range(matrix_size - 1):
        for i in range(main_index + 1, matrix_size):
            coefficient = big_matrix[i][main_index] / big_matrix[main_index][main_index]
            for j in range(main_index, matrix_size + 1):
                big_matrix[i][j] -= big_matrix[main_index][j] * coefficient

    result = [0] * matrix_size
    for i in range(matrix_size - 1, -1, -1):
        result[i] = big_matrix[i][matrix_size]
        for j in range(matrix_size - 1, i, -1):
            result[i] -= big_matrix[i][j] * result[j]
        result[i] /= big_matrix[i][i]
    return result


def get_F(x, y, degree):
    degree += 1
    a = [[0] * degree for i in range(degree)]
    for i in range(degree):
        for j in range(degree):
            a[i][j] = get_sum_x(x, j + i)
        a[i].append(sum(y[index] * math.pow(x[index], i) for index in range(len(x))))
    result = get_a_by_Gauss(degree, a)
    print(f'\n\t\tРезультат F_{degree - 1}(x):')
    for index in range(degree):
        print(f'a_{index + 1} = {round(result[index], 4)}')
    print(f'\tНевязка: '
          f'{round(sum((sum(result[i] * x[j] ** i for i in range(degree)) - y[j]) ** 2 for j in range(len(x))), 4)}')
    return result


def graphic(x, y, first_f, second_f):
    plt.figure(figsize=(10, 5))
    x_values = np.arange(x[0] - 1, x[-1] + 1.01, 0.01)
    plt.plot(x, y, 'ro')
    plt.plot(x_values, np.poly1d(list(reversed(first_f)))(x_values), label=r'$F_1(x)$')
    plt.plot(x_values, np.poly1d(list(reversed(second_f)))(x_values), label=r'$F_2(x)$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()


# x = [0, 1.7, 3.4, 5.1, 6.8, 8.5] # пример
# y = [0, 1.3038, 1.8439, 2.2583, 2.6077, 2.9155]

x = [-55, -33, -11, 11, 33]
y = [73, 51, 30, 11, -8]
graphic(x, y, get_F(x, y, 1), get_F(x, y, 2))



