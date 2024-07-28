import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Drawing App")
    window.geometry("800x600")

    color = "black"

    canvas = tk.Canvas(window, bg="white", width=800, height=600)
    canvas.pack()

    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill=color, width=2)

    def set_color(new_color):
        nonlocal color
        color = new_color

    canvas.bind("<B1-Motion>", paint)

    color_frame = tk.Frame(window)
    color_frame.pack()

    colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink"]
    for c in colors:
        btn = tk.Button(color_frame, bg=c, width=2, height=1, command=lambda col=c: set_color(col))
        btn.pack(side=tk.LEFT)

    window.mainloop()

if __name__ == "__main__":
    create_window()
