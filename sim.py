import math

from linefollow import *

import cv2
import numpy as np

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



class Controller:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.action = 0
    def stop(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.action = 0
    def move_up(self):
        self.y = 1
        self.action = 1
    def move_down(self):
        self.y = -1
        self.action = 1
    def move_right(self):
        self.x = 1
        self.action = 1
    def move_left(self):
        self.x = -1
        self.action = 1
    def move_in(self):
        self.z = 1
        self.action = 1
    def move_back(self):
        self.z = -1
        self.action = 1
    def roll_right(self):
        self.roll = 1
        self.action = 1
    def roll_left(self):
        self.roll = -1
        self.action = 1
    def pitch_up(self):
        self.pitch = 1
        self.action = 1
    def pitch_down(self):
        self.pitch = -1
        self.action = 1
    def yaw_right(self):
        self.yaw = 1
        self.action = 1
    def yaw_left(self):
        self.yaw = -1
        self.action = 1

def Plane(x,y,z,theta,phi,gamma,l,w, wire = True):
    theta =  math.radians(theta)
    phi = math.radians(phi)
    verticies = (
            (x-(l)*math.cos(theta)+(w)*math.sin(gamma),y+(w)*math.cos(phi)+(l)*math.sin(gamma),z-(l)*math.sin(theta)+(w)*math.sin(phi)),
            (x+(l)*math.cos(theta)+(w)*math.sin(gamma),y+(w)*math.cos(phi)-(l)*math.sin(gamma),z+(l)*math.sin(theta)+(w)*math.sin(phi)),
            (x+(l)*math.cos(theta)-(w)*math.sin(gamma),y-(w)*math.cos(phi)-(l)*math.sin(gamma),z+(l)*math.sin(theta)-(w)*math.sin(phi)),
            (x-(l)*math.cos(theta)-(w)*math.sin(gamma),y-(w)*math.cos(phi)+(l)*math.sin(gamma),z-(l)*math.sin(theta)-(w)*math.sin(phi))
            )

    edges = (
            (0,1),
            (1,2),
            (2,3),
            (3,0)
            )

    surfaces = (
            (0,1,2,3)
            )



    if wire == True:
        glBegin(GL_LINES)
        for edge in edges:
           for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()
    else:
        glBegin(GL_QUADS)
        #for surface in surfaces:
            #for vetex in surface: Hardcode edition
        glTexCoord2f(0,0)
        glVertex3fv(verticies[0])
        glTexCoord2f(1,0)
        glVertex3fv(verticies[1])
        glTexCoord2f(1,1)
        glVertex3fv(verticies[2])
        glTexCoord2f(0,1)
        glVertex3fv(verticies[3])
        glEnd()


def loadTexture(file):
    textureSurface = pygame.image.load(file)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def main():
    autonomousMode = False
    
    pygame.init()
    display = (800,600)
    controller = Controller()
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    t = 25
    x,y,z = 0,0,t
    gluPerspective(45, (display[0]/display[1]), 0.1, 100)
    glRotatef(180, 0,1,0)
    glTranslatef(0,0,t)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
            d = 0.1
            f = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    autonomousMode = True

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     glTranslatef(-d,0,0)
                     x -= d
                 if event.key == pygame.K_RIGHT:
                     glTranslatef(d,0,0)
                     x += d
                 if event.key == pygame.K_DOWN:
                     glTranslatef(0,d,0)
                     y += d
                 if event.key == pygame.K_UP:
                     glTranslatef(0,-d,0)
                     y -= d

                 if event.key == pygame.K_q:
                     glTranslatef(-x,-y,-z)
                     glRotatef(f,0,0,1)
                     glTranslatef(x,y,z)
                 if event.key == pygame.K_e:
                     glTranslatef(-x,-y,-z)
                     glRotatef(-f,0,0,1)
                     glTranslatef(x,y,z)
                 if event.key == pygame.K_a:
                     glTranslatef(-x,-y,-z)
                     glRotatef(-f,0,1,0)
                     glTranslatef(x,y,z)
                 if event.key == pygame.K_d:
                     glTranslatef(-x,-y,-z)
                     glRotatef(f,0,1,0)
                     glTranslatef(x,y,z)
                 if event.key == pygame.K_w:
                     glTranslatef(-x,-y,-z)
                     glRotatef(f,1,0,0)
                     glTranslatef(x,y,z)
                 if event.key == pygame.K_s:
                     glTranslatef(-x,-y,-z)
                     glRotatef(-f,1,0,0)
                     glTranslate(x,y,z)



            if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 4:
                     glTranslatef(0,0,d)
                     z += d

                 if event.button == 5:
                     glTranslatef(0,0,-d)
                     z -= d

        if controller.action == 1:
             if controller.x == -1:
                 glTranslatef(-d,0,0)
                 x -= d
             if controller.x == 1:
                 glTranslatef(d,0,0)
                 x += d
             if controller.y == -1:
                 glTranslatef(0,d,0)
                 y += d
             if controller.y == 1:
                 glTranslatef(0,-d,0)
                 y -= d

             if controller.roll == 1:
                 glTranslatef(-x,-y,-z)
                 glRotatef(f,0,0,1)
                 glTranslatef(x,y,z)
             if controller.roll == -1:
                 glTranslatef(-x,-y,-z)
                 glRotatef(-f,0,0,1)
                 glTranslatef(x,y,z)
             if controller.yaw == -1:
                 glTranslatef(-x,-y,-z)
                 glRotatef(-f,0,1,0)
                 glTranslatef(x,y,z)
             if controller.yaw == 1:
                 glTranslatef(-x,-y,-z)
                 glRotatef(f,0,1,0)
                 glTranslatef(x,y,z)
             if controller.pitch == 1:
                 glTranslatef(-x,-y,-z)
                 glRotatef(f,1,0,0)
                 glTranslatef(x,y,z)
             if controller.pitch == -1:
                 glTranslatef(-x,-y,-z)
                 glRotatef(-f,1,0,0)
                 glTranslate(x,y,z)
             if controller.z == -1:
                 glTranslatef(0,0,d)
                 z += d
             if controller.z == 1:
                 glTranslatef(0,0,-d)
                 z -= d


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        loadTexture('redline.bmp')
        Plane(0  , 0 ,  0, 0  , 0  , 0 , 4 , 3, wire = False)
        loadTexture('purple.bmp')
        Plane(-4 , 0 , -8, 90 , 0  , 0 , 8 , 3, wire = False)
        Plane(4  , 0 , -8, 90 , 0  , 0 , 8 , 3, wire = False)
        Plane(0  , -3  , -8 , 0  , 90 , 0 , 4 , 8, wire = False)

        string_image = pygame.image.tostring(screen, 'RGB')
        temp_surf = pygame.image.fromstring(string_image,(800, 600),'RGB' )

        tmp_arr = pygame.surfarray.array3d(temp_surf)
        rotates = np.rot90(tmp_arr,3)
        rotates = np.fliplr(rotates)

        r,g,b = cv2.split(rotates)
        opencv_data = cv2.merge([b,g,r])
        cv2.imwrite("Display.jpg",opencv_data) #debug frame

        pygame.display.flip()

        linefollow.run(opencv_data, controller, autonomousMode)

        pygame.time.wait(10)


main()
