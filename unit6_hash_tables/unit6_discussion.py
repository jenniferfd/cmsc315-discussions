"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # A Python dictionary behaves like a hash table by storing
    # data as key-value pairs. The key is used to quickly locate
    # the value associated with it.
    inventory = {}

    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 22
    inventory["P400"] = 6
    inventory["P500"] = 18

    print("Inventory after inserts:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionary lookups use the key to quickly retrieve its value.
    print("Quantity for P100:", inventory["P100"])
    print("Quantity for P300:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(inventory)

    # Assigning a new value to an existing key replaces
    # the old value instead of creating a duplicate key.
    inventory["P100"] = 20

    print("After updating P100:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:")
    print(inventory)

    # Removing a key deletes both the key and its associated value.
    del inventory["P200"]

    print("After deleting P200:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Safely look up a missing key.
    # The get() method returns None instead of causing an error.
    missing_lookup = inventory.get("P999")
    print("Lookup for missing P999:", missing_lookup)

    # Edge case 2: Safely delete a missing key.
    # Check for the key first so the program does not raise a KeyError.
    if "P999" in inventory:
        del inventory["P999"]
    else:
        print("P999 was not found, so nothing was deleted.")

    # Edge case 3: Updating a missing key creates a new entry.
    inventory["P600"] = 12
    print("After adding P600 through an update-style assignment:")
    print(inventory)


if __name__ == "__main__":
    main()