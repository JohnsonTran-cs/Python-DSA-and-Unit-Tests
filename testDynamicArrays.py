import unittest
from DynamicArray import DynamicArray

"""Unit Tests for Dynamic Arrays"""

class TestDynamicArray(unittest.TestCase):
    

    def testGetSize(self):
        """Test getSize() function"""
        arr1 = DynamicArray(4)
        self.assertEqual(arr1.getSize(), 0)
        arr1.pushback(5)
        self.assertEqual(arr1.getSize(), 1)
        arr1.pushback(10)
        arr1.pushback(15)
        arr1.popback()
        self.assertEqual(arr1.getSize(), 2)
        """
        // save for popback and pop
        for i in range(3):
            arr1.popback()
            self.assertEqual(arr1.getSize(), 4)
        """

    def testGetCapacity(self):
        """Test getCapacity() function"""
        arr1 = DynamicArray(4)
        self.assertEqual(arr1.getCapacity(), 4)
        for i in range(4):
            arr1.pushback(5)
        self.assertEqual(arr1.getCapacity(), 8)
        # Test case for shrink

    def testGet(self):
        """Test get(i) function"""
        arr1 = DynamicArray(4)
        for i in range(5):
            arr1.pushback(i)
        self.assertEqual(arr1.get(3), 3)
        # Assert raise error if not found

    def testSet(self):
        """Test set(i, n) function"""
        arr1 = DynamicArray(4)
        for i in range(5):
            arr1.pushback(i)
        for i in range(5):
            arr1.set(i, i+1)
            self.assertEqual(arr1.get(i), i+1)
        # Assert raise if index out of range
    

if __name__ == "__main__":
    unittest.main()