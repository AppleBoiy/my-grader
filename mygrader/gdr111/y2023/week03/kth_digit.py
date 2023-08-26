
def kth_digit(number, k):
    """
    Returns the k-th digit of the given number.
    """
    value = abs(number) // 10 ** k
    return value % 10
