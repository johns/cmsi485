'''
SearchTreeNodes contain the following information for BFS:

=== state ===
The state represented by the node, a tuple:
(x, y) = (col, row)

=== action ===
The action used to transition from the parent to this node.
- The action's value is None if the initial state
- The action's value will be a string "U", "D", "L", "R" otherwise

=== parent ===
The parent of this node in the search tree.
- The parent's value is None if the initial state
- The parent's value is a reference to the parent node otherwise

=== totalCost ===
The total cost of the path of actions that led to this particular state.
In the notes, we refer to this value as being evaluated through g(n)

=== heuristicCost ===
The heuristic estimate of cost to be incurred from this node to the
optimal solution
'''

class SearchTreeNode:
    """Create node structure for A* Search Tree"""

    def __init__(self, state, action, parent, total_cost, heuristic_cost):
        self.state = state
        self.action = action
        self.parent = parent
        self.total_cost = total_cost
        self.heuristic_cost = heuristic_cost

    def __lt__(self, other):
        return self.total_cost + self.heuristic_cost < other.total_cost + other.heuristic_cost
