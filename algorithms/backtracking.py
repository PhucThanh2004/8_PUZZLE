import pygame
import time
from core.puzzle import get_neighbors, heuristic
from core.config import goal_state, WHITE

def backtracking_search(start_state, screen, clock):
    def backtrack(state, path, visited):
        print(f"Visiting state: {state}")
        # Hiển thị trạng thái hiện tại
        screen.fill(WHITE)
        from ui.drawer import draw_puzzle
        draw_puzzle(start_state, 100, 50, screen)
        draw_puzzle(state, 600, 50, screen)
        pygame.display.flip()
        time.sleep(0.1)
        clock.tick(60)

        if state == goal_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            print(f"Already visited: {state}")
            return None
        visited.add(state_tuple)

        neighbors = get_neighbors(state)
        # Tính f = g + h cho mỗi neighbor, trong đó g = độ sâu = len(path)
        neighbors = sorted(neighbors, key=lambda n: len(path) + 1 + heuristic(n))

        for neighbor in neighbors:
            result = backtrack(neighbor, path + [state], visited)
            if result:
                return result
        return None

    visited = set()
    return backtrack(start_state, [], visited)
