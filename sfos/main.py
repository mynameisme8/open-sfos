import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Tkinter Window")
    root.attributes("-fullscreen", True)

    calculator_window = None

    def open_calculator():
        nonlocal calculator_window
        if calculator_window is not None and calculator_window.winfo_exists():
            calculator_window.deiconify()
            calculator_window.lift()
            return

        calculator_window = tk.Toplevel(root)
        calculator_window.title("Calculator")
        calculator_window.geometry("440x560")
        calculator_window.resizable(False, False)

        entry = tk.Entry(calculator_window, font=("Segoe UI", 24), justify="right", bd=4, relief=tk.RIDGE)
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=12)

        for index in range(4):
            calculator_window.grid_columnconfigure(index, weight=1)
        for index in range(6):
            calculator_window.grid_rowconfigure(index, weight=1)

        def add_to_entry(value):
            entry.insert(tk.END, value)

        def clear_entry():
            entry.delete(0, tk.END)

        def minimize_calculator():
            calculator_window.iconify()

        def calculate():
            try:
                result = str(eval(entry.get()))
                entry.delete(0, tk.END)
                entry.insert(0, result)
            except Exception:
                entry.delete(0, tk.END)
                entry.insert(0, "Error")

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            action = calculate if text == "=" else (lambda value=text: add_to_entry(value))
            btn = tk.Button(
                calculator_window,
                text=text,
                width=8,
                height=3,
                font=("Segoe UI", 16),
                command=action,
            )
            btn.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

        clear_button = tk.Button(
            calculator_window,
            text="C",
            width=8,
            height=2,
            font=("Segoe UI", 16),
            command=clear_entry,
        )
        clear_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=(6, 12))

        minimize_calc_button = tk.Button(
            calculator_window,
            text="Minimize",
            width=8,
            height=2,
            font=("Segoe UI", 16),
            command=minimize_calculator,
        )
        minimize_calc_button.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=10, pady=(6, 12))

    def toggle_start_menu():
        if start_menu_frame.winfo_viewable():
            start_menu_frame.place_forget()
        else:
            start_menu_frame.place(relx=1.0, rely=0.8, anchor="se")

    def minimize_window():
        root.iconify()

    bottom_frame = tk.Frame(root, bd=1, relief=tk.RAISED, height=90, bg="#d9d9d9")
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
    bottom_frame.pack_propagate(False)

    close_button = tk.Button(
        bottom_frame,
        text="Close",
        command=root.destroy,
        width=12,
        height=2,
        font=("Segoe UI", 12),
    )
    close_button.pack(side=tk.LEFT, padx=16, pady=12)

    smile_button = tk.Button(
        bottom_frame,
        text=":)",
        command=toggle_start_menu,
        width=12,
        height=2,
        font=("Segoe UI", 12),
    )
    smile_button.pack(side=tk.RIGHT, padx=16, pady=12)

    start_menu_frame = tk.Frame(root, bd=2, relief=tk.SOLID, bg="#ececec")
    calculator_button = tk.Button(
        start_menu_frame,
        text="Calculator",
        width=20,
        height=2,
        font=("Segoe UI", 11),
        command=open_calculator,
    )
    calculator_button.grid(row=0, column=0, padx=10, pady=4)

    for i in range(2, 11):
        btn = tk.Button(
            start_menu_frame,
            text=f"Useless {i}",
            width=20,
            height=2,
            font=("Segoe UI", 11),
        )
        btn.grid(row=i - 1, column=0, padx=10, pady=4)

    root.mainloop()


if __name__ == "__main__":
    main()
