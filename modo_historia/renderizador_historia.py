import pygame
from typing import Dict, List

class RenderizadorHistoria:
    def __init__(self, ventana, ancho, alto):
        self.ventana = ventana
        self.ancho = ancho
        self.alto = alto
        
        # Colores mejorados
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)
        self.GRIS = (128, 128, 128)
        self.AMARILLO = (255, 255, 0)
        self.ROJO = (255, 0, 0)
        self.VERDE = (0, 255, 0)
        self.AZUL = (0, 0, 255)
        self.MORADO = (128, 0, 128)
        self.DORADO = (255, 215, 0)
        self.ROSA = (255, 192, 203)
        self.MARRON = (139, 69, 19)
        self.VERDE_OSCURO = (0, 100, 0)
        self.AZUL_OSCURO = (0, 0, 100)
        
        # Fuentes
        self.fuente = pygame.font.Font(None, 32)
        self.fuente_grande = pygame.font.Font(None, 48)
        self.fuente_pequena = pygame.font.Font(None, 24)
    
        # Ajustar tamaños de fuente según la resolución
        self._ajustar_fuentes()
    
    def _ajustar_fuentes(self):
        """Ajusta el tamaño de las fuentes según la resolución de pantalla"""
        if self.ancho >= 1920:  # Pantalla completa
            self.fuente = pygame.font.Font(None, 32)
            self.fuente_grande = pygame.font.Font(None, 48)
            self.fuente_pequena = pygame.font.Font(None, 24)
        elif self.ancho >= 1200:  # Pantalla mediana
            self.fuente = pygame.font.Font(None, 28)
            self.fuente_grande = pygame.font.Font(None, 42)
            self.fuente_pequena = pygame.font.Font(None, 22)
        else:  # Pantalla pequeña
            self.fuente = pygame.font.Font(None, 24)
            self.fuente_grande = pygame.font.Font(None, 36)
            self.fuente_pequena = pygame.font.Font(None, 20)
    
    def _centrar_horizontal(self, elemento_ancho):
        """Centra un elemento horizontalmente en la pantalla"""
        return (self.ancho - elemento_ancho) // 2
    
    def _centrar_vertical(self, elemento_alto, offset_y=0):
        """Centra un elemento verticalmente en la pantalla con offset opcional"""
        return (self.alto - elemento_alto) // 2 + offset_y
    
    def _ajustar_tamano_elemento(self, tamano_base):
        """Ajusta el tamaño de los elementos según la resolución"""
        if self.ancho >= 1920:
            return tamano_base
        elif self.ancho >= 1200:
            return int(tamano_base * 0.8)
        else:
            return int(tamano_base * 0.6)
    
    def limpiar_cache(self):
        """Método vacío para mantener compatibilidad"""
        pass
    
    def dibujar_pantalla_historia(self, narrativa, decision_seleccionada: int = 0):
        """Dibuja la pantalla principal de historia"""
        # Fondo degradado
        for y in range(self.alto):
            color = (
                int(20 + (y / self.alto) * 40),
                int(10 + (y / self.alto) * 30),
                int(40 + (y / self.alto) * 80)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        historia_actual = narrativa.obtener_historia_actual()
        titulo = historia_actual.get("titulo", "Historia")
        texto = historia_actual.get("texto", [])
        opciones = historia_actual.get("opciones", [])
        
        # Panel del título - Centrado
        pygame.draw.rect(self.ventana, (60, 40, 80), (0, 0, self.ancho, 100))
        pygame.draw.rect(self.ventana, self.MORADO, (0, 0, self.ancho, 100), 3)
        
        # Título con sombra - Centrado
        titulo_surface = self.fuente_grande.render(titulo, True, self.DORADO)
        sombra = self.fuente_grande.render(titulo, True, self.NEGRO)
        titulo_x = self._centrar_horizontal(titulo_surface.get_width())
        self.ventana.blit(sombra, (titulo_x + 3, 33))
        self.ventana.blit(titulo_surface, (titulo_x, 30))
        
        # Panel del texto de la historia - Centrado
        texto_ancho = self.ancho - 100
        texto_x = 50
        pygame.draw.rect(self.ventana, (40, 30, 60), (texto_x, 120, texto_ancho, 300))
        pygame.draw.rect(self.ventana, self.MORADO, (texto_x, 120, texto_ancho, 300), 3)
        
        # Texto de la historia - Centrado
        y = 140
        for linea in texto:
            if linea.strip():  # Solo renderizar líneas no vacías
                texto_surface = self.fuente.render(linea, True, self.BLANCO)
                # Centrar cada línea de texto
                linea_x = self._centrar_horizontal(texto_surface.get_width())
                self.ventana.blit(texto_surface, (linea_x, y))
                y += 40
        
        # Panel de opciones - Centrado
        opciones_ancho = self.ancho - 100
        opciones_x = 50
        pygame.draw.rect(self.ventana, (60, 40, 80), (opciones_x, 450, opciones_ancho, 200))
        pygame.draw.rect(self.ventana, self.MORADO, (opciones_x, 450, opciones_ancho, 200), 3)
        
        # Opciones - Centradas
        y_opciones = 470
        for i, opcion in enumerate(opciones):
            color = self.AMARILLO if i == decision_seleccionada else self.BLANCO
            color_fondo = (80, 60, 100) if i == decision_seleccionada else (60, 40, 80)
            
            # Marco de la opción seleccionada
            if i == decision_seleccionada:
                pygame.draw.rect(self.ventana, color_fondo, (opciones_x + 10, y_opciones - 5, opciones_ancho - 20, 40))
                pygame.draw.rect(self.ventana, self.AMARILLO, (opciones_x + 10, y_opciones - 5, opciones_ancho - 20, 40), 2)
            
            opcion_surface = self.fuente.render(f"{i+1}. {opcion}", True, color)
            # Centrar cada opción
            opcion_x = self._centrar_horizontal(opcion_surface.get_width())
            self.ventana.blit(opcion_surface, (opcion_x, y_opciones))
            y_opciones += 50
        
        # Panel de instrucciones - Centrado
        instrucciones_ancho = self.ancho - 100
        instrucciones_x = 50
        pygame.draw.rect(self.ventana, (40, 30, 60), (instrucciones_x, 680, instrucciones_ancho, 60))
        pygame.draw.rect(self.ventana, self.AMARILLO, (instrucciones_x, 680, instrucciones_ancho, 60), 3)
        
        # Instrucciones - Centradas
        instrucciones = self.fuente.render("Usa las flechas para navegar y Enter para seleccionar", True, self.AMARILLO)
        instrucciones_x_centrado = self._centrar_horizontal(instrucciones.get_width())
        self.ventana.blit(instrucciones, (instrucciones_x_centrado, 700))
    
    def dibujar_pantalla_combate_historia(self, jugador, enemigo, mensaje: str = ""):
        """Dibuja la pantalla de combate en modo historia"""
        # Fondo degradado
        for y in range(self.alto):
            color = (
                int(15 + (y / self.alto) * 45),
                int(35 + (y / self.alto) * 70),
                int(15 + (y / self.alto) * 45)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Panel superior de información - Centrado
        pygame.draw.rect(self.ventana, (45, 70, 45), (0, 0, self.ancho, 160))
        pygame.draw.rect(self.ventana, self.VERDE, (0, 0, self.ancho, 160), 4)
        
        # Título del combate - Centrado
        titulo_combate = self.fuente_grande.render("COMBATE EN HISTORIA", True, self.DORADO)
        titulo_x = self._centrar_horizontal(titulo_combate.get_width())
        self.ventana.blit(titulo_combate, (titulo_x, 40))
        
        # Mensaje de combate - Centrado
        if mensaje:
            mensaje_surface = self.fuente.render(mensaje, True, self.BLANCO)
            mensaje_x = self._centrar_horizontal(mensaje_surface.get_width())
            self.ventana.blit(mensaje_surface, (mensaje_x, 80))
        
        # Información del jugador - Centrada
        if jugador:
            jugador_x = 100
            self.dibujar_personaje_historia(jugador, jugador_x, 200, self.VERDE)
        
        # Información del enemigo - Centrada
        if enemigo:
            color_enemigo = self.ROSA if hasattr(enemigo, 'es_jefe') and enemigo.es_jefe else self.ROJO
            enemigo_x = self.ancho - 570
            self.dibujar_personaje_historia(enemigo, enemigo_x, 200, color_enemigo)
        
        # Área de batalla central - Centrada
        area_ancho = self._ajustar_tamano_elemento(700)
        area_x = self._centrar_horizontal(area_ancho)
        pygame.draw.rect(self.ventana, (70, 100, 70), (area_x, 480, area_ancho, 220))
        pygame.draw.rect(self.ventana, self.VERDE, (area_x, 480, area_ancho, 220), 4)
        
        # Instrucciones de combate - Centradas
        instrucciones = self.fuente.render("Combate automático en progreso...", True, self.AMARILLO)
        instrucciones_x = self._centrar_horizontal(instrucciones.get_width())
        self.ventana.blit(instrucciones, (instrucciones_x, 500))
        
        # Botón de continuar - Centrado
        boton_ancho = self._ajustar_tamano_elemento(320)
        boton_x = self._centrar_horizontal(boton_ancho)
        pygame.draw.rect(self.ventana, self.AZUL, (boton_x, 720, boton_ancho, 70))
        pygame.draw.rect(self.ventana, self.BLANCO, (boton_x, 720, boton_ancho, 70), 4)
        
        continuar_texto = self.fuente.render("Continuar (Enter)", True, self.BLANCO)
        continuar_x = self._centrar_horizontal(continuar_texto.get_width())
        self.ventana.blit(continuar_texto, (continuar_x, 745))
    
    def dibujar_personaje_historia(self, personaje, x, y, color):
        """Dibuja la información de un personaje en modo historia"""
        if not personaje:
            return
        
        try:
            # Marco del personaje - Optimizado
            marco_ancho = self._ajustar_tamano_elemento(450)
            marco_alto = self._ajustar_tamano_elemento(240)
            pygame.draw.rect(self.ventana, (40, 60, 40), (x-15, y-15, marco_ancho, marco_alto))
            pygame.draw.rect(self.ventana, color, (x-10, y-10, marco_ancho-10, marco_alto-10), 3)
            
            # Nombre del personaje
            nombre_texto = self.fuente.render(str(personaje.nombre), True, color)
            self.ventana.blit(nombre_texto, (x, y))
            
            # Clase del personaje
            if hasattr(personaje, 'clase') and personaje.clase:
                clase_texto = self.fuente.render(f"Clase: {personaje.clase.value}", True, self.BLANCO)
                self.ventana.blit(clase_texto, (x, y + 35))
            
            # Indicador de jefe
            if hasattr(personaje, 'es_jefe') and personaje.es_jefe:
                jefe_texto = self.fuente_pequena.render("JEFE", True, self.ROSA)
                self.ventana.blit(jefe_texto, (x, y + 60))
            
            # Barra de vida
            if hasattr(personaje, 'vida_actual') and hasattr(personaje, 'vida_maxima'):
                vida_porcentaje = personaje.vida_actual / personaje.vida_maxima
                barra_vida_ancho = self._ajustar_tamano_elemento(300)
                barra_vida_x = x + 20
                barra_vida_y = y + 90
                
                pygame.draw.rect(self.ventana, self.ROJO, (barra_vida_x, barra_vida_y, barra_vida_ancho, 25))
                pygame.draw.rect(self.ventana, self.VERDE, (barra_vida_x, barra_vida_y, int(barra_vida_ancho * vida_porcentaje), 25))
                pygame.draw.rect(self.ventana, self.BLANCO, (barra_vida_x, barra_vida_y, barra_vida_ancho, 25), 2)
                
                vida_texto = self.fuente_pequena.render(f"Vida: {personaje.vida_actual}/{personaje.vida_maxima}", True, self.BLANCO)
                self.ventana.blit(vida_texto, (barra_vida_x, barra_vida_y + 30))
            
            # Barra de energía
            if hasattr(personaje, 'energia_actual') and hasattr(personaje, 'energia'):
                energia_porcentaje = personaje.energia_actual / personaje.energia
                barra_energia_ancho = self._ajustar_tamano_elemento(300)
                barra_energia_x = x + 20
                barra_energia_y = y + 120
                
                pygame.draw.rect(self.ventana, self.GRIS, (barra_energia_x, barra_energia_y, barra_energia_ancho, 20))
                pygame.draw.rect(self.ventana, self.AZUL, (barra_energia_x, barra_energia_y, int(barra_energia_ancho * energia_porcentaje), 20))
                pygame.draw.rect(self.ventana, self.BLANCO, (barra_energia_x, barra_energia_y, barra_energia_ancho, 20), 2)
                
                energia_texto = self.fuente_pequena.render(f"Energía: {personaje.energia_actual}/{personaje.energia}", True, self.BLANCO)
                self.ventana.blit(energia_texto, (barra_energia_x, barra_energia_y + 25))
            
            # Estadísticas del personaje - Distribuidas mejor
            y_stats = y + 160
            stats_ancho = self._ajustar_tamano_elemento(200)
            
            # Columna izquierda
            if hasattr(personaje, 'ataque'):
                ataque_texto = self.fuente_pequena.render(f"Ataque: {personaje.ataque}", True, self.ROJO)
                self.ventana.blit(ataque_texto, (x, y_stats))
            
            if hasattr(personaje, 'defensa'):
                defensa_texto = self.fuente_pequena.render(f"Defensa: {personaje.defensa}", True, self.AZUL)
                self.ventana.blit(defensa_texto, (x, y_stats + 25))
            
            if hasattr(personaje, 'velocidad'):
                velocidad_texto = self.fuente_pequena.render(f"Velocidad: {personaje.velocidad}", True, self.VERDE)
                self.ventana.blit(velocidad_texto, (x, y_stats + 50))
            
            # Columna derecha
            x_derecha = x + stats_ancho + 20
            if hasattr(personaje, 'probabilidad_critico'):
                critico_texto = self.fuente_pequena.render(f"Crítico: {personaje.probabilidad_critico}%", True, self.AMARILLO)
                self.ventana.blit(critico_texto, (x_derecha, y_stats))
            
            if hasattr(personaje, 'probabilidad_esquiva'):
                esquiva_texto = self.fuente_pequena.render(f"Esquiva: {personaje.probabilidad_esquiva}%", True, self.MORADO)
                self.ventana.blit(esquiva_texto, (x_derecha, y_stats + 25))
            
            # Estado del personaje
            if hasattr(personaje, 'estado') and personaje.estado != "Normal":
                estado_texto = self.fuente_pequena.render(f"Estado: {personaje.estado}", True, self.NARANJA)
                self.ventana.blit(estado_texto, (x, y_stats + 75))
                
        except Exception as e:
            # Si hay algún error, dibujar solo información básica
            print(f"Error al dibujar personaje en historia: {e}")
            nombre_texto = self.fuente.render(str(personaje.nombre) if hasattr(personaje, 'nombre') else "Personaje", True, color)
            self.ventana.blit(nombre_texto, (x, y))
    
    def dibujar_pantalla_final(self, resultado_final: str):
        """Dibuja la pantalla final de la historia"""
        # Fondo degradado
        for y in range(self.alto):
            color = (
                int(25 + (y / self.alto) * 35),
                int(15 + (y / self.alto) * 25),
                int(35 + (y / self.alto) * 45)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título final - Centrado
        titulo_final = self.fuente_grande.render("FIN DE LA HISTORIA", True, self.DORADO)
        titulo_x = self._centrar_horizontal(titulo_final.get_width())
        titulo_y = self._centrar_vertical(100, -200)
        self.ventana.blit(titulo_final, (titulo_x, titulo_y))
        
        # Resultado final - Centrado
        resultado_surface = self.fuente.render(resultado_final, True, self.BLANCO)
        resultado_x = self._centrar_horizontal(resultado_surface.get_width())
        resultado_y = titulo_y + 100
        self.ventana.blit(resultado_surface, (resultado_x, resultado_y))
        
        # Instrucciones para continuar - Centradas
        instrucciones = self.fuente.render("Presiona Enter para volver al menú principal", True, self.AMARILLO)
        instrucciones_x = self._centrar_horizontal(instrucciones.get_width())
        instrucciones_y = resultado_y + 100
        self.ventana.blit(instrucciones, (instrucciones_x, instrucciones_y))
        
        # Panel decorativo - Centrado
        panel_ancho = self._ajustar_tamano_elemento(600)
        panel_x = self._centrar_horizontal(panel_ancho)
        panel_y = instrucciones_y + 50
        pygame.draw.rect(self.ventana, (60, 40, 80), (panel_x, panel_y, panel_ancho, 100))
        pygame.draw.rect(self.ventana, self.MORADO, (panel_x, panel_y, panel_ancho, 100), 3)
        
        # Mensaje adicional - Centrado
        mensaje_adicional = self.fuente_pequena.render("¡Gracias por jugar la historia!", True, self.BLANCO)
        mensaje_x = self._centrar_horizontal(mensaje_adicional.get_width())
        self.ventana.blit(mensaje_adicional, (mensaje_x, panel_y + 40)) 