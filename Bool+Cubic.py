import numpy


def get_function_value(x):
    return numpy.e ** x


def method_bool(a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(0, n + 1):
        if i == 0 or i == n:
            res += 7 * get_function_value(a)
        if i % 2 != 0:
            res += 32 * get_function_value(a)
        if i % 2 == 0 and i % 4 != 0:
            res += 12 * get_function_value(a)
        if i % 4 == 0:
            res += 14 * get_function_value(a)
        a += h
    res *= (2 * h) / 45
    print(res)



def methol_parabol(a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(0, n+1):
        if i == 0 or i == n:
            res += 7 * get_function_value(a)
        if i % 2 != 0 and i % 3 != 0:
            res += 3 * get_function_value(a)
        if i % 2 == 0 and i % 3 != 0:
            res += 3 * get_function_value(a)
        if i % 3 == 0:
            res += 2 * get_function_value(a)
        a += h
    res *= (3 * h) / 8
    print(res)
    # 0 1 2 3 4 5 6 7 8 9 10 11 12
    # 1 3 3 2 3 3 2 3 3 2 3  3  1


if __name__ == "__main__":
    method_bool(40, 50, 10000)
    methol_parabol(40, 50, 10000)
