from mynode import *
from mycontainer import *

class Queue(Container):

    def __init__(self):
        self._init = None
        self._size = 0

    def push(self, value):
        node = Node(value)
        node.next = None
        if self._size > 0:
            i = self._init
            while i.next != None:
                i = i.next
            i.next = node
        else:
            self._init = node
        self._size += 1

    def pop(self):
        rem = self._init
        self._init = self._init.next
        del rem
        self._size -= 1

    def front(self):
        return self._init.value

    def isEmpty(self):
        return self._size == 0