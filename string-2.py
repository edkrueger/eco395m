def double_char(str):
    """
    Given a string, return a string where for every char in the original, there are two chars.


    double_char('The') → 'TThhee'
    double_char('AAbb') → 'AAAAbbbb'
    double_char('Hi-There') → 'HHii--TThheerree'"""
    return


def count_hi(str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.


    count_hi('abc hi ho') → 1
    count_hi('ABChi hi') → 2
    count_hi('hihi') → 2"""
    return


def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.


    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True"""
    return


def count_code(str):
    """
    Return the number of times that the string "code" appears anywhere in the given string, 
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.


    count_code('aaacodebbb') → 1
    count_code('codexxcode') → 2
    count_code('cozexxcope') → 2"""
    return


def end_other(str1, str2):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string, 
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
    Note: s.lower() returns the lowercase version of a string.


    end_other('Hiabc', 'abc') → True
    end_other('AbC', 'HiaBc') → True
    end_other('abc', 'abXabc') → True"""
    return


def xyz_there(str):
    """

    Return True if the given string contains an appearance of "xyz"
     where the xyz is not directly preceeded by a period (.). 
    So "xxyz" counts but "x.xyz" does not.


    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True"""
    return


if __name__ == "__main__":
    from _check import check_problems

    double_char_cases = [
        (("The",), "TThhee"),
        (("AAbb",), "AAAAbbbb"),
        (("Hi-There",), "HHii--TThheerree"),
        (("Word!",), "WWoorrdd!!"),
        (("!!",), "!!!!"),
        (("",), ""),
        (("a",), "aa"),
        ((".",), ".."),
        (("aa",), "aaaa"),
    ]

    count_hi_cases = [
        (("abc hi ho",), 1),
        (("ABChi hi",), 2),
        (("hihi",), 2),
        (("hiHIhi",), 2),
        (("",), 0),
        (("h",), 0),
        (("hi",), 1),
        (("Hi is no HI on ahI",), 0),
        (("hiho not HOHIhi",), 2),
    ]

    cat_dog_cases = [
        (("catdog",), True),
        (("catcat",), False),
        (("1cat1cadodog",), True),
        (("catxxdogxxxdog",), False),
        (("catxdogxdogxcat",), True),
        (("catxdogxdogxca",), False),
        (("dogdogcat",), False),
        (("dogogcat",), True),
        (("dog",), False),
        (("cat",), False),
        (("ca",), True),
        (("c",), True),
        (("",), True),
    ]

    count_code_cases = [
        (("aaacodebbb",), 1),
        (("codexxcode",), 2),
        (("cozexxcope",), 2),
        (("cozfxxcope",), 1),
        (("xxcozeyycop",), 1),
        (("cozcop",), 0),
        (("abcxyz",), 0),
        (("code",), 1),
        (("ode",), 0),
        (("c",), 0),
        (("",), 0),
        (("AAcodeBBcoleCCccoreDD",), 3),
        (("AAcodeBBcoleCCccorfDD",), 2),
        (("coAcodeBcoleccoreDD",), 3),
    ]

    end_other_cases = [
        (("Hiabc", "abc"), True),
        (("AbC", "HiaBc"), True),
        (("abc", "abXabc"), True),
        (("Hiabc", "abcd"), False),
        (("Hiabc", "bc"), True),
        (("Hiabcx", "bc"), False),
        (("abc", "abc"), True),
        (("xyz", "12xyz"), True),
        (("yz", "12xz"), False),
        (("Z", "12xz"), True),
        (("12", "12"), True),
        (("abcXYZ", "abcDEF"), False),
        (("ab", "ab12"), False),
        (("ab", "12ab"), True),
    ]

    xyz_there_cases = [
        (("abcxyz",), True),
        (("abc.xyz",), False),
        (("xyz.abc",), True),
        (("abcxy",), False),
        (("xyz",), True),
        (("xy",), False),
        (("x",), False),
        (("",), False),
        (("abc.xyzxyz",), True),
        (("abc.xxyz",), True),
        ((".xyz",), False),
        (("12.xyz",), False),
        (("12xyz",), True),
        (("1.xyz.xyz2.xyz",), False),
    ]

    input = [
        (double_char, double_char_cases),
        (count_hi, count_hi_cases),
        (cat_dog, cat_dog_cases),
        (count_code, count_code_cases),
        (end_other, end_other_cases),
        (xyz_there, xyz_there_cases),
    ]

    check_problems(input)
