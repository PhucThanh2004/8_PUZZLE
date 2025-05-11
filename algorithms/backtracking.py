# algorithms/backtracking.py
from core.puzzle import get_neighbors
from core.config import goal_state

def backtracking_search(start_state):
    def backtrack(state, path, visited):
        print(f"Visiting state: {state}")  # Debugging line
        if state == goal_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            print(f"Already visited: {state}")  # Debugging line
            return None
        visited.add(state_tuple)

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            result = backtrack(neighbor, path + [state], visited)
            if result:
                return result
        return None

    visited = set()
    return backtrack(start_state, [], visited)