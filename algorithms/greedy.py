# algorithms/greedy.py
import heapq
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state

def greedy(start_state):
    pq = [(heuristic(start_state), start_state, [])]
    visited = set()
    while pq:
        _, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [state]
        key = tuple(tuple(row) for row in state)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (heuristic(neighbor), neighbor, path + [state]))
    return None