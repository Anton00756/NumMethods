# Метод Гаусса (Nг = Nc = 11)


def get_input_data(user_input, my_task=0):
    if user_input:
        try:
            matrix_size = int(input('Введите размер матрицы: '))
            if matrix_size < 2:
                print("\033[31mНекорректный размер матрицы [< 2]!\033[0m\n")
                raise Exception
            print('\tВведите матрицу (построчно):')
            big_matrix = [[float(element) for element in input().split(' ')] for i in range(matrix_size)]
            input_string = input('\tВведите вектор:\n').split()
            for i in range(matrix_size):
                big_matrix[i].append(float(input_string[i]))
            return matrix_size, big_matrix
        except Exception:
            print('Ошибка ввода. Заполнение стандартными данными')
    if my_task:
        if my_task == 1:
            return 3, [[11.0, 5.0, 2.0, 1.0],
                       [5.0, 11.0, -11.0, 11.0],
                       [2.0, -11.0, 11.0, -11.0]]
        else:
            return 4, [[16.0, 0.0, 11.0, 11.0, 2],
                       [3.0, 3.0, 0.0, 11.0, 2],
                       [2.0, 5.0, 3.0, 11.0, 2],
                       [11, 22.0, 11.0, 1.0, 11]]
    return 3, [[10.0, 1.0, 1.0, 12.0],
               [2.0, 10.0, 1.0, 13.0],
               [2.0, 2.0, 10.0, 14.0]]


matrix_size, big_matrix = get_input_data(user_input=False, my_task=2)
for main_index in range(matrix_size - 1):
    for i in range(main_index + 1, matrix_size):
        coefficient = big_matrix[i][main_index] / big_matrix[main_index][main_index]
        for j in range(main_index, matrix_size + 1):
            big_matrix[i][j] -= big_matrix[main_index][j] * coefficient

print('\t\tРасширенная матрица после прямого хода:')
string_matrix = [[str(round(float(element), 3)) for element in row] for row in big_matrix]
lens = [max(map(len, col)) for col in zip(*string_matrix)]
fmt = '\t\t'.join(f'{{:{length}}}' for length in lens)
table = [fmt.format(*row) for row in string_matrix]
print('\n'.join(table))

result = [0] * matrix_size
for i in range(matrix_size - 1, -1, -1):
    result[i] = big_matrix[i][matrix_size]
    for j in range(matrix_size - 1, i, -1):
        result[i] -= big_matrix[i][j] * result[j]
    result[i] /= big_matrix[i][i]

print('\n\t\tРезультат:')
for index in range(matrix_size):
    print(f'x_{index + 1} = {round(result[index], 3)}')
