import tkinter as tk
from ui.puzzle_game import PuzzleGame
from tests import tests
import PyChromeDevTools

def run_ui():
    root = tk.Tk()
    PuzzleGame(root)
    root.mainloop()

def run_web_solver():
    connect_to_google()
    tests.test_sorting()

def connect_to_google():
    chrome = PyChromeDevTools.ChromeInterface()
    chrome = PyChromeDevTools.ChromeInterface(host="localhost",port=9222)


if __name__ == "__main__":
    run_web_solver()