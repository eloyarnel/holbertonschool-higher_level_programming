#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result."""

    result = None

    try:
        result = a / b
        return result

    except Exception:
        return None

    finally:
        print("Inside result: {}".format(result))
