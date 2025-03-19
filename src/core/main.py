import tkinter as tk
from tkinter import Menu
from config import GUIConfig
from app import App

root = tk.Tk()
root.state('zoom') 
my_app = App(root)
my_app.run().mainloop()
