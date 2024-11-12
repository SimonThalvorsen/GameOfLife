import tkinter as tk
from grid import Grid

CELL_SIZE = 15
GRID_ROWS = 150
GRID_COLS = 150


class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game of Life")

        self.cell_size = CELL_SIZE
        self.grid = Grid(rows=GRID_ROWS, cols=GRID_COLS)
        self.generation = 0

        self.top_frame = tk.Frame(root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.generation_label = tk.Label(
            self.top_frame, text=f"Generation: {self.generation}"
        )
        self.generation_label.pack(side=tk.LEFT)

        self.start_button = tk.Button(
            self.top_frame, text="Start", command=self.start_simulation
        )
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(
            self.top_frame, text="Stop", command=self.stop_simulation
        )
        self.stop_button.pack(side=tk.LEFT)

        self.update_button = tk.Button(
            self.top_frame, text="Update", command=self.update_grid
        )
        self.update_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(
            self.top_frame, text="Reset", command=self.reset_grid
        )
        self.reset_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Configure>", self.resize_canvas)
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_canvas)
        self.canvas.bind("<MouseWheel>", self.zoom_canvas)

        self.offset_x, self.offset_y = 0, 0  
        self.running = False  
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                cell = self.grid.get_grid()[row][col]
                color = "black" if cell.is_alive() else "white"
                x1 = col * self.cell_size + self.offset_x
                y1 = row * self.cell_size + self.offset_y
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

        self.generation_label.config(text=f"Generation: {self.generation}")

    def update_grid(self):
        self.grid.update()
        self.generation += 1
        self.draw_grid()

    def start_simulation(self):
        self.running = True
        self.run_simulation()

    def stop_simulation(self):
        self.running = False

    def reset_grid(self):
        self.grid = Grid(rows=GRID_ROWS, cols=GRID_COLS)
        self.generation = 0  
        self.draw_grid()

    def run_simulation(self):
        if self.running:
            self.update_grid()
            self.root.after(100, self.run_simulation) 

    def resize_canvas(self, event):
        self.canvas.config(width=event.width, height=event.height)
        self.draw_grid()

    def start_drag(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def drag_canvas(self, event):
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        self.offset_x += dx
        self.offset_y += dy
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        self.draw_grid()

    def zoom_canvas(self, event):
        scale_factor = 1.1 if event.delta > 0 else 0.9
        self.cell_size = max(1, int(self.cell_size * scale_factor))
        self.draw_grid()


if __name__ == "__main__":
    root = tk.Tk()
    app = GameOfLifeApp(root)
    root.mainloop()
