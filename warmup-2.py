def string_times(str, n):
    """
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    string_times('Hi', 2) → 'HiHi'
    string_times('Hi', 3) → 'HiHiHi'
    string_times('Hi', 1) → 'Hi'
    """
    return


def front_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

    front_times('Chocolate', 2) → 'ChoCho'
    front_times('Chocolate', 3) → 'ChoChoCho'
    front_times('Abc', 3) → 'AbcAbcAbc'
    """
    return


def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

    string_bits('Hello') → 'Hlo'
    string_bits('Hi') → 'H'
    string_bits('Heeololeo') → 'Hello'"""
    return


def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".

    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'"""
    return


def last2(str):
    """
    Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

    last2('hixxhi') → 1
    last2('xaxxaxaxx') → 1
    last2('axxxaaxx') → 2"""
    return


def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) → 1
    array_count9([1, 9, 9]) → 2
    array_count9([1, 9, 9, 3, 9]) → 3
    """
    return


def array_front9(nums):
    """
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

    array_front9([1, 2, 9, 3, 4]) → True
    array_front9([1, 2, 3, 4, 9]) → False
    array_front9([1, 2, 3, 4, 5]) → False
    """
    return


def array123(nums):
    """
        Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


    array123([1, 1, 2, 3, 1]) → True
    array123([1, 1, 2, 4, 1]) → False
    array123([1, 1, 2, 1, 2, 3]) → True
    """
    return


def string_match(str1, str2):
    """

    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0
    """
    return


if __name__ == "__main__":
    from _check import check_problems

    string_times_cases = [
        (("Hi", 2), "HiHi"),
        (("Hi", 3), "HiHiHi"),
        (("Hi", 1), "Hi"),
        (("Hi", 0), ""),
        (("Hi", 5), "HiHiHiHiHi"),
        (("Oh Boy!", 2), "Oh Boy!Oh Boy!"),
        (("x", 4), "xxxx"),
        (("", 4), ""),
        (("code", 2), "codecode"),
        (("code", 3), "codecodecode"),
    ]

    front_times_cases = [
        (("Chocolate", 2), "ChoCho"),
        (("Chocolate", 3), "ChoChoCho"),
        (("Abc", 3), "AbcAbcAbc"),
        (("Ab", 4), "AbAbAbAb"),
        (("A", 4), "AAAA"),
        (("", 4), ""),
        (("Abc", 0), ""),
    ]

    string_bits_cases = [
        (("Hello",), "Hlo"),
        (("Hi",), "H"),
        (("Heeololeo",), "Hello"),
        (("HiHiHi",), "HHH"),
        (("",), ""),
        (("Greetings",), "Getns"),
        (("Chocoate",), "Coot"),
        (("pi",), "p"),
        (("Hello Kitten",), "HloKte"),
        (("hxaxpxpxy",), "happy"),
    ]

    string_splosion_cases = [
        (("Code",), "CCoCodCode"),
        (("abc",), "aababc"),
        (("ab",), "aab"),
        (("x",), "x"),
        (("fade",), "ffafadfade"),
        (("There",), "TThTheTherThere"),
        (("Kitten",), "KKiKitKittKitteKitten"),
        (("Bye",), "BByBye"),
        (("Good",), "GGoGooGood"),
        (("Bad",), "BBaBad"),
    ]

    last2_cases = [
        (("hixxhi",), 1),
        (("xaxxaxaxx",), 1),
        (("axxxaaxx",), 2),
        (("xxaxxaxxaxx",), 3),
        (("xaxaxaxx",), 0),
        (("xxxx",), 2),
        (("13121312",), 1),
        (("11212",), 1),
        (("13121311",), 0),
        (("1717171",), 2),
        (("hi",), 0),
        (("h",), 0),
        (("",), 0),
    ]

    array_count9_cases = [
        (([1, 2, 9],), 1),
        (([1, 9, 9],), 2),
        (([1, 9, 9, 3, 9],), 3),
        (([1, 2, 3],), 0),
        (([],), 0),
        (([4, 2, 4, 3, 1],), 0),
        (([9, 2, 4, 3, 1],), 1),
    ]

    array_front9_cases = [
        (([1, 2, 9, 3, 4],), True),
        (([1, 2, 3, 4, 9],), False),
        (([1, 2, 3, 4, 5],), False),
        (([9, 2, 3],), True),
        (([1, 9, 9],), True),
        (([1, 2, 3],), False),
        (([1, 9],), True),
        (([5, 5],), False),
        (([2],), False),
        (([9],), True),
        (([],), False),
        (([3, 9, 2, 3, 3],), True),
    ]

    array123_cases = [
        (([1, 1, 2, 3, 1],), True),
        (([1, 1, 2, 4, 1],), False),
        (([1, 1, 2, 1, 2, 3],), True),
        (([1, 1, 2, 1, 2, 1],), False),
        (([1, 2, 3, 1, 2, 3],), True),
        (([1, 2, 3],), True),
        (([1, 1, 1],), False),
        (([1, 2],), False),
        (([1],), False),
        (([],), False),
    ]

    string_match_cases = [
        (("xxcaazz", "xxbaaz"), 3),
        (("abc", "abc"), 2),
        (("abc", "axc"), 0),
        (("hello", "he"), 1),
        (("he", "hello"), 1),
        (("h", "hello"), 0),
        (("", "hello"), 0),
        (("aabbccdd", "abbbxxd"), 1),
        (("aaxxaaxx", "iaxxai"), 3),
        (("iaxxai", "aaxxaaxx"), 3),
    ]

    input = [
        (string_times, string_times_cases),
        (front_times, front_times_cases),
        (string_bits, string_bits_cases),
        (string_splosion, string_splosion_cases),
        (last2, last2_cases),
        (array_count9, array_count9_cases),
        (array_front9, array_front9_cases),
        (array123, array123_cases),
        (string_match, string_match_cases),
    ]

    check_problems(input)
