import turtle as t


def init():
    t.setup(1000, 1000)
    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(20)


def draw_pattern(length, iteration, angle):
    """
    
    :param length:
    :param iteration:
    :param angle:
    :return:
    """
    if iteration > 0:
        t.fd(length)
        t.right(angle)
        draw_pattern(length*1.2, iteration-1, angle)


def main():
    init()
    length = 10
    t.left(180)
    iteration = 20
    angle = 95
    draw_pattern(length, iteration, angle)
    t.mainloop()


if __name__ == "__main__":
    main()
