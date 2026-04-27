# Boggle Solver Tests
import unittest
import sys
from boggle_solver import Boggle

# Module level imports should be at the top
sys.path.append("/home/codio/workspace/")


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    # ADD 4x4, 5x5, 6x6, 7x7...13x13, and LARGER Dictionaries
    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_large_dictionary_small_grid(self):
        grid = [["A", "B"], ["C", "D"]]
        # Large dictionary where only one word exists in grid
        dictionary = [str(i) for i in range(1000)] + ["ABD"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(mygame.getSolution(), ["ABD"])

    def test_13x13_grid_performance(self):
        # Create a 13x13 grid of all 'A's
        grid = [["A"] * 13 for _ in range(13)]
        dictionary = ["AAAAA", "BBBBB"]
        mygame = Boggle(grid, dictionary)
        # This checks if your prefix pruning is actually working
        # to prevent a timeout/infinite recursion
        self.assertEqual(mygame.getSolution(), ["AAAAA"])


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    # ADD MANY SIMPLE TEST CASES
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuite_Complete_Coverage(unittest.TestCase):

    # ADD MANY COMPLEXED TEST CASES
    def test_case_1(self):
        self.assertEqual(True, True)

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_no_tile_reuse(self):
        # Grid has only one 'A'. 'ANA' should not be found.
        grid = [["A", "N", "X"],
                ["X", "X", "X"],
                ["X", "X", "X"]]
        dictionary = ["ANA"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(mygame.getSolution(), [])

    def test_8_way_direction(self):
        # Test that the solver looks diagonally, up, down, left, and right
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        # 'AEI' (diagonal), 'FIH' (L-shape), 'EBAD' (snake)
        dictionary = ["AEI", "FIH", "EBAD"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(len(mygame.getSolution()), 3)


class TestSuite_Qu_and_St(unittest.TestCase):

    # ADD QU AND ST TEST CASES
    def test_Qu_tile_success(self):
        # Simplest possible 3x3 to find "QUART"
        grid = [["QU", "A", "X"],
                ["R", "T", "X"],
                ["X", "X", "X"]]
        dictionary = ["QUART"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(mygame.getSolution(), ["QUART"])

    def test_St_prefix_logic(self):
        # Tests if a multi-letter tile correctly triggers the prefix check
        grid = [["ST", "A", "R"]]
        # Note: Your code requires NxN, so a 1x3 grid will return []
        # based on your current validation logic. Let's use 3x3.
        grid = [["ST", "A", "R"], ["X", "X", "X"], ["X", "X", "X"]]
        dictionary = ["STAR", "STAY"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(mygame.getSolution(), ["STAR"])


if __name__ == '__main__':
    unittest.main()
