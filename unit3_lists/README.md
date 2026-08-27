# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Implementation Documentation

I implemented list insertion, deletion, and search operations using Python lists. For insertion, I used the `insert()` method to place values at the beginning, middle, and end of the list. I observed that inserting near the beginning or middle can require existing elements to shift to the right, while inserting at the end usually requires less shifting.

I implemented deletion by validating the index before removing an item. If the index was valid, I used `pop()` to remove and return the value. If the index was invalid, the function returned `None` so the program could avoid an `IndexError`.

For searching, I implemented a linear search that checked each element in order until the requested value was found. The function returned the matching index or `-1` when the value was not present.

I also tested edge cases, including deleting from an invalid index and inserting into an empty list.

## Real-World Application

A Python list can be used to manage a music playlist. Songs can be inserted at different positions, removed when they are no longer wanted, and searched to find their location in the playlist. This example demonstrates how list operations can support dynamic collections in real-world software.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
