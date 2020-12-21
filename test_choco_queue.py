import unittest
from choco_queue import Queue, QueueEmptyError, QueueFullError


class TestQueueMethods(unittest.TestCase):
    def setUp(self):
        self.max_size = 10
        self.queue = Queue(self.max_size)  # type: Queue

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 2)

    def test_queue_full(self):
        for i in range(self.max_size):
            self.queue.enqueue(i)
        self.assertTrue(self.queue.is_full())

    def test_raise_full(self):
        with self.assertRaises(QueueFullError):
            for i in range(self.max_size + 1):
                self.queue.enqueue(i)

    def test_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_raise_empty(self):
        with self.assertRaises(QueueEmptyError):
            self.queue.dequeue()


if __name__ == '__main__':
    unittest.main()
