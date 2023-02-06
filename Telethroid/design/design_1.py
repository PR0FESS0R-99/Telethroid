def design_1(t, clc):
    t.bgcolor('black')
    t.tracer(100)
    t.pensize(4)
    def main():
        h = 0
        n = 780
        t.up()
        t.goto(159, 0)
        t.down()
        for i in range(460):
            c = clc.hsv_to_rgb(h, 1, 1)
            h += 1/n
            t.color(c)
            t.fillcolor("black")
            t.begin_fill()
            t.rt(46.51)
            t.fd(i)
            t.circle(-25, 180)
            t.end_fill()
            t.circle(i, 21, steps=7)
            t.fd(256)
    main()
    t.down()
