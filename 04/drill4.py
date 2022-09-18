import turtle

count = 0
while (count < 600):
    turtle.penup()
    turtle.goto(-200, count-200)
    turtle.pendown()
    turtle.forward(500)

    turtle.penup()
    turtle.goto(count-200, -200)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    count += 100
   
turtle.exitonclick()
