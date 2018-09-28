import turtle
colour="black"
line_length="0"
angle="0"
colour=input("Enter the colour you wish to draw with\
select any from the following listed in the paranthesis(Red,Green,Brown,Blue) ")
line_length=int(input("Kindly enter the line length you would like to use: "))
angle=int(input("Remember to specify the angle you intend to use \
the angle should be between 0 and 360: "))
while line_length !=0:
    turtle.forward(line_length)
    turtle.right(angle)
    turtle.color(colour)
    line_length=int(input("Enter the line length you would like to use "))
#print("You are such an amazing artist. Well done ")

    if line_length !=0:
        angle=int(input("Specify the angle you intend to use in your drawing: "))
        colour=input("Enter the colour you wish to draw with ")
print("You are such an amazing artist. Keep it up Champ! ")
      


















#import turtle
#shape=input("What shape would you like to draw?")
#sides=int(input("Enter the number of sides of the shape "))
#n=int(360/sides)
#for steps in range(1,sides+1):
#    turtle.forward(50)
#    turtle.left(n)
#    turtle.color("red")
#    print(steps)
#    for colour in range(sides):
#        turtle.forward(25)
#        turtle.left(n)
        
#import turtle
#shapename=input("What shape would you want to draw? ")
#shapesides=int(input("How many sides does your shape have? "))
#n=int(360/shapesides)
#corner=int(input("Enter the number of corners that your shapesides has "))
#counter=0
#while corner==shapesides:
#    turtle.forward(-100)
#    turtle.right(n)
#    turtle.color("red")
#    counter=counter+1
#    if counter==corner:
#        break
#    else:
#        continue

    

#print(counter)   
#print(shapesides)

 
