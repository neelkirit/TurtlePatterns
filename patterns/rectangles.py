import turtle as t

"""
Python Lab Exam
Name- Neel Kirit
"""


def init():
    t.setup(1000, 1000)
    t.bgcolor("black")
    t.color("white")
    t.speed(100)


def draw_rect(size, depth, angle, length):
    """
    :pre: pos(0,0); pen up; heading east
    :post: pos at beginning of last NOT MADE rectangle (relative); pen down; heading towards the direction of rectangle
    :param size:
    :param depth:
    :param angle:
    :param length:
    :return: total length
    """
    if depth == 0:
        return length
    else:
        l = size
        b = size / 1.618

        t.fd(l)
        length = length + l

        t.right(angle)

        t.fd(b)
        length = length + b
        t.right(angle)

        t.fd(l)
        length = length + l

        t.right(angle)
        t.fd(b)
        length = length + b

        t.right(angle)

        t.fd(l / 3)

        t.right(angle)
        length = draw_rect(b, depth - 1, angle * 3, length)
        return length


def main():
    init()
    size = input("Enter size of long edge\n")
    level = input("Enter level\n")
    init_angle = 90
    length = 0
    length = draw_rect(size, level, init_angle, length)
    print(length)
    t.mainloop()


if __name__ == "__main__":
    main()
