import pygame,sys
from pygame.locals import DOUBLEBUF,OPENGL
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init();display=(900,650);pygame.display.set_mode(display,DOUBLEBUF|OPENGL);pygame.display.set_caption('Activity 5: PyOpenGL Hardware Pipeline');glViewport(0,0,*display);glMatrixMode(GL_PROJECTION);glLoadIdentity();gluPerspective(45,display[0]/display[1],.1,50);glMatrixMode(GL_MODELVIEW);glEnable(GL_DEPTH_TEST);glEnable(GL_BLEND);glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
V=[(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1)];F=[(0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)];C=[(1,0,0,1),(0,1,0,1),(0,0,1,1),(1,1,0,1),(1,0,1,1),(0,1,1,1)]
def cube():
 glBegin(GL_QUADS)
 for i,f in enumerate(F):
  glColor4fv(C[i])
  for j in f:glVertex3fv(V[j])
 glEnd()
def arm():
 glPushMatrix();glTranslatef(-2,0,0);glRotatef(25,0,1,0);glPushMatrix();glScalef(.35,1.3,.35);cube();glPopMatrix();glTranslatef(0,1.6,0);glRotatef(45,0,0,1);glPushMatrix();glScalef(.3,1,.3);cube();glPopMatrix();glPopMatrix()
clock=pygame.time.Clock();angle=0.;run=True
while run:
 dt=clock.tick(60);angle+=50*dt/1000
 for e in pygame.event.get():
  if e.type==pygame.QUIT:run=False
  if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:run=False
 glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);glLoadIdentity();glTranslatef(0,0,-8);glPushMatrix();glRotatef(angle,1,1,0);cube();glPopMatrix();glPushMatrix();glTranslatef(2,0,0);glRotatef(angle*.7,0,1,0);glBegin(GL_QUADS);glColor4f(1,.2,.2,.45);glVertex3f(-1,-1,0);glVertex3f(1,-1,0);glVertex3f(1,1,0);glVertex3f(-1,1,0);glColor4f(.2,.3,1,.45);glVertex3f(-1,-1,.8);glVertex3f(1,-1,.8);glVertex3f(1,1,.8);glVertex3f(-1,1,.8);glEnd();glPopMatrix();arm();pygame.display.flip()
pygame.quit();sys.exit()
