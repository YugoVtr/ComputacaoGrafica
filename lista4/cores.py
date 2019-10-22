#!/usr/bin/env python2.*
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

xrot = 0
yrot = 0
zrot = 0
ratio = 0
AlfaVidro = 0.5
x = 0 

def init():
	# Black Background
	glClearColor(0.0, 0.0, 0.0, 1.0)				

def reshape( w, h ):
	global ratio
	# Prevent a divide by zero, when window is too short
	# (you cant make a window of zero width).
	if h == 0:
		h = 1

	ratio = 1.0 * w / h

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	glViewport(0, 0, w, h)

	# Seta o angulo de visao
	gluPerspective(50, ratio, 1, 200)
 
	# Define a posicao do observador
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0, 0, 5, 0, 0, 0, 0.0, 1.0, 0.0)
	print(ratio)

def DrawCube(alfa):
	glBegin ( GL_QUADS )
	# Front Face
	glColor4f( 0.7, 0.7, 0, alfa)
	glVertex3f(-1.0, -1.0,  1.0)
	glVertex3f( 1.0, -1.0,  1.0)
	glVertex3f( 1.0,  1.0,  1.0)
	glVertex3f(-1.0,  1.0,  1.0)
	# Back Face
	glColor4f(0,0,0.7, alfa)
	glVertex3f(-1.0, -1.0, -1.0)
	glVertex3f(-1.0,  1.0, -1.0)
	glVertex3f( 1.0,  1.0, -1.0)
	glVertex3f( 1.0, -1.0, -1.0)
	# Top Face
	glColor4f(0.7,0,0.7, alfa)
	glVertex3f(-1.0,  1.0, -1.0)
	glVertex3f(-1.0,  1.0,  1.0)
	glVertex3f( 1.0,  1.0,  1.0)
	glVertex3f( 1.0,  1.0, -1.0)
	# Bottom Face
	glColor4f(0.7,0.7,0.7, alfa)
	glVertex3f(-1.0, -1.0, -1.0)
	glVertex3f( 1.0, -1.0, -1.0)
	glVertex3f( 1.0, -1.0,  1.0)
	glVertex3f(-1.0, -1.0, 1.0)
	# Right face
	glColor4f(0,0.5,0, alfa)
	glVertex3f( 1.0, -1.0, -1.0)
	glVertex3f( 1.0,  1.0, -1.0)
	glVertex3f( 1.0,  1.0,  1.0)
	glVertex3f( 1.0, -1.0,  1.0)
	# Left Face
	glColor4f(0.7,0,0, alfa)
	glVertex3f(-1.0, -1.0, -1.0)
	glVertex3f(-1.0, -1.0,  1.0)
	glVertex3f(-1.0,  1.0,  1.0)
	glVertex3f(-1.0,  1.0, -1.0)
	glEnd()


def DesenhaPlano(alfa):
	glBegin(GL_QUADS)
	glVertex3f(-1.0, -1.0,  1.0)
	glVertex3f( 1.0, -1.0,  1.0)
	glVertex3f( 1.0,  1.0,  1.0)
	glVertex3f(-1.0,  1.0,  1.0)
	glEnd()

def DesenhaVidro(alfa):
	global x 
	x = -2
	delta = -0.001
	glPushMatrix()
	glTranslatef(x,0,0)

	if (x > 2) or (x < -2):
		delta = delta * -1

	x = x + delta
	glColor4f(1, 1, 1, alfa)
	DesenhaPlano(1)
	glPopMatrix()

def display():

	try:

		global xrot, yrot, zrot, AlfaVidro
		glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

		# Desabilita o BLEND par ao primeiro objeto
		glDisable(GL_BLEND)
		glPushMatrix()
		glTranslatef(0, 0, -1)
		glRotatef ( xrot, 1.0, 0.0, 0.0 )
		glRotatef ( yrot, 0.0, 1.0, 0.0 )
		glRotatef ( zrot, 0.0, 0.0, 1.0 )

		# habilita remocao de faces traseiras
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		DrawCube(0.5)		
		glPopMatrix()

		# Habilita o BLEND para ao segundo objeto
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)	

		glPushMatrix()
		glTranslatef(0, 0, 0)
		DesenhaVidro(AlfaVidro)
		glPopMatrix()

		xrot = xrot + 0.01
		yrot = yrot + 0.001
		zrot = zrot + 0.02
		glutSwapBuffers()
	
	except Exception as e:
		print(e)
		sys.exit(0)

def keyboard(key, x, y):
	if ord(key) == 27:
		sys.exit(0)

def main():    
	glutInit( sys.argv )
	glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA )
	glutInitWindowPosition(0,0)
	glutInitWindowSize( 700, 500 )
	glutCreateWindow( "Computacao Grafica - Teste com Transparencias..." )
		
	init()

	glutDisplayFunc( display ) 
	glutReshapeFunc( reshape )
	glutKeyboardFunc( keyboard )

	glutIdleFunc( display )
	glutMainLoop()  

if __name__ == "__main__": 
	main() 



