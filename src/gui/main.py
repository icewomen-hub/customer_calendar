import tkinter as tk
from tkinter import Menu
from config import GUIConfig
from app import App
from login import login, l_mask

if __name__ == "__main__":
    
    root = tk.Tk()
    root.state('zoomed')
    l_mask(root)
    my_app = App(root)
    my_app.run().mainloop() 
    