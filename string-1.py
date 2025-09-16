def hello_name(str):
    """
        Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


    hello_name('Bob') → 'Hello Bob!'
    hello_name('Alice') → 'Hello Alice!'
    hello_name('X') → 'Hello X!'
    """
    return


def make_abba(str1, str2):
    """
    Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


    make_abba('Hi', 'Bye') → 'HiByeByeHi'
    make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
    make_abba('What', 'Up') → 'WhatUpUpWhat'
    """
    return


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
    In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


    make_tags('i', 'Yay') → '<i>Yay</i>'
    make_tags('i', 'Hello') → '<i>Hello</i>'
    make_tags('cite', 'Yay') → '<cite>Yay</cite>'
    """
    return


def make_out_word(out, word):
    """
        Given an "out" string length 4, such as "<<>>", and a word, 
        return a new string where the word is in the middle of the out string, e.g. "<<word>>".


    make_out_word('<<>>', 'Yay') → '<<Yay>>'
    make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
    make_out_word('[[]]', 'word') → '[[word]]'
    """
    return


def extra_end(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
    The string length will be at least 2.


    extra_end('Hello') → 'lololo'
    extra_end('ab') → 'ababab'
    extra_end('Hi') → 'HiHiHi'

    """
    return


def first_two(str):
    """
    Given a string, return the string made of its first two chars, 
    so the String "Hello" yields "He". If the string is shorter than length 2, 
    return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


    first_two('Hello') → 'He'
    first_two('abcdefg') → 'ab'
    first_two('ab') → 'ab'
    """
    return


def first_half(str):
    """
    Given a string of even length, return the first half. 
    So the string "WooHoo" yields "Woo".


    first_half('WooHoo') → 'Woo'
    first_half('HelloThere') → 'Hello'
    first_half('abcdef') → 'abc'
    """
    return


def without_end(str):
    """
        Given a string, return a version without the first and last char, 
        so "Hello" yields "ell". The string length will be at least 2.


    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'
    """
    return


def combo_string(str1, str2):
    """
    Given 2 strings, a and b, return a string of the form short+long+short, 
    with the shorter string on the outside and the longer string on the inside. 
    The strings will not be the same length, but they may be empty (length 0).


    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    """
    return


def non_start(str1, str2):
    """
    Given 2 strings, return their concatenation, 
    except omit the first char of each. 
    The strings will be at least length 1.


    non_start('Hello', 'There') → 'ellohere'
    non_start('java', 'code') → 'avaode'
    non_start('shotl', 'java') → 'hotlava'

    """
    return


def left2(str):
    """
    Given a string, return a "rotated left 2" version 
    where the first 2 chars are moved to the end. 
    The string length will be at least 2.


    left2('Hello') → 'lloHe'
    left2('java') → 'vaja'
    left2('Hi') → 'Hi'
    """
    return


