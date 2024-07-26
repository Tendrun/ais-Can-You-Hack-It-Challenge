import tkinter as tk
from ui.puzzle_game import PuzzleGame
import PyChromeDevTools

def run_ui():
    #connect_to_google()
    root = tk.Tk()
    PuzzleGame(root)
    root.mainloop()

def connect_to_google():
    chrome = PyChromeDevTools.ChromeInterface()
    chrome = PyChromeDevTools.ChromeInterface(host="localhost",port=9222)


if __name__ == "__main__":
    run_ui()