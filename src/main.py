import tkinter as tk
from gui.config import GUIConfig
from core.data_provider import DataProvider
from gui.app import App
from tkinter import Menu
from gui.login import Login


if __name__ == "__main__":
    my_root = tk.Tk()
    my_root.state('zoomed')
    my_app = App(root=my_root)
    lgn = Login(root=my_root, app=my_app)
    lgn.show_mask()
 
    my_app.run().mainloop() 
    



# TODO - Login -> danach Verteilung der Rollen!!


    
    #dp = DataProvider()
    #print(dp.weekdays)