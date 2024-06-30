# main.py

import math_library


def main():
    try:
        # Basic arithmetic operations
        print("Addition: "+ str(math_library.add(5, 3)))
        print("Subtraction: "+ str(math_library.subtract(5, 3)))
        print("Multiplication: "+ str(math_library.multiply(5, 3)))
        print("Division: "+ str(math_library.divide(6, 3)))
        print("Modulus: "+ str(math_library.modulus(5, 3)))

        # Advanced mathematical operations
        print("Exponent: "+ str(math_library.exponentiate(2, 3)))
        print("Square Root: " + str(math_library.square_root(16)))

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
