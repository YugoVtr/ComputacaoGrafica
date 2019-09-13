#!/usr/bin/env python2.*
# -*- coding: utf-8 -*-
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array, zeros
import sys, os, random 

points = zeros((4,4,3))
show = 0
nurb = None

def init_surface():
    global points, nurb, show
    for u in range(4):
        for v in range(4):
            points[u][v][0] = 2.0 * (u - 1.5)
            points[u][v][1] = 2.0 * (v - 1.5)  
            if (u == 1 or u == 2) and (v == 1 or v == 2):
			    points[u][v][2] = 4.0       
    for u in range(4): 
        points[0][u][2] = -2.0   

def errors(errorCode):
    estring = gluErrorString(errorCode)
    print("Nurbs Error: {0}\n".format(estring))
    sys.exit(0)

def init():
    global points, nurb, show
    mat_diffuse = array((0.7, 0.7, 0.7, 1.0), 'f')
    mat_specular = array((1.0, 1.0, 1.0, 1.0), 'f')
    mat_shininess = array((100.0), 'f')

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_NORMALIZE)

    init_surface()

    nurb = gluNewNurbsRenderer()
    gluNurbsProperty(nurb, GLU_SAMPLING_TOLERANCE, 1.0)
    gluNurbsProperty(nurb, GLU_DISPLAY_MODE, GLU_FILL)
    gluNurbsCallback(nurb, GLU_ERROR, errors)

def display(): 
    global points, nurb, show
    knots = array((0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0), 'f')
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(330.0, 1.0, 0.0, 0.0)
    glScalef (0.5, 0.5, 0.5)
    gluBeginSurface(nurb)
    gluNurbsSurface(nurb, knots, knots, points, GL_MAP2_VERTEX_3)
    gluEndSurface(nurb)

    if show:
        glPointSize(5.0)
        glDisable(GL_LIGHTING)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_POINTS)
        for i in range(4):
            for j in range(4):
                glVertex3f(points[i][j][0], points[i][j][1], points[i][j][2])
        glEnd()
        glEnable(GL_LIGHTING)
    glPopMatrix()
    glFlush()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective (45.0, w/h, 3.0, 8.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef (0.0, 0.0, -5.0)

def keyboard(key, x, y):
    global show
    if key == 'c': 
        show = not show
        glutPostRedisplay()
    elif ord(key) == 27:
        sys.exit(0)

def main(): 
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize (500, 500)
    glutInitWindowPosition (100, 100)
    glutCreateWindow(sys.argv[0])
    init()
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc (keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()