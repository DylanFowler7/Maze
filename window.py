import tkinter as tk
from tkinter import Tk, BOTH, Canvas
from point import Line


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("Maze Solver")
        self.canvas = tk.Canvas()
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.geometry(f"{self.width}x{self.height}")

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
