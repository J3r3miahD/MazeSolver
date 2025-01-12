# Maze Solver

This Python program solves a maze using **Breadth-First Search (BFS)**. It takes a 2D grid representing a maze, where 1 is an open path and 0 is an obstacle, and finds the shortest path from a start point to a destination point.

## Features

- **Breadth-First Search (BFS)** algorithm to find the shortest path.
- Tracks the path and minimum distance from the start point to the destination.
- Handles a maze represented by a 2D matrix.
- Checks for valid moves based on the constraints of the maze.

## Requirements

- Python 3.x

## How to Use

1. Define your maze as a 2D matrix, where:
   - `1` represents an open path.
   - `0` represents an obstacle.

2. Instantiate the `MazeSolver` class with the maze matrix.

3. Call the `solve()` method to find the shortest path between the start and destination coordinates.

4. Call the `results()` method to print the path and distance.

### Example

```python
if __name__ == '__main__':
    # Define the maze (0's are obstacles, 1's are open paths)
    m = [
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    # Initialize the maze solver
    maze = MazeSolver(m)

    # Solve the maze from (0, 0) to (5, 5)
    maze.solve(0, 0, 5, 5)

    # Print the results
    maze.results()

The distance from start to destination is: 10
The path from start to finish is: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
