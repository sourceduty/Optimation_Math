import numpy as np

def display_menu():
    print("\n====== Optimation Terminal v2.0 ======")
    print("1. Set Variable A")
    print("2. Set Variable B")
    print("3. Set Weight for A (1-100)")
    print("4. Choose Optimation Formula")
    print("5. Compute Optimation")
    print("6. Help")
    print("7. Exit")
    print("====================================")

def display_help():
    print("\n[Help] Optimation lets you balance A and B using weights from 1 to 100.")
    print("The weight of A is used to apply influence against B.")
    print("Formulas include: weighted sum, half-adding, exponential, and quadratic balance.")

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
    print("\nSelect an Optimation Formula:")
    print("1. Weighted Sum")
    print("2. Half-Adding")
    print("3. Exponential Weighting")
    print("4. Quadratic Balance")
    return get_integer_input("Enter choice (1-4): ", 1, 4)

def compute_optimation(A, B, wA, formula):
    w = wA / 100
    if formula == 1:
        return A * w + B * (1 - w)
    elif formula == 2:
        return (A + 0.5 * A * w) + (B - 0.5 * B * (1 - w))
    elif formula == 3:
        return A**w + B**(1 - w)
    elif formula == 4:
        return w * A**2 + (1 - w) * B**2

A = 10
B = 20
wA = 50
formula = 1

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        A = get_integer_input("Enter value for A: ")
    elif choice == "2":
        B = get_integer_input("Enter value for B: ")
    elif choice == "3":
        wA = get_integer_input("Enter weight for A (1-100): ", 1, 100)
    elif choice == "4":
        formula = choose_formula()
    elif choice == "5":
        result = compute_optimation(A, B, wA, formula)
        print(f"\nOptimation Result: {result:.2f}")
    elif choice == "6":
        display_help()
    elif choice == "7":
        print("Exiting.")
        break
    else:
        print("Invalid option. Try again.")
