import random
import numpy as np
from core.puzzle import get_neighbors, generate_random_state, find_blank
from core.config import goal_state, GRID_SIZE1

def is_goal_state(state):
    return state == goal_state

def get_state_key(state):
    return tuple(tuple(row) for row in state)

def q_learning(start_state, alpha=0.1, gamma=0.9, epsilon=0.1, num_episodes=10000):
   
    q_table = {}  # Khởi tạo Q-table
    best_path = []
    min_steps = float('inf')

    for episode in range(num_episodes):
        current_state = start_state
        path = [current_state]
        steps = 0
        visited = set()

        while not is_goal_state(current_state) and steps < 200: # Thêm giới hạn bước để tránh vòng lặp vô hạn
            state_key = get_state_key(current_state)
            visited.add(state_key)
            neighbors = get_neighbors(current_state)
            if not neighbors:
                break

            # Chọn hành động (di chuyển ô trống)
            if random.random() < epsilon:
                # Khám phá: Chọn một trạng thái lân cận ngẫu nhiên
                next_state = random.choice(neighbors)
            else:
                # Khai thác: Chọn trạng thái lân cận có giá trị Q lớn nhất
                if state_key not in q_table:
                    q_table[state_key] = {get_state_key(n): 0 for n in neighbors}
                best_action = max(q_table[state_key], key=q_table[state_key].get)
                next_state = next((n for n in neighbors if get_state_key(n) == best_action), None)
                if next_state is None:
                    next_state = random.choice(neighbors)

            next_state_key = get_state_key(next_state)

            # Tính phần thưởng (reward)
            reward = 0
            if is_goal_state(next_state):
                reward = 100
            else:
                reward = -1

            # Cập nhật Q-table
            if state_key not in q_table:
                q_table[state_key] = {next_state_key: 0}
            if next_state_key not in q_table:
                q_table[next_state_key] = {get_state_key(n): 0 for n in get_neighbors(next_state)}
            
            old_value = q_table[state_key][next_state_key]
            next_max_q = max(q_table[next_state_key].values()) if next_state_key in q_table else 0
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max_q)
            q_table[state_key][next_state_key] = new_value

            current_state = next_state
            path.append(current_state)
            steps += 1

        # In ra trạng thái cuối của mỗi episode
        # print(f"Episode {episode + 1}: Goal reached in {steps} steps")

        if is_goal_state(current_state):
            if steps < min_steps:
                min_steps = steps
                best_path = path
            print(f"Episode {episode + 1}: Solution found in {steps} steps")
        else:
            print(f"Episode {episode + 1}: No solution found in 200 steps")

    return q_table, best_path

if __name__ == "__main__":
    # Tạo trạng thái bắt đầu ngẫu nhiên
    start_state = generate_random_state()
    print("Trạng thái bắt đầu:")
    for row in start_state:
        print(row)

    # Giải bài toán bằng Q-Learning
    q_table, best_path = q_learning(start_state)

    # In ra đường đi tốt nhất
    print("\nBest Path:")
    if best_path:
        for state in best_path:
            for row in state:
                print(row)
            print("-" * 10)
    else:
        print("No solution found within the training episodes.")
