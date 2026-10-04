# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

## Implementation Documentation

I created a campus-style graph using an adjacency list. Each building was represented as a node, and the connections between buildings were represented as edges.

I implemented Breadth-First Search using a queue and a visited set. The queue controlled the order in which nodes were explored, while the visited set prevented the same node from being processed more than once.

I tested the BFS traversal starting from the Library and then added a Bookstore to demonstrate how the traversal changed when the graph was updated.

I also tested multiple edge cases. I started the traversal from a different building, tested a missing starting node, and tested a graph containing only one node. The missing node returned an empty list instead of causing an error.

## Discussion Board Reflection

While completing this assignment, I learned how graphs can be represented with adjacency lists and how Breadth-First Search uses a queue to visit connected nodes. Building the graph helped me understand how each node can store a list of its neighbors. I also learned how a visited set prevents BFS from processing the same node multiple times.

The most challenging part was understanding how the queue controls the order of the traversal. At first, it was confusing to see why certain nodes were visited before others. Running the program with different starting nodes and edge cases helped me see that BFS explores nearby nodes first before moving farther away.

BFS and DFS both traverse graphs, but they do it differently. BFS explores nodes level by level using a queue, while DFS follows one path as far as possible before backtracking. BFS would be useful for finding nearby locations or the shortest path in an unweighted network. DFS could be useful for exploring game maps, file structures, or paths where going deeper into one branch first makes more sense.