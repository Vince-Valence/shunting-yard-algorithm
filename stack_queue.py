from collections import deque


class Container:

    """Abstract class for Stacks and Queues"""

    def __init__(self, iterable=None):
        self._tokens = deque(iterable) if iterable else deque()

    def push(self, item):
        pass

    def pull(self):
        pass

    def view_next(self):
        pass

    def __str__(self):
        return str(self._tokens)

    def __bool__(self):
        return bool(self._tokens)


class Stack(Container):

    def push(self, item):
        self._tokens.append(item)

    def pull(self):
        return self._tokens.pop()

    def view_next(self):
        return self._tokens[-1] if len(self._tokens) else None


class Queue(Container):

    def push(self, item):
        self._tokens.append(item)

    def pull(self):
        return self._tokens.popleft()

    def view_next(self):
        return self._tokens[0] if len(self._tokens) else None
