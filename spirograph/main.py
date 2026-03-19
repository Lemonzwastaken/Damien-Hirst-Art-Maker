import turtle
import random
import os
from PIL import Image

timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

timmy.color('LimeGreen')
timmy.speed(0)

radius = int(input("What is the radius of the circle: "))
increment = int(input("How much space do you want between the circles: "))

for rad in range(int(360/increment)):

    timmy.circle(radius)
    timmy.right(increment)
    timmy.color(random_color())


# Save as EPS first, then convert to PNG and removes the eps
save_path = r"spirograph\generated_images\spirograph.png"
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