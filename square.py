from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys, random

WIDTH = 512
HEIGHT = 512
a = {'x':10, 'y':200, 'w':200}
b = {'x':300, 'y':200, 'w':200}
c = None

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(200, 100)
    wind = glutCreateWindow("Square")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMainLoop()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, WIDTH, HEIGHT, 0, -1, 1)
        
def display():
    glClear(GL_COLOR_BUFFER_BIT)    
    square(a['x'],a['y'],a['w'], 0,1,0)
    square(b['x'],b['y'],b['w'], 0,0,1)
    if(c): 
        red,green,blue = random.random(), random.random(), random.random()
        print(" Red: {0};\n Green: {1};\n Blue: {2};\n".format(red,green,blue))
        square(c['x'],c['y'],c['w'], red,green,blue)
    glFlush()
    glutSwapBuffers()

def square(x,y,w,r,g,b):    
    glPolygonMode(GL_BACK, GL_FILL)
    glColor3f(r, g, b)
    glBegin(GL_POLYGON)
    glVertex2i(x,y)
    glVertex2i(x,y+w)
    glVertex2i(x+w,y+w)
    glVertex2i(x+w,y)
    glEnd()
    
def keyboard(key, x, y):
    key = int.from_bytes(key, "big")
    if key == 27:
        sys.exit(0)

def mouse(button, state, x, y):
    global c
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if x > a['x'] and x < a['x'] + a['w'] and y > a['y'] and y < a['y'] + a['w']:  
            print("X:{0} ,Y:{1}".format(x,y))
            glutPostRedisplay()
            c = {'x':x-10, 'y':y-10, 'w':20}
        elif x > b['x'] and x < b['x'] + b['w'] and y > b['y'] and y < b['y'] + b['w']:
            print("X:{0} ,Y:{1}".format(x,y))
            glutPostRedisplay()
            c = {'x':x-10, 'y':y-10, 'w':20}
            
if __name__ == "__main__":
    main()
