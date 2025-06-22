# Główna aplikacja GUI
import tkinter as tk
from tkinter import simpledialog , messagebox
from utils.controller import get_grouped_map
from utils.model import clients, employees , toll_booth
import webbrowser


def gui_main():
    def open_map(file_name="mapa.html"):
        webbrowser.open(file_name)

    def make_menu(title, dataset, type_):
        window = tk.Toplevel(root)
        window.title(title)

    root = tk.Tk()
    root.title("System zarządzania punktami poboru opłat")

    tk.Button(root, text="Punkt poboru opłat", command=lambda: make_menu("Punkt poboru opłat", toll_booth, "toll_booth")).pack(pady=10)
    tk.Button(root, text="Pracownicy", command=lambda: make_menu("Pracownicy", employees, "employees")).pack(pady=10)
    tk.Button(root, text="Klienci", command=lambda: make_menu("Klienci", clients, "clients")).pack(pady=10)

    tk.Button(root, text="Zamknij", command=root.destroy).pack(pady=20)
    root.mainloop()