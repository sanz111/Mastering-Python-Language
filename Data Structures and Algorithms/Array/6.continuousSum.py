#!/usr/bin/python3


def largestSum(array):
    '''returns largest continuous sum of an array'''
    currentSum = largestSum = array[0]
    for num in array[1:]:
        currentSum = max(currentSum+num, num)
        largestSum = max(currentSum, largestSum)
    return largestSum


if __name__ == "__main__":
    print(largestSum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
