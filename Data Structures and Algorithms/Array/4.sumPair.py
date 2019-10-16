#!/usr/bin/python3
from nose.tools import assert_equal

# MY_VERSION


def pairSum(list1, sum):
    '''returns a list containing tuples of two numbers when added becomes equal to sum
        O(n2)
    '''
    pairSum = set()
    count = 0
    if len(list1) < 2:
        return

    while (count < len(list1)-1):
        for j in range(count, len(list1)-1):
            if (list1[j] + list1[j+1]) == sum:
                pairSum.add((list1[j], list1[j+1]))
        count += 1

    pairSum = list(pairSum)
    print(pairSum)
    return len(pairSum)


# INSTRUCTOR_VERSION

def pair_sum(mylist, sum):
    '''returns a string of tuples containing two numbers when added becomes equal to sum
        O(n)
    '''

    if len(mylist) < 2:
        return

    seen = set()
    output = set()

    for num in mylist:
        sumSpouse = sum - num

        if sumSpouse not in seen:
            seen.add(num)
        else:
            output.add((min(sumSpouse, num), max(sumSpouse, num)))

    output = list(output)
    print(output)
    # return '\n'.join(map(str, output))
    return len(output)


class TestPair(object):
    def test(self, solution):
        assert_equal(solution([1, 2, 3, 1], 3), 1)
        assert_equal(solution([1, 3, 2, 2], 4), 2)
        assert_equal(
            solution([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        print('ALL TEST CASES PASSED')


if __name__ == "__main__":
    # print(pairSum([1, 3, 2, 2], 4))
    # print(pair_sum([1, 3, 2, 2], 4))
    t = TestPair()
    t.test(pair_sum)
