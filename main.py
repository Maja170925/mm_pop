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

        listbox = tk.Listbox(window, width=60, height=15)
        listbox.pack(padx=10, pady=10)

        def refresh_list():
            listbox.delete(0, tk.END)
            for item in dataset:
                toll_booth_info = f"       {item['toll_booth']}" if "toll_booth" in item else ""
                listbox.insert(tk.END, f"{item['name']}       {item['location']}{toll_booth_info}")

        def add():
            name = simpledialog.askstring("Dodaj", "Podaj nazwę:")
            location = simpledialog.askstring("Dodaj", "Podaj lokalizację:")

            if not name or not location:
                messagebox.showwarning("Błąd", "Musisz podać nazwę i lokalizację.")
                return

            if type_ in ["clients", "employees"]:
                toll_booth_names = [s["name"] for s in toll_booth]

                toll_booth_window = tk.Toplevel(window)
                toll_booth_window.title("Wybierz punkt poboru opłat")

                tk.Label(toll_booth_window, text="Wybierz punkt poboru opłat dla tej osoby:").pack(pady=5)
                selected_toll_booth = tk.StringVar()
                selected_toll_booth.set(toll_booth_names[0])

                tk.OptionMenu(toll_booth_window, selected_toll_booth, *toll_booth_names).pack(pady=5)

                def confirm_toll_booth():
                    booth = selected_toll_booth.get()
                    dataset.append({
                        "name": name,
                        "location": location,
                        "toll_booth": booth
                    })
                    toll_booth_window.destroy()
                    refresh_list()

                tk.Button(toll_booth_window, text="Zatwierdź", command=confirm_toll_booth).pack(pady=10)
            else:
                dataset.append({
                    "name": name,
                    "location": location
                })
                refresh_list()


root = tk.Tk()
root.title("System zarządzania punktami poboru opłat")












