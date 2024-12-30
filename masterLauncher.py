from draw_circle import drawCircle
from draw_rectangle import drawRectangle

def mainDrawingLauncher():
    draw = input("what do you want to draw a circle or a rectangle").lower().strip()
    if draw == "rectangle":
        drawRectangle()
    elif draw == "circle":
        drawCircle()
    else:
        print("sorry i dont understand try agein")

        
mainDrawingLauncher()