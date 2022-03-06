import math


def boolesrule(func,a, b, n):
    h = (b - a) / n
    sum = 0
    bl = ((7 * func(a) + 32 * func(a + h) + 12 * func(a + 2 * h) +
            32 * func(a + 3 * h) + 7 * func(a + 4 * h)) * 2 * h / 45)
    sum += bl
    print(sum)


if __name__ == '__main__':
    boolesrule(lambda x: math.e ** x,1, 5, 4)