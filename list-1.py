def first_last6(nums):
    """Given an array of ints, return True if 6 appears as either the first or last element in the array. 
    The array will be length 1 or more.


    first_last6([1, 2, 6]) → True
    first_last6([6, 1, 2, 3]) → True
    first_last6([13, 6, 1, 2, 3]) → False"""
    return


def same_first_last(nums):
    """Given an array of ints, 
    return True if the array is length 1 or more, 
    and the first element and the last element are equal.


    same_first_last([1, 2, 3]) → False
    same_first_last([1, 2, 3, 1]) → True
    same_first_last([1, 2, 1]) → True"""
    return


def make_pi():
    """
    Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


    make_pi() → [3, 1, 4]"""
    return


def common_end(arr1, arr2):
    """Given 2 arrays of ints, a and b, 
    return True if they have the same first element or they have the same last element. 
    Both arrays will be length 1 or more.


    common_end([1, 2, 3], [7, 3]) → True
    common_end([1, 2, 3], [7, 3, 2]) → False
    common_end([1, 2, 3], [1, 3]) → True"""
    return


def sum3(nums):
    """
    Given an array of ints length 3, return the sum of all the elements.


    sum3([1, 2, 3]) → 6
    sum3([5, 11, 2]) → 18
    sum3([7, 0, 0]) → 7"""
    return


def rotate_left3(nums):
    """
    Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


    rotate_left3([1, 2, 3]) → [2, 3, 1]
    rotate_left3([5, 11, 9]) → [11, 9, 5]
    rotate_left3([7, 0, 0]) → [0, 0, 7]"""
    return


def reverse3(nums):
    """
    Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


    reverse3([1, 2, 3]) → [3, 2, 1]
    reverse3([5, 11, 9]) → [9, 11, 5]
    reverse3([7, 0, 0]) → [0, 0, 7]"""
    return


def max_end3(nums):
    """n array of ints length 3, figure out which is larger, 
    the first or last element in the array, 
    and set all the other elements to be that value. 
    Return the changed array.


    max_end3([1, 2, 3]) → [3, 3, 3]
    max_end3([11, 5, 9]) → [11, 11, 11]
    max_end3([2, 11, 3]) → [3, 3, 3]"""
    return


def sum2(nums):
    """
    Given an array of ints, return the sum of the first 2 elements in the array. 
    If the array length is less than 2, just sum up the elements that exist, 
    returning 0 if the array is length 0.


    sum2([1, 2, 3]) → 3
    sum2([1, 1]) → 2
    sum2([1, 1, 1, 1]) → 2"""
    return


def middle_way(arr1, arr2):
    """
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


    middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
    middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
    middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]"""
    return


def make_ends(nums):
    """
    Given an array of ints, 
    return a new array length 2 containing the first and last elements from the original array. 
    The original array will be length 1 or more.


    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]"""
    return


