from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, GLPK


def display(status, model):
    # display results
    print(f"status: {status}, {LpStatus[status]}")
    print(f"objective: {model.objective.value()}\n")

    for var in model.variables():
        print(f"{var.name}: {var.value()}")
    print("\n")

    for name, constraint in model.constraints.items():
        print(f"{name}: {constraint.value()}")


def systemSolve():
    # Create model
    model = LpProblem("small-problem", LpMaximize)

    # Initialize the decision variables
    x = LpVariable("x", 0)
    y = LpVariable("y", 0)

    expression = 2 * x + 4 * y
    constraint = 2 * x + 4 * y >= 8

    # Add the constraints to the model
    model += (2 * x + y <= 20, "red_constraint")
    model += (4 * x - 5 * y >= -10, "blue_constraint")
    model += (-x + 2 * y >= -2, "yellow_constraint")
    model += (-x + 5 * y == 15, "green_constraint")

    # Add the objective function to the model
    model += x + 2 * y

    # solve the problem
    status = model.solve()

    # display results
    display(status, model)


def mixedIntegerSystemSolve():
    # Create the model
    model = LpProblem("small-problem", LpMaximize)

    # Initialize the decision variables: x is integer, y is continuous
    x = LpVariable("x", 0, None, "Integer")
    y = LpVariable("y", 0)

    # Add the constraints to the model
    model += (2 * x + y <= 20, "red_constraint")
    model += (4 * x - 5 * y >= -10, "blue_constraint")
    model += (-x + 2 * y >= -2, "yellow_constraint")
    model += (-x + 5 * y == 15, "green_constraint")

    # Add the objective function to the model
    model += x + 2 * y

    # Solve the problem
    status = model.solve()

    # display results
    display(status, model)


def resourceAllocation():
    # Define the model
    model = LpProblem("resource-allocation", LpMaximize)

    # Define the decision variables
    x = {i: LpVariable(f"x{i}", 0) for i in range(1, 5)}
    y = {i: LpVariable(f"y{i}", None, None, "Binary") for i in (1, 3)}

    # Add constraints
    model += (lpSum(x.values()) <= 50, "manpower")
    model += (3 * x[1] + 2 * x[2] + x[3] <= 100, "material_a")
    model += (x[2] + 2 * x[3] + 3 * x[4] <= 90, "material_b")

    M = 100
    model += (x[1] <= y[1] * M, "x1_constraint")
    model += (x[3] <= y[3] * M, "x3_constraint")
    model += (y[1] + y[3] <= 1, "y_constraint")

    # Set the objective
    model += 20 * x[1] + 12 * x[2] + 40 * x[3] + 25 * x[4]

    # Solve the optimization problem
    status = model.solve()

    # Get the results
    display(status, model)


if __name__ == "__main__":
    resourceAllocation()
