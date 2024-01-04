# Tomi, please note that to draw a circle using the midpoint algorithm, you'll need to iterate through octants and use symmetry to plot points.

Let me explain the process:

1. Initialize (x,y)(x,y) to (0,r)(0,r), where rr is the radius (8 units in this case).
2. Calculate the initial decision parameter P=1−rP=1−r.
3. In each step, plot the points in the current octant and update the decision parameter.
4. Use symmetry to plot points in other octants.

In summary sha, keep in mind that the midpoint algorithm allows you to approximate the circle by plotting points along its perimeter. I already wrote the code in the 'midpoint-algo\solution.py' file.

