import tkinter as tk
from ui.puzzle_game import PuzzleGame
from tests import tests
# import PyChromeDevTools
import subprocess


def run_ui():
    root = tk.Tk()
    PuzzleGame(root)
    root.mainloop()


def run_web_solver():
    open_google_remotely()
    #connect_to_google()
    #tests.test_sorting()


def open_google_remotely():
    # disable all Google tabs
    # else it won't work
    subprocess.run(r'commands\open_google_chrome.bat')


#def connect_to_google():
 #   chrome = PyChromeDevTools.ChromeInterface()
  #  chrome.Page.enable()

   # chrome.Page.navigate(url="https://hack.ainfosec.com")
    #tiles_data = chrome.Runtime.evaluate(expression="Tiles_get()")
    p#rint(tiles_data)




if __name__ == "__main__":
    run_ui()
