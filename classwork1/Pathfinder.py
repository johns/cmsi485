'''
Sam Chami
Jackson Myers
John Scott

The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
import queue


class Pathfinder:
    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]

    def action_list(node):
        actions = []
        current_node = node
        while current_node.parent is not None:
            actions.insert(0, current_node.action)
            current_node = current_node.parent
        print(actions)
        return actions

    def solve(problem):
        next_states = queue.Queue(maxsize=0)
        action_node = SearchTreeNode(problem.initial, None, None)
        parentNode = action_node

        while True:
            for transition in problem.transitions(parentNode.state):
                action_node = SearchTreeNode(transition[1], transition[0], parentNode)
                next_states.put(action_node)
                if problem.goalTest(action_node.state):
                    return Pathfinder.action_list(action_node)
            parentNode = next_states.get()


class PathfinderTests(unittest.TestCase):
    def test_maze0(self):
        maze = ["XXX", "X*X", "XGX", "XXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 1)

    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX",
                "X..GX",
                "X...X",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX",
                "X.XXGX",
                "X.X..X",
                "X*..XX",
                "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 5)

    def test_maze5(self):
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
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 16)

    def test_maze6(self):
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

        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 3)

    def test_maze7(self):
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

        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 11)

    def test_maze8(self):
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
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 7)

    def test_maze9(self):
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
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 10)


if __name__ == '__main__':
    unittest.main()
