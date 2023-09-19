# MyGrader - Your Own CS111 Grader

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_my-grader&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=AppleBoiy_my-grader) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_my-grader&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AppleBoiy_my-grader)

## Announcement: Archiving MyGrader Repository in Version 0.45

Dear MyGrader Community,

We want to inform you that in the upcoming version 0.45 of MyGrader, we will be archiving this repository. This decision has been made to transition our efforts toward a new project named ["CMS"](https://github.com/AppleBoiy/cms) (Contest Management System). We believe that CMS will offer an even more robust and versatile platform for testing and grading user-defined functions efficiently.

### Why the Transition?

The decision to archive MyGrader in version 0.45 is driven by our commitment to providing the best tools and solutions for students and developers working on programming assignments. CMS represents a significant step forward in terms of features, flexibility, and scalability. We're excited about the possibilities it brings to the table.

### What to Expect in Version 0.45?

In MyGrader version 0.45, you can expect the following:

- A final release with any pending bug fixes and improvements.
- Clear instructions on transitioning to CMS, including data migration guides if applicable.

### Transitioning to CMS

We encourage all MyGrader users to make a smooth transition to CMS once it becomes available. CMS will offer an easy migration process to ensure that you can continue testing and grading your user-defined functions seamlessly.

Stay tuned for updates on CMS and the official release announcement. We believe that CMS will be a valuable addition to your toolkit for testing and grading assignments.

We sincerely appreciate your support and contributions to MyGrader over the years. Your feedback and engagement have been invaluable in shaping our tools for the better. If you have any questions or concerns regarding this transition, please feel free to reach out to us through the CMS repository.

Thank you for being a part of the MyGrader community, and we look forward to serving you better with [CMS](https://github.com/AppleBoiy/cms).

Best regards,
**AppleBoiy**

## Usage

1. **Define Your User-Defined Function**

   Begin by defining the user-defined function you want to test. For example, let's say you have a
   function `calculate_new_price` that calculates the new price of an item after applying a discount:
    ```python
    def calculate_new_price(old_price):
        # ... (your code here) ...
        return new_price
    ```

2. **Use the Tester Class**

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

3. **View the Test Summary**

   After running the tests, you'll see a summary of the results. If you set `log_option` to `'print'`, the summary will
   be
   printed to the console. If you set it to `'write'`, the summary will be saved to a file named `test_summary.md`.

## Installation

Install the MyGrader package using pip:

```bash
pip install mygrader
```

## Attributes

- `year`: The year of class (Assignments are assigned by year).
- `runtime_limit`: The maximum runtime allowed for test cases (in seconds)
- `log_option`: The logging option ("print" or "write") for the test summary.
- `debug`: If `True`, enable debug mode for additional information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
