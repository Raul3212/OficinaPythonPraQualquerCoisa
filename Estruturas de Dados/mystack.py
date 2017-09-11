from mynode import Node
from mycontainer import *

class Stack(Container):
    
    def __init__(self):
        self._head = None
        self._size = 0
    
    def push(self, value):
        node = Node(value)
        node.next = self._head
        self._head = node
        self._size += 1
    
    def pop(self):
        rem = self._head
        self._head = self._head.next
        del rem
        self._size -= 1

    def top(self):
        return self._head.value

    def isEmpty(self):
        return self._size == 0