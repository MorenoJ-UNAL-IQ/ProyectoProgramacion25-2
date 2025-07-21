

from diccionario import colores
import pygame
pygame.init()
import random
import sys
import os


#limita los fps
clock = pygame.time.Clock()
#DADOS

# print(carcel)
#MOVIMIENTOS
#movimientos = 0
#while True:
  #try:
    #if dado1=5 or dado2=5
      #movimientos = 1
      #break



lista_de_jugadores = [1, 2 , 3 , 4]




#turnos(funciona infinitamente pero funcionan  falta ver como hacer que solo se active cada cierto  tiempo 
# o despues de cierta accion si es haci se le puede quitar el while)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#     try:
#         jugadores1 = int(input("¿Cuántos jugadores habrán? (Seleccione de 2-4)"))
#         if jugadores1 >= 2 and jugadores1 <= 4:
#             break
#         else:
#             print("Debe seleccionar entre 2 y 4 jugadores")
#     except ValueError:
#         print("Debe ingresar un número")


def turnos(lista_de_jugadores):

  global contador_de_turnos




#   if dado2 == dado1:
#       print("puedes volver a tirar los dados")

#   elif contador_de_turnos == 10:

#       print("fin del juego")
#       t = False

#   else:

#        primero = lista_de_jugadores.pop(0)   
#        lista_de_jugadores.append(primero)     
        

#   contador_de_turnos = contador_de_turnos + 1
   

fuente = pygame.font.SysFont("Arial", 40)

turnos(lista_de_jugadores)

# #tamaño de la ventana

Ventana=(1000,800)

#nombre de la ventana

pygame.display.set_caption("Parches proyecto final")


#crear la ventana
screen = pygame.display.set_mode(Ventana)

#variable para el bucle

jugadores1 = None 

texto_ingresado = ""
error = ""
u = True
t = True
    
#inica el juego y lo pone en bucle
while u:
    #muestra cualquier evento 
    for event in pygame.event.get():
        
    #permite cerrar la ventana
        if event.type == pygame.QUIT:
            sys.exit()

        #verifica si se toca una pieza
        if event.type == pygame.KEYDOWN:
            #verifica si da enter
            if event.key == pygame.K_RETURN:
                #creo que esto muestra el mensaje o le codifica no se 
                try:
                    
                    numero = int(texto_ingresado)
                    if 2 <= numero <= 4:
                        jugadores1 = numero
                        u = False 
                        error = "" 
                    else:
                        error = "Debe seleccionar entre 2 y 4 jugadores"
                except ValueError:
                    error = "Debe ingresar un número"
                texto_ingresado = ""
            elif event.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]
            else:
                texto_ingresado += event.unicode
        #pantalla en negro
        screen.fill(colores["BLACK"])
        #tambien puede se resto el mensaje 
    mensaje_render = fuente.render("¿Cuántos jugadores habrán? (2-4)", True, colores["WHITE"])
    screen.blit(mensaje_render, (50, 100))
    pygame.display.flip()

    

while True:
    #lo mismo del otro while 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
    clock.tick(60)

    #vuelve la pantalla en blanco
    screen.fill(colores["WHITE"])


#tablero
#carcel roja
    Carcel_roja = pygame.draw.rect(screen, colores["REED"], (0, 600, 210, 210))


#carcel AZUL
    Carcel_azul = pygame.draw.rect(screen, colores["BLUEE"], (0, 100, 210, 210))


#carcel verde
    Carcel_verde = pygame.draw.rect(screen, colores["GREEEN"], (500, 100, 210, 210))


#carcel amarilla
    Carcel_amarilla = pygame.draw.rect(screen, colores["YEELLOW"], (500, 600, 210, 210))

  #Salidas
    Salida_roja = pygame.draw.rect(screen, colores["REED"], (120, 500, 30, 100))
    Salida_azul = pygame.draw.rect(screen, colores["BLUEE"], (200, 220, 100, 30))
    Salida_amarilla=pygame.draw.rect(screen, colores["YEELLOW"], (400, 660, 100, 30))
    Salida_verde =pygame.draw.rect(screen, colores["GREEEN"], (560, 300, 30, 100))

    #seguros
    Seguro_rojo = pygame.draw.rect(screen, colores["REED"], (200, 660, 100, 30))
    Seguro_azul = pygame.draw.rect(screen, colores["BLUEE"], (120, 300, 30, 100))
    Seguro_verde= pygame.draw.rect(screen, colores["GREEEN"], (400, 220, 100, 30))
    Seguro_amarillo=pygame.draw.rect(screen, colores["YEELLOW"], (560, 500, 30, 100))


    #colores de las llegadas

    pygame.draw.rect(screen, colores["REED"], (300, 570, 100, 240))
    pygame.draw.rect(screen, colores["BLUEE"], (0, 400, 240, 100))
    pygame.draw.rect(screen, colores["YEELLOW"], (470, 400, 240, 100))
    pygame.draw.rect(screen, colores["GREEEN"], (300, 100, 100, 240))



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