if __name__ == "__main__":
    from _check import check_problems

    hello_name_cases = [
        ((("Bob"),), "Hello Bob!"),
        ((("Alice"),), "Hello Alice!"),
        ((("X"),), "Hello X!"),
        ((("Dolly"),), "Hello Dolly!"),
        ((("Alpha"),), "Hello Alpha!"),
        ((("Omega"),), "Hello Omega!"),
        ((("Goodbye"),), "Hello Goodbye!"),
        ((("ho ho ho"),), "Hello ho ho ho!"),
        ((("xyz!"),), "Hello xyz!!"),
        ((("Hello"),), "Hello Hello!"),
    ]

    make_abba_cases = [
        (("Hi", "Bye"), "HiByeByeHi"),
        (("Yo", "Alice"), "YoAliceAliceYo"),
        (("What", "Up"), "WhatUpUpWhat"),
        (("aaa", "bbb"), "aaabbbbbbaaa"),
        (("x", "y"), "xyyx"),
        (("x", ""), "xx"),
        (("", "y"), "yy"),
        (("Bo", "Ya"), "BoYaYaBo"),
        (("Ya", "Ya"), "YaYaYaYa"),
    ]

    make_tags_cases = [
        (("i", "Yay"), "<i>Yay</i>"),
        (("i", "Hello"), "<i>Hello</i>"),
        (("cite", "Yay"), "<cite>Yay</cite>"),
        (("address", "here"), "<address>here</address>"),
        (("body", "Heart"), "<body>Heart</body>"),
        (("i", "i"), "<i>i</i>"),
        (("i", ""), "<i></i>"),
    ]

    make_out_word_cases = [
        (("<<>>", "Yay"), "<<Yay>>"),
        (("<<>>", "WooHoo"), "<<WooHoo>>"),
        (("[[]]", "word"), "[[word]]"),
        (("HHoo", "Hello"), "HHHellooo"),
        (("abyz", "YAY"), "abYAYyz"),
    ]

    extra_end_cases = [
        ((("Hello"),), "lololo"),
        ((("ab"),), "ababab"),
        ((("Hi"),), "HiHiHi"),
        ((("Candy"),), "dydydy"),
        ((("Code"),), "dedede"),
    ]

    first_two_cases = [
        ((("Hello"),), "He"),
        ((("abcdefg"),), "ab"),
        ((("ab"),), "ab"),
        ((("a"),), "a"),
        (((""),), ""),
        ((("Kitten"),), "Ki"),
        ((("hi"),), "hi"),
        ((("hiya"),), "hi"),
    ]

    first_half_cases = [
        ((("WooHoo"),), "Woo"),
        ((("HelloThere"),), "Hello"),
        ((("abcdef"),), "abc"),
        ((("ab"),), "a"),
        (((""),), ""),
        ((("0123456789"),), "01234"),
        ((("kitten"),), "kit"),
    ]

    without_end_cases = [
        ((("Hello"),), "ell"),
        ((("java"),), "av"),
        ((("coding"),), "odin"),
        ((("code"),), "od"),
        ((("ab"),), ""),
        ((("Chocolate!"),), "hocolate"),
        ((("kitten"),), "itte"),
        ((("woohoo"),), "ooho"),
    ]

    combo_string_cases = [
        (("Hello", "hi"), "hiHellohi"),
        (("hi", "Hello"), "hiHellohi"),
        (("aaa", "b"), "baaab"),
        (("b", "aaa"), "baaab"),
        (("aaa", ""), "aaa"),
        (("", "bb"), "bb"),
        (("aaa", "1234"), "aaa1234aaa"),
        (("aaa", "bb"), "bbaaabb"),
        (("a", "bb"), "abba"),
        (("bb", "a"), "abba"),
        (("xyz", "ab"), "abxyzab"),
    ]

    non_start_cases = [
        (("Hello", "There"), "ellohere"),
        (("java", "code"), "avaode"),
        (("shotl", "java"), "hotlava"),
        (("ab", "xy"), "by"),
        (("ab", "x"), "b"),
        (("x", "ac"), "c"),
        (("a", "x"), ""),
        (("kit", "kat"), "itat"),
        (("mart", "dart"), "artart"),
    ]

    left2_cases = [
        ((("Hello"),), "lloHe"),
        ((("java"),), "vaja"),
        ((("Hi"),), "Hi"),
        ((("code"),), "deco"),
        ((("cat"),), "tca"),
        ((("12345"),), "34512"),
        ((("Chocolate"),), "ocolateCh"),
        ((("bricks"),), "icksbr"),
    ]
    input = [
        (hello_name, hello_name_cases),
        (make_abba, make_abba_cases),
        (make_tags, make_tags_cases),
        (make_out_word, make_out_word_cases),
        (extra_end, extra_end_cases),
        (first_two, first_two_cases),
        (first_half, first_half_cases),
        (without_end, without_end_cases),
        (combo_string, combo_string_cases),
        (non_start, non_start_cases),
        (left2, left2_cases),
    ]

    check_problems(input)
