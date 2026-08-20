def best_first_search(graph, heuristic, start, goal):

    OPEN = [start]
    CLOSED = []
    traversal = []

    while OPEN:

        # Select the node with the smallest heuristic value
        x = min(OPEN, key=lambda node: heuristic[node])

        # Remove x from OPEN
        OPEN.remove(x)

        # Add x to traversal
        traversal.append(x)

        # Check if goal is reached
        if x == goal:
            print("Best First Search:", " → ".join(traversal))
            print("Goal found:", x)
            return

        # Add x to CLOSED
        CLOSED.append(x)

        # Generate children
        children = graph[x]

        # Add children to OPEN
        for child in children:
            if child not in OPEN and child not in CLOSED:
                OPEN.append(child)

    print("Goal not found")


# Graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Heuristic values
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 7,
    'F': 5,
    'G': 3,
    'H': 1,
    'I': 8
}

# Start and goal
best_first_search(graph, heuristic, 'A', 'H')