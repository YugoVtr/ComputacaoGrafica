from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np 

ctlpoints = np.empty((4,4,3))
showPoints = 0
theNurb = gluNewNurbsRenderer()

def init_surface():
    for u in range(4):
        for v in range(4):
            ctlpoints[u][v][0] = 2.0*(u - 1.5)
            ctlpoints[u][v][1] = 2.0*(v - 1.5)

            if ( (u == 1 or u == 2) and (v == 1 or v == 2)):
                ctlpoints[u][v][2] = 3.0
            else:
                ctlpoints[u][v][2] = -3.0

def nurbsError(errorCode):
   estring = gluErrorString(errorCode)
   print("Nurbs Error: {0}\n".format(estring)) 

def init():
    mat_diffuse = [ 0.7, 0.7, 0.7, 1.0 ]
    mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
    mat_shininess = [ 100.0 ]

    glClearColor (0.0, 0.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_NORMALIZE)

    init_surface()

    theNurb = gluNewNurbsRenderer()
    gluNurbsProperty(theNurb, GLU_SAMPLING_TOLERANCE, 25.0)
    gluNurbsProperty(theNurb, GLU_DISPLAY_MODE, GLU_FILL)
    gluNurbsCallback(theNurb, GLU_ERROR, nurbsError)


def display():
    knots = [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0]
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(330.0, 1.,0.,0.)
    glScalef (0.5, 0.5, 0.5)

    gluBeginSurface(theNurb)
    gluNurbsSurface(theNurb, 8, knots, 8, knots, 4 * 3, 3, ctlpoints[0][0][0], 4, 4, GL_MAP2_VERTEX_3)
    gluEndSurface(theNurb)

    if showPoints:
        glPointSize(5.0)
        glDisable(GL_LIGHTING)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_POINTS)
    
        for i in range(4):
            for j in range(4):
                glVertex3f(ctlpoints[i][j][0], ctlpoints[i][j][1], ctlpoints[i][j][2])

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
    if key == 'c':
        showPoints = not showPoints
        glutPostRedisplay()
    elif ord(key) == 27:
        sys.exit(0) 

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize (500, 500)
    glutInitWindowPosition (100, 100)
    glutCreateWindow("Superficie")
    init()
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc (keyboard)
    glutMainLoop()