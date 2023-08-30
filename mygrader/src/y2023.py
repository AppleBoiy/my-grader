import math
from random import randint, uniform, choices
from string import punctuation, ascii_letters
from typing import List, Iterable

from faker import Faker


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

    @classmethod
    def increase_left(cls, _iter: Iterable, _max: int) -> Iterable:
        return map(lambda item: str(item) if item >= _max else str(_max), _iter)


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
            group1 = tuple(f'R{randint(0, 1000):03d}' for _ in range(randint(1, 10)))
            group2 = tuple(f'L{randint(0, 1000):03d}' for _ in range(randint(1, 10)))
            test_cases.append((group1, group2))
        return test_cases

    @classmethod
    def base_b_test_cases(cls, num_test_cases: int) -> list:
        test_cases = []
        for _ in range(num_test_cases):
            number = randint(0, 10 ** 9)
            b = randint(2, 10)
            test_cases.append((number, b))
        return test_cases

    @classmethod
    def gcd_test_cases(cls, num_test_cases: int) -> list:
        test_cases = []
        for _ in range(num_test_cases):
            a = randint(-10 ** 9, 10 ** 9)
            b = randint(-10 ** 9, 10 ** 9)
            test_cases.append((a, b))
        return test_cases

    @classmethod
    def pi_test_cases(cls, num_test_cases: int) -> list:
        return cls.corner_frame_test_cases(num_test_cases)

    @classmethod
    def reverse_digits_test_cases(cls, num_test_cases: int) -> list:
        test_cases = []
        for _ in range(num_test_cases):
            number = randint(-10 ** 9, 10 ** 9)
            test_cases.append((number,))
        return test_cases

    @classmethod
    def is_anagram_test_cases(cls, num_test_cases: int) -> list:
        test_cases = []
        fake = Faker()

        for i in range(num_test_cases):
            word = fake.sentence(nb_words=2, variable_nb_words=True, ext_word_list=None)

            if i % 2 == 1:
                # Generate a random anagram by shuffling the characters of the word
                anagram = ''.join(fake.random_choices(word, length=len(word)))
                if i % 2 == 0:
                    anagram += anagram[0]
            else:
                anagram = ''.join(choices(ascii_letters, k=randint(1, len(word))))

            test_cases.append((word, anagram))
        return test_cases

    @classmethod
    def corner_frame_test_cases(cls, num_test_cases: int) -> list:
        _max_test = min(100, num_test_cases)
        return [(i,) for i in range(_max_test + 1)]


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

    @classmethod
    def base_b(cls, number: int, b: int) -> int:
        if number < b:
            return number

        return cls.base_b(number // b, b) * 10 + number % b

    @classmethod
    def gcd(cls, a: int, b: int) -> int:
        if b == 0:
            return abs(a)

        return cls.gcd(b, a % b)

    @classmethod
    def pi(cls, n):
        """
       Calculate an approximation of pi using the Leibniz formula.

       Parameters:
       n (int): The number of terms to consider in the Leibniz formula.

       Returns:
       float: An approximation of pi using the Leibniz formula.
       """
        terms = map(
            lambda x: (-1 if x % 2 == 0 else 1) * (4 / (2 * x * (2 * x + 1) * (2 * x + 2))),
            range(1, n + 1)
        )
        pi_approximation = 3 + sum(terms)
        return pi_approximation

    @classmethod
    def reverse_digits(cls, number: int) -> int:
        if number < 0:
            return -cls.reverse_digits(-number)

        return int(str(number)[::-1])

    @classmethod
    def is_anagram(cls, s1: str, s2: str) -> bool:
        # Clean the input strings by removing non-alphabetic characters and converting to lowercase
        s1_cleaned = filter(str.isalpha, s1.lower())
        s2_cleaned = filter(str.isalpha, s2.lower())

        return sorted(s1_cleaned) == sorted(s2_cleaned)

    @classmethod
    def corner_frame(cls, n: int) -> str:
        nums = range(1, n + 1)

        # Map each line of the corner frame using the increase_left function
        lines = map(lambda x: cls.increase_left(nums, x), nums)

        # Convert each line to a space-separated string
        lines = map(lambda line: " ".join(line), lines)

        # Join the lines with a newline character and return the result
        return "\n".join(lines) + "\n"
