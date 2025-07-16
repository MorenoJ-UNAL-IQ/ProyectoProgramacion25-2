import pygame
import random
import math

# ------------------ CONFIGURACIÓN ------------------ #
pygame.init()
ANCHO, ALTO = 1000, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Parqués Visual")
reloj = pygame.time.Clock()

# Colores
COLORES = {'rojo': (220, 20, 60),'verde': (34, 139, 34),'amarillo': (255, 215, 0),'azul': (30, 144, 255),'gris': (200, 200, 200),'blanco': (255, 255, 255),'negro': (0, 0, 0)}

# Casillas
TOTAL_CASILLAS = 68
SEGUROS = [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63]
SALIDA = {'rojo': 5, 'verde': 22, 'amarillo': 39, 'azul': 56}
LLEGADA = {'rojo': list(range(100, 106)),'verde': list(range(110, 116)),'amarillo': list(range(120, 126)),'azul': list(range(130, 136))}
ENTRADA_LLEGADA = {'rojo': 67,'verde': 17,'amarillo': 34,'azul': 51}

# Casillas gráficas en círculo
def generar_tablero():
    centro_x, centro_y = ANCHO // 2, ALTO // 2
    radio = 250
    posiciones = {}
    for i in range(TOTAL_CASILLAS):
        ang = (i / TOTAL_CASILLAS) * 2 * math.pi
        x = int(centro_x + radio * math.cos(ang))
        y = int(centro_y + radio * math.sin(ang))
        posiciones[i] = (x, y)
    return posiciones

casillas_graf = generar_tablero()

def agregar_zonas_llegada():
    zonas = {
        'rojo': (ANCHO // 2 + 60, ALTO // 2 - 150),
        'verde': (ANCHO // 2 + 150, ALTO // 2 - 60),
        'amarillo': (ANCHO // 2 - 60, ALTO // 2 + 150),
        'azul': (ANCHO // 2 - 150, ALTO // 2 + 60)
    }
    for color, (x, y) in zonas.items():
        for i, casilla in enumerate(LLEGADA[color]):
            dx = 0
            dy = i * 30
            casillas_graf[casilla] = (x, y + dy)

agregar_zonas_llegada()
# ------------------ CLASES ------------------ #
class Ficha:
    def __init__(self, color):
        self.color = color
        self.posicion = -1
        self.en_llegada = False

    def esta_en_juego(self):
        return self.posicion != -1 and self.posicion != 'fin'

    def dibujar(self):
        if isinstance(self.posicion, int) and self.posicion in casillas_graf:
            x, y = casillas_graf[self.posicion]
            pygame.draw.circle(pantalla, COLORES[self.color], (x, y), 15)
            
    def mover(self, pasos, tablero):
        if self.posicion == -1:
            print(f"{self.color} sigue en la cárcel.")
            return False, False

        if self.en_llegada:
            llegada = LLEGADA[self.color]
            if self.posicion in llegada:
                index = llegada.index(self.posicion)
                if index + pasos < len(llegada):
                    self.posicion = llegada[index + pasos]
                elif index + pasos == len(llegada):
                    self.posicion = 'fin'
                    print(f"{self.color} llegó al final.")
                else:
                    print("Número exacto requerido para llegar al final.")
                    return False, False
            return True, False

        nueva_pos = self.posicion + pasos
        entrada = ENTRADA_LLEGADA[self.color]

        if self.posicion <= entrada < nueva_pos:
            exceso = nueva_pos - entrada
            if exceso < len(LLEGADA[self.color]):
                self.posicion = LLEGADA[self.color][exceso]
                self.en_llegada = True
                return True, False
            elif exceso == len(LLEGADA[self.color]):
                self.posicion = 'fin'
                print(f"{self.color} llegó al final.")
                return True, False
            else:
                print("Movimiento demasiado largo para zona de llegada.")
                return False, False

        if nueva_pos >= TOTAL_CASILLAS:
            nueva_pos %= TOTAL_CASILLAS

        if tablero.hay_barrera_entre(self.posicion, nueva_pos):
            print("Movimiento bloqueado por barrera.")
            return False, False

        self.posicion = nueva_pos
        capturada = tablero.verificar_captura(self)
        return True, capturada


class Jugador:
    def __init__(self, color):
        self.color = color
        self.fichas = [Ficha(color) for _ in range(2)]  # Puedes aumentar a 4

    def lanzar_dado(self):
        return random.randint(1, 6)

    def sacar_ficha(self):
        for ficha in self.fichas:
            if ficha.posicion == -1:
                ficha.posicion = SALIDA[self.color]
                print("{self.color} saca ficha a casilla {SALIDA[self.color]}")
                return True
        return False

class Tablero:
    def __init__(self):
        self.casillas = {}

    def actualizar(self, jugadores):
        self.casillas.clear()
        for j in jugadores:
            for ficha in j.fichas:
                if isinstance(ficha.posicion, int):
                    self.casillas.setdefault(ficha.posicion, []).append(ficha)

    def hay_barrera(self, pos):
        fichas = self.casillas.get(pos, [])
        return len(fichas) >= 2 and all(f.color == fichas[0].color for f in fichas)

    def hay_barrera_entre(self, inicio, destino):
        if destino < inicio:
            destino += TOTAL_CASILLAS
        for i in range(inicio + 1, destino + 1):
            if self.hay_barrera(i % TOTAL_CASILLAS):
                return True
        return False

    def verificar_captura(self, ficha):
        pos = ficha.posicion
        if pos in SEGUROS:
            return False
        fichas = self.casillas.get(pos, [])
        for f in fichas:
            if f != ficha and f.color != ficha.color:
                f.posicion = -1
                print(f"¡{ficha.color} capturó a {f.color}!")
                return True
        return False

# ------------------ JUEGO ------------------ #
jugadores = [Jugador('rojo'), Jugador('verde')]
turno = 0
tablero = Tablero()

# ------------------ BUCLE PRINCIPAL ------------------ #
corriendo = True
while corriendo:
    pantalla.fill(COLORES['blanco'])

    # Dibujar casillas
    for pos, (x, y) in casillas_graf.items():
        color = COLORES['gris'] if pos not in SEGUROS else COLORES['negro']
        pygame.draw.circle(pantalla, color, (x, y), 20, 2)

    # Dibujar fichas
    tablero.actualizar(jugadores)
    for jugador in jugadores:
        for ficha in jugador.fichas:
            ficha.dibujar()

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador = jugadores[turno]
                dado = jugador.lanzar_dado()
                print(f"{jugador.color.upper()} lanzó: {dado}")

                if dado == 5:
                    if not jugador.sacar_ficha():
                        ficha = jugador.fichas[0]
                        ok, capturo = ficha.mover(dado, tablero)
                        if capturo:
                            ficha.mover(20, tablero)
                else:
                    ficha = jugador.fichas[0]
                    ok, capturo = ficha.mover(dado, tablero)
                    if capturo:
                        ficha.mover(20, tablero)

                turno = (turno + 1) % len(jugadores)

    reloj.tick(30)

pygame.quit()