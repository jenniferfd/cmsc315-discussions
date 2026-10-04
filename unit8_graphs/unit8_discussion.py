"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty list if the starting node does not exist.
    if start not in graph:
        return []

    visited = set()
    traversal_order = []

    # A queue is used because BFS visits nodes in the order
    # they are discovered, which creates level-by-level traversal.
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        # Add unvisited neighbors to the queue so they can
        # be processed after nodes that were discovered earlier.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Unlike DFS, which follows one path deeply before backtracking,
    # BFS explores all nearby nodes before moving farther away.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # The nodes represent campus buildings.
    # Each list contains the buildings directly connected by walking paths.
    graph = {
        "Library": ["Science Hall", "Cafeteria"],
        "Science Hall": ["Library", "Gym"],
        "Cafeteria": ["Library", "Dorm"],
        "Gym": ["Science Hall", "Student Center"],
        "Dorm": ["Cafeteria", "Student Center"],
        "Student Center": ["Gym", "Dorm"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    for building, neighbors in graph.items():
        print(building + ":", neighbors)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start = "Library"

    # BFS starts at Library, then visits its direct neighbors,
    # followed by buildings that are farther away.
    traversal = bfs(graph, start)

    print("Starting node:", start)
    print("BFS traversal:", traversal)

    # Add a new building and connect it to the Student Center.
    graph["Bookstore"] = ["Student Center"]
    graph["Student Center"].append("Bookstore")

    updated_traversal = bfs(graph, start)

    print("\nAfter adding Bookstore:")
    print("Updated BFS traversal:", updated_traversal)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Starting from a different building.
    # BFS still explores all reachable buildings from the new starting point.
    print("Starting from Gym:", bfs(graph, "Gym"))

    # Edge case 2: Missing starting node.
    # The function safely returns an empty list instead of causing an error.
    print("Missing start node:", bfs(graph, "Parking Garage"))

    # Edge case 3: A graph containing only one node.
    # BFS returns that single node because there are no neighbors to visit.
    single_node_graph = {
        "Library": []
    }

    print("Single-node graph:", bfs(single_node_graph, "Library"))


if __name__ == "__main__":
    main()