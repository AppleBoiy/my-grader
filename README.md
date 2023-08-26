# MyGrader - Your Own CS111 Grader

The **MyGrader** project is a custom testing framework designed to help you test your user-defined functions
efficiently. It generates test cases, runs them against your functions, and provides detailed summaries of the test
results. This can be particularly useful for students and developers working on programming assignments.

## Installation

To install MyGrader, you can use `pip`:

```bash
pip install mygrader
```

MyGrader has a set of dependencies that will be automatically installed.

## Usage

1. **Define Your User-Defined Function**

Begin by defining the user-defined function you want to test. For example, let's say you have a
function `calculate_new_price`
that calculates the new price of an item after applying a discount:

```python
def calculate_new_price(old_price):
    # ... (your code here) ...
    return new_price
```

2. **Use the Tester Class**

Utilize the `Tester` class from MyGrader to test your function. Create a Python script (e.g., `test_my_function.py`)
with the
following code:

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

3. **View the Test Summary**

After running the tests, you'll see a summary of the results. If you set `log_option` to `'print'`, the summary will be
printed
to the console. If you set it to `'write'`, the summary will be saved to a file named `test_summary.md`.

## Contributing

Contributions to the MyGrader project are welcome! If you encounter issues or have ideas for improvements, please open
an
issue or submit a pull request on [GitHub](https://github.com/AppleBoiy/my-grader).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Information

- **Author:** AppleBoiy
- **GitHub Repository:** [MyGrader on GitHub](https://github.com/AppleBoiy/my-grader)

## Project Status

MyGrader is currently in the alpha development stage. It's actively being worked on and improved. Feel free to
contribute and
help make it even better!

## Project Classifiers

- Development Status: 3 - Alpha
- Intended Audience: Developers
- License: MIT License
- Programming Language: Python 3.8, 3.9, 3.10, 3.11