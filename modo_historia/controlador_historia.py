import pygame
from typing import Dict, Optional
from .narrativa import Narrativa, EstadoHistoria
from .renderizador_historia import RenderizadorHistoria
from sistema_guardado.gestor_guardado import GestorGuardado

class ControladorHistoria:
    def __init__(self, ventana, ancho, alto):
        self.ventana = ventana
        self.ancho = ancho
        self.alto = alto
        
        # Componentes del modo historia
        self.narrativa = Narrativa()
        self.renderizador = RenderizadorHistoria(ventana, ancho, alto)
        self.gestor_guardado = GestorGuardado()
        
        # Estado del controlador
        self.estado = "historia"  # historia, final, game_over, guardado
        self.decision_seleccionada = 0
        self.archivo_seleccionado = 0
        self.mensaje = ""
        
        # Integración con el juego principal
        self.juego_principal = None
        self.modo_libre_activado = False
    
    def conectar_juego_principal(self, juego):
        """Conecta el controlador con el juego principal"""
        self.juego_principal = juego
    
    def manejar_evento_individual(self, evento) -> bool:
        """Maneja un evento individual del modo historia"""
        if evento.type == pygame.QUIT:
            return False
        
        if evento.type == pygame.KEYDOWN:
            if self.estado == "historia":
                return self._manejar_eventos_historia(evento.key)
            elif self.estado == "final":
                return self._manejar_eventos_final(evento.key)
            elif self.estado == "game_over":
                return self._manejar_eventos_game_over(evento.key)
            elif self.estado == "guardado":
                return self._manejar_eventos_guardado(evento.key)
        
        return True
    
    def _manejar_eventos_historia(self, tecla) -> bool:
        """Maneja eventos en la pantalla de historia"""
        historia_actual = self.narrativa.obtener_historia_actual()
        opciones = historia_actual.get("opciones", [])
        
        if tecla == pygame.K_UP:
            self.decision_seleccionada = (self.decision_seleccionada - 1) % len(opciones)
        elif tecla == pygame.K_DOWN:
            self.decision_seleccionada = (self.decision_seleccionada + 1) % len(opciones)
        elif tecla == pygame.K_RETURN:
            self._tomar_decision()
        elif tecla == pygame.K_ESCAPE:
            return self._volver_al_menu_principal()
        elif tecla == pygame.K_s:
            self._guardar_partida()
        elif tecla == pygame.K_l:
            self.estado = "guardado"
        
        return True
    
    def _manejar_eventos_final(self, tecla) -> bool:
        """Maneja eventos en la pantalla de final"""
        historia_actual = self.narrativa.obtener_historia_actual()
        opciones = historia_actual.get("opciones", [])
        
        if tecla == pygame.K_UP:
            self.decision_seleccionada = (self.decision_seleccionada - 1) % len(opciones)
        elif tecla == pygame.K_DOWN:
            self.decision_seleccionada = (self.decision_seleccionada + 1) % len(opciones)
        elif tecla == pygame.K_RETURN:
            return self._procesar_opcion_final()
        elif tecla == pygame.K_ESCAPE:
            return self._volver_al_menu_principal()
        
        return True
    
    def _manejar_eventos_game_over(self, tecla) -> bool:
        """Maneja eventos en la pantalla de game over"""
        historia_actual = self.narrativa.obtener_historia_actual()
        opciones = historia_actual.get("opciones", [])
        
        if tecla == pygame.K_UP:
            self.decision_seleccionada = (self.decision_seleccionada - 1) % len(opciones)
        elif tecla == pygame.K_DOWN:
            self.decision_seleccionada = (self.decision_seleccionada + 1) % len(opciones)
        elif tecla == pygame.K_RETURN:
            return self._procesar_opcion_game_over()
        elif tecla == pygame.K_ESCAPE:
            return self._volver_al_menu_principal()
        
        return True
    
    def _manejar_eventos_guardado(self, tecla) -> bool:
        """Maneja eventos en la pantalla de guardado"""
        archivos = self.gestor_guardado.obtener_archivos_guardado()
        
        if not archivos:
            if tecla == pygame.K_ESCAPE:
                self.estado = "historia"
            return True
        
        if tecla == pygame.K_UP:
            self.archivo_seleccionado = (self.archivo_seleccionado - 1) % len(archivos)
        elif tecla == pygame.K_DOWN:
            self.archivo_seleccionado = (self.archivo_seleccionado + 1) % len(archivos)
        elif tecla == pygame.K_RETURN:
            return self._cargar_partida()
        elif tecla == pygame.K_d:
            return self._eliminar_partida()
        elif tecla == pygame.K_ESCAPE:
            self.estado = "historia"
        
        return True
    
    def _tomar_decision(self):
        """Toma la decisión seleccionada y actualiza la narrativa"""
        decision = self.narrativa.tomar_decision(self.decision_seleccionada)
        
        # Mostrar consecuencia de la decisión
        self.mensaje = decision.get("texto", "")
        
        # Verificar si llegamos a un final
        if self.narrativa.estado_actual in [EstadoHistoria.FINAL_BUENO, EstadoHistoria.FINAL_MALO]:
            self.estado = "final"
        elif self.narrativa.estado_actual == EstadoHistoria.GAME_OVER:
            self.estado = "game_over"
        
        # Resetear selección
        self.decision_seleccionada = 0
    
    def _procesar_opcion_final(self) -> bool:
        """Procesa la opción seleccionada en el final"""
        if self.decision_seleccionada == 0:  # Continuar en modo libre
            if self.juego_principal:
                self.modo_libre_activado = True
                return self._activar_modo_libre()
        elif self.decision_seleccionada == 1:  # Reiniciar historia
            self.narrativa.reiniciar_historia()
            self.estado = "historia"
            self.decision_seleccionada = 0
        elif self.decision_seleccionada == 2:  # Salir al menú principal
            return self._volver_al_menu_principal()
        
        return True
    
    def _procesar_opcion_game_over(self) -> bool:
        """Procesa la opción seleccionada en game over"""
        if self.decision_seleccionada == 0:  # Reintentar
            self.narrativa.reiniciar_historia()
            self.estado = "historia"
            self.decision_seleccionada = 0
        elif self.decision_seleccionada == 1:  # Volver al menú principal
            return self._volver_al_menu_principal()
        elif self.decision_seleccionada == 2:  # Salir del juego
            return False
        
        return True
    
    def _guardar_partida(self):
        """Guarda la partida actual"""
        if self.juego_principal:
            datos_partida = self.gestor_guardado.crear_datos_partida(self.juego_principal)
            nombre_partida = f"Historia_{self.narrativa.estado_actual.value}"
            
            if self.gestor_guardado.guardar_partida(datos_partida, nombre_partida):
                self.mensaje = "Partida guardada exitosamente"
            else:
                self.mensaje = "Error al guardar la partida"
    
    def _cargar_partida(self) -> bool:
        """Carga una partida guardada"""
        archivos = self.gestor_guardado.obtener_archivos_guardado()
        
        if not archivos or self.archivo_seleccionado >= len(archivos):
            return True
        
        archivo = archivos[self.archivo_seleccionado]
        datos_partida = self.gestor_guardado.cargar_partida(archivo["nombre_archivo"])
        
        if datos_partida and self.juego_principal:
            if self.gestor_guardado.aplicar_datos_partida(self.juego_principal, datos_partida):
                self.mensaje = f"Partida cargada: {archivo['nombre_partida']}"
                self.estado = "historia"
                return True
            else:
                self.mensaje = "Error al cargar la partida"
        
        return True
    
    def _eliminar_partida(self) -> bool:
        """Elimina una partida guardada"""
        archivos = self.gestor_guardado.obtener_archivos_guardado()
        
        if not archivos or self.archivo_seleccionado >= len(archivos):
            return True
        
        archivo = archivos[self.archivo_seleccionado]
        
        if self.gestor_guardado.eliminar_partida(archivo["nombre_archivo"]):
            self.mensaje = f"Partida eliminada: {archivo['nombre_partida']}"
            self.archivo_seleccionado = 0
        else:
            self.mensaje = "Error al eliminar la partida"
        
        return True
    
    def _activar_modo_libre(self) -> bool:
        """Activa el modo libre después del final"""
        if self.juego_principal:
            # Crear jugador si no existe (modo libre desde historia)
            if not self.juego_principal.jugador:
                from clases.personaje import Personaje, ClasePersonaje
                self.juego_principal.jugador = Personaje("Héroe", ClasePersonaje.GUERRERO)
            
            # Configurar el juego para modo libre
            self.juego_principal.estado = "batalla"
            self.juego_principal.modo_historia_activado = True
            
            # Crear enemigo si no existe
            if not self.juego_principal.enemigo:
                self.juego_principal.enemigo = self.juego_principal.crear_enemigo()
            
            return True
        
        return False
    
    def _volver_al_menu_principal(self) -> bool:
        """Vuelve al menú principal"""
        if self.juego_principal:
            self.juego_principal.estado = "seleccion_clase"
            return True
        
        return False
    
    def dibujar(self):
        """Dibuja la pantalla actual del modo historia"""
        if self.estado == "historia":
            self.renderizador.dibujar_pantalla_historia(self.narrativa, self.decision_seleccionada)
        elif self.estado == "final":
            # Usar pantalla de fin de historia en lugar de pantalla final
            resultado = "Final completado"
            decision_final = "Historia terminada"
            self.renderizador.dibujar_pantalla_fin_historia(resultado, decision_final)
        elif self.estado == "game_over":
            # Usar pantalla de fin de historia para game over
            resultado = "Game Over"
            decision_final = "Has perdido"
            self.renderizador.dibujar_pantalla_fin_historia(resultado, decision_final)
        elif self.estado == "guardado":
            # Usar pantalla de fin de historia para guardado
            resultado = "Gestión de Guardado"
            decision_final = "Archivos de partida"
            self.renderizador.dibujar_pantalla_fin_historia(resultado, decision_final)
        
        # Dibujar mensaje si existe
        if self.mensaje:
            self._dibujar_mensaje()
    
    def _dibujar_mensaje(self):
        """Dibuja un mensaje temporal en la pantalla"""
        if not self.mensaje:
            return
        
        # Crear superficie para el mensaje
        fuente = pygame.font.Font(None, 28)
        mensaje_surface = fuente.render(self.mensaje, True, (255, 255, 0))
        mensaje_rect = mensaje_surface.get_rect(center=(self.ancho // 2, self.alto - 100))
        
        # Solo dibujar el texto, sin fondos ni bordes
        self.ventana.blit(mensaje_surface, mensaje_rect)
    
    def reiniciar(self):
        """Reinicia el controlador de historia"""
        self.narrativa.reiniciar_historia()
        self.estado = "historia"
        self.decision_seleccionada = 0
        self.archivo_seleccionado = 0
        self.mensaje = ""
        self.modo_libre_activado = False
    
    def limpiar_recursos(self):
        """Limpia los recursos del controlador"""
        self.renderizador.limpiar_cache() 