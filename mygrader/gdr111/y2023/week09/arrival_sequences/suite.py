import time
import unittest

from tabulate import tabulate

from template import MARKDOWN_FILENAME, MARKDOWN_TEMPLATE_FILE


# Measure the time and run a test function
def run_test(func, left_lane, right_lane):
    start_time = time.perf_counter()
    expected = func(left_lane, right_lane)
    elapsed_time = time.perf_counter() - start_time
    return expected, elapsed_time


def run_tests(module):
    start_time = time.time()  # Record the start time
    test_program = unittest.TestProgram(module=module, exit=False)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time

    test_result = test_program.result

    print("Test Results:")
    print(f"Total tests run: {test_result.testsRun}")
    print(f"Number of failures: {len(test_result.failures)}")
    print(f"Number of errors: {len(test_result.errors)}")
    print(f"Number of skipped tests: {len(test_result.skipped)}")
    print(f"Number of successful tests: {test_result.testsRun - len(test_result.failures) - len(test_result.errors)}")
    print(f"Total Test Execution Time: {elapsed_time:.5f} seconds")

    if len(test_result.failures) > 0:
        print("\nFailed Tests:")
        for test_case, failure in test_result.failures:
            print(f"Test Case: {test_case}")
            print("Failure:", failure)

    if len(test_result.errors) > 0:
        print("\nErrors in Tests:")
        for test_case, error in test_result.errors:
            print(f"Test Case: {test_case}")
            print("Error:", error)

    print("\nTest Summary:")
    if len(test_result.failures) == 0 and len(test_result.errors) == 0:
        print("All tests passed!")
    else:
        print("Some tests failed or encountered errors.")


# Add failed cases to the list
def add_failed_case(failed_cases, expected, result, left_lane, right_lane):
    for case in expected:
        if case not in result:
            failed_cases.append((left_lane, right_lane, case, 'not found'))
            break
    for case in result:
        if case not in expected:
            failed_cases.append((left_lane, right_lane, 'not found', case))
            break


# Generate a summary table using tabulate
def generate_summary_table(failed_cases, headers):
    return tabulate(failed_cases[:10], headers=headers, tablefmt="pipe")


# Generate the complete summary in Markdown format
def generate_summary_markdown(info):
    with open(MARKDOWN_TEMPLATE_FILE, 'r') as template_file:
        markdown_template = template_file.read()

    headers = ["Left Lane", "Right Lane", "Expected", "Result"]
    failed_cases_table = generate_summary_table(info['failed_cases'], headers)

    summary = markdown_template.format(
        failed_cases_table=failed_cases_table,
        passed=info['passed'],
        failed=info['failed'],
        average_time_expected=info['average_time_expected'],
        average_time_result=info['average_time_result'],
        total_time_expected=info['total_time_expected'],
        total_time_result=info['total_time_result'],
        expected_ratio=info['total_time_result'] / info['total_time_expected']
    )
    return summary


# Print or write the summary with error handling
def print_summary(info, output_option='print'):
    try:
        if output_option == 'None':
            return

        summary = generate_summary_markdown(info)

        if output_option == 'print':
            print(summary)
        elif output_option == 'write':
            with open(MARKDOWN_FILENAME, 'w') as markdown_file:
                markdown_file.write(summary)
        else:
            raise ValueError(f"Invalid output option: {output_option}")

    except Exception as e:
        print(f"An error occurred: {e}")
