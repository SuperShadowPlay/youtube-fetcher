from ast import Import
from app import App
try:
    from tkinter import Tk
except ImportError:
    from Tkinter import Tk

if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()
    