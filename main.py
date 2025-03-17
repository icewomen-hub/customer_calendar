import tkinter as tk
from tkinter import Menu
from gui.config import GUIConfig
from gui.app import App

root =  root = tk.Tk()
root.state('zoom') 
my_app = App(root)
my_app.run().mainloop()
