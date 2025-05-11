# algorithms/beam_search.py
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state

def beam_search(start_state, k=2):
    queue = [(heuristic(start_state), start_state, [])]
    visited = set()

    while queue:
        queue.sort()  # Sắp xếp theo heuristic
        queue = queue[:k]  # Chỉ giữ lại k trạng thái tốt nhất

        new_queue = []
        for _, state, path in queue:
            if state == goal_state:
                return path + [state]

            state_tuple = tuple(tuple(row) for row in state)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            for neighbor in get_neighbors(state):
                new_queue.append((heuristic(neighbor), neighbor, path + [state]))

        queue = new_queue

    return None