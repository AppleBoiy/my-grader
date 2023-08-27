# MyGrader - Your Own CS111 Grader

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_my-grader&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=AppleBoiy_my-grader) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_my-grader&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AppleBoiy_my-grader)

The **MyGrader** project is a custom testing framework designed to help you test your user-defined functions
efficiently. It generates test cases, runs them against your functions, and provides detailed summaries of the test
results. This can be particularly useful for students and developers working on programming assignments.

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
- [Attributes](#attributes)
- [Methods](#methods)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Project Information](#project-information)
- [Project Status](#project-status)
- [Project Classifiers](#project-classifiers)

## Usage

1. **Define Your User-Defined Function**

Begin by defining the user-defined function you want to test. For example, let's say you have a
function `calculate_new_price` that calculates the new price of an item after applying a discount:

```python
def calculate_new_price(old_price):
    # ... (your code here) ...
    return new_price
```

2. **Install MyGrader**

Install the MyGrader package using pip:

```bash
pip install mygrader
```

3. **Use the Tester Class**

Utilize the `Tester` class from MyGrader to test your function. Create a Python script (e.g., `test_my_function.py`)
with the following code:

```python
from mygrader import mygrader


# Define your user-defined function
def calculate_new_price(old_price):
    # ... (your code here) ...
    return new_price


if __name__ == '__main__':
    tester = mygrader.Tester(year=2023, runtime_limit=0.4, log_option="print")
    tester.run_test(calculate_new_price, num_test_cases=1000)
```

4. **View the Test Summary**

After running the tests, you'll see a summary of the results. If you set `log_option` to `'print'`, the summary will be
printed to the console. If you set it to `'write'`, the summary will be saved to a file named `test_summary.md`.

## Installation

Install the MyGrader package using pip:

```bash
pip install mygrader
```

## Attributes

- `year`: The year for which the tests are being run.
- `runtime_limit`: The maximum runtime allowed for a function.
- `log_option`: The logging option ("print" or "write") for the test summary.
- `debug`: If `True`, enable debug mode for additional information.

## Methods

- `run_test(user_func, num_test_cases=100, show_table=False)`: Run tests for the specified user-defined function.
- `return_type(func)`: Return the return type of a given function.
- `capture_printed_text(func, *args)`: Capture the printed output of a function.
- `__dir__()`: Return the list of available functions for the given year.
- `__repr__()`: Return a string representation of available functions for the given year.
- `__str__()`: Return a string representation of the Tester class for the given year.

## Examples

Here are a few examples to demonstrate how to use the `Tester` class:

```python
# Create a Tester object
tester = mygrader.Tester(year=2023, runtime_limit=2, log_option="print")


# Define the user-defined function to be tested
def square(x):
    return x ** 2


# Run tests on the user-defined function
tester.run_test(square, num_test_cases=50, show_table=True)
```

## Contributing

Contributions to the MyGrader project are welcome! If you encounter issues or have ideas for improvements, please open
an issue or submit a pull request on [GitHub](https://github.com/AppleBoiy/my-grader).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Information

- **Author:** AppleBoiy
- **GitHub Repository:** [MyGrader on GitHub](https://github.com/AppleBoiy/my-grader)

## Project Status

MyGrader is currently in the alpha development stage. It's actively being worked on and improved. Feel free to
contribute and help make it even better!

## Project Classifiers

- Development Status: 3 - Alpha
- Intended Audience: Developers
- License: MIT License
- Programming Language: Python 3.8, 3.9, 3.10, 3.11
