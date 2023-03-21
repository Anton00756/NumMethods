# Метод прогонки (Nг = Nc = 11)


def get_input_data(user_input, my_task=0):
    if user_input:
        try:
            count = int(input('Введите N: '))
            if count < 2:
                print("\033[31mНекорректное N [< 2]!\033[0m\n")
                raise Exception
            print('\tВведите A, B, C, D (построчно):')
            A, B, C, D = [], [], [], []
            for i in range(count):
                input_string = input().split()
                if not i:
                    input_string.insert(0, '0')
                elif i == count - 1:
                    input_string.insert(2, '0')
                A.append(float(input_string[0]))
                B.append(float(input_string[1]))
                C.append(float(input_string[2]))
                D.append(float(input_string[3]))
            return count, A, B, C, D
        except Exception:
            print('Ошибка ввода. Заполнение стандартными данными')
    if my_task:
        count = 5
        if my_task == 2:
            count = 10
        A, B, C, D = [], [], [], []
        for i in range(1, count + 1):
            A.append((i + 1) * 11)
            B.append(11 * (i * i + 1))
            C.append(11 * (1 - i))
            D.append(11 * (1 + i))
        A[0] = C[-1] = 0
        return count, A, B, C, D
    return 4, [0, -1, 2, -1], [8, 6, 10, 6], [-2, -2, -4, 0], [6, 3, 8, 5]


count, A, B, C, D = get_input_data(user_input=False, my_task=2)
P, Q = [-C[0] / B[0]], [D[0] / B[0]]
for i in range(1, count):
    denominator = A[i] * P[i-1] + B[i]
    P.append(-C[i] / denominator)
    Q.append((D[i] - A[i] * Q[i-1]) / denominator)

result = [0] * (count - 1) + [Q[-1]]
for i in range(count - 2, -1, -1):
    result[i] = P[i] * result[i + 1] + Q[i]

print('\n\t\tРезультат:')
for index in range(count):
    print(f'x_{index + 1} = {round(result[index], 3)}')
