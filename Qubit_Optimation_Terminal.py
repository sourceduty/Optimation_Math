import numpy as np

def display_menu():
    print("\n====== Qubit Optimation Terminal v1.0 ======")
    print("1. Set Qubit Parameter θ_A")
    print("2. Set Qubit Parameter θ_B")
    print("3. Set Weight for θ_A (1-100)")
    print("4. Choose Quantum Optimation Formula")
    print("5. Compute Qubit Optimation")
    print("6. Help")
    print("7. Exit")
    print("==========================================")

def display_help():
    print("\n[Help] Qubit Optimation allows dynamic tuning of quantum gate parameters θ_A and θ_B.")
    print("Weights (1 to 100) represent relative influence of each parameter in balancing fidelity vs. efficiency.")
    print("Quantum-specific formulas include: weighted tuning, coherence balancing, exponential fidelity, and entanglement optimization.")

def get_integer_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and (value < min_val or value > max_val):
                raise ValueError
            return value
        except ValueError:
            print(f"Please enter a valid integer", end='')
            if min_val is not None:
                print(f" between {min_val} and {max_val}.")
            else:
                print(".")

def choose_formula():
    print("\nSelect a Qubit Optimation Formula:")
    print("1. Weighted Gate Tuning")
    print("2. Coherence Balancing (Half-Adding)")
    print("3. Exponential Fidelity Influence")
    print("4. Quadratic Entanglement Emphasis")
    return get_integer_input("Enter choice (1-4): ", 1, 4)

def compute_optimation(theta_A, theta_B, wA, formula):
    w = wA / 100
    if formula == 1:
        return theta_A * w + theta_B * (1 - w)
    elif formula == 2:
        return (theta_A + 0.5 * theta_A * w) + (theta_B - 0.5 * theta_B * (1 - w))
    elif formula == 3:
        return theta_A**w + theta_B**(1 - w)
    elif formula == 4:
        return w * theta_A**2 + (1 - w) * theta_B**2

theta_A = 1
theta_B = 2
wA = 50
formula = 1

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        theta_A = get_integer_input("Enter value for θ_A: ")
    elif choice == "2":
        theta_B = get_integer_input("Enter value for θ_B: ")
    elif choice == "3":
        wA = get_integer_input("Enter weight for θ_A (1-100): ", 1, 100)
    elif choice == "4":
        formula = choose_formula()
    elif choice == "5":
        result = compute_optimation(theta_A, theta_B, wA, formula)
        print(f"\nQubit Optimation Result: {result:.4f}")
    elif choice == "6":
        display_help()
    elif choice == "7":
        print("Exiting Qubit Optimation Terminal.")
        break
    else:
        print("Invalid option. Try again.")
