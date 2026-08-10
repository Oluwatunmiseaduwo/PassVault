import customtkinter as ctk
import json
import os

from Crypto import encrypt, decrypt
from cryptography.fernet import InvalidToken
from PIL import Image
from PasswordGenerator import generate_password
from PasswordChecker import (CheckStrength, CalculateEntropy, CrackTime, CheckCommonPassword)
from tkinter import messagebox


class MainWindow(ctk.CTkToplevel):
    def __init__(self, master, master_password):
        super().__init__(master)

        self.logo = None
        self.master_password = master_password

        self.title("PassVault")
        self.geometry("900x650")

        self.configure(fg_color="#3D5272")
        self.username = None
        self.password = None
        self.show_password = None
        self.show_button = None
        self.generate_button = None
        self.copy_button = None
        self.save_button = None
        self.search_button = None
        self.delete_button = None
        self.result_label = None
        self.length_entry = None

        self.uppercase_var = ctk.BooleanVar(value=True)
        self.numbers_var = ctk.BooleanVar(value=True)
        self.symbols_var = ctk.BooleanVar(value=True)
        self.periods_var = ctk.BooleanVar(value=False)

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
        self.logo.pack(pady=(25, 5))

        title = ctk.CTkLabel(
            self,
            text="PassVault",
            font=("Segue UI", 30, "bold"),
            text_color="#F1C9DA"
        )
        title.pack(pady=20)

        self.username = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Username",
            fg_color="#F1C9DA",
            text_color="black",
            border_color="#B56387"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Generated Password",
            show="*",
            fg_color="#F1C9DA",
            text_color="black",
            border_color="#B56387"
        )

        self.password.pack(pady=10)

        self.show_password = ctk.BooleanVar(value=False)

        self.show_button = ctk.CTkCheckBox(
            self,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password
        )

        ctk.CTkLabel(
            self,
            text="Password Length",
            text_color="#F1C9DA"
        ).pack()

        self.length_entry = ctk.CTkEntry(
            self,
            width=80,
            fg_color = "#F1C9DA",
            text_color = "black",
            border_color = "#B56387"
        )
        self.length_entry.insert(0, "")
        self.length_entry.pack(pady=5)

        ctk.CTkCheckBox(
            self,
            text="Uppercase",
            variable=self.uppercase_var
        ).pack()

        ctk.CTkCheckBox(
            self,
            text="Numbers",
            variable=self.numbers_var
        ).pack()

        ctk.CTkCheckBox(
            self,
            text="Symbols",
            variable=self.symbols_var
        ).pack()

        ctk.CTkCheckBox(
            self,
            text="Only . and ,",
            variable=self.periods_var
        ).pack()
        self.show_button.pack()

        self.generate_button = ctk.CTkButton(
            self,
            text="Generate Password",
            command=self.generate_newpassword,
            fg_color="#B56387",
            hover_color="#8D3136",
            text_color="white",
            corner_radius=15,
            height=38
        )
        self.generate_button.pack(pady=15)

        self.copy_button = ctk.CTkButton(
            self,
            text="Copy Password",
            command=self.copy_password,
            fg_color="#B56387",
            hover_color="#8D3136",
            text_color="white",
            corner_radius=15,
            height=38
        )
        self.copy_button.pack(pady=5)

        self.save_button = ctk.CTkButton(
            self,
            text="Save Credentials",
            command=self.save_credentials,
            fg_color="#B56387",
            hover_color="#8D3136",
            text_color="white",
            corner_radius=15,
            height=38
        )
        self.save_button.pack(pady=5)

        self.search_button = ctk.CTkButton(
            self,
            text="Search Vault",
            command=self.search_vault,
            fg_color="#B56387",
            hover_color="#8D3136",
            text_color="white",
            corner_radius=15,
            height=38
        )

        self.search_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(
            self,
            text="Delete Entry",
            fg_color="#8D3136",
            hover_color="#5A1F22",
            text_color="white",
            corner_radius=15,
            height=38
        )

        self.delete_button.pack(pady=5)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#F1C9DA"
        )

        self.result_label.pack(pady=20)

    def generate_newpassword(self):
        try:
            length = int(self.length_entry.get())

            password = generate_password(
                length,
                self.uppercase_var.get(),
                self.numbers_var.get(),
                self.symbols_var.get(),
                self.periods_var.get()
            )

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

        self.password.delete(0, "end")
        self.password.insert(0, password)

        strength = CheckStrength(password)

        entropy = CalculateEntropy(password)

        crack_time = CrackTime(entropy)

        warning = ""

        if CheckCommonPassword(password):
            warning = "\n Common password!"

        self.result_label.configure(
            text=
            f"Strength: {strength}\n"
            f"Entropy: {entropy} bits\n"
            f"Crack Time: {crack_time}"
            f"{warning}"
        )

    def save_credentials(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if username == "" or password == "":
            self.result_label.configure(
                text="Username and Password required"
            )
            return

        vault = {"entries": []}

        if os.path.exists("Vault.json"):
            try:
                with open("Vault.json", "r") as file:
                    vault = json.load(file)
            except json.JSONDecodeError:
                    vault = {"entries":[]}
                    return

        for entry in vault["entries"]:
            try:
                saved_username = decrypt(
                    entry["username"],
                    self.master_password
                )
                saved_password = decrypt(
                    entry["password"],
                    self.master_password
                )
            except (ValueError, TypeError, InvalidToken):
                messagebox.showerror(
                    "Vault Error",
                    "Unable to decrypt an existing vault entry."
                )
                return

            if saved_username == username:
                messagebox.showwarning(
                    "Duplicate Username",
                    "This username already exists."
                )

                return

            if saved_password == password:
                messagebox.showwarning(
                    "Duplicate Password",
                    "This password has already been saved."
                )

                return

        encrypted_username = encrypt(
            username,
            self.master_password
        )

        encrypted_password = encrypt(
            password,
            self.master_password
        )

        vault["entries"].append(

            {
                "username": encrypted_username,
                "password": encrypted_password
            }

        )
        with open("Vault.json", "w") as file:
            json.dump(
                vault,
                file,
                indent=6
            )

        self.result_label.configure(
            text="Credentials saved successfully."
        )

        messagebox.showinfo(
            "Success",
            "Credentials Saved"
            )

    def search_vault(self):
        username = self.username.get().strip()
        if username == "":
            messagebox.showwarning(
                "Search",
                "Enter a username to search for"
            )
            return

        if not os.path.exists("Vault.json"):
            messagebox.showinfo(
                "Search",
                "The Vault is empty."
            )
            return
        try:
            with open("Vault.json", "r") as file:
                vault = json.load(file)

        except json.JSONDecodeError:
            messagebox.showerror(
                "Vault Error",
                "The vault file is empty"
            )
            return

        for entry in vault["entries"]:
            try:
                saved_username = decrypt(
                    entry["username"],
                    self.master_password
                )
                saved_password = decrypt(
                    entry["password"],
                    self.master_password
                )

            except (ValueError, TypeError, InvalidToken):
                messagebox.showerror(
                    "Vault Error",
                    "Unable to decrypt the vault."
                )
                return

            if saved_username == username:
                self.password.delete(0, "end")
                self.password.insert(0, saved_password)

                self.result_label.configure(
                    text="Username found in vault."
                )

                return

        messagebox.showinfo(
            "Search",
            "Username was not found."
         )

    def copy_password(self):
        password = self.password.get()

        if password == "":
            messagebox.showwarning(
                "Copy Password",
                "There is no password to copy."
            )
            return

        self.clipboard_clear()
        self.clipboard_append(password)

        self.result_label.configure(
            text="Password copied to clipboard."
        )

    def toggle_password(self):
        if self.show_password.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")
