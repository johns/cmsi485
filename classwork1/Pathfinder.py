'''
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
    def solve(problem):
        actions = []
        next_states = queue.Queue(maxsize=0)
        next_states.put(problem.initial)

        while not next_states.empty():
            current = next_states.get()
            if problem.goalTest(current):
                return actions
            for transition in problem.transitions(current):
                print(problem.goalTest(transition[1]))
                next_states.put(transition[1])
            actions.append(problem.transitions(current)[0][0])

        # for i in next_states:
        #     actions += i[0]
        #     if problem.goalTest(i[1]):
        #         return actions
        #     next_states = problem.transitions(i[1])
        #     print(actions)

        return actions

class PathfinderTests(unittest.TestCase):
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

    # TODO: Add more unit tests!

if __name__ == '__main__':
    unittest.main()
