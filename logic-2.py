def make_bricks(small, big, goal):
    """
    We want to make a row of bricks that is goal inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Return True if it is possible to make the goal by choosing from the given bricks. 
    This is a little harder than it looks and can be done without any loops. 
    See also: Introduction to MakeBricks
    https://codingbat.com/doc/practice/makebricks-introduction.html


    make_bricks(3, 1, 8) → True
    make_bricks(3, 1, 9) → False
    make_bricks(3, 2, 10) → True
    """
    return


def lone_sum(a, b, c):
    """

    Given 3 int values, a b c, return their sum. 
    However, if one of the values is the same as another of the values, it does not count towards the sum.


    lone_sum(1, 2, 3) → 6
    lone_sum(3, 2, 3) → 2
    lone_sum(3, 3, 3) → 0
    """
    return


def lucky_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. 
    However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
    So for example, if b is 13, then both b and c do not count.


    lucky_sum(1, 2, 3) → 6
    lucky_sum(1, 2, 13) → 3
    lucky_sum(1, 13, 3) → 1
    """
    return


def no_teen_sum(a, b, c):
    """

    Given 3 int values, a b c, return their sum. 
    However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
    Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
    In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
    Define the helper below and at the same indent level as the main no_teen_sum().


    no_teen_sum(1, 2, 3) → 6
    no_teen_sum(2, 13, 1) → 3
    no_teen_sum(2, 1, 14) → 3"""
    return


def round_sum(a, b, c):
    """
    For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
    Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
    Given 3 ints, a b c, return the sum of their rounded values. 
    To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
    Write the helper entirely below and at the same indent level as round_sum().


    round_sum(16, 17, 18) → 60
    round_sum(12, 13, 14) → 30
    round_sum(6, 4, 4) → 10
    """
    return


def close_far(a, b, c):
    """
    Given three ints, a b c, 
    return True if one of b or c is "close" (differing from a by at most 1), while the other is "far",
     differing from both other values by 2 or more. 
     Note: abs(num) computes the absolute value of a number.


    close_far(1, 2, 10) → True
    close_far(1, 2, 3) → False
    close_far(4, 1, 3) → True"""
    return


def make_chocolate(small, big, goal):
    """
    We want make a package of goal kilos of chocolate. 
    We have small bars (1 kilo each) and big bars (5 kilos each). 
    Return the number of small bars to use, assuming we always use big bars before small bars. 
    Return -1 if it can't be done.


    make_chocolate(4, 1, 9) → 4
    make_chocolate(4, 1, 10) → -1
    make_chocolate(4, 1, 7) → 2
    """
    return


if __name__ == "__main__":
    from _check import check_problems

    make_bricks_cases = [
        ((3, 1, 8), True),
        ((3, 1, 9), False),
        ((3, 2, 10), True),
        ((3, 2, 8), True),
        ((3, 2, 9), False),
        ((6, 1, 11), True),
        ((6, 0, 11), False),
        ((1, 4, 11), True),
        ((0, 3, 10), True),
        ((1, 4, 12), False),
        ((3, 1, 7), True),
        ((1, 1, 7), False),
        ((2, 1, 7), True),
        ((7, 1, 11), True),
        ((7, 1, 8), True),
        ((7, 1, 13), False),
        ((43, 1, 46), True),
        ((40, 1, 46), False),
        ((40, 2, 47), True),
        ((40, 2, 50), True),
        ((40, 2, 52), False),
        ((22, 2, 33), False),
        ((0, 2, 10), True),
        ((1000000, 1000, 1000100), True),
        ((2, 1000000, 100003), False),
        ((20, 0, 19), True),
        ((20, 0, 21), False),
        ((20, 4, 51), False),
        ((20, 4, 39), True),
    ]

    lone_sum_cases = [
        ((1, 2, 3), 6),
        ((3, 2, 3), 2),
        ((3, 3, 3), 0),
        ((9, 2, 2), 9),
        ((2, 2, 9), 9),
        ((2, 9, 2), 9),
        ((2, 9, 3), 14),
        ((4, 2, 3), 9),
        ((1, 3, 1), 3),
    ]

    lucky_sum_cases = [
        ((1, 2, 3), 6),
        ((1, 2, 13), 3),
        ((1, 13, 3), 1),
        ((1, 13, 13), 1),
        ((6, 5, 2), 13),
        ((13, 2, 3), 0),
        ((13, 2, 13), 0),
        ((13, 13, 2), 0),
        ((9, 4, 13), 13),
        ((8, 13, 2), 8),
        ((7, 2, 1), 10),
        ((3, 3, 13), 6),
    ]

    no_teen_sum_cases = [
        ((1, 2, 3), 6),
        ((2, 13, 1), 3),
        ((2, 1, 14), 3),
        ((2, 1, 15), 18),
        ((2, 1, 16), 19),
        ((2, 1, 17), 3),
        ((17, 1, 2), 3),
        ((2, 15, 2), 19),
        ((16, 17, 18), 16),
        ((17, 18, 19), 0),
        ((15, 16, 1), 32),
        ((15, 15, 19), 30),
        ((15, 19, 16), 31),
        ((5, 17, 18), 5),
        ((17, 18, 16), 16),
        ((17, 19, 18), 0),
    ]

    round_sum_cases = [
        ((16, 17, 18), 60),
        ((12, 13, 14), 30),
        ((6, 4, 4), 10),
        ((4, 6, 5), 20),
        ((4, 4, 6), 10),
        ((9, 4, 4), 10),
        ((0, 0, 1), 0),
        ((0, 9, 0), 10),
        ((10, 10, 19), 40),
        ((20, 30, 40), 90),
        ((45, 21, 30), 100),
        ((23, 11, 26), 60),
        ((23, 24, 25), 70),
        ((25, 24, 25), 80),
        ((23, 24, 29), 70),
        ((11, 24, 36), 70),
        ((24, 36, 32), 90),
        ((14, 12, 26), 50),
        ((12, 10, 24), 40),
    ]

    close_far_cases = [
        ((1, 2, 10), True),
        ((1, 2, 3), False),
        ((4, 1, 3), True),
        ((4, 5, 3), False),
        ((4, 3, 5), False),
        ((-1, 10, 0), True),
        ((0, -1, 10), True),
        ((10, 10, 8), True),
        ((10, 8, 9), False),
        ((8, 9, 10), False),
        ((8, 9, 7), False),
        ((8, 6, 9), True),
    ]

    make_chocolate_cases = [
        ((4, 1, 9), 4),
        ((4, 1, 10), -1),
        ((4, 1, 7), 2),
        ((6, 2, 7), 2),
        ((4, 1, 5), 0),
        ((4, 1, 4), 4),
        ((5, 4, 9), 4),
        ((9, 3, 18), 3),
        ((3, 1, 9), -1),
        ((1, 2, 7), -1),
        ((1, 2, 6), 1),
        ((1, 2, 5), 0),
        ((6, 1, 10), 5),
        ((6, 1, 11), 6),
        ((6, 1, 12), -1),
        ((6, 1, 13), -1),
        ((6, 2, 10), 0),
        ((6, 2, 11), 1),
        ((6, 2, 12), 2),
        ((60, 100, 550), 50),
        ((1000, 1000000, 5000006), 6),
        ((7, 1, 12), 7),
        ((7, 1, 13), -1),
        ((7, 2, 13), 3),
    ]

    input = [
        (make_bricks, make_bricks_cases),
        (lone_sum, lone_sum_cases),
        (lucky_sum, lucky_sum_cases),
        (no_teen_sum, no_teen_sum_cases),
        (round_sum, round_sum_cases),
        (close_far, close_far_cases),
        (make_chocolate, make_chocolate_cases),
    ]

    check_problems(input)
