from turtle import *
'''''''''
speed(10)
bgcolor("black")
for i in range(220):
    pencolor("red")
    forward(100)  # draw base
    pencolor("blue")
    towards(-100, 100)
    left(120)
    goto(i, i)
    pencolor("orange")
    forward(100)
    pencolor("purple")
    left(120)
    pencolor("yellow")
    forward(100)
    pencolor("green")
    right(100)
    goto(i*50, i+10)
    pencolor("gray")
    back(100)

'''''''''''
t= Turtle()

def triangle():
    color('blue')
    forward(100) # Draws a line at 0 degrees on a xy coordinate
    left(120) #Faces the angle to left by 120 degrees
    forward(100) #continues forward by 100 degrees
    left(120)
    forward(100)
    fillcolor('orange')

def square():
    color('blue')
    fillcolor('yellow')
    for i in range(4):
        forward(100)
        left(90)

    #fillcolor('yellow')


def spiral():

    colormode()
    t.speed(10)
    bgcolor('blue')
    for i in range(100):
        if i % 2 == 0:
            t.pencolor('#C4FAFC') # light blue
            #t.begin_fill()
            #t.fillcolor('#C4FAFC')

        if i %3 == 0:
            t.pencolor('#87044E') # magenta
            #t.begin_fill()
            #t.fillcolor('#87044E')

        if i % 4 ==0:
            t.pencolor('#DD90F4') # light purple
            #t.begin_fill()
            #t.fillcolor('#DD90F4')

        if i %5==0:
            t.pencolor('#67E75D') # green
            #t.begin_fill()
            #t.fillcolor('#67E75D')

        if i % 6==0:
            t.pencolor('#4A62C7') #blue
            #t.begin_fill()
            #t.fillcolor('#4A62C7')
        if i % 7==0:
            t.pencolor('#FF283E') #red
            #t.begin_fill()
            #t.fillcolor('#FF283E')

        if i % 8 ==0:
            t.pencolor('#EBEF6B')
            #t.begin_fill()
            #t.fillcolor('#EBEF6B')
        if i % 9 ==0:
            t.pencolor('#F29F7B')
            #t.begin_fill()
            #t.fillcolor('#F29F7B')
        t.circle(5*i)
        t.circle(-5*i)
        t.left(i)
        #t.end_fill()



def rainbow():
    colors = ['#8c80ed', '#a0a6f7', '#f7a0af', '#6aed9a', '#96fff9', '#ed896a']
    pen()
    bgcolor('black')
    for x in range(360):
        pencolor(colors[x%6])
        width(x//100 +1)
        forward(x)
        left(59)





#rainbow()
spiral()

done = input('are you done?')
if done =='yes':
     t.done()
