import pygame
import random
import sys

# Importar las clases organizadas
from clases.personaje import Personaje, ClasePersonaje
from clases.jefe import Jefe
from objetos.objeto import Tienda, Objeto, TipoObjeto
from sistema_combate.maestro_habilidades import MaestroHabilidades
from sistema_combate.generador_enemigos import GeneradorEnemigos
from interfaz.renderizador import Renderizador

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO = 1200
ALTO = 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Fantasy Battle - Juego de Peleas por Turnos")

class Juego:
    def __init__(self):
        self.jugador = None
        self.enemigo = None
        self.estado = "seleccion_clase"
        self.turno = "jugador"
        self.mensaje = ""
        self.habilidad_seleccionada = 0
        self.piso_actual = 1
        self.jefes_derrotados = []
        
        # Sistema de economía y objetos
        self.monedas_oro = 0
        self.tienda = Tienda()
        self.estado_tienda = False
        self.objeto_seleccionado_tienda = 0
        self.objeto_seleccionado_bolsa = 0
        
        # Sistema de maestro de habilidades
        self.maestro_habilidades = MaestroHabilidades()
        self.estado_maestro = False
        self.mejora_seleccionada = 0
        self.jefe_derrotado_reciente = False
        
        # Generador de enemigos
        self.generador_enemigos = GeneradorEnemigos()
        
        # Renderizador
        self.renderizador = Renderizador(ventana, ANCHO, ALTO)
        
    def dar_recompensa_oro(self):
        # Recompensa base por piso
        oro_base = 10 + (self.piso_actual * 2)
        
        # Bonus por jefe
        if self.enemigo.es_jefe:
            oro_base *= 3
        
        self.monedas_oro += oro_base
        return oro_base
    
    def comprar_objeto(self, indice):
        if indice >= len(self.tienda.objetos_disponibles):
            return "Objeto no disponible"
        
        objeto = self.tienda.objetos_disponibles[indice]
        
        if self.monedas_oro >= objeto.precio:
            self.monedas_oro -= objeto.precio
            # Crear una copia del objeto para el jugador
            objeto_copia = Objeto(objeto.tipo, objeto.precio, objeto.descripcion, objeto.efecto)
            self.jugador.agregar_objeto(objeto_copia)
            return f"Compraste {objeto.tipo.value} por {objeto.precio} monedas de oro"
        else:
            return f"No tienes suficientes monedas. Necesitas {objeto.precio} pero tienes {self.monedas_oro}"
    
    def comprar_mejora_habilidad(self, indice):
        if not self.jugador:
            return "No hay jugador"
        
        mejoras = self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, [])
        if indice >= len(mejoras):
            return "Mejora no disponible"
        
        mejora = mejoras[indice]
        
        # Verificar si ya se aplicó esta mejora
        if mejora["nombre"] in self.jugador.mejoras_aplicadas:
            return f"Ya tienes la mejora: {mejora['nombre']}"
        
        if self.monedas_oro >= mejora["precio"]:
            self.monedas_oro -= mejora["precio"]
            resultado = self.jugador.aplicar_mejora_habilidad(mejora)
            return f"{resultado} por {mejora['precio']} monedas de oro"
        else:
            return f"No tienes suficientes monedas. Necesitas {mejora['precio']} pero tienes {self.monedas_oro}"
    
    def crear_enemigo(self):
        return self.generador_enemigos.crear_enemigo(self.piso_actual)
    
    def dibujar_interfaz(self):
        ventana.fill((0, 0, 0))  # NEGRO
        
        if self.estado == "seleccion_clase":
            self.renderizador.dibujar_seleccion_clase()
        elif self.estado == "batalla":
            if self.estado_tienda:
                self.renderizador.dibujar_tienda(self.tienda, self.monedas_oro, self.piso_actual, self.objeto_seleccionado_tienda)
            elif self.estado_maestro:
                self.renderizador.dibujar_maestro_habilidades(self.maestro_habilidades, self.jugador, self.monedas_oro, self.piso_actual, self.mejora_seleccionada)
            else:
                self.renderizador.dibujar_batalla(self.jugador, self.enemigo, self.piso_actual, self.monedas_oro, 
                                                self.mensaje, self.turno, self.habilidad_seleccionada, 
                                                self.objeto_seleccionado_bolsa, self.jefe_derrotado_reciente)
        
        pygame.display.flip()
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.KEYDOWN:
                if self.estado == "seleccion_clase":
                    self.manejar_seleccion_clase(evento.key)
                elif self.estado == "batalla":
                    if self.estado_tienda:
                        self.manejar_tienda(evento.key)
                    elif self.estado_maestro:
                        self.manejar_maestro(evento.key)
                    else:
                        self.manejar_batalla(evento.key)
        
        return True
    
    def manejar_seleccion_clase(self, tecla):
        clases = list(ClasePersonaje)
        if tecla == pygame.K_1 and len(clases) >= 1:
            self.jugador = Personaje("Héroe", clases[0])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_2 and len(clases) >= 2:
            self.jugador = Personaje("Héroe", clases[1])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_3 and len(clases) >= 3:
            self.jugador = Personaje("Héroe", clases[2])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_4 and len(clases) >= 4:
            self.jugador = Personaje("Héroe", clases[3])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_5 and len(clases) >= 5:
            self.jugador = Personaje("Héroe", clases[4])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
    
    def manejar_tienda(self, tecla):
        if tecla == pygame.K_UP:
            self.objeto_seleccionado_tienda = (self.objeto_seleccionado_tienda - 1) % len(self.tienda.objetos_disponibles)
        elif tecla == pygame.K_DOWN:
            self.objeto_seleccionado_tienda = (self.objeto_seleccionado_tienda + 1) % len(self.tienda.objetos_disponibles)
        elif tecla == pygame.K_RETURN:
            self.mensaje = self.comprar_objeto(self.objeto_seleccionado_tienda)
        elif tecla == pygame.K_t:
            self.estado_tienda = False
            self.mensaje = "Tienda cerrada"
    
    def manejar_batalla(self, tecla):
        if self.turno == "jugador":
            if tecla == pygame.K_UP:
                self.habilidad_seleccionada = (self.habilidad_seleccionada - 1) % len(self.jugador.habilidades)
            elif tecla == pygame.K_DOWN:
                self.habilidad_seleccionada = (self.habilidad_seleccionada + 1) % len(self.jugador.habilidades)
            elif tecla == pygame.K_RETURN:
                self.ejecutar_turno_jugador()
            elif tecla == pygame.K_r:
                self.jugador.recuperar_energia()
                self.mensaje = f"{self.jugador.nombre} descansa y recupera energía"
                self.turno = "enemigo"
            elif tecla == pygame.K_t and self.piso_actual % 5 == 0:
                self.estado_tienda = True
                self.mensaje = "Tienda abierta"
            elif tecla == pygame.K_m and self.jefe_derrotado_reciente:
                self.estado_maestro = True
                self.mensaje = "Maestro de Habilidades abierto"
            elif tecla == pygame.K_o and self.jugador.bolsa_objetos:
                self.objeto_seleccionado_bolsa = (self.objeto_seleccionado_bolsa + 1) % len(self.jugador.bolsa_objetos)
            elif tecla == pygame.K_i and self.jugador.bolsa_objetos:
                self.usar_objeto_jugador()
    
    def manejar_maestro(self, tecla):
        if tecla == pygame.K_UP:
            self.mejora_seleccionada = (self.mejora_seleccionada - 1) % len(self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, []))
        elif tecla == pygame.K_DOWN:
            self.mejora_seleccionada = (self.mejora_seleccionada + 1) % len(self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, []))
        elif tecla == pygame.K_RETURN:
            self.mensaje = self.comprar_mejora_habilidad(self.mejora_seleccionada)
        elif tecla == pygame.K_m:
            self.estado_maestro = False
            self.mensaje = "Maestro de Habilidades cerrado"
    
    def usar_objeto_jugador(self):
        if not self.jugador.bolsa_objetos:
            self.mensaje = "No tienes objetos para usar"
            return
        
        objeto = self.jugador.bolsa_objetos[self.objeto_seleccionado_bolsa]
        
        # Determinar objetivo para objetos que lo requieren
        objetivo = None
        if objeto.tipo == TipoObjeto.BOMBA_VENENO:
            objetivo = self.enemigo
        
        self.mensaje = self.jugador.usar_objeto(self.objeto_seleccionado_bolsa, objetivo)
        self.turno = "enemigo"
    
    def ejecutar_turno_jugador(self):
        if self.jugador.estado == "Paralizado":
            self.mensaje = f"{self.jugador.nombre} está paralizado y no puede atacar"
            self.turno = "enemigo"
            return
        
        habilidad = self.jugador.habilidades[self.habilidad_seleccionada]
        self.mensaje = self.jugador.usar_habilidad(habilidad, self.enemigo)
        self.turno = "enemigo"
        
        if self.enemigo.vida_actual <= 0:
            # Dar recompensa de oro
            oro_ganado = self.dar_recompensa_oro()
            
            if self.enemigo.es_jefe:
                self.generador_enemigos.marcar_jefe_derrotado(self.enemigo.nombre)
                self.mensaje = f"¡{self.jugador.nombre} ha derrotado al JEFE {self.enemigo.nombre}! +{oro_ganado} oro"
                self.jefe_derrotado_reciente = True  # Activar maestro de habilidades
            else:
                self.mensaje = f"¡{self.jugador.nombre} ha derrotado a {self.enemigo.nombre}! +{oro_ganado} oro"
            
            # Avanzar al siguiente piso
            self.piso_actual += 1
            self.enemigo = self.crear_enemigo()
            self.jugador.vida_actual = self.jugador.vida_maxima  # Curar al jugador
            self.jugador.energia_actual = self.jugador.energia   # Recuperar energía
    
    def ejecutar_turno_enemigo(self):
        if self.enemigo.estado == "Paralizado":
            self.mensaje = f"{self.enemigo.nombre} está paralizado y no puede atacar"
            self.turno = "jugador"
            return
        
        # IA simple del enemigo
        if self.enemigo.energia_actual < 20:
            self.enemigo.recuperar_energia()
            self.mensaje = f"{self.enemigo.nombre} descansa y recupera energía"
        else:
            # Seleccionar habilidad aleatoria
            habilidad = random.choice(self.enemigo.habilidades)
            self.mensaje = self.enemigo.usar_habilidad(habilidad, self.jugador)
        
        self.turno = "jugador"
        
        if self.jugador.vida_actual <= 0:
            self.mensaje = f"¡{self.enemigo.nombre} ha derrotado a {self.jugador.nombre}!"
            # Reiniciar al piso 1
            self.piso_actual = 1
            self.generador_enemigos.reiniciar_jefes()
            self.monedas_oro = 0  # Perder todo el oro
            self.estado = "seleccion_clase"
    
    def actualizar(self):
        if self.estado == "batalla" and self.turno == "enemigo":
            # Pequeño delay para el turno del enemigo
            pygame.time.wait(1000)
            self.ejecutar_turno_enemigo()
        
        # Actualizar estados de los personajes
        if self.jugador:
            self.jugador.actualizar_estado()
        if self.enemigo:
            self.enemigo.actualizar_estado()

def main():
    juego = Juego()
    reloj = pygame.time.Clock()
    
    ejecutando = True
    while ejecutando:
        ejecutando = juego.manejar_eventos()
        juego.actualizar()
        juego.dibujar_interfaz()
        reloj.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
