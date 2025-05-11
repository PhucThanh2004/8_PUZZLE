import pygame
from core.config import WIDTH, HEIGHT, GRID_SIZE, CELL_SIZE, WHITE, BLACK, BLUE, GRAY, FONT_SIZE, BUTTON_COLOR, BUTTON_HOVER, TEXT_COLOR, GREEN
# ... (import các hằng số màu sắc khác nếu cần)

def draw_puzzle(state, top_left_x, top_left_y, screen): # Thêm tham số screen
    font = pygame.font.SysFont('arial', FONT_SIZE, bold=True)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            val = state[i][j]
            rect = pygame.Rect(top_left_x + j * CELL_SIZE, top_left_y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            shadow_rect = rect.move(4, 4)
            pygame.draw.rect(screen, GRAY, shadow_rect, border_radius=8)
            color = BLUE if val != 0 else WHITE
            pygame.draw.rect(screen, color, rect, border_radius=8)
            pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
            if val != 0:
                text = font.render(str(val), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def draw_status(message, y_position, screen): # Thêm tham số screen
    status_font = pygame.font.SysFont(None, 48)
    status_surf = status_font.render(message, True, BLACK)
    status_rect = status_surf.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(status_surf, status_rect)

def draw_background(screen): # Thêm tham số screen
    for y in range(HEIGHT):
        r = int(255 - (y / HEIGHT) * 50)
        g = int(255 - (y / HEIGHT) * 50)
        b = int(255 - (y / HEIGHT) * 20)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def draw_buttons(buttons, button_rects, mouse_pos, screen): # Thêm tham số screen
    font = pygame.font.SysFont('calibri', 28, bold=True)
    for idx, (label, _) in enumerate(buttons):
        btn_rect = button_rects[idx]
        color = BUTTON_HOVER if btn_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(screen, color, btn_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, btn_rect, 2, border_radius=10)
        text = font.render(label, True, TEXT_COLOR)
        text_rect = text.get_rect(center=btn_rect.center)
        screen.blit(text, text_rect)