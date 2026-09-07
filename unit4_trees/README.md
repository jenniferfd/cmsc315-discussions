# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.


## Implementation Documentation

I implemented a Binary Search Tree in Python using a `Node` class and a `BST` class. Each node stored a value along with references to its left and right child nodes. The tree started with an empty root and values were inserted recursively.

During insertion, smaller values were placed in the left subtree and larger values were placed in the right subtree. This ordering allowed the tree to reduce the search space as values were compared.

I also implemented recursive searching. The search checked the current node and then moved either left or right depending on whether the target value was smaller or larger. If the value was found, the method returned `True`; otherwise, it returned `False`.

For traversal, I implemented an in-order traversal that visited the left subtree, then the current node, and finally the right subtree. Because of the BST ordering rule, this produced the values in sorted order.

I also tested edge cases by searching an empty tree and inserting a duplicate value. In this implementation, duplicate values were ignored.

## Real-World Application

A Binary Search Tree can be used to organize employee records by employee ID. Smaller IDs can be stored in the left subtree and larger IDs in the right subtree. This structure can make searching more efficient when the tree remains reasonably balanced.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.