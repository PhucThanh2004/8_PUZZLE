# algorithms/ids.py
from core.puzzle import get_neighbors
from core.config import goal_state

def ids(start_state):
    def dls(state, depth, visited):
        if state == goal_state:
            return [state]
        if depth == 0:
            return None
        key = tuple(tuple(row) for row in state)
        visited.add(key)
        for neighbor in get_neighbors(state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                result = dls(neighbor, depth - 1, visited)
                if result:
                    return [state] + result
        return None

    for d in range(50):
        visited = set()
        result = dls(start_state, d, visited)
        if result:
            return result
    return None