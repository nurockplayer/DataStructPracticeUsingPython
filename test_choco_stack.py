import unittest
from choco_stack import Stack, StackEmptyError, StackFullError


class TestStackMethods(unittest.TestCase):
    def setUp(self):
        self.max_size = 10
        self.stack = Stack(self.max_size)  # type: Stack

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 1)

    def test_stack_full(self):
        for i in range(self.max_size):
            self.stack.push(i)
        self.assertTrue(self.stack.is_full())

    def test_raise_full(self):
        with self.assertRaises(StackFullError):
            for i in range(self.max_size + 1):
                self.stack.push(i)

    def test_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_raise_empty(self):
        with self.assertRaises(StackEmptyError):
            self.stack.pop()


if __name__ == '__main__':
    unittest.main()
