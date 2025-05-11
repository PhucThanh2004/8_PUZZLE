# algorithms/uniform_cost.py
import heapq
from core.puzzle import get_neighbors
from core.config import goal_state

def uniform_cost(start_state):
    pq = [(0, start_state, [])]
    visited = set()
    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [state]
        key = tuple(tuple(row) for row in state)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (cost + 1, neighbor, path + [state]))
    return None