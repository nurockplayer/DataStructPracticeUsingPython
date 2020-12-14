class StackEmptyError(Exception):
    def __init__(self):
        super().__init__('Stack is empty.')


class StackFullError(Exception):
    def __init__(self):
        super().__init__('Stack is full.')


class _StackNode():
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Stack():
    def __init__(self, max_size=10):
        self._top = None
        self._size = 0
        self._max_size = max_size

    def is_full(self):
        return self._size >= self._max_size

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        if self.is_empty():
            raise StackEmptyError()
        return self._top.item

    def pop(self):
        if self.is_empty():
            raise StackEmptyError()
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        if self.is_full():
            raise StackFullError()
        self._top = _StackNode(item, self._top)
        self._size += 1
