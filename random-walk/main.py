import turtle
import random
from PIL import Image
import os

#CONSTANTS(FOR CUSTOMIZABILITY)
WALKS = 100




timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

timmy.color('LimeGreen')
timmy.pensize(15)
timmy.speed("fast")

directions = [90,180,270,360]

for i in range(WALKS):
    
    timmy.forward(30)

    timmy.right(random.choice(directions))

    timmy.color(random_color())

timmy.penup()
timmy.goto(1000,1000)



# Save as EPS first, then convert to PNG and removes the eps
save_path = r"random-walk\generated_Images\randomwalk.png"
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