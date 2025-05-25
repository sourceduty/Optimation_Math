from optimation import Model, Variable, Objective, minimize

# Step 1: Define a model
model = Model()

# Step 2: Define variable(s)
x = Variable(name="x")

# Step 3: Define the objective
objective = Objective((x - 3)**2)

# Step 4: Add the objective to the model
model.objective = minimize(objective)

# Step 5: Solve the model
solution = model.solve()

# Step 6: Display the result
print(f"Optimal value of x: {solution.variable_values['x']}")
print(f"Minimum value of the function: {solution.objective_value}")
