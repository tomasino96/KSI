class Grid2D:
    def __init__(self, values: list[list[int]]) -> None:
        self.height = len(values)
        self.width = len(values[0])
        self.grid = values

    def __add__(self, other: "Grid2D"):
        min_height = min(self.height, other.height)
        min_width = min(self.width, other.width)

        new_grid = [
            [
                self.grid[row][col] + other.grid[row][col] for col in range(min_width)
            ]
            for row in range(min_height)
        ]
        return Grid2D(new_grid)
    
    def __pow__(self, other: "Grid2D"):
        min_height = min(self.height, other.height)
        min_width = min(self.width, other.width)

        new_grid = [
            [
                self.grid[row][col] ** other.grid[row][col] for col in range(min_width)
            ]
            for row in range(min_height)
        ]
        return Grid2D(new_grid)
    
    def __eq__(self, other: "Grid2D"):
        min_height = min(self.height, other.height)
        min_width = min(self.width, other.width)

        for row in range(min_height):
            for col in range(min_width):
                if self.grid[row][col] != other.grid[row][col]:
                    return False
        return True
    
    def __contains__(self, other: "Grid2D"):
        for row in range(self.height - other.height + 1):
            for col in range(self.width - other.width + 1):
                match = True
                for other_row in range(other.height):
                    for other_col in range(other.width):
                        if self.grid[row + other_row][col + other_col] != other.grid[other_row][other_col]:
                            match = False
                            break
                    if not match:
                        break
                if match:
                    return True
        return False


# Základní testy:
grid1 = Grid2D([[1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [3, 4, 5, 6, 7],
                [4, 5, 6, 7, 8]])
grid2 = Grid2D([[1, 1, 1, 1, 1]])

print((grid1 + grid2).grid)
print((grid1 ** grid1).grid)
print(grid1 == grid1)

print(Grid2D([[1, 2], [2, 3]]) in grid1)