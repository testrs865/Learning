import pygame
from pathlib import Path

pygame.init()

# 画面設定
WIDTH, HEIGHT = 560, 280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("手書きアプリ")

# 色設定
BLACK = (0, 0, 0)              # 描画可能領域
WHITE = (255, 255, 255)        # ペンの色
BUTTON_COLOR = (200, 0, 0)     # ボタン本体
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_BG_COLOR = (150, 150, 150)  # ボタン以外の背景（灰色）
BRUSH_RADIUS = 5

# 描画状態
drawing = False
last_pos = None  # 前回のマウス座標（線をつなぐ用）

# 日本語フォント（macOS の例）
font = pygame.font.Font("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc", 20)
label_font = pygame.font.Font("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc", 30)

# 説明テキスト（ラベル）
label_text = "出力結果"

# ボタンサイズ
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_SPACING = 20  # ボタン間の縦スペース

# クリアボタン（右上）
clear_button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
# 保存ボタンはクリアボタンの下
save_button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 20, 20 + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT)

# ボタンテキスト
clear_button_text = font.render("クリア", True, BUTTON_TEXT_COLOR)
save_button_text = font.render("識別", True, BUTTON_TEXT_COLOR)

# テキストボックス設定（保存ボタンの下）
TEXTBOX_WIDTH = 100
TEXTBOX_HEIGHT = 40
textbox_rect = pygame.Rect(
    WIDTH - TEXTBOX_WIDTH - 20,
    save_button_rect.bottom + 50,
    TEXTBOX_WIDTH,
    TEXTBOX_HEIGHT
)
textbox_text = "test"

# 描画可能領域（ボタン領域を除外）
canvas_rect = pygame.Rect(0, 0, WIDTH - BUTTON_WIDTH - 40, HEIGHT)  # 左側にキャンバス確保

# キャンバス専用 Surface
canvas_surface = pygame.Surface(canvas_rect.size)
canvas_surface.fill(BLACK)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if clear_button_rect.collidepoint(event.pos):               #クリア
                canvas_surface.fill(BLACK)
            elif save_button_rect.collidepoint(event.pos):              #保存して識別
                # キャンバス部分だけ保存
                surface_to_save = canvas_surface.copy()
                pygame.image.save(surface_to_save, "drawing.png")
            elif canvas_rect.collidepoint(event.pos):
                drawing = True
                mx, my = event.pos
                last_pos = (mx - canvas_rect.x, my - canvas_rect.y)

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

    # 描画
    if drawing and canvas_rect.collidepoint(pygame.mouse.get_pos()):
        mx, my = pygame.mouse.get_pos()
        canvas_x = mx - canvas_rect.x
        canvas_y = my - canvas_rect.y
        if last_pos is not None:
            pygame.draw.line(canvas_surface, WHITE, last_pos, (canvas_x, canvas_y), BRUSH_RADIUS*2)
        else:
            pygame.draw.circle(canvas_surface, WHITE, (canvas_x, canvas_y), BRUSH_RADIUS)
        last_pos = (canvas_x, canvas_y)

    # 画面更新
    screen.fill(BUTTON_BG_COLOR)                   # 背景灰色
    screen.blit(canvas_surface, canvas_rect.topleft)  # キャンバス貼り付け

    # ボタン描画
    pygame.draw.rect(screen, BUTTON_COLOR, clear_button_rect)
    screen.blit(clear_button_text, (clear_button_rect.x + 10, clear_button_rect.y + 5))

    pygame.draw.rect(screen, BUTTON_COLOR, save_button_rect)
    screen.blit(save_button_text, (save_button_rect.x + 10, save_button_rect.y + 5))

    # 説明テキスト描画
    label_surface = label_font.render(label_text, True, WHITE)
    screen.blit(label_surface, (textbox_rect.x - 5, textbox_rect.y - label_surface.get_height() - 5))

    # テキストボックス描画
    pygame.draw.rect(screen, WHITE, textbox_rect)
    pygame.draw.rect(screen, BLACK, textbox_rect, 2)
    textbox_surface = font.render(textbox_text, True, BLACK)
    screen.blit(textbox_surface, (textbox_rect.x + 5, textbox_rect.y + 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()