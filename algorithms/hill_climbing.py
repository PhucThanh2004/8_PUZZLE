# algorithms/hill_climbing.py
import random
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state

def simple_hill_climbing(start_state):
    current_state = start_state
    path = [current_state]
    visited = set()

    while True:
        key = tuple(tuple(row) for row in current_state)
        visited.add(key)
        neighbors = get_neighbors(current_state)
        better_neighbor = None

        for neighbor in neighbors:
            n_key = tuple(tuple(row) for row in neighbor)
            if n_key not in visited and heuristic(neighbor) < heuristic(current_state):
                better_neighbor = neighbor
                break  # Dừng lại với hàng xóm tốt hơn đầu tiên

        if better_neighbor:
            current_state = better_neighbor
            path.append(current_state)
            if current_state == goal_state:
                return path
        else:
            return path  # Không có hàng xóm tốt hơn

def steepest_ascent_hill_climbing(start_state):
    current_state = start_state
    path = [current_state]
    visited = set()

    while True:
        key = tuple(tuple(row) for row in current_state)
        visited.add(key)
        neighbors = get_neighbors(current_state)

        best_neighbor = None
        best_h = heuristic(current_state)

        for neighbor in neighbors:
            n_key = tuple(tuple(row) for row in neighbor)
            h = heuristic(neighbor)
            if h < best_h and n_key not in visited:
                best_h = h
                best_neighbor = neighbor

        if best_neighbor:
            current_state = best_neighbor
            path.append(current_state)
            if current_state == goal_state:
                return path
        else:
            return path  # Không tìm được hàng xóm tốt hơn

def stochastic_hill_climbing(start_state):
    current_state = start_state
    path = [current_state]
    visited = set()

    while True:
        key = tuple(tuple(row) for row in current_state)
        visited.add(key)
        neighbors = get_neighbors(current_state)

        # Lọc ra các trạng thái có heuristic tốt hơn
        better_neighbors = [n for n in neighbors if heuristic(n) < heuristic(current_state)]

        if better_neighbors:
            current_state = random.choice(better_neighbors)
            path.append(current_state)
            if current_state == goal_state:
                return path
        else:
            return path