import tkinter as tk
from tkinter import Menu
from config import GUIConfig

class App:
    root = False
    config = False
    
    def __init__(self, root):
        self.root = root
        self.config = GUIConfig()
        self.root.title(self.config.app_title)
        
        
        
    def run(self):
        self.menu()
        return self.root
        # self.loop()
   
    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        for topic in self.config.menu_topics.keys():
        
            curr_mnu = Menu(menubar)
            for item in self.config.menu_topics[topic]:
                curr_mnu.add_command(label=item, command=self.root.destroy)
                menubar.add_cascade(label=topic, menu=curr_mnu)
   
    def loop(self):
         self.root.mainloop()
        
        