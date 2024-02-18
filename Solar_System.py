
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import math

# Global variables
angle = 0.0  # Angle for Earth's orbit around the Sun
moon_angle = 0.0  # Angle for the Moon's orbit around the Earth
march_angle = 0.0  # Angle for the additional orbiting object
mercury_angle =0.0
venus_angle =0.0
jupiter_angle =0.0
satrun_angle =0.0
uranus_angle =0.0
neptune_angle =0.0
satrunring_angle =0.0

def _sphere(radius, slices, stacks):
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluQuadricTexture(quad, GL_TRUE)
    gluSphere(quad, radius, slices, stacks)

    # visual representation of orbit
def _orbit(radius):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        theta = math.radians(i)
        x = radius * math.cos(theta)
        y = 0.0
        z = radius * math.sin(theta)
        glVertex3f(x, y, z)
    glEnd()

def _solar_system():
    #  Sun
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    _sphere(1.0, 50, 50)
    
    glColor3f(0.5, 0.5, 0.5)  # Gray
    _orbit(6.5)

    
    glColor3f(1.0, 0.0, 0.0)  # Red
    glPushMatrix()
    glRotatef(march_angle, 0.0, 1.0, 0.0)
    glTranslatef(6.5, 0.0, 0.0)
    _sphere(0.25, 25, 25)

    glPopMatrix()
     # mercury orbiting object's orbit
    glColor3f(0.5, 0.5, 0.5)  # Gray
    _orbit(2.5)

    # mercury orbiting object
    glColor3f(1.0, 0.0, 0.0)  # Red
    glPushMatrix()
    glRotatef(mercury_angle, 0.0, 1.0, 0.0)
    glTranslatef(2.5, 0.0, 0.0)
    _sphere(0.2, 20, 20)

    glPopMatrix()

    # Earth's orbit
    glColor3f(0.5, 0.5, 0.5)  # Gray
    _orbit(4.5)

    # Earth
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glPushMatrix()
    glRotatef(angle, 0.0, 1.0, 0.0)
    glTranslatef(4.5, 0.0, 0.0)
    _sphere(0.3, 30, 30)

    # Moon's orbit around Earth
    glColor3f(0.5, 0.5, 0.5)  # Gray
    _orbit(0.8)

    #  Moon
    glColor3f(0.7, 0.7, 0.7)  # Light Gray
    glRotatef(moon_angle, 0.0, 1.0, 0.0)
    glTranslatef(0.8, 0.0, 0.0)
    _sphere(0.2, 20, 20)

    glPopMatrix()

    # venus
    glColor3f(0.5, 0.5, 0.5)  # Gray
    _orbit(3.5)

    #  venus orbiting object
    glColor3f(0.647, 0.165, 0.165)  # brown
    glPushMatrix()
    glRotatef(venus_angle, 0.0, 1.0, 0.0)
    glTranslatef(3.5, 0.0, 0.0)
    _sphere(0.3, 30, 30)

    glPopMatrix()

   # jupiter
    glColor3f(0.5, 0.5, 0.5) #gray
    _orbit(5.5)

    glColor3f(1.0,1.0,1.0)
    glPushMatrix()
    glRotatef(jupiter_angle,0.0,1.0,0.0)
    glTranslatef(5.5, 0.0, 0.0 )
    _sphere(0.5,50,50)

    glPopMatrix()


 
    # satrun
    glColor3f(0.5, 0.5, 0.5)
    _orbit(7.5)
    glColor3f(0.0,0.0,0.5)
    glPushMatrix()
    glRotatef(satrun_angle,0.0,1.0,0.0)
    glTranslatef(7.5,0.0,0.0)
    _sphere(0.45,45,45)
    # ring around satrun
    glColor3f(0.5, 0.5, 0.5)  # Gray
    _orbit(0.5)
    _orbit(0.6)   
    glPopMatrix()

    # uranus
    glColor3f(0.5, 0.5, 0.5)
    _orbit(8.5)
    glColor3f(0.0,1.0,0.0)
    glPushMatrix()
    glRotatef(uranus_angle,0.0,1.0,0.0)
    glTranslatef(8.5,0.0,0.0)
    _sphere(0.45,45,45)
    glPopMatrix()

    # neptune
    glColor3f(0.5, 0.5, 0.5)
    _orbit(9.5)
    glColor3f(0.5, 0.5,0.5)
    glPushMatrix()
    glRotatef(neptune_angle,0.0,1.0,0.0)
    glTranslatef(9.5,0.0,0.0)
    _sphere(0.45,45,45)
    glPopMatrix()



def display():
    global angle, moon_angle, march_angle,mercury_angle,venus_angle,satrun_angle,jupiter_angle,uranus_angle,neptune_angle,satrunring_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluPerspective(45.0, 1.0, 1.0, 100.0)
    gluLookAt(10, 10, 20, 0, 0, 0, 0, 1, 0)

    _solar_system()

    pygame.display.flip()

def update():
    global angle, moon_angle,mercury_angle, march_angle,venus_angle,jupiter_angle,satrun_angle,uranus_angle,neptune_angle
    angle += 0.5  # Earth's rotation speed
    moon_angle += 2.0  # Moon's rotation speed around Earth
    march_angle += 0.5  
    mercury_angle += 1.0
    venus_angle += 2.5
    jupiter_angle += 2.2
    satrun_angle +=0.7
    uranus_angle +=1.5
    neptune_angle +=0.7
  

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((800, 800), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        update()
        display()
        pygame.time.Clock().tick(30)