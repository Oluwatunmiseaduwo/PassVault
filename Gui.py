import customtkinter as ctk

from Vault import create_vault

def open_main_window():
    create_vault()
    app = ctk.CTk()
    app.geometry("700x500")
    app.title(
        "PassVault"
    )

    title = ctk.CTkLabel(
        app,
        text="PassVault Password Manager",
        font=("Arial", 24)
    )
    title.pack(pady=30)

    username = ctk.CTkEntry(
        app,
        placeholder_text="Username"
    )
    username.pack(pady=10)

    password = ctk.CTkEntry(
        app,
        placeholder_text="Password",
        show="*"
    )
    password.pack(pady=10)

    app.mainloop()

'''
import tkinter as tk
from tkinter import messagebox

from PasswordGenerator import generate_password
from PasswordChecker import (CheckStrength, CalculateEntropy, CrackTime
                             )

def create_password():
    try:
        length = int(length_entry.get())

        password = generate_password(
            length,
            use_upper_var.get(),
            use_digits_var.get(),
            use_symbols_var.get(),
            use_periods_var.get()
        )

        strength = CheckStrength(password)

        if strength == "Weak Strength":
            strength_label.config(
                text="Weak Password",
                fg="red"
            )

        if strength == "Medium Strength":
            strength_label.config(
                text="Medium Password",
                fg="orange"
            )

        if strength == "Strong Strength":
            strength_label.config(
                text="Strong Password",
                fg="lime"
            )

        entropy = CalculateEntropy(password)

        time = CrackTime(entropy)

        password_output.config(state="normal")
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state="readonly")

        results.config(
            text= f"Strength: {strength}\n"
                  f"Entropy: {entropy} bits \n"
                  f"Estimated Crack Time: {time}"
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )

window = tk.Tk()

window.title("Password Generator Tool")

window.configure(bg="#260309")

window.geometry("500x500")

title = tk.Label(
    window,
    text="Secure Password Generator",
    font=("Arial", 18,"bold"),
    bg="#260309",
    fg="#F9EBF2"
)

title.pack(pady=10)

length_label = tk.Label(
    window,
    text="Password Length"
)

length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

use_upper_var = tk.BooleanVar(value= True )
use_digits_var = tk.BooleanVar(value= True)
use_symbols_var = tk.BooleanVar(value= True)
use_periods_var = tk.BooleanVar(value= False)

upper_cb = tk.Checkbutton(
    window,
    text="Uppercase Letters",
    variable=use_upper_var,
    fg="#F9EBF2",
    bg="#260309",
    selectcolor="#BF3054",
    activebackground="#260309",
    activeforeground="#F9EBF2"
)

upper_cb.pack()

upper_cb = tk.Checkbutton(
    window,
    text="Numbers",
    variable=use_digits_var,
    fg="#F9EBF2",
    bg="#260309",
    selectcolor="#BF3054",
    activebackground="#260309",
    activeforeground="#F9EBF2"
)

upper_cb.pack()

upper_cb = tk.Checkbutton(
    window,
    text="Symbols",
    variable=use_symbols_var,
    fg="#F9EBF2",
    bg="#260309",
    selectcolor="#BF3054",
    activebackground="#260309",
    activeforeground="#F9EBF2"
)

upper_cb.pack()

upper_cb = tk.Checkbutton(
    window,
    text="Only use '.' and ','",
    variable=use_periods_var,
    fg="#F9EBF2",
    bg="#260309",
    selectcolor="#BF3054",
    activebackground="#260309",
    activeforeground="#F9EBF2"
)

upper_cb.pack()

generate_button = tk.Button(
    window,
    text="Generate Password",
    bg="#BF3054",
    fg="#F9EBF2",
    activebackground="#EBA2B9",
    command=create_password
)

generate_button.pack(pady=20)

password_title = tk.Label(
    window,
    text="Generated Password:"
)

password_title.pack()

password_output = tk.Entry(
    window,
   font=("Arial", 14),
    width=35
)

password_output.pack()

results = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    fg="#F9EBF2",
    bg="#260309"
)

results.pack(pady=20)

strength_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    fg="#F9EBF2",
    bg="#260309"
)

strength_label.pack()

def copy_password():
    password = password_output.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        status_label.config(
            text="Password Copied!"
        )

status_label = tk.Label(
    window,
    text="",
    fg="#F9EBF2",
    bg="#260309"
)

status_label.pack()

copy_button = tk.Button(
    window,
    text="Copy Password",
    command=copy_password
)

copy_button.pack(pady=10)

window.mainloop()
'''