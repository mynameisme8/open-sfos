import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Tkinter Window")
    root.geometry("400x250")

    bottom_frame = tk.Frame(root, bd=1, relief=tk.RAISED)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    close_button = tk.Button(bottom_frame, text="Close", command=root.destroy)
    close_button.pack(side=tk.RIGHT, padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
