import customtkinter as ctk

from LoginPage import LoginWindow

ctk.set_appearance_mode(
    "dark"
)

ctk.set_default_color_theme(
    "blue"
)

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()