# algorithms/uncertain_bfs.py
from collections import deque
import random
from core.puzzle import get_neighbors
from core.config import goal_state

def uncertain_bfs(start_state, probability=0.8, double_step_chance=0.3):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if random.random() < probability:
                extended_path = path + [state]

                # Với một xác suất, ta mở rộng luôn bước tiếp theo từ neighbor
                if random.random() < double_step_chance:
                    sub_neighbors = get_neighbors(neighbor)
                    for sub_neighbor in sub_neighbors:
                        if random.random() < probability:
                            queue.append((sub_neighbor, extended_path + [neighbor]))
                else:
                    queue.append((neighbor, extended_path))

    return None