import tkinter as tk
from tkinter import Menu
from config import GUIConfig
from app import App

tk._test()
root = tk.Tk()
# Vollbild anzeigen
root.state('zoomed')
my_app = App(root)

# hier steht der Applikations-Code Rolle/Ansicht
# Z.B: 


my_app.run().mainloop()
