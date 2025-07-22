

from diccionario import colores
from diccionario import reglas
from diccionario import Casillas
from diccionario import Carceles
from diccionario import llegadasamarillas
from diccionario import llegadasazules
from diccionario import llegadasverdes
from diccionario import llegadaroja
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


fuente_reglas = pygame.font.SysFont("Arial", 16)
fuente = pygame.font.SysFont("Arial", 40)

# #tamaño de la ventana

Ventana=(1000,800)

#nombre de la ventana

pygame.display.set_caption("Parches proyecto final")


#crear la ventana
screen = pygame.display.set_mode(Ventana)

#variables para el bucle
puntos = {
    "RED": 0,
    "BLUE": 0,
    "GREEN": 0,
    "YELLOW": 0
}
jugadores1 = None 
lista_de_jugadores = [1, 2 , 3 , 4]
# Diccionario de salidas por color
inicio = 5
fin = 68
texto_ingresado = ""
error = ""
u = True
t = True
estado = "menu"
contador_de_turnos = 0
texto_de_dado1 = None
texto_de_dado2 = None
dado1_rect = None
dado2_rect = None
llrojo = "llegada_roja1"
llazul = "llegada azul1"
llverde = "llegada verde1"
llamarillo = "llegada amarilla1"
dado1 = 0
dado2 = 0
dado_usado = 0  # 0 = ninguno, 1 = dado1 usado, 2 = dado2 usado
ficha_seleccionada = None




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
    #comporbar un click o un pocisionamiento
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


#crea las fichas

class ficha :
        def __init__ (self, color1, color2, color3, pocision):
            self.color1 = color1 
            self.color2 = color2
            self.color3 = color3
            self.pocision_actual = pocision
            self.completada = False 

      
        def dibujar(self, screen, colores):
            if self.completada:
                return
            
            pos_str = str(self.pocision_actual)

            if pos_str in Casillas:
                x, y = Casillas[pos_str]
            elif pos_str in Carceles:
                x, y = Carceles[pos_str]
            elif pos_str in llegadaroja:
                x, y = llegadaroja[pos_str]
            elif pos_str in llegadasamarillas:
                x, y = llegadasamarillas[pos_str]
            elif pos_str in llegadasverdes:
                x, y = llegadasverdes[pos_str]
            elif pos_str in llegadasazules:
                x, y = llegadasazules[pos_str]
            else:
                print(f"Posición inválida: {self.pocision_actual}")
                

            pygame.draw.circle(screen, colores[self.color1], (x, y), 20)
            pygame.draw.circle(screen, colores[self.color2], (x, y), 15)
            pygame.draw.circle(screen, colores[self.color3], (x, y), 10)



        
        def mover_por_dado(self, pasos, pocision):
            # Movimiento dentro del camino de llegada
            if str(self.pocision_actual).startswith("llegada"):
                try:
                    partes = str(self.pocision_actual).split("_")
                    color = partes[1]
                    numero = int(partes[2])
                    nuevo_numero = numero + pasos
                    clave = f"llegada_{color}{nuevo_numero}"

                    diccionario_llegada = {
                        "roja": llegadaroja,
                        "amarilla": llegadasamarillas,
                        "verde": llegadasverdes,
                        "azul": llegadasazules
                    }

                    if clave in diccionario_llegada[color]:
                        self.pocision_actual = clave
                    else:
                        print(f"No puedes avanzar más allá de la llegada final ({clave})")
                    return
                except Exception as e:
                    print(f"Error moviendo dentro de la llegada: {e}")
                    return
            if self.pocision_actual in Carceles:
                if pasos == 5:
                    self.pocision_actual = str(inicio)
                    print("¡La ficha salió de la cárcel!")
                else:
                    print("No puedes salir de la cárcel aún.")
                return

            try:
                actual = int(self.pocision_actual)
                nueva = actual + pasos

                # Si debe entrar al camino de llegada
                if nueva > fin:
                    contador = nueva - fin  # pasos sobrantes
                    if self.color1 == "RED":
                        clave = f"llegada_roja{contador}"
                        if clave in llegadaroja:
                            self.pocision_actual = clave
                            print(f"Ficha roja entró a {clave}")
                            if contador >= 8:
                                puntos["RED"] += 1
                                self.completada = True
                                print("¡Punto para ROJO!")
                            return
                    elif self.color1 == "BLUE":
                        clave = f"llegada azul{contador}"
                        if clave in llegadasazules:
                            self.pocision_actual = clave
                            print(f"Ficha azul entró a {clave}")
                            if contador >= 8:
                                puntos["BLUE"] += 1
                                self.completada = True
                                print("¡Punto para AZUL!")
                            return
                    elif self.color1 == "GREEN":
                        clave = f"llegada verde{contador}"
                        if clave in llegadasverdes:
                            self.pocision_actual = clave
                            print(f"Ficha verde entró a {clave}")
                            if contador >= 8:
                                puntos["GREEN"] += 1
                                self.completada = True
                                print("¡Punto para VERDE!")
                            return
                    elif self.color1 == "YELLOW":
                        clave = f"llegada amarilla{contador}"
                        if clave in llegadasamarillas:
                            self.pocision_actual = clave
                            print(f"Ficha amarilla entró a {clave}")
                            if contador >= 8:
                                puntos["YELLOW"] += 1
                                self.completada = True
                                print("¡Punto para AMARILLO!")
                            return

                # Movimiento normal
                while nueva > 68:
                    nueva -= 68

                nueva_str = str(nueva)
                if nueva_str in pocision:
                    self.pocision_actual = nueva_str
                else:
                    print("Movimiento fuera del rango.")
            except ValueError:
                print(f"No se puede mover desde posición: {self.pocision_actual}")
        
