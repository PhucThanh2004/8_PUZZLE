# core/puzzle.py
import random
from core.config import GRID_SIZE

def find_blank(state):
    """Tìm vị trí của ô trống (0) trong trạng thái của puzzle."""
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if state[r][c] == 0:
                return r, c
    return None, None  # Trả về None, None nếu không tìm thấy (trường hợp không hợp lệ)


def get_neighbors(state):
    """
    Lấy tất cả các trạng thái lân cận có thể có của trạng thái hiện tại bằng cách di chuyển ô trống.

    Args:
        state (list of list): Trạng thái hiện tại của puzzle.

    Returns:
        list of list of list: Danh sách các trạng thái lân cận.
    """
    neighbors = []
    r, c = find_blank(state)

    if r is None or c is None:
        return []  # Trả về list rỗng nếu không tìm thấy ô trống (trạng thái không hợp lệ)

    # Các hướng di chuyển: xuống, lên, phải, trái
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < GRID_SIZE and 0 <= new_c < GRID_SIZE:
            # Tạo một bản sao mới của trạng thái để không sửa đổi trạng thái gốc
            new_state = [list(row) for row in state]
            # Hoán đổi vị trí ô trống và ô kề cạnh
            new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
            neighbors.append(new_state)
    return neighbors

def generate_random_state():
    """Tạo một trạng thái ngẫu nhiên có thể giải được của puzzle."""
    import random
    numbers = list(range(GRID_SIZE * GRID_SIZE))
    random.shuffle(numbers)
    state = [numbers[i:i + GRID_SIZE] for i in range(0, GRID_SIZE * GRID_SIZE, GRID_SIZE)]

    # Kiểm tra tính giải được (solvability)
    inversions = 0
    for i in range(GRID_SIZE * GRID_SIZE):
        for j in range(i + 1, GRID_SIZE * GRID_SIZE):
            if numbers[j] and numbers[i] and numbers[i] > numbers[j]:
                inversions += 1
    blank_row = GRID_SIZE - 1 - (numbers.index(0) // GRID_SIZE)

    if GRID_SIZE % 2 == 0:  # Nếu GRID_SIZE chẵn
        if (inversions + blank_row) % 2 == 0:
            return state
        else:
            return generate_random_state() # Đệ quy để tạo lại nếu không giải được
    else:  # Nếu GRID_SIZE lẻ
        if inversions % 2 == 0:
            return state
        else:
            return generate_random_state() # Đệ quy để tạo lại nếu không giải được
def heuristic(state):
    distance = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            val = state[i][j]
            if val != 0:
                tx, ty = (val - 1) // GRID_SIZE, (val - 1) % GRID_SIZE
                distance += abs(i - tx) + abs(j - ty)
    return distance

GRID_SIZE1 = 3  # Kích thước của ma trận 3x3