"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Store the value held by this node.
        self.value = value

        # New nodes start without any children.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # The tree starts empty, so the root is None.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start the recursive insertion at the root.
        # Smaller values move left and larger values move right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # If this position is empty, create a new node here.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this implementation.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # Start searching from the root.
        # A BST can reduce the search space at each step by
        # moving left for smaller values or right for larger values.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If we reach an empty location, the value is not in the tree.
        if node is None:
            return False

        # If the current node matches, the value was found.
        if value == node.value:
            return True

        # Smaller values can only be in the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Larger values can only be in the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []

        # Start the traversal at the root.
        self._inorder_recursive(self.root, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # Stop when there is no node to visit.
        if node is None:
            return

        # Visit the left subtree first.
        self._inorder_recursive(node.left, values)

        # Visit the current node.
        values.append(node.value)

        # Visit the right subtree last.
        self._inorder_recursive(node.right, values)

        # Because smaller values are stored on the left and larger
        # values are stored on the right, in-order traversal produces
        # the BST values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    tree = BST()

    values = [50, 30, 70, 20, 40, 60, 80]

    print("Values inserted:", values)

    # Each comparison moves either left or right, reducing
    # the portion of the tree that needs to be searched.
    for value in values:
        tree.insert(value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits left, current, then right,
    # which produces values in sorted order for a BST.
    traversal = tree.inorder()
    print("In-order traversal:", traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # These values exist in the tree.
    print("Search for 40:", tree.search(40))
    print("Search for 70:", tree.search(70))

    # These values do not exist in the tree.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case: search an empty tree.
    empty_tree = BST()
    print("Search empty tree for 10:", empty_tree.search(10))

    # Edge case: insert a duplicate value.
    # Duplicate values are ignored by this implementation.
    tree.insert(50)
    print("Traversal after duplicate 50:", tree.inorder())


if __name__ == "__main__":
    main()