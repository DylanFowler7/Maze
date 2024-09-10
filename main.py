from window import *
from point import Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(200, 300)
    p2 = Point(300, 500)
    line1 = Line(p1,p2)
    win.draw_line(line1, "black")
    win.wait_for_close()

if __name__ == '__main__':
    main()

