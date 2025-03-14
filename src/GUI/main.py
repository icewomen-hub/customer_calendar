import tkinter as tk
from tkinter import Menu
from config import GUIConfig

cfg = GUIConfig()






# print(main_topics.keys())
# root window
root = tk.Tk()
root.title("Kundenkalender")

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)


menu_dct = []
for topic in cfg.menu_topics.keys():
    print(topic)
    curr_mnu = Menu(menubar)
    for item in cfg.menu_topics[topic]:
        curr_mnu.add_command(label=item, command=root.destroy)
    menubar.add_cascade(label=topic, menu=curr_mnu)

    menu_dct.append(curr_mnu)
# add the File menu to the menubar


root.mainloop()
