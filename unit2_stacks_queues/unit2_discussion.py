"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Stack is empty."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Queue is empty."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return "Queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding values to the stack:")
    for value in [10, 20, 30, 40]:
        stack.push(value)
        print(f"Pushed: {value}")

    print("\nTop value without removing it:", stack.peek())

    print("\nRemoving values to demonstrate LIFO:")
    while not stack.is_empty():
        print("Popped:", stack.pop())

    print("\nTrying to pop from an empty stack:")
    print(stack.pop())

    print("\nTrying to peek at an empty stack:")
    print(stack.peek())

    print("\nSingle-item stack test:")
    single_stack = Stack()
    single_stack.push(99)
    print("Popped:", single_stack.pop())
    print("Is the stack empty?", single_stack.is_empty())


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding values to the queue:")
    for value in [10, 20, 30, 40]:
        queue.enqueue(value)
        print(f"Enqueued: {value}")

    print("\nFront value without removing it:", queue.front())

    print("\nRemoving values to demonstrate FIFO:")
    while not queue.is_empty():
        print("Dequeued:", queue.dequeue())

    print("\nTrying to dequeue from an empty queue:")
    print(queue.dequeue())

    print("\nTrying to view the front of an empty queue:")
    print(queue.front())

    print("\nSingle-item queue test:")
    single_queue = Queue()
    single_queue.enqueue(99)
    print("Dequeued:", single_queue.dequeue())
    print("Is the queue empty?", single_queue.is_empty())

    print("\n=== CUSTOM EXAMPLE: BROWSER HISTORY ===")

    browser_history = Stack()

    browser_history.push("Homepage")
    browser_history.push("Products")
    browser_history.push("Shopping Cart")

    print("Current page:", browser_history.peek())

    print("Going back to:", browser_history.pop())
    print("Now on:", browser_history.peek())

if __name__ == "__main__":
    main()
