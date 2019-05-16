#!/usr/bin/env python3
# nick nazari 
# may 16 2019
# bouncing rectangle simulator like the dvd logo

import cv2
import numpy as np
import random

def randomColor(bright=False):
    # returns a random color
    # bright guarantees that color is never black
    if bright:
        return (random.randint(100,255), random.randint(100,255), random.randint(100,255))

    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# window size
width, height = 600, 400

# defining starting positions
x,y = 400,200

# used to increment x and y
xspeed = 6 
yspeed = 6

# size of bouncing box
boxheight = 40
boxwidth = 60 

# keeps track of times that box has collided with both edges simultaneously
cornerHits = 0

# set color of bouncing rectangle
rectangleColor = randomColor(True) 

# set color of corner hit counter text
counterColor = (0,0,255)

# one iteration is one frame
for i in range(100000):
    # making blank black canvas
    img = np.zeros((height, width, 3), np.uint8)

    # drawing rectangle in current position
    cv2.rectangle(img, (x, y), (x+boxwidth,y+boxheight), rectangleColor, -1)

    # displaying corner hits value
    cv2.putText(img, ('corner hits: %i' % cornerHits), (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, counterColor)

    # displaying rectangle
    cv2.imshow("img", img)
    cv2.waitKey(20)
    
    # checking if box is colliding with both edges (for corner hits)
    if (x >= width and y >= height) or (x <= 0 and y <= 0):
        cornerHits +=1
        rectangleColor = randomColor(True) 
        print("corner hit count increased")
        print("new count: %i" % cornerHits)

    # checking if box is colliding with edge
    if x >= width - boxwidth or x <= 0:
        rectangleColor = randomColor(True) 
        xspeed = -xspeed
    
    if y >= height - boxheight or y <= 0:
        rectangleColor = randomColor(True) 
        yspeed = -yspeed

    # moves the box
    x += xspeed
    y += yspeed 
