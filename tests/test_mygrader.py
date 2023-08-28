import contextlib
import io

import pytest

from mygrader import Tester
from mygrader.src.y2023 import Solution


def test_import():
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


def test_create_tester():
    try:
        Tester(2023)
    except Exception as e:
        assert False, f"Failed to create Tester object: {e}"
    assert True, "Successfully created Tester object"


def test_run_test():
    tester = Tester(2023, debug=True)

    try:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tester.run_test(Solution.sphere_volume, num_test_cases=1000)

    except Exception as e:
        assert False, f"Failed to run test: {e}"
    assert True


def test_run_test_with_runtime_limit():
    tester = Tester(2023, runtime_limit=0.1, debug=True)

    try:
        buffer = io.StringIO()
        with contextlib.redirect_stderr(buffer):
            # Run the test cases with the sphere_volume function from Solution class
            tester.run_test(Solution.sphere_volume, num_test_cases=1000000)

        # If the code execution completes within the time limit, this point is reached
        assert False, "Failed to raise exception when runtime limit is exceeded"

    except TimeoutError:  # Catch the TimeoutError exception raised when the runtime limit is exceeded
        assert True  # Assertion will pass if the exception is caught


if __name__ == '__main__':
    pytest.main()
