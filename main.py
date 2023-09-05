from collections import deque


class MazeSolver:
    def __init__(self, matrix):
        # Initialize Variables
        self.matrix = matrix
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.path = []
        self.min_distance = float('-inf')
        # Directions Down (0,1), Up (0,-1), Left(-1,0), Right (1,0)
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]

    def is_valid(self, row, col):
        # Check if the next move is valid, between the range horizontally
        if row < 0 or row >= len(self.matrix):
            return False
        # Check if the next move is valid, between the range vertically
        if col < 0 or col >= len(self.matrix):
            return False
        # Check if location has been visited
        if self.visited[row][col]:
            return False
        # Check if location is an obstacle, 0 is an obstacle
        if self.matrix[row][col] == 0:
            return False
        return True

    def solve(self, i, j, destination_x, destination_y):

        # Initialize the queue
        queue = deque()
        self.visited[i][j] = True
        # Append variables to the queue
        queue.append((i, j, 0, [(i, j)]))

        while queue:
            # Implement queue
            i, j, dist, path = queue.popleft()
            # Break if you reached the destination
            if i == destination_x and j == destination_y:
                self.path = path
                self.min_distance = dist
                break
            # From location (i,j), find the next move, check if the move is valid
            # Update the queue
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]
                # Check if the next move is valid
                if self.is_valid(next_x, next_y):
                    # If valid mark location as visited,
                    # Increment the distance, add next location to the path
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1, path + [(next_x, next_y)]))

    def results(self):
        if self.min_distance != float('-inf'):
            print('The distance from start to destination', self.min_distance)
            print('The path from start to finish is: ', self.path)
        else:
            print('No feasible path from start to destination')


if __name__ == '__main__':
    m = [[1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 0, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1]
         ]

    maze = MazeSolver(m)
    maze.solve(0, 0, 5, 5)
    maze.results()


