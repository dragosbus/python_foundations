import turtle

window = turtle.Screen()
window.bgcolor('red')

def draw_square(s):
    for i in range(4):
            s.forward(100)
            s.right(90)


def draw_shape():
    t = turtle.Turtle()
    t.speed(10)
    t.color('yellow') 
    for i in range(36):
        draw_square(t)
        t.right(10)
        
    
    window.exitonclick()

draw_shape()
