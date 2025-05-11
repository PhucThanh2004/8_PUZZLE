# algorithms/po_dfs.py
from core.puzzle import find_blank, get_neighbors, generate_random_state
from core.config import goal_state, GRID_SIZE1

def partially_observable_dfs(start_state_unused):
    def get_known_neighbors(state, known_tiles):
        x, y = find_blank(state)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dx,dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE1 and 0 <= ny < GRID_SIZE1:
                if state[nx][ny] in known_tiles or state[nx][ny] == 0:
                    new_state = [row[:] for row in state]  # Tạo bản sao
                    new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                    neighbors.append(new_state)
        return neighbors

    def observe(state, known_tiles):
        x, y = find_blank(state)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE1 and 0 <= ny < GRID_SIZE1:
                known_tiles.add(state[nx][ny])

    def dfs_known(start, goal, known_tiles):
        stack = [(start, [])]
        visited = set()  # Dùng frozenset để giảm chi phí so với tuple
        visited.add(frozenset(tuple(row) for row in start))  # Tạo frozenset ban đầu

        while stack:
            state, path = stack.pop()  # Lấy trạng thái ở đỉnh ngăn xếp
            if state == goal:
                return path + [state]

            for neighbor in get_known_neighbors(state, known_tiles):
                state_key = frozenset(tuple(row) for row in neighbor)
                if state_key not in visited:
                    visited.add(state_key)
                    stack.append((neighbor, path + [state]))  # Thêm trạng thái vào ngăn xếp
        return None

    # Tạo trạng thái ban đầu và trạng thái đích ngẫu nhiên
    start_state1 = generate_random_state()

    # Khởi tạo
    current_state = start_state1
    path = [current_state]
    known_tiles = set()
    observe(current_state, known_tiles)

    while current_state != goal_state:
        plan = dfs_known(current_state, goal_state, known_tiles)

        if not plan:
            print("Không thể lập kế hoạch do thiếu thông tin!")
            return path

        for next_state in plan[1:]:
            current_state = next_state
            path.append(current_state)
            observe(current_state, known_tiles)

            if current_state != plan[-1]:  # Nếu khám phá thêm ô mới -> cần replan
                break
    return path