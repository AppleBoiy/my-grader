# Test Results

## First 10 Failed Test Cases:

| Left Lane                | Right Lane               | Expected                | Result    |
|:-------------------------|:-------------------------|:------------------------|:----------|
| ['R1']                   | ['L1', 'L2']             | R1>L1>L2                | not found |
| ['R1', 'R2', 'R3']       | ['L1', 'L2', 'L3']       | R1>R2>R3>L1>L2>L3       | not found |
| ['R1', 'R2', 'R3']       | ['L1', 'L2']             | R1>R2>R3>L1>L2          | not found |
| ['R1', 'R2', 'R3', 'R4'] | ['L1', 'L2', 'L3', 'L4'] | R1>R2>R3>R4>L1>L2>L3>L4 | not found |
| ['R1', 'R2', 'R3']       | ['L1', 'L2', 'L3']       | R1>R2>R3>L1>L2>L3       | not found |
| ['R1', 'R2', 'R3']       | ['L1', 'L2', 'L3']       | R1>R2>R3>L1>L2>L3       | not found |
| ['R1', 'R2']             | ['L1', 'L2', 'L3']       | R1>R2>L1>L2>L3          | not found |
| ['R1', 'R2']             | ['L1']                   | R1>R2>L1                | not found |
| ['R1', 'R2', 'R3', 'R4'] | ['L1', 'L2', 'L3', 'L4'] | R1>R2>R3>R4>L1>L2>L3>L4 | not found |
| ['R1', 'R2']             | ['L1', 'L2', 'L3', 'L4'] | R1>R2>L1>L2>L3>L4       | not found |

Test cases passed: 0

Test cases failed: 1000

Average time per test case (Expected): 0.00001 seconds
Average time per test case (Result): 0.00753 seconds
Total time taken (Expected): 0.01 seconds
Total time taken (Result): 7.53 seconds

## Performance Comparison:

Expected Calculation Time: 0.01 seconds
Result Calculation Time: 7.53 seconds
Expected Calculation is 593.52 times faster
