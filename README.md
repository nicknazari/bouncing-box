# Bouncing box

This program simulates the bouncing dvd logo and counts corner collisions.

To use the program, simply set your values in config.yml, verify that they work with verify.py, and run dvd.py.

There is an equation to verify that a certain set of values will guarantee a collision:

- x = starting x
- y = starting y
- W = canvas width
- H = canvas height
- w = box width
- h = box height
- xspeed and yspeed must be equal

*|x-y| mod gcd(W - w, H - h) == 0*

If this condition is not met, the logo will never hit a corner

##### Interesting blog post about bouncing dvd logo
http://prgreen.github.io/blog/2013/09/30/the-bouncing-dvd-logo-explained/