def ficha_clickeada(fichas, mouse_pos, colores):
    for ficha in fichas:
        if ficha.completada:
            continue
        pos_str = str(ficha.pocision_actual)
        if pos_str in Casillas:
            x, y = Casillas[pos_str]
        elif pos_str in Carceles:
            x, y = Carceles[pos_str]
        elif pos_str in llegadaroja:
            x, y = llegadaroja[pos_str]
        elif pos_str in llegadasamarillas:
            x, y = llegadasamarillas[pos_str]
        elif pos_str in llegadasverdes:
            x, y = llegadasverdes[pos_str]
        elif pos_str in llegadasazules:
            x, y = llegadasazules[pos_str]
        else:
            continue

        distancia = ((mouse_pos[0] - x)**2 + (mouse_pos[1] - y)**2)**0.5
        if distancia <= 20:  # radio de la ficha
            return ficha
    return None

#fichas rojas
ficha_roja1 = ficha("RED", "REED", "RED", "rcarcel1")
ficha_roja2 = ficha("RED", "REED", "RED", "rcarcel2")
ficha_roja3 = ficha("RED", "REED", "RED", "rcarcel3")
ficha_roja4 = ficha("RED", "REED", "RED", "rcarcel4")

#fichas azules
ficha_azul1 = ficha("BLUE", "BLUEE", "BLUE", "acarcel1")
ficha_azul2 = ficha("BLUE", "BLUEE", "BLUE", "acarcel2")
ficha_azul3 = ficha("BLUE", "BLUEE", "BLUE", "acarcel3")
ficha_azul4 = ficha("BLUE", "BLUEE", "BLUE", "acarcel4")

#fichas verde
ficha_verde1 = ficha("GREEN", "GREEEN", "GREEN", "vcarcel1")
ficha_verde2 = ficha("GREEN", "GREEEN", "GREEN", "vcarcel2")
ficha_verde3 = ficha("GREEN", "GREEEN", "GREEN", "vcarcel3")
ficha_verde4 = ficha("GREEN", "GREEEN", "GREEN", "vcarcel4")

#fichass amarillas
ficha_amarilla1 = ficha("YELLOW", "YEELLOW", "YELLOW", "amcarcel1")
ficha_amarilla2 = ficha("YELLOW", "YEELLOW", "YELLOW", "amcarcel2")
ficha_amarilla3 = ficha("YELLOW", "YEELLOW", "YELLOW", "amcarcel3")
ficha_amarilla4 = ficha("YELLOW", "YEELLOW", "YELLOW", "amcarcel4")

fichas_rojas = [ficha_roja1, ficha_roja2, ficha_roja3, ficha_roja4]
fichas_azules = [ficha_azul1, ficha_azul2, ficha_azul3, ficha_azul4]
fichas_verdes = [ficha_verde1, ficha_verde2, ficha_verde3, ficha_verde4]
fichas_amarillas = [ficha_amarilla1, ficha_amarilla2, ficha_amarilla3, ficha_amarilla4]


while t:
    #lo mismo del otro while 
    for evento in pygame.event.get():
