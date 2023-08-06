# Test Results and Failed Cases

This Python script provides functions to display test results and record failed test cases. It includes two functions:

1. `print_test_results`: This function prints the number of test cases passed and the list of failed test cases. If there are more than 10 failed cases, it displays detailed information for each failed case.

2. `write_failed_cases_to_file`: This function writes the list of failed cases to a file specified by the user. By default, it creates a file named `failed_cases.txt`.

## Usage

```python
    # Import the functions
from src.mygrader import print_test_results, write_failed_cases_to_file

# Example usage
# Assuming you have a list of failed test cases named 'failed_cases'
num_passed = 90
num_failed = 10
failed_cases = [
    ("input_1", "expected_1", "got_1"),
    ("input_2", "expected_2", "got_2"),
    ("input_3", "expected_3", "got_3"),
    ("input_4", "expected_4", "got_4"),
    ("input_5", "expected_5", "got_5"),
]

# Call the function to print the results and write failed cases to a file
print_test_results(num_passed, num_failed, failed_cases)

write_failed_cases_to_file(failed_cases, "custom_failed_cases.txt")

```

## Function Descriptions

### `print_test_results(num_passed, num_failed, failed_cases)`

Prints the test results and returns the list of failed cases.

**Parameters:**

- `num_passed` (int): Number of test cases passed.
- `num_failed` (int): Number of test cases failed.
- `failed_cases` (list): List of tuples containing failed test cases.

**Returns:**

A list of dictionaries containing failed test cases.

### `write_failed_cases_to_file(failed_cases, filename="failed_cases.txt")`

Writes the list of failed cases to a file.

**Parameters:**

- `failed_cases` (list): List of dictionaries containing failed test cases.
- `filename` (str, optional): The name of the output file. Defaults to "failed_cases.txt".

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.