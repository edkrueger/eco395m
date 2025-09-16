def cigar_party(cigars, is_weekend):
    """

    When squirrels get together for a party, they like to have cigars.
    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
    Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
    Return True if the party with the given values is successful, or False otherwise.


    cigar_party(30, False) → False
    cigar_party(50, False) → True
    cigar_party(70, True) → True
    """
    return


def date_fashion(you, date):
    """

    You and your date are trying to get a table at a restaurant. 
    The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. 
    The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
    If either of you is very stylish, 8 or more, then the result is 2 (yes). 
    With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
    Otherwise the result is 1 (maybe).


    date_fashion(5, 10) → 2
    date_fashion(5, 2) → 0
    date_fashion(5, 5) → 1
    """
    return


def squirrel_play(temp, is_summer):
    """The squirrels in Palo Alto spend most of the day playing. 
    In particular, they play if the temperature is between 60 and 90 (inclusive). 
    Unless it is summer, then the upper limit is 100 instead of 90. 
    Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


    squirrel_play(70, False) → True
    squirrel_play(95, False) → False
    squirrel_play(95, True) → True"""
    return


def caught_speeding(speed, is_birthday):
    """
    You are driving a little too fast, and a police officer stops you. 
    Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
    If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
    If speed is 81 or more, the result is 2. 
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.


    caught_speeding(60, False) → 0
    caught_speeding(65, False) → 1
    caught_speeding(65, True) → 0"""
    return


def sorta_sum(a, b):
    """
    Given 2 ints, a and b, return their sum. 
    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21"""
    return


def alarm_clock(day, vacation):
    """

    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
    return a string of the form "7:00" indicating when the alarm clock should ring. 
    Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


    alarm_clock(1, False) → '7:00'
    alarm_clock(5, False) → '7:00'
    alarm_clock(0, False) → '10:00'"""
    return


def love6(a, b):
    """
    The number 6 is a truly great number. 
    Given two int values, a and b, return True if either one is 6. 
    Or if their sum or difference is 6. 
    Note: the function abs(num) computes the absolute value of a number.


    love6(6, 4) → True
    love6(4, 5) → False
    love6(1, 5) → True"""
    return


def in1to10(n, outside_mode):
    """
    Given a number n, return True if n is in the range 1..10, inclusive. 
    Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


    in1to10(5, False) → True
    in1to10(11, False) → False
    in1to10(11, True) → True"""
    return


def near_ten(num):
    """
    Given a non-negative number "num", 
    return True if num is within 2 of a multiple of 10. 
    Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. 
    Hint: mod functions
    https://codingbat.com/doc/practice/mod-introduction.html

    near_ten(12) → True
    near_ten(17) → False
    near_ten(19) → True"""
    return


if __name__ == "__main__":
    from _check import check_problems

    cigar_party_cases = [
        ((30, False), False),
        ((50, False), True),
        ((70, True), True),
        ((30, True), False),
        ((50, True), True),
        ((60, False), True),
        ((61, False), False),
        ((40, False), True),
        ((39, False), False),
        ((40, True), True),
        ((39, True), False),
    ]

    date_fashion_cases = [
        ((5, 10), 2),
        ((5, 2), 0),
        ((5, 5), 1),
        ((3, 3), 1),
        ((10, 2), 0),
        ((2, 9), 0),
        ((9, 9), 2),
        ((10, 5), 2),
        ((2, 2), 0),
        ((3, 7), 1),
        ((2, 7), 0),
        ((6, 2), 0),
    ]

    squirrel_play_cases = [
        ((70, False), True),
        ((95, False), False),
        ((95, True), True),
        ((90, False), True),
        ((90, True), True),
        ((50, False), False),
        ((50, True), False),
        ((100, False), False),
        ((100, True), True),
        ((105, True), False),
        ((59, False), False),
        ((59, True), False),
        ((60, False), True),
    ]

    caught_speeding_cases = [
        ((60, False), 0),
        ((65, False), 1),
        ((65, True), 0),
        ((80, False), 1),
        ((85, False), 2),
        ((85, True), 1),
        ((70, False), 1),
        ((75, False), 1),
        ((75, True), 1),
        ((40, False), 0),
        ((40, True), 0),
        ((90, False), 2),
    ]

    sorta_sum_cases = [
        ((3, 4), 7),
        ((9, 4), 20),
        ((10, 11), 21),
        ((12, -3), 9),
        ((-3, 12), 9),
        ((4, 5), 9),
        ((4, 6), 20),
        ((14, 7), 21),
        ((14, 6), 20),
    ]

    alarm_clock_cases = [
        ((1, False), "7:00"),
        ((5, False), "7:00"),
        ((0, False), "10:00"),
        ((6, False), "10:00"),
        ((0, True), "off"),
        ((6, True), "off"),
        ((1, True), "10:00"),
        ((3, True), "10:00"),
        ((5, True), "10:00"),
    ]

    love6_cases = [
        ((6, 4), True),
        ((4, 5), False),
        ((1, 5), True),
        ((1, 6), True),
        ((1, 8), False),
        ((1, 7), True),
        ((7, 5), False),
        ((8, 2), True),
        ((6, 6), True),
        ((-6, 2), False),
        ((-4, -10), True),
        ((-7, 1), False),
        ((7, -1), True),
        ((-6, 12), True),
        ((-2, -4), False),
        ((7, 1), True),
        ((0, 9), False),
        ((8, 3), False),
        ((3, 3), True),
        ((3, 4), False),
    ]

    in1to10_cases = [
        ((5, False), True),
        ((11, False), False),
        ((11, True), True),
        ((10, False), True),
        ((10, True), True),
        ((9, False), True),
        ((9, True), False),
        ((1, False), True),
        ((1, True), True),
        ((0, False), False),
        ((0, True), True),
        ((-1, False), False),
        ((-1, True), True),
        ((99, False), False),
        ((-99, True), True),
    ]

    near_ten_cases = [
        (((12),), True),
        (((17),), False),
        (((19),), True),
        (((31),), True),
        (((6),), False),
        (((10),), True),
        (((11),), True),
        (((21),), True),
        (((22),), True),
        (((23),), False),
        (((54),), False),
        (((155),), False),
        (((158),), True),
        (((3),), False),
        (((1),), True),
    ]

    input = [
        (cigar_party, cigar_party_cases),
        (date_fashion, date_fashion_cases),
        (squirrel_play, squirrel_play_cases),
        (caught_speeding, caught_speeding_cases),
        (sorta_sum, sorta_sum_cases),
        (alarm_clock, alarm_clock_cases),
        (love6, love6_cases),
        (in1to10, in1to10_cases),
        (near_ten, near_ten_cases),
    ]

    check_problems(input)
