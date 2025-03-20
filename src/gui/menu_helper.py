import tkinter as tk
from tkinter import Menu

class MenuHelper:
    def __init__(self, context):
        self.context = context
    
    def get_menu_by_role(self, role_name, content):
        if role_name == 'admin':
            return self.adm_mnu(content)
        elif role_name == 'guest':
            return self.adm_mnu
        
    def adm_mnu(self, content):
        menubar = Menu(self.context)
        self.context.config(menu=menubar)
        curr_menu = Menu(menubar)
        menubar.add_cascade(label='Objekte', menu=curr_menu)
        
        for label in content:
            curr_menu.add_command(label=label, command=content[label])    
        curr_menu.add_separator()
        curr_menu.add_command(label="Beenden", command=self.context.destroy)
        
        
        curr_menu = Menu(menubar)
        menubar.add_cascade(label='Statistiken', menu=curr_menu)
        curr_menu.add_command(label="Diagramme", command=self.context.destroy)
        curr_menu.add_command(label="Quartalsberichte", command=self.context.destroy)
        menubar.entryconfig("Statistiken", state="disabled")
        return menubar