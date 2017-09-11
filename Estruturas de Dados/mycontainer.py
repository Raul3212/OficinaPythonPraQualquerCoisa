import abc

class Container:
    
    @abc.abstractproperty    
    def _size(self):
        pass
    
    def __len__(self):
        return self._size