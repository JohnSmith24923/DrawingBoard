import tkinter as tk
from tkinter import filedialog

def create_window():
    window = tk.Tk()
    window.title("Simple Drawing App")
    window.geometry("800x600")

    color = "black"
    brush_size = 2

    canvas = tk.Canvas(window, bg="white", width=800, height=600)
    canvas.pack()

    def paint(event):
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)

    def set_color(new_color):
        nonlocal color
        color = new_color

    def set_brush_size(new_size):
        nonlocal brush_size
        brush_size = new_size

    def clear_canvas():
        canvas.delete("all")

    def save_canvas():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            canvas.postscript(file=file_path + ".eps")
            from PIL import Image
            img = Image.open(file_path + ".eps")
            img.save(file_path, "png")

    canvas.bind("<B1-Motion>", paint)

    control_frame = tk.Frame(window)
    control_frame.pack()

    color_frame = tk.Frame(control_frame)
    color_frame.pack(side=tk.LEFT)

    colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink"]
    for c in colors:
        btn = tk.Button(color_frame, bg=c, width=2, height=1, command=lambda col=c: set_color(col))
        btn.pack(side=tk.LEFT)

    size_frame = tk.Frame(control_frame)
    size_frame.pack(side=tk.LEFT)

    sizes = [2, 5, 8, 10]
    for s in sizes:
        btn = tk.Button(size_frame, text=str(s), width=2, height=1, command=lambda size=s: set_brush_size(size))
        btn.pack(side=tk.LEFT)

    action_frame = tk.Frame(control_frame)
    action_frame.pack(side=tk.LEFT)

    clear_btn = tk.Button(action_frame, text="Clear", command=clear_canvas)
    clear_btn.pack(side=tk.LEFT)

    save_btn = tk.Button(action_frame, text="Save", command=save_canvas)
    save_btn.pack(side=tk.LEFT)

    window.mainloop()

if __name__ == "__main__":
    create_window()