class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        return_count = 0
        row_freq = {}

        for row in grid:
            row_tuple = tuple(row)
            row_freq[row_tuple] = row_freq.get(row_tuple, 0) + 1

        for col in range(grid_len):
            col_tuple = tuple(grid[i][col] for i in range(grid_len))
            return_count += row_freq.get(col_tuple, 0)

        return return_count
