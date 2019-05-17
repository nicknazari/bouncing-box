#!/usr/bin/env python3
# nick nazari
# may 16 2019
# this function can be used to verify if a set of values will guarantee corner collisions
import math
import yaml

def verify(W,H,w,h,x,y):
    if abs(x-y) % math.gcd(W - w, H - h) == 0:
        return True

    return False

if __name__ == "__main__":
    # loading config values
    with open('config.yml', 'r') as cfgfile:
        config = yaml.load(cfgfile, Loader=yaml.FullLoader)

    # window width/height
    width = config['width']
    height = config['height']
    # bouncing box width/height
    boxwidth = config['boxwidth']
    boxheight = config['boxheight']
    # bouncing box starting position
    x = config['x']
    y = config['y']

    if verify(boxwidth, boxheight, width, height, x, y):
        print("This configuration works")
    else:
        print("This configuration will not work")
