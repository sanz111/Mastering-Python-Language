#!/usr/bin/python3
import timeit


def sum1(n):
    totalSum = 0
    for i in range(n+1):
        totalSum += i
    return totalSum


def sum2(n):
    return n*(n+1)/2


if __name__ == "__main__":

    start_time = timeit.default_timer()
    print(sum1(10))
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print(sum2(10))
    print(timeit.default_timer() - start_time)
