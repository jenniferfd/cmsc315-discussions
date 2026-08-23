# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation Documentation
I implemented a stack using a Python list and a queue using `collections.deque`.
For the stack, I completed the `push`, `pop`, `peek`, and `is_empty` operations. The stack demonstrated LIFO behavior because the most recently added item was the first item removed. I also tested edge cases by using `pop()` and `peek()` on an empty stack and verifying that a single-item stack became empty after removal.
For the queue, I completed the `enqueue`, `dequeue`, `front`, and `is_empty` operations. The queue demonstrated FIFO behavior because the first item added was the first item removed. I also tested empty queue operations and verified that a single-item queue became empty after removal.

## Real-World Applications
A stack can be used for browser history or an undo feature because the most recent action or page should be accessed first.
A queue can be used for customer service requests because the first request received should normally be handled first.

## Student-Created Example
I added a browser history example using a stack. The most recently visited page was removed first when going back, which demonstrated LIFO behavior in a real-world application.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
