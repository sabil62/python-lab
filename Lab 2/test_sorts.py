import unittest
from insertion_sort import insertionSort
from merge_sort import mergeSort

class SortingTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        input = [30, 10, 20, 5, 25, 15,35,45,40]
        output = [5,10,15,20,25,30,35,40,45]

        insertionSort(input)

        self.assertListEqual(input, output)

    def test_merge_sort(self):
        input = [30, 10, 20, 5, 25, 15,35,45,40]
        output = [5,10,15,20,25,30,35,40,45]

        mergeSort(input, 0, len(input)-1)

        self.assertListEqual(input, output)

if __name__ == "__main__":
    unittest.main()
