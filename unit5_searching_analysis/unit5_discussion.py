"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check each item from the beginning of the list to the end.
    # In the worst case, every element may need to be checked,
    # which gives linear search O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 if the target does not appear in the list.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        # Return the index if the middle value matches the target.
        if lst[middle] == target:
            return middle

        # If the target is larger, discard the left half.
        if lst[middle] < target:
            left = middle + 1

        # If the target is smaller, discard the right half.
        else:
            right = middle - 1

        # Each loop removes about half of the remaining search area,
        # which is why binary search has O(log n) time complexity.

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_data = [10, 20, 30, 40, 50, 60, 70]

    print("Small dataset:", small_data)

    # Search for a value that exists.
    print("Linear search for 40:", linear_search(small_data, 40))
    print("Binary search for 40:", binary_search(small_data, 40))

    # Search for a value that does not exist.
    print("Linear search for 45:", linear_search(small_data, 45))
    print("Binary search for 45:", binary_search(small_data, 45))

    # Both methods return the correct index when a value exists
    # and return -1 when the value is missing.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(1, 1001))

    print("Large dataset size:", len(large_data))

    # Search near the end of the dataset.
    print("Linear search for 999:", linear_search(large_data, 999))
    print("Binary search for 999:", binary_search(large_data, 999))

    # Linear search may need to check many values one at a time.
    # Binary search repeatedly cuts the remaining search area in half,
    # so the performance difference becomes more noticeable
    # as the dataset grows.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    empty_list = []
    print("Linear search empty list:", linear_search(empty_list, 10))
    print("Binary search empty list:", binary_search(empty_list, 10))

    # Both searches safely return -1 because there is no data.

    # Edge case 2: Single-element list.
    single_item = [81]
    print("Linear search single item:", linear_search(single_item, 81))
    print("Binary search single item:", binary_search(single_item, 81))

    # Both searches return index 0 because the target is the only item.

    # Edge case 3: Target at the last position.
    print("Linear search last item:", linear_search(small_data, 70))
    print("Binary search last item:", binary_search(small_data, 70))


if __name__ == "__main__":
    main()
