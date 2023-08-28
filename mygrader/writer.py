import csv


def write_failed_cases_to_csv(failed_cases, filename="failed_cases.csv"):
    """
    Write the list of failed cases to a CSV file.

    Parameters:
        failed_cases (list): List of dictionaries containing failed tests cases.
        filename (str, optional): The name of the output CSV file. Defaults to "failed_cases.csv".

    """
    with open(filename, "w", newline="") as file:
        fieldnames = ["Input", "Expected", "Got"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for failed_case in failed_cases:
            writer.writerow(
                {"Input": failed_case["Input"], "Expected": failed_case["Expected"], "Got": failed_case["Got"]})
