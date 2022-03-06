import unittest
from main import numerical_derivative_X, analytic_derivative_X, numerical_derivative_Y, analytic_derivative_Y

EPS = 10e-7


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_derivatives_x_01():
        point_x = 1
        point_y = 3
        step = 0.001
        assert (numerical_derivative_X(point_x, point_y, step) - analytic_derivative_X(point_x, point_y)) <= EPS

    @staticmethod
    def test_derivatives_y_01():
        point_x = 1
        point_y = 3
        step = 0.001
        assert (numerical_derivative_Y(point_x, point_y, step) - analytic_derivative_Y(point_x, point_y)) <= EPS

    @staticmethod
    def test_derivatives_xy_01():
        point_x = 1
        point_y = 3
        step = 0.001
        assert (numerical_derivative_X(point_x, point_y, step) + analytic_derivative_X(point_x, point_y) !=
                numerical_derivative_Y(point_x, point_y, step) + analytic_derivative_Y(point_x, point_y))


if __name__ == '__main__':
    unittest.main()
