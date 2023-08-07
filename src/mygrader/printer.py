
def print_test_results(num_passed, num_failed, failed_cases):
    """
    Print the test results and return the list of failed cases.

    Parameters:
        num_passed (int): Number of test cases passed.
        num_failed (int): Number of test cases failed.
        failed_cases (list): List of tuples containing failed test cases.

    Returns:
        list: List of dictionaries containing failed test cases.

    """
    print(f"{num_passed} test cases passed.")


    if num_failed > 0:
        print(f"{num_failed} test cases failed.")

        for i, failed_case in enumerate(failed_cases, start=1):
            if i > 10:
                break

            print(f"{i}. Input: {failed_case[0]}, Expected: {failed_case[1]}, Got: {failed_case[2]}")

    else:
        print("All test cases passed successfully.")

    return [
        {"Input": case[0], "Expected": case[1], "Got": case[2]} for case in failed_cases
    ]


def write_failed_cases_to_file(failed_cases, filename="failed_cases.txt"):
    """
    Write the list of failed cases to a file.

    Parameters:
        failed_cases (list): List of dictionaries containing failed test cases.
        filename (str, optional): The name of the output file. Defaults to "failed_cases.txt".

    """
    with open(filename, "w") as file:
        for i, failed_case in enumerate(failed_cases, start=1):
            file.write(f"{i}. Input: {failed_case['Input']}, Expected: {failed_case['Expected']}, Got: {failed_case['Got']}\n")
