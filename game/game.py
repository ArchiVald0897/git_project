import math
import turtle

tr = turtle.Turtle()
window = turtle.Screen()
window.setup(width=1200, height=800)
window.addshape("background.gif")
window.screensize(1200, 800)
tr.shape("background.gif")

BASE_X, BASE_Y = 0, -300


def get_an_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx ** 2 + dy ** 2)
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if dy < 0:
        alpha = -alpha
    return alpha


def fire_missile(x, y):
    missile = turtle.Turtle(visible=False)
    missile.speed(0)
    missile.color("white")
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    heading = get_an_angle(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(heading)
    missile.showturtle()
    info = {"missile": missile, "target": [x, y], "state": "launched", "radius": 0}
    our_missiles.append(info)


window.onclick(fire_missile)
our_missiles = []

while True:
    window.update()

    for i in our_missiles:
        state = i["state"]
        missile = i["missile"]
        if state == "launched":
            missile.forward(4)
            target = i["target"]
            if missile.distance(x=target[0], y=target[1]) < 20:
                i["state"] = "explode"
                missile.shape("circle")
        elif state == "explode":
            i["radius"] += 1
            if i["radius"] > 5:
                missile.clear()
                missile.hideturtle()
                i["state"] = "dead"
            else:
                missile.shapesize(i["radius"])

    dead_missiles = [info for info in our_missiles if info["state"] == "dead"]
    for dead in dead_missiles:
        our_missiles.remove(dead)
