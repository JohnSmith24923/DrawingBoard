import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Drawing App")
    window.geometry("800x600")

    canvas = tk.Canvas(window, bg="white", width=800, height=600)
    canvas.pack()

    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

    canvas.bind("<B1-Motion>", paint)

    window.mainloop()

if __name__ == "__main__":
    create_window()
