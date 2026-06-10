from abc import ABC, abstractmethod
"""Template Function Signatures for Dynamic Arrays.
Do not change the function signatures!!!
"""

class DynamicArrayInterface:
    @abstractmethod
    def __init__[T](self, capacity: int):
        """This is the Dynamic Array Constructor."""
        pass
    
    @abstractmethod
    def getSize(self) -> int:
        """Return the size of the array."""
        pass
    
    @abstractmethod
    def getCapacity(self) -> int:
        """Get the capacity of the array."""
        pass

    @abstractmethod 
    def get[T](self, i: int) -> T:
        """Get the value of the item at the given index (i)."""
        pass

    @abstractmethod
    def set[T](self, i: int, n: T) -> None:
        """Set the value of the item at the given index (i) to the given value (n)."""
        pass

    @abstractmethod
    def __getitem__[T](self, i: int) -> T:
        """Get the value of the item at the given index [i]."""
        pass

    @abstractmethod
    def __setitem__[T](self, i: int, n: T) -> None:
        """Set the value of the item at the given index [i] to the given number (n)."""
        pass

    @abstractmethod
    def pushback[T](self, n: T) -> None:
        """Add a number (n) to the end of the array. Resize if needed."""
        pass

    @abstractmethod
    def popback[T](self) -> T:
        """Remove a number (n) at the end of the array. Resize if needed.
        Return the popped value.
        """
        pass

    @abstractmethod
    def pop[T](self, i: int) -> T:
        """Remove a value at an index (i). Resize if needed.
        Return the removed value.
        """
        pass

    @abstractmethod
    def insert[T](self, i: int, n: T) -> None:
        """Insert a value (n) at an index (i). Resize if needed."""
        pass

    @abstractmethod
    def resize[T](self) -> None:
        """Resize the array. Double the capacity when size reaches capacity.
        Reduce the size of the array by half when the size is 1/3 of the capacity.
        """
        pass