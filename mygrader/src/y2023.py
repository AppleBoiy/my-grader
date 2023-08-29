import math
from random import randint, uniform, choices
from string import punctuation, ascii_letters
from typing import List


class Helper:

    @classmethod
    def queue_bus(cls, result, prefix, seq1, seq2) -> None:
        if not seq2 and not seq1:
            # Joining the prefix to form a complete sequence
            result.append('>'.join(prefix))

        if seq1:
            cls.queue_bus(result, prefix + [seq1[0]], seq1[1:], seq2)

        if seq2:
            cls.queue_bus(result, prefix + [seq2[0]], seq1, seq2[1:])


class Generator:

    @classmethod
    def calculate_sum_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            x = randint(1, 10 ** 9)  # Generate random x value
            y = randint(x, 10 ** 9)  # Generate random y value
            test_cases.append((x, y))
        return test_cases

    @classmethod
    def calculate_new_price_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            old_price = uniform(0.0, 1000.0)  # Generate random old price between 0 and 1000
            test_cases.append((old_price,))
        return test_cases

    @classmethod
    def calculate_triangle_area_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        while len(test_cases) < num_test_cases:
            a = uniform(1.0, 100.0)
            b = uniform(1.0, 100.0)

            # Ensure that the sum of a and b is greater than c
            c_min = abs(a - b) + 0.0001  # Add a small epsilon to avoid floating point precision issues
            c_max = a + b - 0.0001  # Subtract a small epsilon to avoid floating point precision issues

            c = uniform(c_min, c_max)
            test_cases.append((a, b, c))

        return test_cases

    @classmethod
    def display_time_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            test_cases.append((randint(1, 10 ** 20),))

        return test_cases

    @classmethod
    def find_intersection_test_cases(cls, num_test_cases: int) -> List:
        """
        Generate a list of tests cases with random parameters.

        Args:
            num_test_cases (int): Number of tests cases to generate.
        """
        test_cases = []
        for _ in range(num_test_cases):
            m1 = uniform(0.0, 1000.0)
            b1 = uniform(0.0, 1000.0)
            m2 = uniform(0.0, 1000.0)
            b2 = uniform(0.0, 1000.0)
            test_cases.append((m1, b1, m2, b2))
        return test_cases

    @classmethod
    def find_r_from_surface_area_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            surface_area = uniform(0.0, 1000.0)
            test_cases.append((surface_area,))
        return test_cases

    @classmethod
    def sphere_volume_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            radius = uniform(0.0, 1000.0)
            test_cases.append((radius,))
        return test_cases

    @classmethod
    def kth_digit_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            number = randint(0, 10 ** 9)
            k = randint(0, 9)
            test_cases.append((number, k))
        return test_cases

    @classmethod
    def nearest_odd_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            x = uniform(0.0, 1000.0)
            test_cases.append((x,))
        return test_cases

    @classmethod
    def octagon_area_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            side_length = uniform(0.0, 1000.0)
            test_cases.append((side_length,))
        return test_cases

    @classmethod
    def set_kth_digit_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            number = randint(0, 10 ** 9)
            k = randint(0, 9)
            value = randint(0, 9)
            test_cases.append((number, k, value))
        return test_cases

    @classmethod
    def patterned_message_test_cases(cls, num_test_cases: int) -> list:

        test_cases = []
        for _ in range(num_test_cases):
            message = ''.join(choices(punctuation + ascii_letters, k=randint(1, 10)))
            pattern = ''.join(choices(['*', ' '], k=randint(1, 100)))
            test_cases.append((message, pattern))
        return test_cases

    @classmethod
    def life_path_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            n = randint(1, 10 ** 9)
            test_cases.append((n,))
        return test_cases

    @classmethod
    def median_of_median_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            list_a = [uniform(0.0, 1000.0) for _ in range(randint(1, 100))]
            test_cases.append((list_a,))
        return test_cases

    @classmethod
    def left_max_test_cases(cls, num_test_cases: int) -> List:
        return cls.median_of_median_test_cases(num_test_cases)

    @classmethod
    def arrival_sequences_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            left_lane = tuple(choices(['R', 'O'], k=randint(1, 100)))
            right_lane = tuple(choices(['R', 'O'], k=randint(1, 100)))
            test_cases.append((left_lane, right_lane))
        return test_cases


