import tkinter as tk
from ui.puzzle_game import PuzzleGame
import PyChromeDevTools

def run_ui():
    connectToGoogle()
    root = tk.Tk()
    PuzzleGame(root)
    root.mainloop()

def connectToGoogle():
    chrome = PyChromeDevTools.ChromeInterface()
    chrome = PyChromeDevTools.ChromeInterface(host="1.1.1.1",port=1234)


if __name__ == "__main__":
    run_ui()