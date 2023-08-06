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
