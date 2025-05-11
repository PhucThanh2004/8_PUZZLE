# algorithms/search_no_obs.py
from collections import deque
import random
from core.puzzle import get_neighbors, generate_random_state
from core.config import goal_state

def search_with_no_observations(start_state_unused, probability=0.8, num_initial_beliefs=5):
    # Khởi tạo belief với num_initial_beliefs trạng thái ngẫu nhiên
    belief = [generate_random_state() for _ in range(num_initial_beliefs)]
    queue = deque([(state, []) for state in belief])  # Khởi tạo BFS từ các trạng thái belief
    visited = set()

    while queue:
        state, path = queue.popleft()

        # Nếu trạng thái này đã đạt đến trạng thái mục tiêu, trả về đường đi
        if state == goal_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # Duyệt qua các trạng thái kế tiếp
        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            # Cập nhật belief với xác suất cho các trạng thái kế tiếp
            if random.random() < probability:
                queue.append((neighbor, path + [state]))

    return None