#casillas arriba de la carcel amarilla
    for cordenada in range(500, 710, 30):
        pygame.draw.line(screen, colores["BLACK"], [cordenada, 600], [cordenada, 310], 5)

    for cordenada in range(400, 600, 100):
        pygame.draw.line(screen, colores["BLACK"], [470, cordenada], [710, cordenada], 5)




#esquina superior cercana a la carcel
#lineas de x central

    # pygame.draw.line(screen, colores["BLACK"], [210, 310], [240, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [500, 310], [210, 600], 5)
    pygame.draw.line(screen, colores["BLACK"], [210, 310], [500, 600], 5)

#de casillas que tocan la x central
    pygame.draw.line(screen, colores["BLACK"], [240, 570], [240, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [240, 570], [470, 570], 5)
    pygame.draw.line(screen, colores["BLACK"], [470, 570], [470, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [240, 340], [470, 340], 5)





        # dado1 = random.randint(1,6) 
        # dado2 = random.randint(1,6)
        # print("Dado 1:", dado1)
        # print("Dado 2:", dado2)
        


    for cordenada in range(75, 175, 50):
        pygame.draw.circle(screen, colores["RED"], (cordenada, 675), 20)
        pygame.draw.circle(screen, colores["REED"], (cordenada, 675), 15)
        pygame.draw.circle(screen, colores["RED"], (cordenada, 675), 10)

        pygame.draw.circle(screen, colores["RED"], (cordenada, 725), 20)
        pygame.draw.circle(screen, colores["REED"], (cordenada, 725), 15)
        pygame.draw.circle(screen, colores["RED"], (cordenada, 725), 10)

        pygame.draw.circle(screen, colores["BLUE"], (cordenada,175), 20)
        pygame.draw.circle(screen, colores["BLUEE"], (cordenada,175), 15)
        pygame.draw.circle(screen, colores["BLUE"], (cordenada,175), 10)

        pygame.draw.circle(screen, colores["BLUE"], (cordenada,225), 20)
        pygame.draw.circle(screen, colores["BLUEE"], (cordenada,225), 15)
        pygame.draw.circle(screen, colores["BLUE"], (cordenada,225), 10)

    if jugadores1 == 3:

    #  del lista_de_jugadores["jugadores"][3]
    
#fichas verdes 
        for cordenada in range(575, 675, 50):
            pygame.draw.circle(screen, colores["GREEN"], (cordenada,225), 20)
            pygame.draw.circle(screen, colores["GREEEN"], (cordenada,225), 15)
            pygame.draw.circle(screen, colores["GREEN"], (cordenada,225), 10)

            pygame.draw.circle(screen, colores["GREEN"], (cordenada,175), 20)
            pygame.draw.circle(screen, colores["GREEEN"], (cordenada,175), 15)
            pygame.draw.circle(screen, colores["GREEN"], (cordenada,175), 10)


    elif jugadores1 == 4: 

    #  del lista_de_jugadores["jugadores"][2]
    #  del lista_de_jugadores["jugadores"][3]
#fichas amarillas 
        for cordenada in range(575, 675, 50):
            pygame.draw.circle(screen, colores["YELLOW"], (cordenada,725), 20)
            pygame.draw.circle(screen, colores["YEELLOW"], (cordenada,725), 15)
            pygame.draw.circle(screen, colores["YELLOW"], (cordenada,725), 10)

            pygame.draw.circle(screen, colores["YELLOW"], (cordenada,675), 20)
            pygame.draw.circle(screen, colores["YEELLOW"], (cordenada,675), 15)
            pygame.draw.circle(screen, colores["YELLOW"], (cordenada,675), 10)

       
            pygame.draw.circle(screen, colores["GREEN"], (cordenada,225), 20)
            pygame.draw.circle(screen, colores["GREEEN"], (cordenada,225), 15)
            pygame.draw.circle(screen, colores["GREEN"], (cordenada,225), 10)

            pygame.draw.circle(screen, colores["GREEN"], (cordenada,175), 20)
            pygame.draw.circle(screen, colores["GREEEN"], (cordenada,175), 15)
            pygame.draw.circle(screen, colores["GREEN"], (cordenada,175), 10)

    pygame.display.flip()
