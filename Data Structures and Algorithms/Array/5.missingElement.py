#!/usr/bin/python3
from nose.tools import assert_equal

# Algorithms have been put in order of best approch to start solving problem.

# using BIT OPERATION
# using XOR bitwise operation, but how the thing is working still need to be found.


def missingFinder1(list1, list2):
    '''O(1)'''
    result = 0
    for num in list1+list2:
        result = result ^ num
    return result

# using CUSTOM MATHS TRICK OR MATHEMATICAL FORMULA


def missingFinder2(list1, list2):
    '''O(n)'''
    list1sum = sum(list1)
    list2sum = sum(list2)
    return list1sum - list2sum

# using built-in functions


def missingFinder3(list1, list2):
    '''finds the missing element in list2
    O(n)
    '''
    d = dict()
    for i in list2:
        # if i not in d:
        #     d[i] = 1
        # else:
        #     d[i] += 1
        # it is just one liner for above commented code which has ability to count each key.
        # get(key,default value of any type ) returns either key's value first if possible if not returns default value.
        d[i] = d.get(i, 0) + 1

    for i in list1:
        if i not in d:
            return i
        else:
            d[i] -= 1

    for i in d:
        if d[i] != 0:
            return i


# using ITERATIONS

def missingFinder4(list1, list2):
    '''O(n)'''
    list1.sort()
    print(list1)
    list2.sort()
    print(list2)

    # nice trick
    for num1, num2 in zip(list1, list2):
        if num1 != num2:
            return num1
    return list1[-1]


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        print("first test case passed")
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1],
                         [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print("second test case passed")
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        print('ALL TEST CASES PASSED')


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 4, 5, 6]
    l2 = [3, 5, 2, 1, 6, 4]
    # print("%d is missing element" % missingFinder3(l1, l2))
    t = TestFinder()
    t.test(missingFinder3)
