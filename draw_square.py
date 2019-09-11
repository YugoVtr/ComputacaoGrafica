#!/usr/bin/env python2.*
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(256, 256)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Preenchendo regiões")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMainLoop()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, 256, 0, 256, -1, 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_POLYGON_STIPPLE)

    glPolygonMode(GL_BACK, GL_LINE)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2i(30,226)
    glVertex2i(113,226)
    glVertex2i(113,143)
    glVertex2i(30,143);
    glEnd()
    
    glPolygonMode(GL_BACK, GL_FILL);
    glColor3f(0, 1, 0);
    glBegin(GL_POLYGON);
    glVertex2i(143,226); glVertex2i(226,226);
    glVertex2i(226,143); glVertex2i(143,143);
    glEnd();
    
    glBegin(GL_POLYGON);
    glColor3f(1.0, 0.0, 0.0);  glVertex2i(30,113);
    glColor3f(0.0, 1.0, 0.0);  glVertex2i(113,113);
    glColor3f(0.0, 0.0, 1.0);  glVertex2i(113,30);
    glColor3f(1.0, 1.0, 0.0);  glVertex2i(30,30);
    glEnd();

    glFlush()
    glutSwapBuffers()

def keyboard(key, x, y):
    key = int.from_bytes(key, "big")
    if key == 27:
        sys.exit(0)

def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_LEFT_BUTTON:
        print('oi')

if __name__ == "__main__":
    main()
