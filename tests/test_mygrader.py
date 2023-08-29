import contextlib
import io

import pytest

from mygrader import Tester
from tests import MockClass


class TestMyGrader:

    # Test module imports
    def test_import(self):
        modules = [
            'mygrader', 'mygrader.printer', 'mygrader.template', 'mygrader.writer',
            'mygrader.template.log_template', 'mygrader.src', 'mygrader.src.y2023',
        ]
        for module_name in modules:
            assert __import__(module_name)

    # Test creation of a Tester object
    def test_create_tester(self):
        try:
            tester = Tester(2023, debug=True)
        except Exception as e:
            pytest.fail(f"Failed to create Tester object: {e}")
        assert isinstance(tester, Tester)

    # Test running a test
    def test_run_test(self):
        tester = Tester(2023, debug=True)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tester.run_test(MockClass.calculate_sum)
        assert buffer.getvalue() != ""

    # Test running a test with a custom number of test cases
    def test_run_test_with_custom_num_test_cases(self):
        tester = Tester(2023, debug=True, runtime_limit=60)
        buffer = io.StringIO()
        for num_test_cases in range(1, 7):
            with contextlib.redirect_stdout(buffer):
                tester.run_test(MockClass.calculate_sum, num_test_cases=10 ** num_test_cases)
            assert buffer.getvalue() != ""

    # Test running a test with a runtime limit
    def test_run_test_with_runtime_limit(self):
        tester = Tester(2023, runtime_limit=0.01, debug=True)
        with pytest.raises(TimeoutError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(MockClass.nearest_odd, num_test_cases=1_000_000)

    # Test running a test that exceeds the memory limit
    def test_run_test_with_memory_limit(self):
        tester = Tester(2023, debug=True)
        with pytest.raises(MemoryError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(MockClass.calculate_sum, num_test_cases=100_000_000)

    # Test running a test with mismatched data type
    def test_run_test_mismatched_data_type(self):
        tester = Tester(2023, debug=True)
        with pytest.raises(TypeError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(MockClass.display_time, num_test_cases="1")

    # Test running a test with an invalid function
    def test_run_test_with_invalid_function(self):
        tester = Tester(2023, debug=True)
        with pytest.raises(AttributeError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(print, num_test_cases="1")


if __name__ == '__main__':
    pytest.main()
