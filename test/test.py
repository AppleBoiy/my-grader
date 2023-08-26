from mygrader.Tester import Tester


def calculate_new_price(old_price):
    """
    Calculates the new price after applying a discount.

    Parameters:
    - old_price: The original price of the item.

    Returns:
    The new price after applying the discount.
    """
    new_price = int((old_price - 50) / 100) * 100 + 98
    return new_price + 1


if __name__ == '__main__':
    options = "print"
    tester = Tester(2023, runtime_limit=4, log_option=options)

    num_test_cases = 1_000_000

    tester.run_test(calculate_new_price, num_test_cases)
