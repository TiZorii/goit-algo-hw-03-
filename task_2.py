import turtle

def koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)
        turtle.right(120)
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)

def draw_snowflake(length, depth):
    for _ in range(3):
        koch_snowflake(length, depth)
        turtle.right(120)

if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    draw_snowflake(300, level)
    turtle.done()
