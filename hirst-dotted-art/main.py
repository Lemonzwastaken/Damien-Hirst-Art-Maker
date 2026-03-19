#EXTRACTS COLOR FROM A COLOR PALLET WE LIKE
import colorgram
rgb_colors = []
colors = colorgram.extract('hirst-dotted-art\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r,g,b))

import turtle
import random
from PIL import Image
import os

#Setting timmy up
timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def draw_dots():
    for _ in range(10):
        timmy.dot(25, random.choice(rgb_colors))
        timmy.forward(50)
        
def change_line():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

lines = int(input("How many lines do you want: "))

for dots in range(lines):
    draw_dots()
    change_line()



save_path = r"hirst-dotted-art\generated_Images\hirst-dotted-art.png"
eps_path = "randomwalk.eps"

canvas = screen.getcanvas()
canvas.postscript(file=eps_path)

print("EPS saved:", os.path.exists(eps_path))

img = Image.open(eps_path)
img.load()
img_copy = img.copy()
img.close()

print("Image size:", img_copy.size)
print("Image mode:", img_copy.mode)

img_copy.save(save_path)
print("PNG saved:", os.path.exists(save_path))
print("Saved to:", os.path.abspath(save_path))

os.remove(eps_path)


screen.exitonclick()


screen.exitonclick()