__author__ = "neelkirit"

import turtle as t


def init():
    """
    This method initializes the turtle window
    :return: nothing
    """
    t.setup(1000, 1000)
    t.bgcolor("black")
    t.color("white")
    t.speed(20)
    t.pensize(5)


def draw_trunk(trunk_length):
    """
    This method draws the trunk of the tree
    :pre: pos(0,0), pen up, heading right
    :post: post(0,trunk_length), pen up, heading up
    :param trunk_length:
    :return: nothing
    """
    t.pd()
    t.left(90)
    t.fd(trunk_length)
    t.pu()


def draw_leaves(length, branches):
    """
    This method draws the branches of the tree
    :pre: pos(0,trunk_length), pen up, heading up
    :post: post(0,trunk_length), pen up, heading up
    :param length:
    :param branches:
    :return: nothing
    """
    t.left(45)
    t.pd()
    t.fd(length)
    t.pu()
    if branches-1 > 0:
        draw_leaves(length/2, branches-1)
    t.bk(length)
    t.right(90)
    t.pd()
    t.fd(length)
    t.up()
    if branches-1 > 0:
        draw_leaves(length/2, branches-1)
    t.bk(length)
    t.left(45)


def bring_turtle_back(trunk_length):
    """
    This method brings the turtle back to init position
    :pre: pos(0,trunk_length), pen up, heading up
    :post: post(0,0), pen up, heading right
    :param trunk_length:
    :return: nothing
    """
    t.bk(trunk_length)
    t.right(90)


def main():
    """
    main method
    :return: nothing
    """
    init()
    trunk_length = 100
    branch_length = 100
    no_of_branches = 5
    draw_trunk(trunk_length)
    draw_leaves(branch_length, no_of_branches)
    bring_turtle_back(trunk_length)
    t.mainloop()


if __name__ == "__main__":
    main()
