import turtle
objectname=input("Which object do you wanna draw?\n")
nsides=int(input("How many sides does the object have?\n"))
n=int(360/nsides)
for steps in range(1,nsides+1):
    turtle.forward(-100)
    turtle.color("red")
    turtle.right(n)
    print(steps)
    for steps2 in range(1,nsides+1):
        turtle.color("blue")
        turtle.forward(-50)
        turtle.right(n)
        print(steps2)
      