from gui.config import GUIConfig
from core.state import State
from gui.app import App
import tkinter as tk
from tkinter import Menu
# from gui.config import GUIConfig
# from gui.app import App
from gui.login import Login



if __name__ == "__main__":
    
    
    root = tk.Tk()
    root.state('zoomed')
    lgn = Login()
    lgn.l_mask(root)
    my_app = App(root)
    my_app.run().mainloop() 
    