import random
import time
import unittest

from tqdm import tqdm

import recursion_life_path
from while_life_path import life_path, life_path1, life_path2


class TestLifePath(unittest.TestCase):
    def test_random_cases(self):
        num_test_cases = 100_000

        passed = 0
        failed = 0
        total_time = 0

        with tqdm(total=num_test_cases, unit='tests') as pbar:

            for i in range(num_test_cases):
                n = random.randint(0, 10 ** 100)

                start_time = time.time()

                expected = recursion_life_path.life_path(n)
                result = life_path(n)
                result1 = life_path1(n)
                result2 = life_path2(n)

                try:
                    self.assertEqual(expected, result)
                    self.assertEqual(expected, result1)
                    self.assertEqual(expected, result2)

                    passed += 1
                except AssertionError:
                    failed += 1

                elapsed_time = time.time() - start_time
                total_time += elapsed_time

                pbar.update(1)

        average_time = total_time / num_test_cases

        print(f"Test cases passed: {passed}")
        print(f"Test cases failed: {failed}")
        print(f"Average time per tests case: {average_time:.5f} seconds")
        print(f"Total time taken: {total_time:.2f} seconds")


if __name__ == '__main__':
    unittest.main()
