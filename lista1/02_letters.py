#!/usr/bin/env python2.*
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys, random, json
from const import JSON_PATH

WIDTH = 800
HEIGHT = 400
RED, GREEN, BLUE = random.random(), random.random(), random.random()
SCALE = 1.6

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(250, 0)
    wind = glutCreateWindow("Letters")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMainLoop()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
    
def initRGB(): 
    global RED, GREEN, BLUE
    RED, GREEN, BLUE = random.random(), random.random(), random.random()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    with open("{0}/letters.json".format(JSON_PATH)) as file:
        letters = json.load(file)
        for letter in letters:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            initRGB()
            if letters.index(letter) == len(letters) -1:
                glColor3f(1.0, 1.0, 1.0)
            else:
                glColor3f(RED, GREEN, BLUE)
            glBegin(GL_POLYGON)
            for coordinate in letter: 
                x = float( coordinate.split(',')[0] ) * SCALE
                y = float( coordinate.split(',')[1] ) * SCALE
                glVertex2f(x,y)
            glEnd()
    
        glFlush()
        glutSwapBuffers()

def keyboard(key, x, y):
    key = int.from_bytes(key, "big")
    if key == 27:
        sys.exit(0)

def mouse(button, state, x, y):
    initRGB()
    glutPostRedisplay()

if __name__ == "__main__":
    main()
