from typing import List, Tuple

from .writer import write_failed_cases_to_file


def print_test_results(num_passed: int, num_failed: int, failed_cases: List[Tuple], write_on_file: bool = False):
    """
    Print the test results and return the list of failed cases.

    Parameters:
        :param num_passed: Number of test cases passed.
        :param num_failed: Number of test cases failed.
        :param failed_cases: List of tuples containing failed test cases.
        :param write_on_file:

    Returns:
        list: List of dictionaries containing failed test cases.

    """
    print(f"{num_passed} test cases passed.")

    failed_cases_list = []

    if num_failed > 0:
        print(f"{num_failed} test cases failed.")

        for i, failed_case in enumerate(failed_cases, start=1):
            if i < 10:
                print(f"{i}. Input: {failed_case[0]}, Expected: {failed_case[1]}, Got: {failed_case[2]}")
            failed_cases_list.append(
                {"Input": failed_cases[i][0], "Expected": failed_case[i][1], "Got": failed_cases[i][2]}
            )

        if write_on_file:
            write_failed_cases_to_file(failed_cases_list)


    else:
        print("All test cases passed successfully.")
