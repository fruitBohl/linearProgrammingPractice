import pulp
from scipy.optimize import linprog
import numpy


def linearProblem():
    # put system of equations into arrays
    obj = [-1, -2]

    lhsIneq = [[2, 1], [-4, 5], [1, -2]]
    rhsIneq = [20, 10, 2]
    lhsEq = [[-1, 5]]
    rhsEq = 15

    # define bounds for each variable
    bounds = [(0, numpy.inf), (0, numpy.inf)]

    # optimize and output system
    opt = linprog(obj, lhsIneq, rhsIneq, lhsEq, rhsEq, bounds, "revised simplex")
    print(opt)


def resourceAllocationProblem():
    obj = [-20, -12, -40, -25]

    lhsIneq = [[1, 1, 1, 1], [3, 2, 1, 0], [0, 1, 2, 3]]
    rhsIneq = [50, 100, 90]

    opt = linprog(obj, lhsIneq, rhsIneq, "revised simplex")
    print(opt)


if __name__ == "__main__":
    resourceAllocationProblem()
