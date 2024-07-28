import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Drawing App")
    window.geometry("800x600")
    window.mainloop()

if __name__ == "__main__":
    create_window()
