"""Factorial program - computes the factorial of a non-negative integer."""

def factorial(n: int) -> int:
    """Compute n! (n factorial).

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    """Run the factorial program from command-line input."""
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <non-negative-integer>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        sys.exit(1)
    print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()
