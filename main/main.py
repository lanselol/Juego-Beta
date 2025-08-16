import pygame
import random
import sys
import os
import gc
import weakref

# Agregar el directorio raíz al path para que Python pueda encontrar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar las clases organizadas
from clases.personaje import Personaje, ClasePersonaje
from clases.jefe import Jefe
from objetos.objeto import Tienda, Objeto, TipoObjeto
from sistema_combate.maestro_habilidades import MaestroHabilidades
from sistema_combate.generador_enemigos import GeneradorEnemigos
from interfaz.renderizador import Renderizador

# Importar modo historia
from modo_historia.controlador_historia import ControladorHistoria

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO = 1920
ALTO = 1080
ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
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
        
        # Modo historia
        self.controlador_historia = ControladorHistoria(ventana, ANCHO, ALTO)
        self.controlador_historia.conectar_juego_principal(self)
        self.modo_historia_activado = False
        
        # Optimizaciones de memoria
        self._limpiar_memoria()
        
    def _limpiar_memoria(self):
        """Limpia la memoria no utilizada"""
        gc.collect()
        
    def _verificar_enemigo(self):
        """Verifica que el enemigo existe, si no, crea uno nuevo"""
        if not self.enemigo:
            print("DEBUG: ERROR - No hay enemigo! Creando uno nuevo...")
            self.enemigo = self.crear_enemigo()
            return False
        return True
    
    def _limpiar_enemigo_anterior(self):
        """Limpia la memoria del enemigo anterior sin eliminarlo"""
        if self.enemigo:
            # Limpiar objetos del enemigo
            if hasattr(self.enemigo, 'bolsa_objetos'):
                self.enemigo.bolsa_objetos.clear()
            if hasattr(self.enemigo, 'efectos_temporales'):
                self.enemigo.efectos_temporales.clear()
            # NO establecer self.enemigo = None aquí, solo limpiar memoria
            gc.collect()
        
    def dar_recompensa_oro(self):
        # Verificar que el enemigo existe
        if not self.enemigo:
            print("DEBUG: ERROR - No hay enemigo en dar_recompensa_oro!")
            return 0
        
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
        # Crear nuevo enemigo directamente
        enemigo = self.generador_enemigos.crear_enemigo(self.piso_actual)
        
        # Debug: Verificar que el enemigo se creó correctamente
        print(f"DEBUG: Enemigo creado - Nombre: {enemigo.nombre}, Vida: {enemigo.vida_actual}/{enemigo.vida_maxima}, Es Jefe: {enemigo.es_jefe}")
        
        return enemigo
    
    def dibujar_interfaz(self):
        ventana.fill((0, 0, 0))  # NEGRO
        
        if self.estado == "seleccion_clase":
            self.renderizador.dibujar_seleccion_clase()
        elif self.estado == "modo_historia":
            self.controlador_historia.dibujar()
        elif self.estado == "batalla":
            # Verificar que el enemigo existe
            self._verificar_enemigo()
            
            # Debug: Verificar estado del enemigo
            if self.enemigo:
                print(f"DEBUG: Dibujando batalla - Enemigo: {self.enemigo.nombre}, Vida: {self.enemigo.vida_actual}/{self.enemigo.vida_maxima}")
            else:
                print("DEBUG: ERROR - No hay enemigo para dibujar!")
            
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
                # Salir de pantalla completa con F11 o ESC
                if evento.key == pygame.K_F11 or evento.key == pygame.K_ESCAPE:
                    global ANCHO, ALTO
                    if pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
                        pygame.display.set_mode((1200, 800))
                        # Actualizar dimensiones para ventana normal
                        ANCHO, ALTO = 1200, 800
                    else:
                        pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                        # Actualizar dimensiones para pantalla completa
                        ANCHO, ALTO = 1920, 1080
                
                if self.estado == "seleccion_clase":
                    self.manejar_seleccion_clase(evento.key)
                elif self.estado == "modo_historia":
                    resultado = self.controlador_historia.manejar_evento_individual(evento)
                    if resultado is not None:
                        return resultado
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
        elif tecla == pygame.K_h:
            # Activar modo historia
            self.estado = "modo_historia"
            self.controlador_historia.reiniciar()
    
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
            
            # Crear nuevo enemigo
            self.enemigo = self.crear_enemigo()
            
            self.jugador.vida_actual = self.jugador.vida_maxima  # Curar al jugador
            self.jugador.energia_actual = self.jugador.energia   # Recuperar energía
            
            # Limpiar memoria después de cada piso (pero mantener el enemigo)
            gc.collect()
    
    def ejecutar_turno_enemigo(self):
        if not self.enemigo:
            print("DEBUG: ERROR - No hay enemigo en ejecutar_turno_enemigo!")
            self.turno = "jugador"
            return
        
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
            
            # Limpiar memoria al reiniciar
            self._limpiar_memoria()
    
    def actualizar(self):
        if self.estado == "batalla" and self.turno == "enemigo":
            # Verificar que el enemigo existe
            self._verificar_enemigo()
            
            # Pequeño delay para el turno del enemigo
            pygame.time.wait(1000)
            self.ejecutar_turno_enemigo()
        
        # Actualizar estados de los personajes
        if self.jugador:
            self.jugador.actualizar_estado()
        if self.enemigo:
            self.enemigo.actualizar_estado()
        else:
            print("DEBUG: ERROR - No hay enemigo para actualizar!")
    
    def limpiar_recursos(self):
        """Limpia todos los recursos al cerrar el juego"""
        if self.jugador:
            self.jugador.limpiar_objetos()
        if self.enemigo:
            self.enemigo.limpiar_objetos()
        
        # Limpiar cache del renderizador
        self.renderizador.limpiar_cache()
        
        # Limpiar recursos del modo historia
        self.controlador_historia.limpiar_recursos()
        
        # Limpiar memoria
        self._limpiar_memoria()

def main():
    juego = Juego()
    reloj = pygame.time.Clock()
    
    ejecutando = True
    while ejecutando:
        ejecutando = juego.manejar_eventos()
        juego.actualizar()
        juego.dibujar_interfaz()
        reloj.tick(60)
    
    # Limpiar recursos antes de salir
    juego.limpiar_recursos()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
