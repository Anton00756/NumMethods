# Метод вращений Якоби (Nг = Nc = 11)
import math


def multiplication(a, b, matrix_size):
    end_matrix = [[0.0] * matrix_size for i in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                end_matrix[i][j] += a[i][k] * b[k][j]
    return end_matrix


def get_input_data(user_input, my_task=0):
    if user_input:
        try:
            matrix_size = int(input('Введите размер матрицы: '))
            if matrix_size < 2:
                print("\033[31mНекорректный размер матрицы [< 2]!\033[0m\n")
                raise Exception
            print('\tВведите матрицу (построчно):')
            matrix = [[float(element) for element in input().split(' ')] for i in range(matrix_size)]
            return matrix
        except Exception:
            print('Ошибка ввода. Заполнение стандартными данными')
    if my_task:
        if my_task == 1:
            return [[21.0, 11.0, 1.0], [11.0, 21.0, 3.0], [1.0, 3.0, 15.0]]
        else:
            return [[21.0, 11.0, 1.0, 1.0],
                    [11.0, 21.0, 2.0, 2.0],
                    [1.0, 2.0, 15.0, 1.0],
                    [1.0, 1.0, 1.0, 22.0]]
    return [[17.0, 1.0, 1.0], [1.0, 17.0, 2.0], [1.0, 2.0, 4.0]]


matrix = get_input_data(user_input=False, my_task=2)
precision = 0.00001

count = len(matrix)
result_matrix = None
while True:
    max_i, max_j = max([max([(abs(matrix[i][j]), i, j) for j in range(i + 1, count)], key=lambda el: el[0])
                        for i in range(count - 1)], key=lambda el: el[0])[1:]
    rotation_matrix = [[0.0] * count for i in range(count)]
    for i in range(count):
        rotation_matrix[i][i] = 1.0
    if matrix[max_i][max_i] == matrix[max_j][max_j]:
        angle = math.pi / 4 if matrix[max_i][max_j] > 0 else -math.pi / 4
    else:
        angle = 0.5 * math.atan(2 * matrix[max_i][max_j] / (matrix[max_i][max_i] - matrix[max_j][max_j]))
    rotation_matrix[max_i][max_j] = -math.sin(angle)
    rotation_matrix[max_j][max_i] = math.sin(angle)
    rotation_matrix[max_i][max_i] = rotation_matrix[max_j][max_j] = math.cos(angle)

    reversed_matrix = [element.copy() for element in rotation_matrix]
    for i in range(count - 1):
        for j in range(i + 1, count):
            reversed_matrix[i][j], reversed_matrix[j][i] = reversed_matrix[j][i], reversed_matrix[i][j]

    result = multiplication(multiplication(reversed_matrix, matrix, count), rotation_matrix, count)
    matrix = [element.copy() for element in result]

    if result_matrix is None:
        result_matrix = [element.copy() for element in rotation_matrix]
    else:
        result_matrix = multiplication(result_matrix, rotation_matrix, count)

    calc_E = math.sqrt(sum(sum(matrix[i][j] * matrix[i][j] for j in range(i + 1, count)) for i in range(count - 1)))
    if calc_E < precision:
        break

print('\t\tРезультат:')
for index in range(count):
    print(f'λ_{index + 1} = {matrix[index][index]}, вектор: '
          f'{[result_matrix[j][index]/result_matrix[index][index] for j in range(count)]}')
