import os
import json
import hashlib
import customtkinter as ctk

from tkinter import messagebox
from PIL import Image
from MainWindow import MainWindow


MASTER_FILE = "master.json"


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.logo = None
        self.main_window = None
        self.title("PassVault")
        self.geometry("500x500")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.password_entry = None
        self.confirm_entry = None
        self.button = None
        self.create_widgets()

    def create_widgets(self):

        logo_image = ctk.CTkImage(
            light_image=Image.open("assets/PassVaultLogo.png"),
            dark_image=Image.open("assets/PassVaultLogo.png"),
            size=(120, 120)
        )

        self.logo = ctk.CTkLabel(
            self,
            text="",
            image=logo_image
        )
        self.logo.pack(pady=(25,5))

        ctk.CTkLabel(
            self,
            text="PassVault",
            font=("Segue UI", 28, "bold"),
            text_color="#F1C9DA"
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            self,
            text="Secure Password Manager",
            font=("Segue UI", 14)
        ).pack(pady=(0, 25))

        self.password_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Master Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        self.confirm_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Confirm Password (First Launch Only)",
            show="*"
        )
        self.confirm_entry.pack(pady=10)

        self.button = ctk.CTkButton(
            self,
            width=300,
            text="Unlock Vault",
            command=self.login
        )
        self.button.pack(pady=30)

    @staticmethod
    def hash_password( password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    def create_master_password(self):

        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if len(password) < 8:

            messagebox.showerror(
                "Error",
                "Master password must be at least 8 characters."
            )
            return

        if password != confirm:

            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        data = {
            "master_password": self.hash_password(password)
        }

        with open(MASTER_FILE, "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo(
            "Success",
            "Vault created successfully."
        )

        self.open_main_window()

    def login(self):

        if not os.path.exists(MASTER_FILE):

            self.create_master_password()
            return

        password = self.password_entry.get()

        with open(MASTER_FILE, "r") as file:
            data = json.load(file)

        if self.hash_password(password) == data["master_password"]:

            self.open_main_window()

        else:

            messagebox.showerror(
                "Login Failed",
                "Incorrect master password."
            )

    def open_main_window(self):

        self.withdraw()

        self.main_window = MainWindow(
            self,
            self.password_entry.get()
        )

        """mainloop()"""