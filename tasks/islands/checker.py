from testing import TestError
from typing import List, Tuple


def test_from_str(test: str) -> List[List[int]]:
    return list(map(lambda x: list(map(int, x)), filter(None, test.split('\n'))))


def colorize_islands(grid: List[List[int]]) -> List[List[int]]:
    height = len(grid)
    width = len(grid[0])
    islands = [[0 for _ in range(width)] for _ in range(height)]
    def dfs(pos: Tuple[int, int], color: int):
        islands[pos[0]][pos[1]] = color
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            pos_x = pos[1] + dx
            pos_y = pos[0] + dy
            if 0 <= pos_x < width and 0 <= pos_y < height:
                if grid[pos_y][pos_x] == 1 and islands[pos_y][pos_x] == 0:
                    dfs((pos_y, pos_x), color)
    
    color_id = 2
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1 and islands[row][col] == 0:
                dfs((row, col), color_id)

                color_id += 1
    return islands


def type_check(grid: List[List[int]], grid2: List[List[int]]):
    height = len(grid)
    width = len(grid[0])
    if not isinstance(grid, list):
        raise TestError('Returned grid is not a list')
    if height != len(grid2):
        raise TestError('Invalid dimensions of grid: height does not match')
    for row in grid2:
        if not isinstance(row, list):
            raise TestError('Returned grid is not a list of lists')
        if width != len(row):
            raise TestError('Invalid dimensions of grid: width does not match')
        for field in row:
            if not isinstance(field, int):
                raise TestError('Returned grid contains non-int value')


def isomorphic(grid: List[List[int]], grid2: List[List[int]]):
    mapping = {}
    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            val2 = grid2[row_idx][col_idx]
            if val == 0:
                if val2 != 0:
                    raise TestError(f'Detected ground on ({row_idx}, {col_idx}), but it should be water')
            else:
                if val in mapping:
                    if val2 != mapping[val]:
                        raise TestError(f'Invalid number on ({row_idx}, {col_idx})')
                else:
                    if val2 == 0:
                        raise TestError(f'Detected water on ({row_idx}, {col_idx}), but it should be ground')
                    for _, mapped in mapping.items():
                        if mapped == val2:
                            raise TestError(f'Invalid number on ({row_idx}, {col_idx})')
                    mapping[val] = val2


def run_test(test: str, module):
    test = test_from_str(test)
    mark_islands = getattr(module, 'mark_islands')
    result = mark_islands(test)
    if result is None:
        raise TestError("Returned none")
    type_check(test, result)
    isomorphic(colorize_islands(test), result)
