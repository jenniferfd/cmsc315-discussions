# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Implementation Documentation

I implemented Bubble Sort and Merge Sort in Python and tested both algorithms with multiple datasets. For Bubble Sort, I created a copy of the original list and compared neighboring values. When two values were out of order, I swapped them. I also added an early-stop condition so the algorithm could finish if no swaps occurred during a full pass.

For Merge Sort, I used recursion to divide the list into smaller halves until each section contained one or zero elements. I then merged the sorted halves back together by comparing values from each side and adding the smaller value to a new result list.

I tested both algorithms with two different unsorted datasets and confirmed that they produced the same sorted results. I also tested edge cases involving an empty list, an already sorted list, and duplicate values.

## Real-World Scenario

A real-world example of sorting is an online shopping platform that allows customers to organize products by price. A sorting algorithm can arrange product prices from lowest to highest so customers can quickly compare options. Merge Sort would be useful when working with large collections of products because it scales better than Bubble Sort as the amount of data increases.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.