# Bouncing box

This program simulates the bouncing dvd logo and counts corner collisions.

There is some math to verify that a certain set of values will guarantee a collision:

- x = starting x
- y = starting y
- W = canvas width
- H = canvas height
- w = box width
- h = box height

*|x-y| mod gcd(W - w, H - h) == 0*

If this condition is not met, the logo will never hit a corner

### Interesting configurations

##### Bounces from corner to corner
- default values
- x = 537
- y = 358
- xspeed = 3
- yspeed = 2
