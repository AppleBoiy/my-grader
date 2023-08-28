simple = """Test Results:
+-----------------+------------+
|  Passed         | {passed_count:-7d}    |
|  Failed         | {failed_count:-7d}    |
|  Success Rate   | {success_rate:8.2f}%  |
+-----------------+------------+"""

more_info = """
# Test Results

## Summary

Test cases passed: {passed_count}
Test cases failed: {failed_count}
Success rate: {success_rate:.2f}%

## Execution Time

Average time per tests case: {average_time:.5f} seconds
Total time taken: {total_time_result:.2f} seconds
Tests conducted at a rate of: {test_per_second:.2f} tests/second

## Failed Test Cases

{failed_cases_table}
{more_info}
"""
