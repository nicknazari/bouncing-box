#!/usr/bin/env python3
# nick nazari 
# may 16 2019
# bouncing rectangle simulator like the dvd logo

import cv2
import numpy as np
import random

def randomColor(noblack=False):
    # returns a random color
    # bright guarantees that color is never black
    if noblack:
        chooser = random.randint(-1,1)
        if chooser == -1:
            return (255,0,0)
        elif chooser == 1:
            return (0,255,0)
        else:
            return (0,0,255)

    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# window size
width, height = 600, 400

def randomCoordinates():
    return (random.randint(width,height), random.randint(width, height))

# defining starting positions
x,y = 200 , 348 

# used to increment x and y
xspeed = 2
yspeed = 2 

# size of bouncing box
boxwidth = 60 
boxheight = 40

# keeps track of times that box has collided with both edges simultaneously
cornerHits = 0

# set color of bouncing rectangle
rectangleColor = randomColor(True) 

# set color of corner hit counter text
counterColor = (0,255,0)

# storing all circle positions placed on canvas
circlePositions = []

# one iteration is one frame
for i in range(100000):
    # making blank black canvas
    img = np.zeros((height, width, 3), np.uint8)

    # drawing rectangle in current position
    cv2.rectangle(img, (x, y), (x+boxwidth,y+boxheight), rectangleColor, -1)

    # drawing circle to trace path
    circlePositions.append((x,y))
    for pos in circlePositions:
        cv2.circle(img, pos, 2, (0,0,255))

    # displaying corner hits value
    cv2.putText(img, ('corner hits: %i' % cornerHits), (150, 250), cv2.FONT_HERSHEY_PLAIN, 1, counterColor)

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
