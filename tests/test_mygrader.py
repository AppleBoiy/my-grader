import contextlib
import io

import pytest

from mygrader import Tester


def calculate_sum(x: int, y: int) -> int:
    """
        Calculates the sum of a sequence of numbers.

        Given two numbers, x and y, this function calculates the sum of the sequence
        of numbers starting from x and ending at y, inclusive, using the formula for
        the sum of an arithmetic series.

        Parameters:
        - x: Starting number of the sequence
        - y: Ending number of the sequences

        Returns:
        The sum of the sequence.
        """
    summation = int((x + y) * ((y - x + 1) / 2))
    return summation


class TestMyGrader:
    def test_import(self):
        modules = [
            'mygrader', 'mygrader', 'mygrader.printer', 'mygrader.template', 'mygrader.writer',
            'mygrader.template.log_template', 'mygrader.src', 'mygrader.src.y2023',

        ]
        passed_modules = []

        for module_name in modules:
            try:
                __import__(module_name)
                passed_modules.append(module_name)
            except ImportError:
                assert False, f'Failed to import {module_name}'

        assert True

    def test_create_tester(self):
        try:
            Tester(2023)
        except Exception as e:
            assert False, f"Failed to create Tester object: {e}"
        assert True, "Successfully created Tester object"

    def test_run_test(self):
        tester = Tester(2023, debug=True)
        try:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                tester.run_test(calculate_sum)

        except Exception as e:
            assert False, f"Failed to run test: {e}"
        assert True

    def test_run_test_with_runtime_limit(self):
        tester = Tester(2023, runtime_limit=0.1, debug=True)

        try:
            buffer = io.StringIO()
            with contextlib.redirect_stderr(buffer):
                # Run the test cases with the sphere_volume function from Solution class
                tester.run_test(calculate_sum, num_test_cases=1000000)

            # If the code execution completes within the time limit, this point is reached
            assert False, "Failed to raise exception when runtime limit is exceeded"

        except TimeoutError:  # Catch the TimeoutError exception raised when the runtime limit is exceeded
            assert True  # Assertion will pass if the exception is caught


if __name__ == '__main__':
    pytest.main()
