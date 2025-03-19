import tkinter as tk
import pandas as pd
from tkinter import Menu
from gui.config import GUIConfig
from gui.app import App



class Login:

    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.valid_roles = ['guest', 'admin', 'member', 'staff']
        
    def login(self):
        name = self.name_var.get()
        password = self.passw_var.get()
        self.app.set_role({'name': name, 'pass':password})
        if name not in self.valid_roles:
            lbl = tk.Label(self.root, text="Fehler: Authentifizierung fehlgeschlagen!", fg='red')
            
        else: 
            lbl = tk.Label(self.root, text="Sie sind eingeloggt als " + name, fg='green')
             
            children = [self.name_lbl, self.name_entry, self.passw_lbl, self.passw_entry, self.sub_btn]
            for child in children:
                child.destroy()
        
        lbl.grid(row=3, column=1)
        
        self.app.dispatch_role(name)
        
    def show_mask(self):
        my_cfg = GUIConfig
        self.name_var = tk.StringVar()
        self.passw_var = tk.StringVar()
        self.name_lbl = tk.Label(self.root, text="Username", font=my_cfg.font)
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var, font=my_cfg.font)
        self.passw_lbl = tk.Label(self.root, text="Password", font=my_cfg.font)
        self.passw_entry = tk.Entry(
            self.root, textvariable=self.passw_var, font=my_cfg.font, show="*"
        )

        self.sub_btn = tk.Button(
            self.root, text="Login", command=self.login, font=my_cfg.btn_font
        )

        # Placing elements into grid
        self.name_lbl.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.passw_lbl.grid(row=1, column=0)
        self.passw_entry.grid(row=1, column=1)
        self.sub_btn.grid(row=2, column=1)
