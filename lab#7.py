
from graphics import *
import math


#using distance formula 
def distance(point, circle):
    x = point.getX() - circle.getCenter().getX()
    y = point.getY() - circle.getCenter().getY()
    dist = math.sqrt(x*x + y*y)

    return dist <= circle.getRadius()

    
def main():

    score = 0
    
    win = GraphWin('Archery',300,300)
    center=Point(150, 150)

    c1=Circle(center,100)
    c1.setFill("white")
    c1.draw(win)

    c2=Circle(center,80)
    c2.setFill("black")
    c2.draw(win)

    c3=Circle(center, 60)
    c3.setFill("blue")
    c3.draw(win)

    c4=Circle(center, 40)
    c4.setFill("red")
    c4.draw(win)

    c5=Circle(center,20)
    c5.setFill("yellow")
    c5.draw(win)

    for x in range(5):
        click= win.getMouse()
        
        if(distance(click, c5)):
            score += 9
            print("+9")
        elif(distance(click, c4)):
            score += 7
            print("+7")
        elif(distance(click, c3)):
            score += 5
            print("+5")
        elif(distance(click, c2)):
            score += 3
            print("+3")
        elif(distance(click, c1)):
            score += 1
            print("+1")
        else:
            score += 0
            print("+0")
    
    
    print("Your total points are: ", score)

                    
    win.getMouse()
    win.close()
    
main()
