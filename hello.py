import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
glViewport(0, 0, width, height)
glOrtho(0, width, height, 0, -1, 1)

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 100)  # Vertex 1
    glVertex2f(200, 100)  # Vertex 2
    glVertex2f(150, 200)  # Vertex 3
    glEnd()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Red color
    drawTriangle()

    pygame.display.flip()

pygame.quit()
