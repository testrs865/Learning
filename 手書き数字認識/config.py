from pathlib import Path
import pygame

# ===== パス =====
BASE_DIR = Path.home()                  #windowsなら"C:"
DATA_DIR = BASE_DIR /"Learning"/"手書き数字認識"

MODEL_PATH = DATA_DIR /"model"/"model.pth"
DEFAULT_IMAGE_PATH = BASE_DIR /"Learning"/"手書き数字認識"/"save_image"/"drawing.png"

# ===== モデル設定 =====
INPUT_WIDTH = 56
INPUT_HEIGHT = 28
NUM_CLASSES = 6   # 10〜15

# ===== 推論設定 =====
THRESHOLD = 50


# ---------- 画面設定 ----------
WIDTH, HEIGHT = 560, 280

# ---------- 色設定 ----------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_COLOR = (200, 0, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_BG_COLOR = (150, 150, 150)

# ---------- ペン設定 ----------
BRUSH_RADIUS = 5

# ---------- ボタンサイズ ----------
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_SPACING = 20

# ---------- パス ----------
SAVE_PATH = DATA_DIR / "save_image" / "drawing.png"

# ---------- 初期化用関数 ----------
def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("手書きアプリ")

    # フォント
    font = pygame.font.Font("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc", 20)
    label_font = pygame.font.Font("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc", 30)

    # ボタン
    clear_button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
    save_button_rect = pygame.Rect(
        WIDTH - BUTTON_WIDTH - 20,
        20 + BUTTON_HEIGHT + BUTTON_SPACING,
        BUTTON_WIDTH,
        BUTTON_HEIGHT
    )

    # テキストボックス
    textbox_rect = pygame.Rect(
        WIDTH - 100 - 20,
        save_button_rect.bottom + 50,
        100,
        40
    )

    # キャンバス
    canvas_rect = pygame.Rect(0, 0, WIDTH - BUTTON_WIDTH - 40, HEIGHT)
    canvas_surface = pygame.Surface(canvas_rect.size)
    canvas_surface.fill(BLACK)

    return {
        "screen": screen,
        "font": font,
        "label_font": label_font,
        "clear_button_rect": clear_button_rect,
        "save_button_rect": save_button_rect,
        "textbox_rect": textbox_rect,
        "canvas_rect": canvas_rect,
        "canvas_surface": canvas_surface,
    }