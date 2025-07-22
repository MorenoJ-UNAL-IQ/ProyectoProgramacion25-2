

from diccionario import colores
from diccionario import reglas
from diccionario import Casillas
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






def turnos(lista_de_jugadores):

  global contador_de_turnos


#turnos(funciona infinitamente pero funcionan  falta ver como hacer que solo se active cada cierto  tiempo 
# o despues de cierta accion si es haci se le puede quitar el while)


#   if dado2 == dado1:
#       print("puedes volver a tirar los dados")

#   elif contador_de_turnos == 10:

#       print("fin del juego")
#       t = False

#   else:

#        primero = lista_de_jugadores.pop(0)   
#        lista_de_jugadores.append(primero)     
        

#   contador_de_turnos = contador_de_turnos + 1
   
fuente_reglas = pygame.font.SysFont("Arial", 16)
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
estado = "menu"

texto_de_bienvenida = fuente.render("¡Bienvenido a nuestro proyecto de parchís!", True, colores["WHITE"])
bienvenida_rect = texto_de_bienvenida.get_rect(topleft=(100, 100))

boton_de_volver = fuente.render("Volver", True, colores["WHITE"])
volver_rect = boton_de_volver.get_rect(topleft=(50, 50))           


boton_de_inicio = fuente.render("Iniciar", True, colores["WHITE"])
inicio_rect = boton_de_inicio.get_rect(topleft=(100, 250))

boton_de_salir = fuente.render("Salir", True, colores["WHITE"])
salir_rect = boton_de_salir.get_rect(topleft=(100, 350))

#boton de reglas
boton_de_reglas = fuente.render("Ver las reglas", True, colores["WHITE"])
reglas_rect = boton_de_reglas.get_rect(topleft=(100, 450))           
screen.blit(boton_de_reglas, reglas_rect)

# texto_de_las_reglas = fuente.render(, True, colores["WHITE"])
# texto_reglas_rect = texto_de_las_reglas.get_rect(topleft=(200, 200))


        
# Inicia el juego y lo pone en bucle
while u:
    screen.fill(colores["BLACK"])

    # Comprueba estados del mouse
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    hover_de_reglas = reglas_rect.collidepoint(mouse_pos)
    hover_inicio = inicio_rect.collidepoint(mouse_pos)
    hover_salir = salir_rect.collidepoint(mouse_pos)
    hover_volver = volver_rect.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Entrada de texto cuando estamos en input_jugadores
        if estado == "input_jugadores":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
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

    # Estado: Menú principal
    if estado == "menu":
        screen.blit(texto_de_bienvenida, bienvenida_rect)
        screen.blit(boton_de_inicio, inicio_rect)
        screen.blit(boton_de_salir, salir_rect)
        screen.blit(boton_de_reglas, reglas_rect)

        if hover_inicio and mouse_click[0]:
            pygame.time.delay(300)
            estado = "input_jugadores"

        if hover_salir and mouse_click[0]:
            pygame.quit()
            sys.exit()

        if hover_de_reglas and mouse_click[0]:
            pygame.time.delay(300)
            estado = "menu_de_reglas"

    # Estado: Ingreso de número de jugadores
    elif estado == "input_jugadores":
        pregunta = fuente.render("¿Cuántos jugadores habrán? (2-4)", True, colores["WHITE"])
        texto_render = fuente.render(texto_ingresado, True, colores["WHITE"])
        screen.blit(pregunta, (50, 100))
        screen.blit(texto_render, (50, 150))
        pygame.display.update()

        if error:
            error_render = fuente.render(error, True, colores["WHITE"])
            screen.blit(error_render, (50, 200))


    elif estado == "menu_de_reglas":
        # screen.blit(texto_de_las_reglas, (250, 250))
        y = 150
        screen.blit(boton_de_volver, volver_rect)
        for numero, texto in reglas.items():


            regla_texto = fuente_reglas.render(f" {texto}", True, colores["WHITE"])
            screen.blit(regla_texto, (50, y))
            y += 25
            

        if hover_volver and mouse_click[0]:
            pygame.time.delay(300)
            estado = "menu"

    pygame.display.flip()

class ficha :
        def __init__ (self, color1, color2, color3, Casilla):
            self.color1 = color1 
            self.color2 = color2
            self.color3 = color3
            self.casilla_actual = Casilla

      
        def dibujar(self, screen, colores):
            x, y = Casillas[str(self.casilla_actual)]
            pygame.draw.circle(screen, colores[self.color1], (x, y), 20)
            pygame.draw.circle(screen, colores[self.color2], (x, y), 15)
            pygame.draw.circle(screen, colores[self.color3], (x, y), 10)

        def mover_por_dado(self, pasos, casillas):
                nueva = str(int(self.casilla_actual) + pasos)
                if nueva in casillas:
                    self.casilla_actual = nueva
                else:
                    print("Movimiento fuera del rango.")

casilla_inicial_roja = "5"
ficha_roja1 = ficha("RED", "REED", "RED", casilla_inicial_roja)

