import pygame
import random
import arabic_reshaper
from bidi.algorithm import get_display

pygame.init()

# تنظیمات پنجره
WIDTH = 800
HEIGHT = 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("بازی سنگ کاغذ قیچی")

# رنگ‌ها
BACKGROUND = (30, 35, 55)
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
GREEN = (60, 170, 100)
RED = (200, 70, 70)

# فونت فارسی ویندوز
title_font = pygame.font.Font("C:/Windows/Fonts/tahoma.ttf", 38)
text_font = pygame.font.Font("C:/Windows/Fonts/tahoma.ttf", 26)
button_font = pygame.font.Font("C:/Windows/Fonts/tahoma.ttf", 25)

options = ["سنگ", "کاغذ", "قیچی"]

user_wins = 0
computer_wins = 0
computer_pick = ""
result_text = "یکی از گزینه‌ها را انتخاب کنید"

# دکمه‌های بازی
buttons = {
    "سنگ": pygame.Rect(70, 400, 200, 70),
    "کاغذ": pygame.Rect(300, 400, 200, 70),
    "قیچی": pygame.Rect(530, 400, 200, 70)
}


def make_persian(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


def draw_text(text, font, color, x, y):
    text_surface = font.render(make_persian(text), True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def get_result(user_input, computer_pick):
    if user_input == computer_pick:
        return "برابر شدید"

    if (
        (user_input == "سنگ" and computer_pick == "قیچی")
        or (user_input == "کاغذ" and computer_pick == "سنگ")
        or (user_input == "قیچی" and computer_pick == "کاغذ")
    ):
        return "شما برنده شدید"

    return "کامپیوتر برنده شد"


running = True

while running:
    screen.fill(BACKGROUND)

    # عنوان و امتیازها
    draw_text("بازی سنگ کاغذ قیچی", title_font, WHITE, 400, 55)
    draw_text("برد شما: " + str(user_wins), text_font, GREEN, 170, 125)
    draw_text("برد کامپیوتر: " + str(computer_wins), text_font, RED, 620, 125)

    # نتیجه و انتخاب کامپیوتر
    if computer_pick != "":
        draw_text(
            "انتخاب کامپیوتر: " + computer_pick,
            text_font,
            WHITE,
            400,
            205
        )

    draw_text(result_text, text_font, WHITE, 400, 280)

    # دکمه‌ها
    for choice, button in buttons.items():
        pygame.draw.rect(screen, BLUE, button, border_radius=12)
        draw_text(choice, button_font, WHITE, button.centerx, button.centery)

    # رویداد کلیک و بستن پنجره
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()

            for user_input, button in buttons.items():
                if button.collidepoint(mouse_position):
                    computer_pick = random.choice(options)
                    result_text = get_result(user_input, computer_pick)

                    if result_text == "شما برنده شدید":
                        user_wins += 1

                    elif result_text == "کامپیوتر برنده شد":
                        computer_wins += 1

    pygame.display.update()

pygame.quit()