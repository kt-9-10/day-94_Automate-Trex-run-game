import pyautogui
import numpy as np


def capture_game_screenshot():
    x, y, width, height = 440, 930, 200, 10

    game_window_element = pyautogui.screenshot(region=(x, y, width, height))
    return game_window_element


def is_obstacle(game_window_element):
    game_array = np.array(game_window_element.convert('L'))
    return np.any(game_array == 83)


def jump():
    pyautogui.press('space')


while True:
    game_window = capture_game_screenshot()
    game_window.save("image.png")
    if is_obstacle(game_window):
        jump()
