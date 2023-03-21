# Вычисление 1-й и 2-й производной от таблично заданной функции (Вариант 11)


point_x = 1
x = [0, 0.5, 1, 1.5, 2]
y = [1, 1.3776, 1.5403, 1.5707, 1.5839]

index = x.index(point_x)
h = x[1] - x[0]
print(f'1-я производная (левая) в точке x = {point_x}: {round((y[index] - y[index - 1]) / h, 4)}')
print(f'1-я производная (правая) в точке x = {point_x}: {round((y[index + 1] - y[index]) / h, 4)}')
print(f'1-я производная (центральная) в точке x = {point_x}: {round((y[index + 1] - y[index - 1]) / (2 * h), 4)}')
print(f'2-я производная в точке x = {point_x}: {round((y[index + 1] - 2 * y[index] + y[index - 1]) / h ** 2, 4)}')
