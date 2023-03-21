# Аппроксимация табличной функции кубическими сплайнами (Nг = Nc = 11)
import numpy as np
import matplotlib.pyplot as plt


def run_through(a, b, c, d):
    count = len(a)
    p, q = [-c[0] / b[0]], [d[0] / b[0]]
    for i in range(1, count):
        denominator = a[i] * p[i - 1] + b[i]
        p.append(-c[i] / denominator)
        q.append((d[i] - a[i] * q[i - 1]) / denominator)

    result = [0] * (count - 1) + [q[-1]]
    for i in range(count - 2, -1, -1):
        result[i] = p[i] * result[i + 1] + q[i]
    return result


def calculate(splines, x):
    correct_key = None
    for border in sorted(splines.keys()):
        if x >= border:
            correct_key = border
        else:
            break
    if correct_key is not None:
        return splines.get(correct_key)
    raise Exception(f"x = {x} не входит в границы отрезка!")


def interpolation(x, y):
    h = [x[i + 1] - x[i] for i in range(len(x) - 1)]
    a = [0.0] + [h_element / 6 for h_element in h[1:-1]]
    b = [(h[i] + h[i + 1]) / 3 for i in range(len(h) - 1)]
    c = a[1:] + [0]
    d = [(y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1] for i in range(1, len(h))]
    q = [0] + run_through(a, b, c, d) + [0]
    splines = dict()
    for i in range(1, len(q)):
        splines[x[i - 1]] = ((float(q[i]) * np.poly1d([1, -x[i - 1]]) ** 3 + float(q[i - 1]) * np.poly1d(
            [-1, x[i]]) ** 3) / 6 +
                             (float(y[i]) - float(q[i]) * h[i - 1] ** 2 / 6) * np.poly1d([1, -x[i - 1]]) +
                             (float(y[i - 1]) - float(q[i - 1]) * h[i - 1] ** 2 / 6) * np.poly1d([-1, x[i]])) / h[i - 1]
    return splines


x = [i for i in range(11, 16)]
y = [11*x_element+np.sin(x_element) for x_element in x]

# x = [i for i in range(-9, 10)]
# y = [x_element * np.sin(2 * x_element) for x_element in x]

splines = interpolation(x, y)
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'ro')
x_values = np.arange(x[0], x[-1] + 0.01, 0.01)
# plt.plot(x_values, x_values * np.sin(2 * x_values), label=r'$x*sin(2 * x)$')
plt.plot(x_values, 11*x_values+np.sin(x_values), label=r'$11*x+sin(x)$')
for i in range(len(x) - 1):
    x_values = np.arange(x[i], x[i + 1] + 0.01, 0.01)
    plt.plot(x_values, calculate(splines, x[i])(x_values))
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()
