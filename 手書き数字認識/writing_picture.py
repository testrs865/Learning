import pygame
import torch
from config import *
from model_10_15 import SimpleCNN, predict_image

def writing():
    objects = setup()

    screen = objects["screen"]
    font = objects["font"]
    label_font = objects["label_font"]
    clear_button_rect = objects["clear_button_rect"]
    save_button_rect = objects["save_button_rect"]
    textbox_rect = objects["textbox_rect"]
    canvas_rect = objects["canvas_rect"]
    canvas_surface = objects["canvas_surface"]

    clear_text = font.render("クリア", True, BUTTON_TEXT_COLOR)
    save_text = font.render("識別", True, BUTTON_TEXT_COLOR)
    label_text = "出力結果"
    textbox_text = f""

    drawing = False
    last_pos = None
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if clear_button_rect.collidepoint(event.pos):
                    canvas_surface.fill(BLACK)
                    textbox_text = f""

                elif save_button_rect.collidepoint(event.pos):
                    pygame.image.save(canvas_surface, SAVE_PATH)
                    
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

                    model = SimpleCNN().to(device)
                    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

                    result = predict_image(model, DEFAULT_IMAGE_PATH, device)
                    #print(f"予測結果: {result}")
                    textbox_text = f"{result}"

                elif canvas_rect.collidepoint(event.pos):
                    drawing = True
                    mx, my = event.pos
                    last_pos = (mx - canvas_rect.x, my - canvas_rect.y)

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                last_pos = None

        if drawing and canvas_rect.collidepoint(pygame.mouse.get_pos()):
            mx, my = pygame.mouse.get_pos()
            x = mx - canvas_rect.x
            y = my - canvas_rect.y
            if last_pos:
                pygame.draw.line(canvas_surface, WHITE, last_pos, (x, y), BRUSH_RADIUS * 2)
            last_pos = (x, y)

        # 描画
        screen.fill(BUTTON_BG_COLOR)
        screen.blit(canvas_surface, canvas_rect.topleft)

        pygame.draw.rect(screen, BUTTON_COLOR, clear_button_rect)
        screen.blit(clear_text, (clear_button_rect.x + 10, clear_button_rect.y + 5))

        pygame.draw.rect(screen, BUTTON_COLOR, save_button_rect)
        screen.blit(save_text, (save_button_rect.x + 10, save_button_rect.y + 5))

        label_surface = label_font.render(label_text, True, WHITE)
        screen.blit(label_surface, (textbox_rect.x - 5, textbox_rect.y - 35))

        pygame.draw.rect(screen, WHITE, textbox_rect)
        pygame.draw.rect(screen, BLACK, textbox_rect, 2)
        textbox_surface = font.render(textbox_text, True, BLACK)
        screen.blit(textbox_surface, (textbox_rect.x + 35, textbox_rect.y + 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    writing()