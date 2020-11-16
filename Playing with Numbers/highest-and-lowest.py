from unittest import TestCase

# Solution
def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]
    numbers = [max(numbers), min(numbers)]
    numbers = ' '.join([str(elem) for elem in numbers])
    print(numbers)
    return numbers

# Testing
class Testing(TestCase):


    def test(self):
        self.assertEquals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")