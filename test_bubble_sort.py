from random import randint
import unittest
from bubble_sort import bubble_sort


class TestBubbleSortMethods(unittest.TestCase):
    def test_bubble_sort(self):
        test_data = [randint(1, 99) for i in range(randint(4, 8))]
        self.assertEqual(bubble_sort(test_data), sorted(test_data))


if __name__ == '__main__':
    unittest.main()
