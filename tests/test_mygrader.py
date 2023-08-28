import contextlib
import io

import pytest

import mocker
from mygrader import Tester


class TestMyGrader:

    def test_import(self):
        modules = [
            'mygrader', 'mygrader', 'mygrader.printer', 'mygrader.template', 'mygrader.writer',
            'mygrader.template.log_template', 'mygrader.src', 'mygrader.src.y2023',
        ]
        for module_name in modules:
            assert __import__(module_name)

    def test_create_tester(self):
        try:
            tester = Tester(2023, debug=True)
        except Exception as e:
            pytest.fail(f"Failed to create Tester object: {e}")
        assert isinstance(tester, Tester)

    def test_run_test(self):
        tester = Tester(2023, debug=True)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tester.run_test(mocker.calculate_sum)
        assert buffer.getvalue() != ""

    def test_run_test_with_runtime_limit(self):
        tester = Tester(2023, runtime_limit=0.01, debug=True)

        with pytest.raises(TimeoutError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(mocker.calculate_sum, num_test_cases=1000)

    def test_run_test_with_memory_limit(self):
        tester = Tester(2023, debug=True)

        with pytest.raises(MemoryError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(mocker.calculate_sum, num_test_cases=100000000)

    def test_run_test_mismatched_data_type(self):
        tester = Tester(2023, debug=True)
        with pytest.raises(TypeError):
            with contextlib.redirect_stderr(io.StringIO()):
                tester.run_test(mocker.display_time, num_test_cases="100000000")


if __name__ == '__main__':
    pytest.main()