def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.

    has23([2, 5]) → True
    has23([4, 3]) → True
    has23([4, 5]) → False
    """
    return


if __name__ == "__main__":
    from _check import check_problems

    first_last6_cases = [
        (([1, 2, 6],), True),
        (([6, 1, 2, 3],), True),
        (([13, 6, 1, 2, 3],), False),
        (([13, 6, 1, 2, 6],), True),
        (([3, 2, 1],), False),
        (([3, 6, 1],), False),
        (([3, 6],), True),
        (([6],), True),
        (([3],), False),
        (([5, 6],), True),
        (([5, 5],), False),
        (([1, 2, 3, 4, 6],), True),
        (([1, 2, 3, 4],), False),
    ]

    same_first_last_cases = [
        (([1, 2, 3],), False),
        (([1, 2, 3, 1],), True),
        (([1, 2, 1],), True),
        (([7],), True),
        (([],), False),
        (([1, 2, 3, 4, 5, 1],), True),
        (([1, 2, 3, 4, 5, 13],), False),
        (([13, 2, 3, 4, 5, 13],), True),
        (([7, 7],), True),
    ]

    make_pi_cases = [((), [3, 1, 4])]

    common_end_cases = [
        (([1, 2, 3], [7, 3]), True),
        (([1, 2, 3], [7, 3, 2]), False),
        (([1, 2, 3], [1, 3]), True),
        (([1, 2, 3], [1]), True),
        (([1, 2, 3], [2]), False),
    ]

    sum3_cases = [
        ((([1, 2, 3]),), 6),
        ((([5, 11, 2]),), 18),
        ((([7, 0, 0]),), 7),
        ((([1, 2, 1]),), 4),
        ((([1, 1, 1]),), 3),
        ((([2, 7, 2]),), 11),
    ]

    rotate_left3_cases = [
        ((([1, 2, 3]),), [2, 3, 1]),
        ((([5, 11, 9]),), [11, 9, 5]),
        ((([7, 0, 0]),), [0, 0, 7]),
        ((([1, 2, 1]),), [2, 1, 1]),
        ((([0, 0, 1]),), [0, 1, 0]),
    ]

    reverse3_cases = [
        ((([1, 2, 3]),), [3, 2, 1]),
        ((([5, 11, 9]),), [9, 11, 5]),
        ((([7, 0, 0]),), [0, 0, 7]),
        ((([2, 1, 2]),), [2, 1, 2]),
        ((([1, 2, 1]),), [1, 2, 1]),
        ((([2, 11, 3]),), [3, 11, 2]),
        ((([0, 6, 5]),), [5, 6, 0]),
        ((([7, 2, 3]),), [3, 2, 7]),
    ]

    max_end3_cases = [
        ((([1, 2, 3]),), [3, 3, 3]),
        ((([11, 5, 9]),), [11, 11, 11]),
        ((([2, 11, 3]),), [3, 3, 3]),
        ((([11, 3, 3]),), [11, 11, 11]),
        ((([3, 11, 11]),), [11, 11, 11]),
        ((([2, 2, 2]),), [2, 2, 2]),
        ((([2, 11, 2]),), [2, 2, 2]),
        ((([0, 0, 1]),), [1, 1, 1]),
    ]

    sum2_cases = [
        ((([1, 2, 3]),), 3),
        ((([1, 1]),), 2),
        ((([1, 1, 1, 1]),), 2),
        ((([1, 2]),), 3),
        ((([1]),), 1),
        ((([]),), 0),
        ((([4, 5, 6]),), 9),
        ((([4]),), 4),
    ]

    middle_way_cases = [
        (([1, 2, 3], [4, 5, 6]), [2, 5]),
        (([7, 7, 7], [3, 8, 0]), [7, 8]),
        (([5, 2, 9], [1, 4, 5]), [2, 4]),
        (([1, 9, 7], [4, 8, 8]), [9, 8]),
        (([1, 2, 3], [3, 1, 4]), [2, 1]),
        (([1, 2, 3], [4, 1, 1]), [2, 1]),
    ]

    make_ends_cases = [
        ((([1, 2, 3]),), [1, 3]),
        ((([1, 2, 3, 4]),), [1, 4]),
        ((([7, 4, 6, 2]),), [7, 2]),
        ((([1, 2, 2, 2, 2, 2, 2, 3]),), [1, 3]),
        ((([7, 4]),), [7, 4]),
        ((([7]),), [7, 7]),
        ((([5, 2, 9]),), [5, 9]),
        ((([2, 3, 4, 1]),), [2, 1]),
    ]

    has23_cases = [
        ((([2, 5]),), True),
        ((([4, 3]),), True),
        ((([4, 5]),), False),
        ((([2, 2]),), True),
        ((([3, 2]),), True),
        ((([3, 3]),), True),
        ((([7, 7]),), False),
        ((([3, 9]),), True),
        ((([9, 5]),), False),
    ]

    input = [
        (first_last6, first_last6_cases),
        (same_first_last, same_first_last_cases),
        (make_pi, make_pi_cases),
        (common_end, common_end_cases),
        (sum3, sum3_cases),
        (rotate_left3, rotate_left3_cases),
        (reverse3, reverse3_cases),
        (max_end3, max_end3_cases),
        (sum2, sum2_cases),
        (middle_way, middle_way_cases),
        (make_ends, make_ends_cases),
        (has23, has23_cases),
    ]

    check_problems(input)