class Solution(Helper):

    @classmethod
    def calculate_sum(cls, x: int, y: int) -> int:
        """
            Calculates the sum of a sequence of numbers.

            Given two numbers, x and y, this function calculates the sum of the sequence
            of numbers starting from x and ending at y, inclusive, using the formula for
            the sum of an arithmetic series.

            Parameters:
            - x: Starting number of the sequence
            - y: Ending number of the sequences

            Returns:
            The sum of the sequence.
            """
        summation = int((x + y) * ((y - x + 1) / 2))
        return summation

    @classmethod
    def calculate_new_price(cls, old_price: float) -> int:
        """
        Calculates the new price after applying a discount.

        Parameters:
        - old_price: The original price of the item.

        Returns:
        The new price after applying the discount.
        """
        new_price = int((old_price - 50) / 100) * 100 + 98
        return new_price

    @classmethod
    def calculate_triangle_area(cls, a: float, b: float, c: float) -> float:
        """
        Calculates the area of a triangle using Heron's formula.

        Given the lengths of the three sides of a triangle, this function
        calculates the area of the triangle using Heron's formula, which is based
        on the semi-perimeter and the lengths of the sides.

        Parameters:
        - a: Length of side a of the triangle
        - b: Length of side b of the triangle
        - c: Length of side c of the triangle

        Returns:
        The area of the triangle.
        """

        s = (a + b + c) / 2
        area_squared = s * (s - a) * (s - b) * (s - c)
        area = math.sqrt(area_squared)
        return area

    @classmethod
    def display_time(cls, ms: int) -> None:
        """
        The function `display_time` takes in a time in milliseconds and prints it in the format "X day(s), X
        hour(s), X minute(s), X second(s), and X millisecond(s)".

        Args:
          ms: The parameter `ms` represents the number of milliseconds.
        """
        sec = ms // 1000
        ms = ms % 1000

        minute = sec // 60
        sec = sec % 60

        hr = minute // 60
        minute = minute % 60

        day = hr // 24
        hr = hr % 24

        print(
            f"{day} day(s), {hr} hour(s), {minute} minute(s), {sec} second(s), and {ms} millisecond(s)")

    @classmethod
    def find_intersection(cls, m1: float, b1: float, m2: float, b2: float) -> tuple:
        """
        Calculates the intersection point of two lines.

        Given the slopes and y-intercepts of two lines, this function calculates
        the coordinates of the intersection point of the two lines in a
        two-dimensional plane.

        Parameters:
        - m1: Slope of the first line
        - b1: Y-intercept of the first line
        - m2: Slope of the second line
        - b2: Y-intercept of the second line

        Returns:
        A tuple (x, y) representing the coordinates of the intersection point.
        """

        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return x, y

    @classmethod
    def find_r_from_surface_area(cls, surface_area: float) -> float:
        """
        Calculates and returns the radius of a sphere given its surface area.
        """
        radius = (surface_area / (4 * math.pi)) ** 0.5
        return radius

    @classmethod
    def sphere_volume(cls, radius: float) -> float:
        """
        Calculates and returns the volume of a sphere given its radius.
        """
        volume = (4 / 3) * math.pi * radius ** 3
        return volume

    @classmethod
    def kth_digit(cls, number: int, k: int) -> int:
        """
        Returns the k-th digit of the given number.
        """
        value = abs(number) // 10 ** k
        return value % 10

    @classmethod
    def nearest_odd(cls, x: float) -> int:
        """
        Returns the nearest odd integer to the given number x.
        """
        return math.ceil(x / 2) * 2 - 1

    @classmethod
    def octagon_area(cls, side_length: float) -> float:
        """
        Calculates and returns the area of an octagon given the side length.
        """
        full_area = side_length ** 2
        outer_white_area = ((side_length / 3) ** 2) * 2
        return full_area - outer_white_area

    @classmethod
    def set_kth_digit(cls, number: int, k: int, value: int) -> int:
        """
        Replaces the kth digit of a given number with the specified value.
        """
        coeff = 10 ** k
        kth = cls.kth_digit(number, k) * coeff
        new_kth = value * coeff
        result = number - kth + new_kth
        return result

    @classmethod
    def median_of_median(cls, list_a: list) -> float:
        # Base cases
        if len(list_a) == 1:
            return list_a[0]

        if len(list_a) == 2:
            return sum(list_a) / 2

        # Calculate sublist size
        sub_size = len(list_a) // 3

        # Divide the list into sublist
        sub1 = list_a[:sub_size]
        sub2 = list_a[sub_size:2 * sub_size]
        sub3 = list_a[2 * sub_size:]

        # Recursively find medians of sublist
        med1 = cls.median_of_median(sub1)
        med2 = cls.median_of_median(sub2)
        med3 = cls.median_of_median(sub3)

        # Calculate median of medians
        med_of_meds_lst = [med1, med2, med3]

        # Calculate final median
        return sorted(med_of_meds_lst)[1]

    @classmethod
    def patterned_message(cls, message: str, pattern: str) -> None:
        if not pattern:
            return

        message = message.replace(' ', '')

        char: str = pattern[0]
        tailer = pattern[1:]

        if char == '*':
            print(message[0], end='')
            message = message[1:] + message[0]
        else:
            print(char, end='')

        cls.patterned_message(message, tailer)

    @classmethod
    def life_path(cls, n: int) -> int:
        while n >= 10:
            n = n // 10 + n % 10
        return n

    @classmethod
    def left_max(cls, list_a: list) -> list:
        result = []
        it = iter(list_a)
        max_value = float('-inf')

        while True:
            try:
                value = next(it)
                max_value = max(max_value, value)
                result.append(max_value)
            except StopIteration:
                break

        return result

    @classmethod
    def arrival_sequences(cls, left_lane: tuple, right_lane: tuple) -> list:
        result = []
        cls.queue_bus(result, [], left_lane, right_lane)
        return result
