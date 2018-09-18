'''
Sam Chami
Jackson Myers
John Scott

The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the search_tree_node DS.
'''

import unittest
import queue
from maze_problem import MazeProblem
from search_tree_node import SearchTreeNode


class Pathfinder:
    """TODO"""
    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]

    def action_list(node):
        """TODO"""
        actions = []
        current_node = node
        while current_node.parent is not None:
            actions.insert(0, current_node.action)
            current_node = current_node.parent
        print(actions)
        return actions

    def solve(problem):
        """TODO"""
        next_states = queue.Queue(maxsize=0)
        action_node = SearchTreeNode(problem.initial, None, None)
        parent_node = action_node

        while True:
            for transition in problem.transitions(parent_node.state):
                action_node = SearchTreeNode(transition[1], transition[0], parent_node)
                next_states.put(action_node)
                if problem.goal_test(action_node.state):
                    return Pathfinder.action_list(action_node)
            parent_node = next_states.get()


class PathfinderTests(unittest.TestCase):
    """TODO"""
    def test_maze0(self):
        """TODO"""
        maze = ["XXX", "X*X", "XGX", "XXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 1)

    def test_maze1(self):
        """TODO"""
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze2(self):
        """TODO"""
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze3(self):
        """TODO"""
        maze = ["XXXXX",
                "X..GX",
                "X...X",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze4(self):
        """TODO"""
        maze = ["XXXXXX",
                "X.XXGX",
                "X.X..X",
                "X*..XX",
                "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 5)

    def test_maze5(self):
        """TODO"""
        maze = ["XXXXXXXX",
                "X.....*X",
                "X.XXXXXX",
                "X......X",
                "XXXXXX.X",
                "X......X",
                "X.XXXX.X",
                "X.....GX",
                "XXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 16)

    def test_maze6(self):
        """TODO"""
        maze = ["XXXXXXXXXX",
                "X........X",
                "XXX.X.*.XX",
                "X........X",
                "X....G...X",
                "X....X...X",
                "X...XX...X",
                "X........X",
                "X........X",
                "XXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)

        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 3)

    def test_maze7(self):
        """TODO"""
        maze = ["XXXXXXXXXX",
                "X*.......X",
                "XXX.X...XX",
                "X........X",
                "X........X",
                "X....X...X",
                "X...XX...X",
                "X.XX...X.X",
                "XG....X..X",
                "XXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)

        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 11)

    def test_maze8(self):
        """TODO"""
        maze = ["XXXXXXXXXX",
                "X........X",
                "XXX.XX.X.X",
                "XXXXXX.X.X",
                "X...XX.X.X",
                "X.X.*....X",
                "X.XXXX.X.X",
                "X....X.X.X",
                "X......XGX",
                "XXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 7)

    def test_maze9(self):
        """TODO"""
        maze = ["XXXXXXXXXXXXX",
                "X........XX.X",
                "XXX.XX.X.XX.X",
                "XXXXXX.X.XX.X",
                "X...XX.X.XX.X",
                "X.X.*.......X",
                "X.XXXX.X.XX.X",
                "X....X.X.X.XX",
                "X......X...GX",
                "XXXXXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 10)


if __name__ == '__main__':
    unittest.main()
