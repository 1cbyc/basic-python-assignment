import turtle

def draw_circle(radius):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    
    x, y = 0, radius
    decision_parameter = 1 - radius

    def plot_points(x, y):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(5)  # Adjust the dot size as needed
        turtle.penup()

    def update_parameters():
        nonlocal x, y, decision_parameter
        decision_parameter += 2 * x + 1
        x += 1

        if decision_parameter > 0:
            decision_parameter += 2 - 2 * y
            y -= 1

    # Plotting the initial point in each octant
    for _ in range(2):
        plot_points(x, y)
        update_parameters()

    while y >= 0:
        plot_points(x, y)
        update_parameters()

    turtle.done()

# Draw a circle with radius 8 units
draw_circle(8)
