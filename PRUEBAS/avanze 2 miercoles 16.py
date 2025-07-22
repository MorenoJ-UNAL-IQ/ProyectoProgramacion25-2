

from diccionario import colores
import pygame
pygame.init()
import random
import sys
import os

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

    screen.fill(colores["WHITE"])

   #fichas

    # for i in range
    # pygame.draw.circle(screen, colores["RED"], (50,50), 20)
    # pygame.draw.circle(screen, colores["REED"], (50,50), 15)
    # pygame.draw.circle(screen, colores["RED"], (50,50), 10)

#tablero
#carcel roja
    pygame.draw.rect(screen, colores["REED"], (0, 600, 210, 210))

#carcel AZUL
    pygame.draw.rect(screen, colores["BLUEE"], (0, 100, 210, 210))

#carcel verde
    pygame.draw.rect(screen, colores["GREEEN"], (500, 100, 210, 210))

#carcel amarilla
    pygame.draw.rect(screen, colores["YEELLOW"], (500, 600, 210, 210))


#lineas que pasan por todo el parches
    for cordenada in range(0, 420, 210):

        pygame.draw.line(screen, colores["BLACK"], [cordenada, 100], [cordenada, 800], 5)

    for cordenada in range(500, 820, 210):
   
        pygame.draw.line(screen, colores["BLACK"], [cordenada, 100], [cordenada, 800], 5)



    for cordenada in range(100, 420, 210):
         pygame.draw.line(screen, colores["BLACK"], [0, cordenada], [710, cordenada], 5)

    for cordenada in range(600, 1020, 210):
         pygame.draw.line(screen, colores["BLACK"], [0, cordenada], [710, cordenada], 5)

        


#lineas de las casillas
#casillas a la derecha de la carcel roja
    for cordenada in range(600, 800, 30):
        pygame.draw.line(screen, colores["BLACK"], [210, cordenada], [500, cordenada], 5)


    for cordenada in range(300, 600, 100):

        pygame.draw.line(screen, colores["BLACK"], [cordenada, 570], [cordenada, 800], 5)


#casillas abajo de la carcel azul
    for cordenada in range(0, 210, 30):
        pygame.draw.line(screen, colores["BLACK"], [cordenada, 600], [cordenada, 310], 5)

    for cordenada in range(400, 600, 100):
        pygame.draw.line(screen, colores["BLACK"], [0, cordenada], [240, cordenada], 5)

#casillas a la derecha de la carcel azul
    for cordenada in range(100, 310, 30):
        pygame.draw.line(screen, colores["BLACK"], [210, cordenada], [500, cordenada], 5)


    for cordenada in range(300, 600, 100):

        pygame.draw.line(screen, colores["BLACK"], [cordenada, 100], [cordenada, 340], 5)

#casillas abajo de la carcel amarilla
    for cordenada in range(500, 710, 30):
        pygame.draw.line(screen, colores["BLACK"], [cordenada, 600], [cordenada, 310], 5)

    for cordenada in range(400, 600, 100):
        pygame.draw.line(screen, colores["BLACK"], [470, cordenada], [710, cordenada], 5)
        



#esquina superior cercana a la carcel
#horizontales 
    pygame.draw.line(screen, colores["BLACK"], [210, 600], [240, 570], 5)
    pygame.draw.line(screen, colores["BLACK"], [210, 310], [240, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [500, 310], [470, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [500, 600], [470, 570], 5)

#verticales
    pygame.draw.line(screen, colores["BLACK"], [240, 570], [240, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [240, 570], [470, 570], 5)
    pygame.draw.line(screen, colores["BLACK"], [470, 570], [470, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [240, 340], [470, 340], 5)






    pygame.display.flip()
