def insertion_sort(items):
    """Return a new list with items in ascending order, leaving the input unchanged."""
    sorted_items = list(items)

    for i in range(1, len(sorted_items)):
        current = sorted_items[i]
        j = i - 1

        while j >= 0 and current < sorted_items[j]:
            sorted_items[j + 1] = sorted_items[j]
            j -= 1

        sorted_items[j + 1] = current

    return sorted_items


def test_sorts_correctly():
    assert insertion_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]
    assert insertion_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert insertion_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []


def test_duplicates_and_negatives():
    assert insertion_sort([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
    assert insertion_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
    assert insertion_sort([-1, 5, 0, -3]) == [-3, -1, 0, 5]


def test_does_not_mutate_input():
    original = [5, 2, 4, 6, 1, 3]
    result = insertion_sort(original)
    assert result == [1, 2, 3, 4, 5, 6]
    assert original == [5, 2, 4, 6, 1, 3]


if __name__ == "__main__":
    test_sorts_correctly()
    test_duplicates_and_negatives()
    test_does_not_mutate_input()
    print("All tests passed.")
