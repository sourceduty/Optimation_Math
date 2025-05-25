import unittest
import optimation

class TestOptimationModel(unittest.TestCase):
    def test_simple_minimization(self):
        # Create variables
        x = optimation.Variable("x", value=10)
        y = optimation.Variable("y", value=20)

        # Define the objective function
        def total(variables):
            return sum(var.value for var in variables)

        # Build model
        model = optimation.Model()
        model.add_variable(x)
        model.add_variable(y)
        model.add_objective(optimation.Objective(total, sense="minimize"))

        # Execute solver
        result = optimation.minimize(model)

        # Assertions
        self.assertIn("minimize", result)
        self.assertEqual(result["minimize"], 30)

if __name__ == '__main__':
    unittest.main()
