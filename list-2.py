def count_evens(nums):
    """
    Return the number of even ints in the given array. 
    Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
    https://codingbat.com/doc/practice/mod-introduction.html


    count_evens([2, 1, 2, 3, 4]) → 3
    count_evens([2, 2, 0]) → 3
    count_evens([1, 3, 5]) → 0
    """
    return


def big_diff(nums):
    """
        Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
        Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


    big_diff([10, 3, 5, 6]) → 7
    big_diff([7, 2, 10, 9]) → 8
    big_diff([2, 10, 7, 2]) → 8"""
    return


def centered_average(nums):
    """
        Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
        except ignoring the largest and smallest values in the array. 
        If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
        Use int division to produce the final average. 
        You may assume that the array is length 3 or more.


    centered_average([1, 2, 3, 4, 100]) → 3
    centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
    centered_average([-10, -4, -2, -4, -2, 0]) → -3"""
    return


def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


    sum13([1, 2, 2, 1]) → 6
    sum13([1, 1]) → 2
    sum13([1, 2, 2, 1, 13]) → 6"""
    return


def sum67(nums):
    """
    Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
    (every 6 will be followed by at least one 7). 
    Return 0 for no numbers.


    sum67([1, 2, 2]) → 5
    sum67([1, 2, 2, 6, 99, 99, 7]) → 5
    sum67([1, 1, 6, 7, 2]) → 4"""
    return


def has22(nums):
    """
    Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


    has22([1, 2, 2]) → True
    has22([1, 2, 1, 2]) → False
    has22([2, 1, 2]) → False"""
    return


if __name__ == "__main__":
    from _check import check_problems

    count_evens_cases = [
        (([2, 1, 2, 3, 4],), 3),
        (([2, 2, 0],), 3),
        (([1, 3, 5],), 0),
        (([],), 0),
        (([11, 9, 0, 1],), 1),
        (([2, 11, 9, 0],), 2),
        (([2],), 1),
        (([2, 5, 12],), 2),
    ]

    big_diff_cases = [
        (([10, 3, 5, 6],), 7),
        (([7, 2, 10, 9],), 8),
        (([2, 10, 7, 2],), 8),
        (([2, 10],), 8),
        (([10, 2],), 8),
        (([10, 0],), 10),
        (([2, 3],), 1),
        (([2, 2],), 0),
        (([2],), 0),
        (([5, 1, 6, 1, 9, 9],), 8),
        (([7, 6, 8, 5],), 3),
        (([7, 7, 6, 8, 5, 5, 6],), 3),
    ]

    centered_average_cases = [
        (([1, 2, 3, 4, 100],), 3),
        (([1, 1, 5, 5, 10, 8, 7],), 5),
        (([-10, -4, -2, -4, -2, 0],), -3),
        (([5, 3, 4, 6, 2],), 4),
        (([5, 3, 4, 0, 100],), 4),
        (([100, 0, 5, 3, 4],), 4),
        (([4, 0, 100],), 4),
        (([0, 2, 3, 4, 100],), 3),
        (([1, 1, 100],), 1),
        (([7, 7, 7],), 7),
        (([1, 7, 8],), 7),
        (([1, 1, 99, 99],), 50),
        (([1000, 0, 1, 99],), 50),
        (([4, 4, 4, 4, 5],), 4),
        (([4, 4, 4, 1, 5],), 4),
        (([6, 4, 8, 12, 3],), 6),
    ]

    sum13_cases = [
        (([1, 2, 2, 1],), 6),
        (([1, 1],), 2),
        (([1, 2, 2, 1, 13],), 6),
        (([1, 2, 13, 2, 1, 13],), 4),
        (([13, 1, 2, 13, 2, 1, 13],), 3),
        (([],), 0),
        (([13],), 0),
        (([13, 13],), 0),
        (([13, 0, 13],), 0),
        (([13, 1, 13],), 0),
        (([5, 7, 2],), 14),
        (([5, 13, 2],), 5),
        (([0],), 0),
        (([13, 0],), 0),
    ]

    sum67_cases = [
        (([1, 2, 2],), 5),
        (([1, 2, 2, 6, 99, 99, 7],), 5),
        (([1, 1, 6, 7, 2],), 4),
        (([1, 6, 2, 2, 7, 1, 6, 99, 99, 7],), 2),
        (([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7],), 2),
        (([2, 7, 6, 2, 6, 7, 2, 7],), 18),
        (([2, 7, 6, 2, 6, 2, 7],), 9),
        (([1, 6, 7, 7],), 8),
        (([6, 7, 1, 6, 7, 7],), 8),
        (([6, 8, 1, 6, 7],), 0),
        (([],), 0),
        (([6, 7, 11],), 11),
        (([11, 6, 7, 11],), 22),
        (([2, 2, 6, 7, 7],), 11),
    ]

    has22_cases = [
        (([1, 2, 2],), True),
        (([1, 2, 1, 2],), False),
        (([2, 1, 2],), False),
        (([2, 2, 1, 2],), True),
        (([1, 3, 2],), False),
        (([1, 3, 2, 2],), True),
        (([2, 3, 2, 2],), True),
        (([4, 2, 4, 2, 2, 5],), True),
        (([1, 2],), False),
        (([2, 2],), True),
        (([2],), False),
        (([],), False),
        (([3, 3, 2, 2],), True),
        (([5, 2, 5, 2],), False),
    ]

    input = [
        (count_evens, count_evens_cases),
        (big_diff, big_diff_cases),
        (centered_average, centered_average_cases),
        (sum13, sum13_cases),
        (sum67, sum67_cases),
        (has22, has22_cases),
    ]

    check_problems(input)
