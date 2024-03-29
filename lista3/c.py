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

    draw_c()
    
    glFlush()
    glutSwapBuffers()
    
def draw_c():
    x, y = WIDTH // 2, HEIGHT // 2
    objeto_c(x,y,2)
    glPushMatrix()
    glTranslatef(x,y,0)
    glRotatef(60,0,0,1)
    glTranslatef(-x,-y,0)
    objeto_c(10, 220, 2)
    glPopMatrix()

def objeto_c(x,y,e):
    glBegin(GL_POLYGON)
    glVertex2i(x + 10 * e, y + 10 * e)
    glVertex2i(x + 40 * e, y + 40 * e)
    glVertex2i(x + 20 * e, y + 40 * e)
    glVertex2i(x + 40 * e, y + 60 * e)
    glVertex2i(x + 30 * e, y + 60 * e)
    glVertex2i(x + 50 * e, y + 80 * e)
    glVertex2i(x + 60 * e, y + 80 * e)
    glVertex2i(x + 80 * e, y + 60 * e)
    glVertex2i(x + 70 * e, y + 60 * e)
    glVertex2i(x + 90 * e, y + 40 * e)
    glVertex2i(x + 70 * e, y + 40 * e)
    glVertex2i(x + 100 * e, y + 10 * e)
    glEnd()

def keyboard(key, x, y):
    if ord(key) == 27:
        sys.exit(0)
            
if __name__ == "__main__":
    main()