while t:
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

    pygame.draw.rect(screen, colores["BLUEE"], (300, 570, 100, 240))
    pygame.draw.rect(screen, colores["YEELLOW"], (0, 400, 240, 100))
    pygame.draw.rect(screen, colores["GREEN"], (470, 400, 240, 100))
    pygame.draw.rect(screen, colores["REED"], (300, 100, 100, 240))



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

    pygame.draw.line(screen, colores["BLACK"], [500, 310], [210, 600], 5)
    pygame.draw.line(screen, colores["BLACK"], [210, 310], [500, 600], 5)

#de casillas que tocan la x central
    pygame.draw.line(screen, colores["BLACK"], [240, 570], [240, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [240, 570], [470, 570], 5)
    pygame.draw.line(screen, colores["BLACK"], [470, 570], [470, 340], 5)
    pygame.draw.line(screen, colores["BLACK"], [240, 340], [470, 340], 5)




        
    


        #FICHAS ROJAS
        
    

    
    

    # def movimiento():
    #     global dado1
    #     global dado2
    #     dado1 = random.randint(1,6) 
    #     dado2 = random.randint(1,6)

    # dado1 = random.randint(1,6) 
    # dado2 = random.randint(1,6)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            t = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                total = dado1 + dado2
                print("Dado 1:", dado1)
                print("Dado 2:", dado2)

                ficha_roja1.mover_por_dado(total, Casillas)
                pygame.display.update()


    # casilla_incial_roja = casilla_incial_roja + dado2 + dado1

    # def mover_por_dado(self, pasos, casillas):
    #     nueva = str(int(self.casilla_actual) + pasos)
    #     if nueva in casillas:
    #         self.casilla_actual = nueva
    #     else:
    #      print("Movimiento fuera del rango.")

    # mover_por_dado

    # ficha_roja2 = ficha("RED", "REED", "RED", 75, 725)
    # ficha_roja3 = ficha("RED", "REED", "RED", 125, 675)
    # ficha_roja4 = ficha("RED", "REED", "RED", 125, 725)

    # #FICHAS AZULES
    # ficha_azul1 = ficha("BLUE", "BLUEE", "BLUE", 75, 175)
    # ficha_azul2 = ficha("BLUE", "BLUEE", "BLUE", 75, 225)
    # ficha_azul3 = ficha("BLUE", "BLUEE", "BLUE", 125, 225)
    # ficha_azul4 = ficha("BLUE", "BLUEE", "BLUE", 125, 175)


    #FICHAS VERDES 
    # ficha_verde1 = ficha("GREEN", "GREEEN", "GREEN", 575, 225)
    # ficha_verde2 = ficha("GREEN", "GREEEN", "GREEN", 625, 225)
    # ficha_verde3 = ficha("GREEN", "GREEEN", "GREEN", 625, 175)
    # ficha_verde4 = ficha("GREEN", "GREEEN", "GREEN", 575, 175)

    #FICHAS AMARILLAS
    # ficha_amarilla1 = ficha("YELLOW", "YEELLOW", "YELLOW", 575, 725)
    # ficha_amarilla2 = ficha("YELLOW", "YEELLOW", "YELLOW", 625, 725)
    # ficha_amarilla3 = ficha("YELLOW", "YEELLOW", "YELLOW", 575, 675)
    # ficha_amarilla4 = ficha("YELLOW", "YEELLOW", "YELLOW", 625, 675)

    #dibujar fichas rojas y azules(en ese orden)
    ficha_roja1.dibujar(screen, colores)
    # ficha_roja2.dibujar(screen, colores)
    # ficha_roja3.dibujar(screen, colores)
    # ficha_roja4.dibujar(screen, colores)

    # ficha_azul1.dibujar(screen, colores)
    # ficha_azul2.dibujar(screen, colores)
    # ficha_azul3.dibujar(screen, colores)
    # ficha_azul4.dibujar(screen, colores)



    #DIBUJA FICHAS AMARILLAS 




#     if jugadores1 == 3:
#         #DIBUJA FICHAS VERDES
# #  del lista_de_jugadores["jugadores"][3]
#         ficha_verde1.dibujar(screen, colores)
#         ficha_verde2.dibujar(screen, colores)
#         ficha_verde3.dibujar(screen, colores)
#         ficha_verde4.dibujar(screen, colores)
    




    # elif jugadores1 == 4: 
    #     #DIBUJA FICHAS VERDES

    # #  del lista_de_jugadores["jugadores"][2]
    # #  del lista_de_jugadores["jugadores"][3]

    #     ficha_verde1.dibujar(screen, colores)
    #     ficha_verde2.dibujar(screen, colores)
    #     ficha_verde3.dibujar(screen, colores)
    #     ficha_verde4.dibujar(screen, colores)

    #     ficha_amarilla1.dibujar(screen, colores)
    #     ficha_amarilla2.dibujar(screen, colores)
    #     ficha_amarilla3.dibujar(screen, colores)
    #     ficha_amarilla4.dibujar(screen, colores)





    pygame.display.flip()
