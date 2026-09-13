# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation Documentation

I implemented both linear search and binary search in Python. The linear search checked each value from the beginning of the list until the target was found or the end of the list was reached. If the target was found, the method returned its index. If it was not found, the method returned `-1`.

I implemented binary search using a sorted list. The algorithm compared the target to the middle value and then reduced the remaining search area to either the left or right half. This process continued until the target was found or there were no values left to search.

I tested both algorithms using a small dataset and a larger dataset. The larger dataset helped show why binary search becomes more efficient as the amount of data increases. Linear search may need to check many values one at a time, while binary search repeatedly removes about half of the remaining search space.

I also tested edge cases, including an empty list, a single-element list, a missing value, and a target located at the end of the list.

## Real-World Application

A real-world example of search algorithms is a contact list. Linear search could be useful when the contacts are not sorted or when the list is small. Binary search could be more efficient when the contact list is sorted because it can quickly eliminate large portions of the list during each comparison.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.