# algorithms/bfs.py
from collections import deque
from core.puzzle import get_neighbors
from core.config import goal_state

def bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        key = tuple(tuple(row) for row in state)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))
    return None