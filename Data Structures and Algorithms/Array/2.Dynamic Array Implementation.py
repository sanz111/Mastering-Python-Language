#!/usr/bin/python3

import ctypes

# implementing custom dynamic array same like how list has been implementd in array.


class DynamicArray(object):
    '''Dynamic array class similar to python list
    '''

    def __init__(self):
        self.elementCount = 0  # count actual elements in array(default is 0)
        self.capacity = 1  # default capacity
        # creating array A with capacity 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.elementCount

    def __getitem__(self, index):
        if not 0 <= index <= self.elementCount:
            return IndexError('index is out of bound')
        return self.A[index]

    def __setitem__(self, index, value):
        self.A[index] = value

    def append(self, element):
        if self.elementCount == self.capacity:
            self._resize(2*self.capacity)  # 2x if capacity isn't enough
        self.A[self.elementCount] = element
        self.elementCount += 1

    def _resize(self, newCapacity):
        B = self.make_array(newCapacity)

        for i in range(self.elementCount):
            B[i] = self.A[i]  # copying each element references

        self.A = B  # copying reference of new array to the old array
        self.capacity = newCapacity

    def make_array(self, newCapacity):
        return (newCapacity * ctypes.py_object)()


arr = DynamicArray()
arr.append(1)
arr.append(3)
print(arr[1])
arr[1] = 5
print(arr[1])
print(len(arr))
