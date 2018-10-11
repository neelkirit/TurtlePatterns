import turtle


def s(n, l):
    if n == 0:
        # turtle.fd(l / 2)
        # turtle.left(120)
        # turtle.fd(l / 2)
        # turtle.left(120)
        # turtle.fd(l / 2)
        # turtle.left(120)
        return
    else:
        turtle.fd(l/2)
        turtle.left(120)
        s(n-1, l/2)
        turtle.fd(l / 2)
        turtle.left(120)
        s(n - 1, l/2)
        turtle.fd(l / 2)
        turtle.left(120)
        s(n - 1, l/2)
        # return





def init():
    turtle.setup(1000,1000)
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.speed(10)
    turtle.pd()


def main():
    init()
    s(4, 500)
    turtle.mainloop()


if __name__ == "__main__":
    main()