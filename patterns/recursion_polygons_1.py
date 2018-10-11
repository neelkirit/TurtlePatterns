import turtle as t


def init():
    t.setup(1000, 1000)
    t.bgcolor("black")
    t.color("white")
    t.speed(2)
    t.pensize(2)


def draw_polygon(n, s):
    if n-1 > 0:
        t.left(36)
        t.pd()
        total_angle = 180 * (s-2)
        angle = total_angle / s
        for i in range(s):
            t.fd(100)
            t.left(180-angle)
        t.pu()
        draw_polygon(n-1, s)


def main():
    init()
    no_of_polygons = 10
    no_of_sides = 5
    draw_polygon(no_of_polygons, no_of_sides)
    t.mainloop()


if __name__ == "__main__":
    main()
