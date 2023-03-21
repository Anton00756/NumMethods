# Метод дихотомии, метод итераций, метод Ньютона (Nг = Nc = 11)
import numpy as np
import matplotlib.pyplot as plt


def graphic(method=''):
    if method == '':
        return
    global coefficients
    x = np.arange(-30, 30.01, 0.01)
    plt.figure(figsize=(10, 5))
    plt.plot(x, (x / 11) ** 3 - x / 11 + 1 / 11, label=r'$f(x) = \left(\frac{x}{11}\right)^{3}-\frac{x}{'
                                                       r'11}+\frac{1}{11}$')
    plt.plot(np.roots(coefficients), [0] * (len(coefficients) - 1), 'ro', label=r'$f(x) = 0$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)

    if method == 'i':
        equal_x = np.arange(-11.8, -11.39, 0.01)
        plt.plot(equal_x, equal_func(equal_x), label=r"$\phi(x) = \sqrt[3]{121x-121}$")
        plt.plot(equal_x, 121/(3 * np.cbrt((121 * equal_x - 121) ** 2)), label=r"$\phi'(x) = \frac{121}{3\cdot\sqrt[3]"
                                                                               r"{\left(121x-121\right)^{2}}}$")
        plt.legend(loc='best', fontsize=12)
    elif method == 'n':
        derivative_x = np.arange(10, 12.01, 0.01)
        plt.plot(derivative_x, np.poly1d(coefficients).deriv()(derivative_x),
                 label=r"$f'(x) = 0.002254*x^2 - 0.09091$")
        plt.legend(loc='best', fontsize=12)
        x = 0
        new_x = 12
        while not abs(new_x - x) < E:
            x = new_x
            y = function(x)
            new_x = x - (y / first_derivative(x))
            plt.plot([x, new_x], [y, 0])
            plt.plot([new_x, new_x], [0, function(new_x)], linestyle='dashed')
    plt.show()


def function(x):
    return np.poly1d(coefficients)(x)


def dichotomy(a, b):
    global E
    print('\n\t\tМетод дихотомии:')
    if function(a) * function(b) > 0:
        print(f'Некорректные a и b: {a}, {b}')
        return
    in_a, in_b = a, b
    while not abs(a - b) < 2 * E:
        fa = function(a)
        mid_x = (a + b) / 2
        mid_y = function(mid_x)
        if not mid_y:
            break
        elif fa * mid_y < 0:
            b = mid_x
        else:
            a = mid_x
    print(f"a = {a}; b = {b}")
    print(f"f(x) = 0 в [{in_a}; {in_b}] при x = {(a + b) / 2}")


def equal_func(x):
    return np.cbrt(121*x - 121)


def iteration(a, b):
    global E
    print('\n\t\tМетод итераций:')
    q = 0.33
    e_coefficient = q/(1 - q)
    x = 0
    new_x = (a + b) / 2
    while not abs(new_x - x)*e_coefficient < E:
        x = new_x
        new_x = equal_func(x)
    print(f"f(x) = 0 в [{a}; {b}] при x = {new_x}")


def first_derivative(x):
    global coefficients
    return np.poly1d(coefficients).deriv()(x)


def second_derivative(x):
    global coefficients
    return np.poly1d(coefficients).deriv(2)(x)


def newton(a, b):
    print('\n\t\tМетод Ньютона (касательных):')
    if not function(a) * function(b) < 0 or not function(b) * second_derivative(b) > 0:
        print("Не выполняется условие сходимости!")
        return
    x = 0
    new_x = b
    while not abs(new_x - x) < E:
        x = new_x
        y = function(x)
        new_x = x - (y / first_derivative(x))
    print(f"f(x) = 0 в [{a}; {b}] при x = {new_x}")


E = 0.001
coefficients = [1 / (11 ** 3), 0, -1 / 11, 1 / 11]  # "(x/11)^3-x/11+1/11"
print(np.roots(coefficients))
dichotomy(-15, -10)
iteration(-11.8, -11.4)
newton(10, 12)
graphic('n')
