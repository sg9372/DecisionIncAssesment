import unittest
from src.calculateNewRectangles import findNewIslands, processIsland

class test_calculateNewRectangles(unittest.TestCase):

    def test_singleRectangle(self):
        island = [[0, 3, 5, 0]]
        ans = findNewIslands(island)
        self.assertEqual(ans, [[[0, 3, 5, 0]]])

    def test_multipleRectangles_noZero(self):
        island = [[0, 5, 10, 0], [10, 4, 15, 0], [15, 3, 20, 0]]
        ans = findNewIslands(island)
        self.assertEqual(ans, [[[0, 5, 10, 0], [10, 4, 15, 0], [15, 3, 20, 0]]])

    def test_zeroHeightDelimiter(self):
        island = [[0, 5, 10, 0], [10, 4, 15, 0], [15, 0, 20, -3], [20, 3, 25, 0]]
        ans = findNewIslands(island)
        self.assertEqual(ans, [[[0, 5, 10, 0],[10, 4, 15, 0]],[[20, 3, 25, 0]]])

    def test_multipleIslands_withMultipleZeros(self):
        island = [[0, 5, 10, 0], [10, 0, 15, -3], [15, 4, 20, 0], [20, 0, 25, -3], [25, 1, 30, 0]]
        ans = findNewIslands(island)
        self.assertEqual(ans, [
            [[0, 5, 10, 0]], [[15, 4, 20, 0]], [[25, 1, 30, 0]]
        ])

    def test_emptyIsland(self):
        island = []
        ans = findNewIslands(island)
        self.assertEqual(ans, [])

    def test_basicProcessIsland(self):
        island = [[0, 2, 2, 0]]
        ans = processIsland(island, 0)
        print(ans)
        self.assertEqual(ans, [[0, 2, 2, 0]])

    def test_processIslandWithGap(self):
        island = [[0, 3, 2, 0], [2, 1, 4, 0], [4, 3, 6, 0]]
        ans = processIsland(island, 0)
        self.assertEqual(ans, [[0, 1, 6, 0], [0, 3, 2, 1], [4, 3, 6, 1]])

    def test_processIslandWithMultipleGaps(self):
        island = [[0, 4, 2, 0], [2, 1, 5, 0], [5, 3, 7, 0], [7, 2, 10, 0], [10, 1, 13, 0], [13, 4, 15, 0]]
        ans = processIsland(island, 0)
        self.assertEqual(ans, [[0, 1, 15, 0], [0, 4, 2, 1], [5, 2, 10, 1], [5, 3, 7, 2], [13, 4, 15, 1]])

    def test_endGaps(self):
        island = [[0, 1, 1, 0], [1, 4, 2, 0], [2, 1, 3, 0], [3, 4, 4, 0], [4, 1, 5, 0]]
        ans = processIsland(island, 0)
        self.assertEqual(ans, [[0, 1, 5, 0], [1, 4, 2, 1], [3, 4, 4, 1]])

    