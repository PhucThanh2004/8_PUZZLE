# algorithms/ida_star.py
import heapq
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state

def ida_star(start_state):
    threshold = heuristic(start_state)

    def search(state, g, threshold, path, visited):
        f = g + heuristic(state)
        if f > threshold:
            return f, None
        if state == goal_state:
            return f, path + [state]
        min_threshold = float('inf')
        key = tuple(tuple(row) for row in state)
        visited.add(key)
        for neighbor in get_neighbors(state):
            n_key = tuple(tuple(row) for row in neighbor)
            if n_key not in visited:
                temp_threshold, result_path = search(neighbor, g + 1, threshold, path + [state], visited)
                if result_path is not None:
                    return temp_threshold, result_path
                if temp_threshold < min_threshold:
                    min_threshold = temp_threshold
        visited.remove(key)
        return min_threshold, None

    while True:
        visited = set()
        temp_threshold, result = search(start_state, 0, threshold, [], visited)
        if result is not None:
            return result
        if temp_threshold == float('inf'):
            return None
        threshold = temp_threshold