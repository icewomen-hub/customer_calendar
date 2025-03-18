import tkinter as tk
from tkinter import Menu
from gui.config import GUIConfig
from core.state import State

class App:
    root = False
    config = False
    role = False
    
    def __init__(self, root):
        self.root = root
        self.config = GUIConfig()
        self.root.title(self.config.app_title)
        self.debug()

    def set_role(self, role_name='guest'):
        self.role = role_name
        
    def run(self):
        #self.menu()
        return self.root
    
    def dispatch_role(self, role_name='guest'):
        #print(role_name)
        if role_name.lower() == '':
            self.admin() 
        self.menu()
   
   
    def admin(self):
        print('admin')
        pass
    
    def guest(self):
        print('guest')
        pass
    
    def staff(self):
        print('Mitarbeiter')
        pass
    
    def member(self):
        print('Mitglied')
        pass
    
    
   
    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        for topic in self.config.menu_topics.keys():
            
            curr_mnu = Menu(menubar)
            menubar.add_cascade(label=topic, menu=curr_mnu)
            for item in self.config.menu_topics[topic]:
                curr_mnu.add_command(label=item, command=self.root.destroy)
                
    def debug(self):
        import os 
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
                
   
   
        
        