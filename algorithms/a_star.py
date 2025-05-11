# algorithms/a_star.py
import heapq
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state

def a_star(start_state):
    pq = [(heuristic(start_state), 0, start_state, [])]
    visited = set()
    while pq:
        est_total, cost, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [state]
        key = tuple(tuple(row) for row in state)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(state):
            new_cost = cost + 1
            est_total = new_cost + heuristic(neighbor)
            heapq.heappush(pq, (est_total, new_cost, neighbor, path + [state]))
    return None