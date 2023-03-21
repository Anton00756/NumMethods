# Метод простых итераций (Nг = Nc = 11)
import math


def get_input_data(user_input, my_task=0):
    if user_input:
        try:
            matrix_size = int(input('Введите размер матрицы: '))
            if matrix_size < 2:
                print("\033[31mНекорректный размер матрицы [< 2]!\033[0m\n")
                raise Exception
            print('\tВведите матрицу (построчно):')
            matrix = [[float(element) for element in input().split(' ')] for i in range(matrix_size)]
            vector = [float(element) for element in input('\tВведите вектор:\n').split()]
            return matrix, vector
        except Exception:
            print('Ошибка ввода. Заполнение стандартными данными')
    if my_task:
        if my_task == 1:
            return [[21.0, 11.0, 1.0], [11.0, 21.0, 3.0], [1.0, 3.0, 15.0]], [11.0, 21.0, 0.0]
        else:
            return [[21.0, 11.0, 1.0, 1.0],
                    [11.0, 21.0, 2.0, 2.0],
                    [1.0, 2.0, 15.0, 1.0],
                    [1.0, 1.0, 1.0, 22.0]], [11.0, 21.0, 0.0, 1.0]
    return [[20.0, 4.0, -8.0], [-3.0, 15.0, 5.0], [6.0, 3.0, -18.0]], [1.0, -2.0, 3.0]


matrix, vector = get_input_data(user_input=False, my_task=2)
precision = 0.01

count = len(matrix)
for i in range(count):
    element = matrix[i][i]
    for j in range(count):
        matrix[i][j] /= -element
    vector[i] /= element
    matrix[i][i] = 0

norm_values = [[1, max(sum(abs(element) for element in string) for string in matrix)], [2, 0],
               [3, math.sqrt(sum(sum(element * element for element in string) for string in matrix))]]
for i in range(count):
    column_sum = 0
    for j in range(count):
        column_sum += abs(matrix[j][i])
    norm_values[1][1] = max(norm_values[1][1], column_sum)
norm_values = min(norm_values, key=lambda el: el[0])
matrix_norm = norm_values[1]

coefficient = 0
if matrix_norm < 1:
    if norm_values[0] == 1:
        coefficient = max(abs(element) for element in vector)
    elif norm_values[0] == 2:
        coefficient = sum(abs(element) for element in vector)
    else:
        coefficient = math.sqrt(sum(element * element for element in vector))
    coefficient /= (1 - matrix_norm)

x = vector.copy()
while True:
    new_x = vector.copy()
    for i in range(count):
        for j in range(count):
            if i != j:
                new_x[i] += matrix[i][j] * x[j]
    if matrix_norm < 1:
        coefficient *= matrix_norm
    else:
        sub_x = [new_x[i] - x[i] for i in range(len(x))]
        coefficient = min(max(abs(element) for element in sub_x), sum(abs(element) for element in sub_x),
                          math.sqrt(sum(element * element for element in sub_x)))
    if coefficient < precision:
        break
    x = new_x.copy()


print('\t\tРезультат:')
for index in range(count):
    print(f'x_{index + 1} = {x[index]}')
