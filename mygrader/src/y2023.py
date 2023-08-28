import math
import random
from typing import List


class Helper:
    ...


class Generator:

    @classmethod
    def calculate_sum_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            x = random.randint(1, 10 ** 9)  # Generate random x value
            y = random.randint(x, 10 ** 9)  # Generate random y value
            test_cases.append((x, y))
        return test_cases

    @classmethod
    def calculate_new_price_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            old_price = random.uniform(0.0, 1000.0)  # Generate random old price between 0 and 1000
            test_cases.append((old_price,))
        return test_cases

    @classmethod
    def calculate_triangle_area_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        while len(test_cases) < num_test_cases:
            a = random.uniform(1.0, 100.0)
            b = random.uniform(1.0, 100.0)

            # Ensure that the sum of a and b is greater than c
            c_min = abs(a - b) + 0.0001  # Add a small epsilon to avoid floating point precision issues
            c_max = a + b - 0.0001  # Subtract a small epsilon to avoid floating point precision issues

            c = random.uniform(c_min, c_max)
            test_cases.append((a, b, c))

        return test_cases

    @classmethod
    def display_time_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            test_cases.append((random.randint(1, 10 ** 20),))

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
            m1 = random.uniform(0.0, 1000.0)
            b1 = random.uniform(0.0, 1000.0)
            m2 = random.uniform(0.0, 1000.0)
            b2 = random.uniform(0.0, 1000.0)
            test_cases.append((m1, b1, m2, b2))
        return test_cases

    @classmethod
    def find_r_from_surface_area_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            surface_area = random.uniform(0.0, 1000.0)
            test_cases.append((surface_area,))
        return test_cases

    @classmethod
    def sphere_volume_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            radius = random.uniform(0.0, 1000.0)
            test_cases.append((radius,))
        return test_cases

    @classmethod
    def kth_digit_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            number = random.randint(0, 10 ** 9)
            k = random.randint(0, 9)
            test_cases.append((number, k))
        return test_cases

    @classmethod
    def nearest_odd_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            x = random.uniform(0.0, 1000.0)
            test_cases.append((x,))
        return test_cases

    @classmethod
    def octagon_area_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            side_length = random.uniform(0.0, 1000.0)
            test_cases.append((side_length,))
        return test_cases

    @classmethod
    def set_kth_digit_test_cases(cls, num_test_cases: int) -> List:
        test_cases = []
        for _ in range(num_test_cases):
            number = random.randint(0, 10 ** 9)
            k = random.randint(0, 9)
            value = random.randint(0, 9)
            test_cases.append((number, k, value))
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
        num_str = str(number)
        kth_digit_index = len(num_str) - k - 1
        return int(num_str[kth_digit_index])

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
