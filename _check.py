import sys


def check_case(function, args, correct_result):
    result = function(*args)
    is_correct = result == correct_result
    status_msg = "Case Correct!" if is_correct else "Case WRONG!"
    expected = f"Expected: {function.__name__}{args} → {correct_result}"
    run = f"Run: {result}"
    print(f"{status_msg} | {expected} | {run}")
    return is_correct


def check_problem(function, cases):
    print(f"Results for problem {function.__name__}")
    print("*" * 50)
    num_cases = len(cases)
    num_correct = 0
    for args, correct_result in cases:
        if check_case(function, args, correct_result):
            num_correct += 1
    is_complete = num_correct == num_cases
    status_msg = "Problem Complete!" if is_complete else "Problem Incomplete"
    print("*" * 50)
    print(f"{status_msg} | {num_correct} out of {num_cases} cases")
    return is_complete


def check_problems(input):
    print("=" * 100)
    print(f"Results for Problem Set {sys.argv[0]}")
    print("=" * 100)
    num_problems = len(input)
    num_correct = 0
    for function, cases in input:
        if check_problem(function, cases):
            num_correct += 1
    print("=" * 100)
    print(f"{num_correct} out of {num_problems} problems")
    print("=" * 100)
