class MockClass:
    @staticmethod
    def calculate_sum(x: int, y: int) -> int:
        """
            Mock test function to test the Tester class

        description: for general purpose
        """
        summation = int((x + y) * ((y - x + 1) / 2))
        return summation

    @staticmethod
    def display_time(ms: int) -> tuple:
        """
            Mock test function to test the Tester class

        Raise expect: TypeError
        description: this function must print instead of return int
        """
        seconds = ms // 1000
        minutes = seconds // 60
        hours = minutes // 60
        return hours, minutes, seconds

    @staticmethod
    def nearest_odd(x: float) -> int:
        """
            Mock test function to test the Tester class

        Raise expect: TimeoutError
        description: this function must be timeout
        """
        __import__('time').sleep(1)

        return __import__('math').ceil(x / 2) * 2 - 1
