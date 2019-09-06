from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys, json

WIDTH = 800
HEIGHT = 400
RED, GREEN, BLUE = 0,0,0
SCALE = 1.1

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(250, 0)
    wind = glutCreateWindow("Animal")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
    glLineWidth(2)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_POLYGON_STIPPLE)

    displayBird(0,0, GL_LINE)
    displayBird(320,0, GL_FILL)
    glFlush()
    glutSwapBuffers()
    
def displayBird( x, y, flag ): 
    glPolygonMode(GL_FRONT_AND_BACK, flag)
    glColor3f(RED, GREEN, BLUE)
    glBegin(GL_POLYGON)
    with open("json/bird.json") as file:
        coordinates = json.load(file)
        for coordinate in coordinates:
            x1 = float( coordinate['value'].split(',')[0] ) * SCALE + x
            y1 = float( coordinate['value'].split(',')[1] ) * SCALE + y 
            glVertex2f(x1,y1)
    glEnd()

def keyboard(key, x, y):
    if ord(key) == 27:
        sys.exit(0)

if __name__ == "__main__":
    main()
