'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''

import random
import arcade

SW = 500
SH = 300
radius = 10

class Circle:
    def __init__(self):
        self.pos_x = random.randint(radius,(SW-radius))
        self.pos_y = random.randint(radius, (SH - radius))
        self.radius = radius
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def draw_circle(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.radius,self.color)



def main():
    arcade.open_window(SW,SH,"1000 Circles")
    arcade.start_render()

    for i in range (1000):

        circ = Circle()
        circ.draw_circle()

    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()