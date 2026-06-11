from DynamicArrayTemplate import DynamicArrayInterface
"""Function Signatures Implementation for Dynamic Arrays"""

class DynamicArray(DynamicArrayInterface):

    def __init__[T](self, capacity: int):
        """This is the Dynamic Array Constructor."""
        self._capacity = capacity
        self._size = 0
        self._arr = [T] * self._capacity

    def getSize(self) -> int:
        """Return the size of the array."""
        return self._size
    
    def getCapacity(self) -> int:
        """Get the capacity of the array."""
        return self._capacity
     
    def get[T](self, i: int) -> T:
        """Get the value of the item at the given index (i)."""
        return self._arr[i]

    def set[T](self, i: int, n: T) -> None:
        """Set the value of the item at the given index (i) to the given value (n)."""
        self._arr[i] = n

    def __getitem__[T](self, i: int) -> None:
        """Get the value of the item at the given index [i]."""
        return self._arr[i]

    def __setitem__[T](self, i: int, n: T) -> None:
        """Set the value of the item at the given index [i] to the given number (n)."""
        self._arr[i] = n

    def pushback[T](self, n: T) -> None:
        """Add a number (n) to the end of the array. Resize if needed."""
        self._size += 1
        if(self._capacity == self._size):
            self.resize()
        self._arr[self._size] = n

    def popback[T](self) -> T:
        """Remove a number (n) at the end of the array. Resize if needed.
        Return the popped value.
        """
        self._size -= 1
        return self._arr[self._size]

    def pop[T](self, i: int) -> T:
        """Remove a value at an index (i). Resize if needed.
        Return the removed value.
        """
        for _ in range(i,self._size):
            self._arr[i] = self._arr[i+1]
        self._size -= 1
        return

    def insert[T](self, i: int, n: T) -> None:
        """Insert a value (n) at an index (i). Resize if needed."""
        self._size += 1
        if(self._capacity == self._size):
            self.resize()
        for x in range(self._size - 1, i, -1):
            self._arr[x] = self._arr[x - 1]
        self._arr[i] = n

    def resize[T](self) -> None:
        """Resize the array. Double the capacity when size reaches capacity.
        Reduce the size of the array by half when the size is 1/3 of the capacity.
        Minimum size of 4.
        """
        if(self._size == self._capacity):
            self._capacity *= 2
        elif(self._size < (self._capcity/3)):
            self._capacity /= 2

        tempArr = [T] * self._capacity
        for i in range (self._size):
            tempArr[i] = self._arr[i]
        self._arr = tempArr