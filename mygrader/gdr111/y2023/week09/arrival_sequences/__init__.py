def run_tests_and_get_summary(_test_suite_module, _num_test_cases, _output_option='None'):
    try:
        test_suite_instance = _test_suite_module.TestArrivalSequences()

        if _output_option == 'print':
            print("Running tests with only text report:")

        elif _output_option == 'write':
            print("\nRunning tests with markdown report:")

        else:
            raise ValueError(f"Invalid output option: {_output_option}")

        test_suite_instance.test_random_cases(num_test_cases=_num_test_cases, output_option=_output_option)

    except ValueError as e:
        print(f'ValueError: {e}')

    except Exception as e:
        print(f'Exception: {e}')


if __name__ == '__main__':
    test_suite_module = __import__('test')
    num_test_cases = 1000

    run_tests_and_get_summary(test_suite_module, num_test_cases, _output_option='None')
