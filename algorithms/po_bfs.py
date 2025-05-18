from core.puzzle import find_blank, get_neighbors, generate_random_state
from core.config import goal_state, GRID_SIZE1

def partially_observable_bfs(start_state):
    """
    Giải bài toán 8-puzzle với Partially Observable Breadth-First Search.

    Args:
        start_state: Trạng thái ban đầu của puzzle.

    Returns:
        Một danh sách các trạng thái dẫn từ trạng thái ban đầu đến trạng thái mục tiêu,
        hoặc None nếu không tìm thấy giải pháp.
    """
    def get_known_neighbors(state, known_tiles):
        """
        Lấy các trạng thái lân cận có thể đi tới từ trạng thái hiện tại,
        chỉ sử dụng các ô cờ có trong known_tiles.

        Args:
            state: Trạng thái hiện tại của puzzle.
            known_tiles: Tập hợp các giá trị của các ô cờ đã biết.

        Returns:
            Một danh sách các trạng thái lân cận.
        """
        x, y = find_blank(state)
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE1 and 0 <= ny < GRID_SIZE1:
                if state[nx][ny] in known_tiles or state[nx][ny] == 0:
                    new_state = [row[:] for row in state]
                    new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                    neighbors.append(new_state)
        return neighbors

    def observe(state, known_tiles):
        """
        Cập nhật tập hợp các ô cờ đã biết bằng cách quan sát các ô cờ
        liền kề với ô trống trong trạng thái hiện tại.

        Args:
            state: Trạng thái hiện tại của puzzle.
            known_tiles: Tập hợp các giá trị của các ô cờ đã biết (được cập nhật).
        """
        x, y = find_blank(state)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE1 and 0 <= ny < GRID_SIZE1:
                known_tiles.add(state[nx][ny])

    # Khởi tạo
    current_state = start_state
    path = [current_state]
    known_tiles = set()
    observe(current_state, known_tiles)
    queue = [(current_state, path)]  # Sử dụng queue thay vì stack cho BFS
    visited = set()

    while queue:
        current_state, path = queue.pop(0)  # Lấy trạng thái đầu tiên trong queue

        if current_state == goal_state:
            return path

        visited.add(tuple(map(tuple, current_state))) # Thêm trạng thái hiện tại vào visited

        for neighbor in get_known_neighbors(current_state, known_tiles):
            if tuple(map(tuple, neighbor)) not in visited:
                observe(neighbor, known_tiles)
                queue.append((neighbor, path + [neighbor]))  # Thêm vào cuối queue

    return None  # Không tìm thấy giải pháp

if __name__ == "__main__":
    # Tạo trạng thái bắt đầu ngẫu nhiên
    start_state = generate_random_state()
    print("Trạng thái bắt đầu:")
    for row in start_state:
        print(row)

    # Giải bài toán
    solution_path = partially_observable_bfs(start_state)

    if solution_path:
        print("Đã tìm thấy giải pháp:")
        for state in solution_path:
            for row in state:
                print(row)
            print("-" * 10)
    else:
        print("Không tìm thấy giải pháp.")
