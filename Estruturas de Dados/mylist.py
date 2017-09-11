from mycontainer import *
from mynode import *

class InvalidPositionValue(Exception):
    pass

class List(Container):

    def __init__(self):
        self._last = None
        self._size = 0

    def insert(self, value, position):
        if position < 0 or position > self._size:
            raise InvalidPositionValue
        else:
            node = Node(value)
            if position == self._size:
                node.next = self._last
                self._last = node
            else:
                n = self._last
                for i in range(self._size-1, -1, -1):
                    if i == position:
                        break
                    n = n.next
                node.next = n.next
                n.next = node
            self._size += 1

    def get(self, position):
        if position < 0 or position > self._size:
            raise InvalidPositionValue
        else:
            n = self._last
            for i in range(self._size-1, -1, -1):
                if i == position:
                    break
                n = n.next
            return n.value
    
    def __getitem__(self, position):
        return self.get(position)

    def remove(self, position):
        if position < 0 or position > self._size:
            raise InvalidPositionValue
        else:
            if position == self._size:
                aux = self._last
                self._last = self._last.next
                del aux
            else:
                n = self._last
                for i in range(self._size-1, -1, -1):
                    if i == position+1:
                        break
                    n = n.next
                aux = n.next
                n.next = n.next.next
                del aux

            self._size -= 1

    def __setitem(self, position, value):
        self.remove(position)
        self.insert(value, position)