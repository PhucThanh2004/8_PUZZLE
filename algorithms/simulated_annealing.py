# algorithms/simulated_annealing.py
import random
import math
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state

def simulated_annealing(start_state):
    current_state = start_state
    path = [current_state]
    visited = set()
    temperature = 100.0  # Nhiệt độ ban đầu
    cooling_rate = 0.99  # Tốc độ làm nguội
    min_temperature = 0.1  # Ngưỡng nhiệt độ tối thiểu

    while temperature > min_temperature:
        key = tuple(tuple(row) for row in current_state)
        visited.add(key)
        neighbors = get_neighbors(current_state)

        if not neighbors:
            break  # Không có hàng xóm để chọn

        next_state = random.choice(neighbors)
        delta_e = heuristic(next_state) - heuristic(current_state)

        if delta_e < 0 or random.random() < math.exp(-delta_e / temperature):
            current_state = next_state
            path.append(current_state)
            if current_state == goal_state:
                return path

        temperature *= cooling_rate  # Giảm nhiệt độ

    return path