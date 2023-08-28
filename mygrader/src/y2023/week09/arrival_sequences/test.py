import random
import unittest

from tqdm import tqdm

import permutation_arrival_sequences as pas
from dest_arrival_sequences import arrival_sequences
from suite import run_test, add_failed_case, print_summary


class TestArrivalSequences(unittest.TestCase):

    def run_tests(self, num_test_cases):
        results = {
            'passed': 0,
            'failed': 0,
            'failed_cases': [],
            'average_time_expected': 0,
            'average_time_result': 0,
            'total_time_expected': 0,
            'total_time_result': 0
        }

        red_lane = [f'L{i}' for i in range(1, 5)]
        orange_lane = [f'R{i}' for i in range(1, 5)]

        with tqdm(total=num_test_cases, unit='tests') as pbar:
            for _ in range(num_test_cases):
                left_lane_length = random.randint(1, 5)
                right_lane_length = random.randint(1, 5)
                left_lane = orange_lane[:left_lane_length]
                right_lane = red_lane[:right_lane_length]

                expected, elapsed_time_expected = run_test(arrival_sequences, left_lane=left_lane,
                                                           right_lane=right_lane)
                result, elapsed_time_result = run_test(pas.arrival_sequences, left_lane=left_lane,
                                                       right_lane=right_lane)

                results['total_time_expected'] += elapsed_time_expected
                results['total_time_result'] += elapsed_time_result

                with self.subTest(left_lane=left_lane, right_lane=right_lane):
                    if result == expected:
                        results['passed'] += 1
                    else:
                        results['failed'] += 1
                        if len(results['failed_cases']) < 10:
                            add_failed_case(results['failed_cases'], expected, result, left_lane, right_lane)
                pbar.update(1)

            results['average_time_expected'] = results['total_time_expected'] / num_test_cases
            results['average_time_result'] = results['total_time_result'] / num_test_cases

        return results

    def test_random_cases(self, output_option, num_test_cases=100):
        results = self.run_tests(num_test_cases)
        print_summary(results, output_option=output_option)


if __name__ == '__main__':
    unittest.main()
