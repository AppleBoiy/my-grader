from typing import List, Tuple
from tabulate import tabulate

from .writer import write_failed_cases_to_csv


def print_test_results(num_passed: int, num_failed: int, failed_cases: List[Tuple], write_on_file: bool = False):
    """
    Print the tests results as a table using the tabulate package and return the list of failed cases.

    Parameters:
        :param num_passed: Number of tests cases passed.
        :param num_failed: Number of tests cases failed.
        :param failed_cases: List of tuples containing failed tests cases.
        :param write_on_file: Whether to write the failed cases to a file.

    Returns:
        list: List of dictionaries containing failed tests cases.

    """
    table_headers = ["Input", "Expected", "Got"]
    table_data = []

    # Write the first 100 failed cases to a file
    if write_on_file:
        num_to_write = min(100, num_failed)
        failed_cases_list = [{"Input": case[0], "Expected": case[1], "Got": case[2]} for case in
                             failed_cases[:num_to_write]]
        write_failed_cases_to_csv(failed_cases_list)

    # Print only the first 10 failed cases
    num_to_print = min(10, num_failed)
    for i, case in enumerate(failed_cases[:num_to_print], start=1):
        table_data.append([case[0], case[1], case[2]])

    table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid")

    if num_failed > 0:
        print(table)
        if num_failed > 10:
            print(f"... and {num_failed - num_to_print} more cases not shown.")
        print(f"Total tests cases: {num_passed + num_failed}")
        print(f"Passed: {num_passed} | Failed: {num_failed}")
    else:
        print("All tests cases passed successfully.")
