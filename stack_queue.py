from collections import deque


class Container:

    """Abstract class for Stacks and Queues"""

    def __init__(self, iterable=None):
        self._tokens = deque(iterable) if iterable else deque()

    def push(self, item):
        pass

    def pull(self, item):
        pass

    def __str__(self):
        return str(self._tokens)


class Stack(Container):

    def push(self, item):
        self._tokens.append(item)

    def pull(self, item):
        return self._tokens.pop()


class Queue(Container):

    def push(self, item):
        self._tokens.append(item)

    def pull(self, item):
        self._tokens.popleft()