#vuelve la pantalla en blanco
        screen.fill(colores["WHITE"])
        clock.tick(60)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_pos = pygame.mouse.get_pos()

        # Determina el grupo de fichas según el turno
        if lista_de_jugadores[0] == 1:
            fichas_turno = fichas_rojas
        elif lista_de_jugadores[0] == 2:
            fichas_turno = fichas_azules
        elif lista_de_jugadores[0] == 3:
            fichas_turno = fichas_verdes
        elif lista_de_jugadores[0] == 4:
            fichas_turno = fichas_amarillas
        pocision = Casillas

        ficha_seleccionada = ficha_clickeada(fichas_turno, mouse_pos, colores)

        if ficha_seleccionada:
            if dado_usado == 0:
                ficha_seleccionada.mover_por_dado(dado1, pocision)
                dado_usado = 1
            elif dado_usado == 1:
                ficha_seleccionada.mover_por_dado(dado2, pocision)
                dado_usado = 2
            else:
                print("Ya se usaron ambos dados. Presiona ESPACIO para el siguiente turno.")

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            

        if evento.type == pygame.QUIT:
            u = False

        if evento.type == pygame.KEYDOWN:
            dado_usado = 0
            ficha_seleccionada = None
            if evento.key == pygame.K_SPACE:
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                total = dado1 + dado2
                print("Dado 1:", dado1)
                print("Dado 2:", dado2)

                

                texto_de_dado1 = fuente.render(f"Dado 1: {dado1}", True, colores["BLACK"])
                texto_de_dado2 = fuente.render(f"Dado 2: {dado2}", True, colores["BLACK"])
                dado1_rect = texto_de_dado1.get_rect(topleft=(750, 100))
                dado2_rect = texto_de_dado2.get_rect(topleft=(750, 150))
                if dado2 == dado1:
                    print("puedes volver a tirar los dados")

                elif contador_de_turnos == 500:

                    print("fin del juego")
                    t = False

                else:

                    primero = lista_de_jugadores.pop(0)   
                    lista_de_jugadores.append(primero)

                    if lista_de_jugadores[0] == 1:
                        fin = 68
                        inicio = 5
              
                        # Verificar si alguien ganó
                        for color, score in puntos.items():
                            if score == 4:
                                screen.blit(texto_ganador, (300, 300))
                                pygame.display.update()
                                pygame.time.wait(5000)
                                print(f"¡{color} ha ganado el juego!")
                                t = False  # Detiene el bucle principal
                                break

                    if lista_de_jugadores[0] == 2:
                        fin = 51
                        inicio = 56
                 

                        for color, score in puntos.items():
                            if score == 4:
                                texto_ganador = fuente.render(f"¡{color} ha ganado el juego!", True, colores["BLACK"])
                                screen.blit(texto_ganador, (300, 300))
                                pygame.display.update()
                                pygame.time.wait(5000)
                                print(f"¡{color} ha ganado el juego!")
                                t = False  # Detiene el bucle principal
                                break

                    if lista_de_jugadores[0] == 3:
                        fin = 34
                        inicio = 39
                        

                        for color, score in puntos.items():
                            if score == 4:
                                screen.blit(texto_ganador, (300, 300))
                                pygame.display.update()
                                pygame.time.wait(5000)
                                print(f"¡{color} ha ganado el juego!")
                                t = False  # Detiene el bucle principal
                                break

                    if lista_de_jugadores[0] == 4:
                        fin = 17
                    
                        for color, score in puntos.items():
                            if score == 4:
                                screen.blit(texto_ganador, (300, 300))
                                pygame.display.update()
                                pygame.time.wait(5000)
                                print(f"¡{color} ha ganado el juego!")
                                t = False  # Detiene el bucle principal
                                break

                

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

        pygame.draw.rect(screen, colores["YEELLOW"], (300, 570, 100, 240))
        pygame.draw.rect(screen, colores["REED"], (0, 400, 240, 100))
        pygame.draw.rect(screen, colores["GREEEN"], (470, 400, 240, 100))
        pygame.draw.rect(screen, colores["BLUEE"], (300, 100, 100, 240))



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


        # Dibuja los textos de los dados si existen
        if texto_de_dado1 and dado1_rect:
            screen.blit(texto_de_dado1, dado1_rect)

        if texto_de_dado2 and dado2_rect:
            screen.blit(texto_de_dado2, dado2_rect)

        pygame.display.flip()



        # casilla_incial_roja = casilla_incial_roja + dado2 + dado1

        # def mover_por_dado(self, pasos, casillas):
        #     nueva = str(int(self.casilla_actual) + pasos)
        #     if nueva in casillas:
        #         self.casilla_actual = nueva
        #     else:
        #      print("Movimiento fuera del rango.")

        if jugadores1 >= 3:
            #DIBUJA FICHAS VERDES
            ficha_verde1.dibujar(screen, colores)
            ficha_verde2.dibujar(screen, colores)
            ficha_verde3.dibujar(screen, colores)
            ficha_verde4.dibujar(screen, colores)


        if jugadores1 == 4: 

            ficha_amarilla1.dibujar(screen, colores)
            ficha_amarilla2.dibujar(screen, colores)
            ficha_amarilla3.dibujar(screen, colores)
            ficha_amarilla4.dibujar(screen, colores)

        ficha_roja1.dibujar(screen, colores)
        ficha_roja2.dibujar(screen, colores)
        ficha_roja3.dibujar(screen, colores)
        ficha_roja4.dibujar(screen, colores)

        ficha_azul1.dibujar(screen, colores)
        ficha_azul2.dibujar(screen, colores)
        ficha_azul3.dibujar(screen, colores)
        ficha_azul4.dibujar(screen, colores)


        pygame.display.flip()
