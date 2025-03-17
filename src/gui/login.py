import tkinter as tk
from tkinter import Menu
from gui.config import GUIConfig
from gui.app import App


class Login:

    def login(self):
        name = self.name_var.get()
        password = self.passw_var.get()

        print("The name is : " + name)
        print("The password is : " + password)

    def l_mask(self, root):
        my_cfg = GUIConfig
        self.name_var = tk.StringVar()
        self.passw_var = tk.StringVar()
        self.name_lbl = tk.Label(root, text="Username", font=my_cfg.font)
        self.name_entry = tk.Entry(root, textvariable=self.name_var, font=my_cfg.font)
        self.passw_lbl = tk.Label(root, text="Password", font=my_cfg.font)
        self.passw_entry = tk.Entry(
            root, textvariable=self.passw_var, font=my_cfg.font, show="*"
        )

        sub_btn = tk.Button(
            root, text="Login", command=self.login, font=my_cfg.btn_font
        )

        # Placing elements into grid
        self.name_lbl.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.passw_lbl.grid(row=1, column=0)
        self.passw_entry.grid(row=1, column=1)
        sub_btn.grid(row=2, column=1)
