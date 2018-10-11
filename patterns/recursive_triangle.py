import turtle as t


def init():
    t.setup(1000,1000)
    t.bgcolor("black")
    t.color("white")
    t.speed(1)
    t.pd()


def draw_triangle(length, depth):
    if depth > 1:
        for i in range(3):
            t.fd(length)
            t.left(120)
        t.fd(length)
        draw_triangle(length / 2, depth - 1)
        for i in range(3):
            t.fd(length)
            t.left(120)
        t.left(120)
        t.fd(length)
        t.right(120)
        draw_triangle(length / 2, depth - 1)
        for i in range(3):
            t.fd(length)
            t.left(120)
        t.right(120)
        t.fd(length)
        t.left(120)
        draw_triangle(length / 2, depth - 1)


def main():
    init()
    length = 100
    depth = 2
    draw_triangle(length, depth)
    t.mainloop()


if __name__ == "__main__":
    main()