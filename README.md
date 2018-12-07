run with python sim.py

hey sluggos, this simulation is pretty simple to use. Here's how it works.

requirements:
python version of opencv
pyopengl
pygame
numpy (don't know if this is installed by default)

ALL OF THESE CAN AND SHOULD BE INSTALLED WITH PIP. just do pip install <package>, you might need root (sudo).

Evey frame, algo.run() is given the given, the RGB array which is already set up nicely work work with 
opencv, and a controller to move around the ROV. There is full degree of movement with transpositions 
(like sliding along x,y,z) and rotations (pitch, yaw, roll). These can be used by doing something like
controller.move_in() or controller.pitch_left(). controller.stop() should be called at the start of each
algo.run() iteration because there is no way to return specific transformations to neutral.

In order to debug, there are also keyboard bindings to move around the enviroment:

w - pitch up

s - pitch down

a - turn left

d - right

q - roll left

e - roll right

scroll in - move in (along z)

scroll down - move back

up - move up

down - move down

left - move left

right - move right

![alt text](https://raw.githubusercontent.com/jcirimel/sluggosim/master/Display.jpg)

