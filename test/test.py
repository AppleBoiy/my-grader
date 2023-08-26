from mygrader.TestUnit import Test


def func(a, b):
    result = 0
    for i in range(a, b + 1):
        result += i
    return result


if __name__ == '__main__':
    # Example usage:
    test_function_name = "calculate_sum"
    num_test_cases = 900_000
    options = "print"
    Test.run_test(test_function_name, num_test_cases, options, func)
