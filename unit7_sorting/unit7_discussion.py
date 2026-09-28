"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Create a copy so the original list is not changed.
    sorted_list = lst.copy()

    # Bubble sort compares neighboring values and swaps them
    # when they are in the wrong order.
    n = len(sorted_list)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )
                swapped = True

        # If no swaps happened, the list is already sorted.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # A list with zero or one item is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two halves.
    midpoint = len(lst) // 2
    left_half = lst[:midpoint]
    right_half = lst[midpoint:]

    # Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []
    left_index = 0
    right_index = 0

    # Compare the current values from both lists and
    # add the smaller value to the result.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from either list.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 19, 88, 7, 31, 55, 23]

    print("Original list:", dataset1)
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort:", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    dataset2 = [64, 12, 91, 33, 5, 47, 28, 76]

    print("Original list:", dataset2)
    print("Bubble Sort:", bubble_sort(dataset2))
    print("Merge Sort:", merge_sort(dataset2))

    # Both algorithms should produce the same sorted result.
    print(
        "Results match:",
        bubble_sort(dataset2) == merge_sort(dataset2)
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty list should remain empty.
    empty_list = []
    print("Empty list with Bubble Sort:", bubble_sort(empty_list))
    print("Empty list with Merge Sort:", merge_sort(empty_list))

    # Edge case 2: An already sorted list should stay unchanged.
    sorted_list = [1, 2, 3, 4, 5]
    print("Already sorted with Bubble Sort:", bubble_sort(sorted_list))
    print("Already sorted with Merge Sort:", merge_sort(sorted_list))

    # Edge case 3: Duplicate values should remain in the result.
    duplicate_list = [8, 3, 8, 1, 3]
    print("Duplicates with Bubble Sort:", bubble_sort(duplicate_list))
    print("Duplicates with Merge Sort:", merge_sort(duplicate_list))


if __name__ == "__main__":
    main()