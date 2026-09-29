class Solution:
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        if (rows + cols - 1) % 2 == 1:
            return False

        if grid[0][0] == ")" or grid[rows - 1][cols - 1] == "(":
            return False

        memo = {}

        def dfs(row, col, count):
            count += 1 if grid[row][col] == "(" else -1

            if count < 0:
                return False

            remaining = (rows - row - 1) + (cols - col - 1)

            if count > remaining:
                return False

            if row == rows - 1 and col == cols - 1:
                return count == 0

            key = (row, col, count)

            if key in memo:
                return memo[key]

            result = False

            if row + 1 < rows:
                result = dfs(row + 1, col, count)

            if not result and col + 1 < cols:
                result = dfs(row, col + 1, count)

            memo[key] = result
            return result

        return dfs(0, 0, 0)
