"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    def insert_at(lst, index, value):
        """
        TODO (Student):
        Insert a value into the list at the specified index.

        Requirements:
        - Use a list operation to insert the value.
        - Add comments explaining what happens to existing elements
          after an insertion occurs.
        - Use comments to explain how insertion performance may vary depending on
          where the insertion occurs.
        """

    # Insert the new value at the requested index.
    lst.insert(index, value)

    # Elements at and after this index shift one position to the right.
    # Inserting near the beginning usually takes more work than inserting
    # near the end because more elements may need to be shifted.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    def delete_at(lst, index):
        """
        TODO (Student):
        Remove and return the value at the specified index.

        Requirements:
        - Validate that the index exists.
        - Return the removed value.
        - Return None if the index is invalid.
        - Add comments explaining why index validation and safe deletion are important.
        """

    # Check that the index is within the valid range before removing anything.
    if index < 0 or index >= len(lst):
        return None

    # Removing safely prevents an IndexError when the position does not exist.
    # pop() removes the item at the specified index and returns the removed value.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    def search_value(lst, value):
        """
        TODO (Student):
        Search for a value within the list.

        Requirements:
        - Return the index if the value is found.
        - Return -1 if the value is not found.
        - Add comments explaining why this is a linear search and why it scans sequentially.
        """

    # Check each item from the beginning of the list to the end.
    # This is a linear search because values are examined one at a time in sequence.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 when the value does not appear anywhere in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Start with a list containing several values.
    values = [10, 20, 30, 40]
    print("Original list:", values)

    # Insert a value at the beginning of the list.
    insert_at(values, 0, 5)
    print("After inserting 5 at the beginning:", values)

    # Insert a value in the middle of the list.
    insert_at(values, 3, 25)
    print("After inserting 25 in the middle:", values)

    # Insert a value at the end of the list.
    insert_at(values, len(values), 50)
    print("After inserting 50 at the end:", values)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first item and display what was removed.
    removed = delete_at(values, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", values)

    # Remove an item from the middle of the list.
    middle_index = len(values) // 2
    removed = delete_at(values, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", values)

    # Remove the last item in the list.
    removed = delete_at(values, len(values) - 1)
    print("Removed from end:", removed)
    print("Updated list:", values)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists in the list.
    result = search_value(values, 20)
    print("Index of 20:", result)

    # Search for a value that is not in the list.
    result = search_value(values, 99)
    print("Index of 99:", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Try deleting from an invalid index.
    invalid_delete = delete_at(values, 100)
    print("Deleting at invalid index returns:", invalid_delete)

    # Edge case 2: Insert into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 99)
    print("After inserting into an empty list:", empty_list)


if __name__ == "__main__":
    main()