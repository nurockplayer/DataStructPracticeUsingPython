class QueueEmptyError(Exception):
    def __init__(self):
        super().__init__('Queue is empty.')


class QueueFullError(Exception):
    def __init__(self):
        super().__init__('Queue is full.')


class _QueueNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue():
    def __init__(self, max_size=10):
        self._qhead = None
        self._qtail = None
        self._count = 0
        self._max_size = max_size

    def is_empty(self):
        return self._qhead is None

    def is_full(self):
        return self._count >= self._max_size

    def __len__(self):
        return self._count

    def peek(self):
        if self.is_empty():
            raise QueueEmptyError()
        return self._qhead.item

    def enqueue(self, item):
        if self.is_full():
            raise QueueFullError()
        node = _QueueNode(item)
        if self.is_empty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError()
        node = self._qhead
        item = node.item
        del node
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return item
