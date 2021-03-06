'''
John Scott

The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

import itertools
import unittest
from queue import PriorityQueue
from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode

def get_solution(node):
    """TODO"""
    soln = []
    while node.parent is not None:
        soln.append(node.action)
        node = node.parent
    soln.reverse()
    return soln

def possible_path(problem, start, goal):
    """TODO"""
    # Setup
    frontier = PriorityQueue()
    graveyard = set()

    # Search!
    frontier.put(SearchTreeNode(start, None, None, 0, abs(start[0] - goal[0]) + abs(start[1] - goal[1])))
    while not frontier.empty():
        # Get front of queue
        expanding = frontier.get()
        graveyard.add(expanding.state)

        # Test for goal state
        if expanding.state == goal:
            return get_solution(expanding)

        # Generate new nodes on frontier
        for move in problem.transitions(expanding.state):
            if move[2] not in graveyard:
                heuristic_cost = abs(move[2][0] - goal[0]) + abs(move[2][1] - goal[1])
                frontier.put(SearchTreeNode(move[2], move[0], expanding, move[1] + expanding.total_cost, heuristic_cost))

    return None

def solve(problem, initial, goals):
    """TODO"""
    solution_paths = []
    goals_permutation = itertools.permutations(goals)

    for paths in goals_permutation:
        solution_path = []
        if possible_path(problem, initial, paths[0]) is None:
            return None
        solution_path.extend(possible_path(problem, initial, paths[0]))
        if len(paths) - 1 > 0:
            for i in range(0, len(paths) - 1):
                solution_path.extend(possible_path(problem, paths[i], paths[i+1]))
        solution_paths.append(solution_path)

    return min(solution_paths)


class PathfinderTests(unittest.TestCase):
    """TODO"""

    def test_maze1(self):
        """TODO"""
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    def test_maze2(self):
        """TODO"""
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(3, 3), (5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze3(self):
        """TODO"""
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.MMX",
                "X...M.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze4(self):
        """TODO"""
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.XXX",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)


if __name__ == '__main__':
    unittest.main()
