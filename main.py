import numpy as np
import matplotlib.pyplot as plt


def numerical_derivative_X(x, y, step):
    return (function(x + step, y) - function(x - step, y)) / (2 * step)


def numerical_derivative_Y(x, y, step):
    return (function(x, y + step) - function(x, y - step)) / (2 * step)


def function(x, y):
    return (np.sin(x**2)/y) + (np.cos(y*x)/y) + np.log(x)/5


def analytic_derivative_X(x, y):
    return (2*x*np.cos(x**2)/y)-np.sin(y*x)+1/(5*x)


def analytic_derivative_Y(x, y):
    return (-x * y * np.sin(x * y) - np.cos(x * y) - np.sin(x ** 2)) / y ** 2


def gradient_length(derivative_X, derivative_Y):
    return np.sqrt(derivative_X ** 2 + derivative_Y ** 2)


def draw_function():
    x = np.arange(1.0, 5.0, 0.01)
    y = x
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = function(x_grid, y_grid)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_grid, y_grid, z_grid, rstride=10, cstride=10, cmap='gnuplot2')
    ax.set(xlabel='x', ylabel='y', zlabel='z')
    plt.show()


if __name__ == "__main__":
    step = 0.001
    point_x = 2.5784
    point_y = 3.9564

    print("Numerical derivative X: ", numerical_derivative_X(point_x, point_y, step))
    print("Analytic derivative X: ", analytic_derivative_X(point_x, point_y))
    print("Numerical derivative Y: ", numerical_derivative_Y(point_x, point_y, step))
    print("Analytic derivative Y: ", analytic_derivative_Y(point_x, point_y))
    print("Gradient: ", gradient_length(analytic_derivative_X(point_x, point_y), analytic_derivative_Y(point_x, point_y)))

    draw_function()

