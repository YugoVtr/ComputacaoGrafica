#!/usr/bin/env python2.*
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys, random

WIDTH = 512
HEIGHT = 512

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(200, 100)
    glutCreateWindow("Transformacoes Geometricas")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
        
def display():
    glClear(GL_COLOR_BUFFER_BIT)  
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3f(0., 0., 0.)

    draw_d()
    
    glFlush()
    glutSwapBuffers()
    
def draw_d():
    x, y = WIDTH // 2, HEIGHT // 2
    objeto_d(x,y,2)
    glPushMatrix()
    glTranslatef(x,y,0)
    glRotatef(60,0,0,1)
    glTranslatef(-x,-y,0)
    objeto_d(10, 220, 2)
    glPopMatrix()

def objeto_d(x,y,e):
    glBegin(GL_POLYGON)
    glVertex2i(x + 35 * e, y + 10 * e)
    glVertex2i(x + 20 * e, y + 50 * e)
    glVertex2i(x + 55 * e, y + 75 * e)
    glVertex2i(x + 90 * e, y + 50 * e)
    glVertex2i(x + 75 * e, y + 10 * e)
    glVertex2i(x + 35 * e, y + 10 * e)
    glVertex2i(x + 55 * e, y + 75 * e)
    glVertex2i(x + 75 * e, y + 10 * e)
    glVertex2i(x + 20 * e, y + 50 * e)
    glVertex2i(x + 90 * e, y + 50 * e)
    glEnd()

def keyboard(key, x, y):
    if ord(key) == 27:
        sys.exit(0)
            
if __name__ == "__main__":
    main()
