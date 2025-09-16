def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday, and the parameter vacation
    is True if we are on vacation. We sleep in if it is not a weekday or we're on
    vacation. Return True if we sleep in.

    sleep_in(False, False) → True
    sleep_in(True, False) → False
    sleep_in(False, True) → True
    """
    return


def monkey_trouble(a_smile, b_smile):
    """
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
    if each is smiling. We are in trouble if they are both smiling or if neither
    of them is smiling. Return True if we are in trouble.

    monkey_trouble(True, True) → True
    monkey_trouble(False, False) → True
    monkey_trouble(True, False) → False
    """
    return


def sum_double(a, b):
    """
    Given two int values, return their sum. Unless the two values are the same,
    then return double their sum.

    sum_double(1, 2) → 3
    sum_double(3, 2) → 5
    sum_double(2, 2) → 8
    """
    return


def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return
    double the absolute difference if n is over 21.

    diff21(19) → 2
    diff21(10) → 11
    diff21(21) → 0
    """
    return


def parrot_trouble(talking, hour):
    """
    We have a loud talking parrot. The "hour" parameter is the current hour time
    in the range 0..23. We are in trouble if the parrot is talking and the hour
    is before 7 or after 20. Return True if we are in trouble.

    parrot_trouble(True, 6) → True
    parrot_trouble(True, 7) → False
    parrot_trouble(False, 6) → False
    """
    return


def makes10(a, b):
    """
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

    makes10(9, 10) → True
    makes10(9, 9) → False
    makes10(1, 9) → True
    """
    return


def near_hundred(n):
    """
    Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

    near_hundred(93) → True
    near_hundred(90) → True
    near_hundred(89) → False
    """
    return


def pos_neg(a, b, negative):
    """
    Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

    pos_neg(1, -1, False) → True
    pos_neg(-1, 1, False) → True
    pos_neg(-4, -5, True) → True
    """
    return


def not_string(str):
    """
    Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

    not_string('candy') → 'not candy'
    not_string('x') → 'not x'
    not_string('not bad') → 'not bad'
    """
    return


def missing_char(str, n):
    """
    Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

    missing_char('kitten', 1) → 'ktten'
    missing_char('kitten', 0) → 'itten'
    missing_char('kitten', 4) → 'kittn'
    """
    return


def front_back(str):
    """
    Given a string, return a new string where the first and last chars have been exchanged.

    front_back('code') → 'eodc'
    front_back('a') → 'a'
    front_back('ab') → 'ba'
    """
    return


def front3(str):
    """
    Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

    front3('Java') → 'JavJavJav'
    front3('Chocolate') → 'ChoChoCho'
    front3('abc') → 'abcabcabc'
    """
    return


if __name__ == "__main__":
    from _check import check_problems

    sleep_in_cases = [
        ((False, False), True),
        ((True, False), False),
        ((False, True), True),
        ((True, True), True),
    ]

    monkey_trouble_cases = [
        ((True, True), True),
        ((False, False), True),
        ((True, False), False),
        ((False, True), False),
    ]

    sum_double_cases = [
        ((1, 2), 3),
        ((3, 2), 5),
        ((2, 2), 8),
        ((-1, 0), -1),
        ((0, 0), 0),
        ((0, 1), 1),
        ((3, 4), 7),
    ]

    diff21_cases = [
        ((19,), 2),
        ((10,), 11),
        ((21,), 0),
        ((22,), 2),
        ((25,), 8),
        ((30,), 18),
        ((0,), 21),
        ((2,), 19),
        ((-1,), 22),
        ((-2,), 23),
        ((50,), 58),
    ]

    parrot_trouble_cases = [
        ((True, 6), True),
        ((True, 7), False),
        ((False, 6), False),
        ((True, 21), True),
        ((False, 21), False),
        ((False, 20), False),
        ((True, 23), True),
        ((False, 23), False),
        ((True, 20), False),
        ((False, 12), False),
    ]

    makes10_cases = [
        ((9, 10), True),
        ((9, 9), False),
        ((1, 9), True),
        ((10, 1), True),
        ((10, 10), True),
        ((8, 2), True),
        ((8, 3), False),
        ((10, 42), True),
        ((12, -2), True),
    ]

    near_hundred_cases = [
        ((93,), True),
        ((90,), True),
        ((89,), False),
        ((110,), True),
        ((111,), False),
        ((121,), False),
        ((-101,), False),
        ((-209,), False),
        ((190,), True),
        ((209,), True),
        ((0,), False),
        ((5,), False),
        ((-50,), False),
        ((191,), True),
        ((189,), False),
        ((200,), True),
        ((210,), True),
        ((211,), False),
        ((290,), False),
    ]

    pos_neg_cases = [
        ((1, -1, False), True),
        ((-1, 1, False), True),
        ((-4, -5, True), True),
        ((-4, -5, False), False),
        ((-4, 5, False), True),
        ((-4, 5, True), False),
        ((1, 1, False), False),
        ((-1, -1, False), False),
        ((1, -1, True), False),
        ((-1, 1, True), False),
        ((1, 1, True), False),
        ((-1, -1, True), True),
        ((5, -5, False), True),
        ((-6, 6, False), True),
        ((-5, -6, False), False),
        ((-2, -1, False), False),
        ((1, 2, False), False),
        ((-5, 6, True), False),
        ((-5, -5, True), True),
    ]

    not_string_cases = [
        (("candy",), "not candy"),
        (("x",), "not x"),
        (("not bad",), "not bad"),
        (("bad",), "not bad"),
        (("not",), "not"),
        (("is not",), "not is not"),
        (("no",), "not no"),
    ]

    missing_char_cases = [
        (("kitten", 1), "ktten"),
        (("kitten", 0), "itten"),
        (("kitten", 4), "kittn"),
        (("Hi", 0), "i"),
        (("Hi", 1), "H"),
        (("code", 0), "ode"),
        (("code", 1), "cde"),
        (("code", 2), "coe"),
        (("code", 3), "cod"),
        (("chocolate", 8), "chocolat"),
    ]

    front_back_cases = [
        (("code",), "eodc"),
        (("a",), "a"),
        (("ab",), "ba"),
        (("abc",), "cba"),
        (("",), ""),
        (("Chocolate",), "ehocolatC"),
        (("aavJ",), "Java"),
        (("hello",), "oellh"),
    ]

    front3_cases = [
        (("Java",), "JavJavJav"),
        (("Chocolate",), "ChoChoCho"),
        (("abc",), "abcabcabc"),
        (("abcXYZ",), "abcabcabc"),
        (("ab",), "ababab"),
        (("a",), "aaa"),
        (("",), ""),
    ]

    input = [
        (sleep_in, sleep_in_cases),
        (monkey_trouble, monkey_trouble_cases),
        (sum_double, sum_double_cases),
        (diff21, diff21_cases),
        (parrot_trouble, parrot_trouble_cases),
        (makes10, makes10_cases),
        (near_hundred, near_hundred_cases),
        (pos_neg, pos_neg_cases),
        (not_string, not_string_cases),
        (missing_char, missing_char_cases),
        (front_back, front_back_cases),
        (front3, front3_cases),
    ]

    check_problems(input)
