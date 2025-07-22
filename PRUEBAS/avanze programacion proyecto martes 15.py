


import pygame
pygame.init()
import random
import sys

#definir colores

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
REED  = ( 230,   0,   0)  
BLUE  = (   0,   0, 255)

# tablero = [["-----","-----","-----","-----","-----","___/","___/","___/","-----","-----","-----","-----","-----"],
#            ["-----","     ","     ","     ","-----","___/","___/","___/","-----","     ","     ","     ","-----"],
#            ["-----","'''''inicio rojo'''''''","-----","___/","___/","___/","-----","'''''inicio azul'''''''","-----"],
#            ["-----","     ","     ","     ","-----","___/","___/","___/","-----","     ","     ","     ","-----"],
#            ["-----","-----","-----","-----","-----","___/","___/","___/","-----","-----","-----","-----","-----"],
#            ["___/","___/","___/","___/","___/","___/","''''''''''''''","___/","___/","___/","___/","___/","___/"],
#            ["___/","___/","___/","___/","___/","___/","''''''''''''''","___/","___/","___/","___/","___/","___/"],
#            ["___/","___/","___/","___/","___/","___/","'''llegada''''","___/","___/","___/","___/","___/","___/"],
#            ["___/","___/","___/","___/","___/","___/","''''''''''''''","___/","___/","___/","___/","___/","___/"],
#            ["___/","___/","___/","___/","___/","___/","''''''''''''''","___/","___/","___/","___/","___/","___/"],
#            ["-----","-----","-----","-----","-----","___/","___/","___/","-----","-----","-----","-----","-----"],
#            ["-----","     ","     ","     ","-----","___/","___/","___/","-----","     ","     ","     ","-----"],
#            ["-----","'''''inicio verde''''''","-----","___/","___/","___/","-----","'''''inicio amarillo'''","-----"],
#            ["-----","     ","     ","     ","-----","___/","___/","___/","-----","     ","     ","     ","-----"],
#            ["-----","-----","-----","-----","-----","___/","___/","___/","-----","-----","-----","-----","-----"],
        
#     ]

# for yi in tablero:
#     print(yi)

# #tamaño de la ventana 

Ventana=(1000,800)

#nombre de la ventana 

pygame.display.set_caption("Parches proyecto final")


#crear la ventana 
screen = pygame.display.set_mode(Ventana)

#inica el juego y lo pone en bucle
while True:
    #permite cerrar la ventana 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #vuelve la pantalla en blanco 

    screen.fill(WHITE)

   #ficha colores

    # pygame.draw.circle(screen, RED, (50,50), 20)
    # pygame.draw.circle(screen, REED, (50,50), 15)
    # pygame.draw.circle(screen, RED, (50,50), 10)

#tablero
#carcel roja
    pygame.draw.rect(screen, REED, (0, 600, 200, 200))

    #lineas cercana a la carcel roja 
    pygame.draw.line(screen, BLACK, [0, 600], [200, 600], 5)
    pygame.draw.line(screen, BLACK, [0, 500], [300, 500], 5)
    pygame.draw.line(screen, BLACK, [300, 800], [300, 500], 5)
    pygame.draw.line(screen, BLACK, [200, 600], [200, 800], 5)
    pygame.draw.line(screen, BLACK, [500, 500], [500, 800], 5)

    for cordenada in range(0, 210, 30):
        pygame.draw.line(screen, BLACK, [cordenada, 600], [cordenada, 500], 5)

#esquina superior cercana a la carcel roja
    pygame.draw.line(screen, BLACK, [200, 600], [210, 570], 5)
    pygame.draw.line(screen, BLACK, [210, 570], [210, 500], 5)
    pygame.draw.line(screen, BLACK, [210, 570], [300, 570], 5)

    for cordenada2 in range(600, 800, 30):
        pygame.draw.line(screen, BLACK, [200, cordenada2], [300, cordenada2], 5)

    for cordenada3 in range(500, 800, 30):
        pygame.draw.line(screen, BLACK,[300, cordenada3], [500, cordenada3], 5)    

    pygame.display.flip()
    
