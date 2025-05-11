# algorithms/dfs.py
from core.puzzle import get_neighbors
from core.config import goal_state

def dfs(start_state):
    stack = [(start_state, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal_state:
            return path + [state]
        key = tuple(tuple(row) for row in state)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(state):
            stack.append((neighbor, path + [state]))
    return None