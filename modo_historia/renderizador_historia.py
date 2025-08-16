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
        
        # Panel del título
        pygame.draw.rect(self.ventana, (60, 40, 80), (0, 0, self.ancho, 100))
        pygame.draw.rect(self.ventana, self.MORADO, (0, 0, self.ancho, 100), 3)
        
        # Título con sombra
        titulo_surface = self.fuente_grande.render(titulo, True, self.DORADO)
        sombra = self.fuente_grande.render(titulo, True, self.NEGRO)
        self.ventana.blit(sombra, (self.ancho//2 - titulo_surface.get_width()//2 + 3, 33))
        self.ventana.blit(titulo_surface, (self.ancho//2 - titulo_surface.get_width()//2, 30))
        
        # Panel del texto de la historia
        pygame.draw.rect(self.ventana, (40, 30, 60), (50, 120, self.ancho - 100, 300))
        pygame.draw.rect(self.ventana, self.MORADO, (50, 120, self.ancho - 100, 300), 3)
        
        # Texto de la historia
        y = 140
        for linea in texto:
            if linea.strip():  # Solo renderizar líneas no vacías
                texto_surface = self.fuente.render(linea, True, self.BLANCO)
                self.ventana.blit(texto_surface, (70, y))
                y += 40
        
        # Panel de opciones
        pygame.draw.rect(self.ventana, (60, 40, 80), (50, 450, self.ancho - 100, 200))
        pygame.draw.rect(self.ventana, self.MORADO, (50, 450, self.ancho - 100, 200), 3)
        
        # Opciones
        y_opciones = 470
        for i, opcion in enumerate(opciones):
            color = self.AMARILLO if i == decision_seleccionada else self.BLANCO
            color_fondo = (80, 60, 100) if i == decision_seleccionada else (60, 40, 80)
            
            # Marco de la opción seleccionada
            if i == decision_seleccionada:
                pygame.draw.rect(self.ventana, color_fondo, (60, y_opciones - 5, self.ancho - 140, 40))
                pygame.draw.rect(self.ventana, self.AMARILLO, (60, y_opciones - 5, self.ancho - 140, 40), 2)
            
            opcion_surface = self.fuente.render(f"{i+1}. {opcion}", True, color)
            self.ventana.blit(opcion_surface, (70, y_opciones))
            y_opciones += 50
        
        # Panel de instrucciones
        pygame.draw.rect(self.ventana, (40, 30, 60), (50, 680, self.ancho - 100, 60))
        pygame.draw.rect(self.ventana, self.AMARILLO, (50, 680, self.ancho - 100, 60), 3)
        
        # Instrucciones
        instrucciones = self.fuente.render("Usa las flechas para navegar y Enter para seleccionar", True, self.AMARILLO)
        self.ventana.blit(instrucciones, (70, 700))
    
    def dibujar_pantalla_combate_historia(self, jugador, enemigo, mensaje: str = ""):
        """Dibuja la pantalla de combate en modo historia"""
        # Fondo degradado
        for y in range(self.alto):
            color = (
                int(40 + (y / self.alto) * 60),
                int(20 + (y / self.alto) * 40),
                int(20 + (y / self.alto) * 40)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Panel del título
        pygame.draw.rect(self.ventana, (80, 40, 40), (0, 0, self.ancho, 100))
        pygame.draw.rect(self.ventana, self.ROJO, (0, 0, self.ancho, 100), 3)
        
        # Título con sombra
        titulo = self.fuente_grande.render("COMBATE", True, self.AMARILLO)
        sombra = self.fuente_grande.render("COMBATE", True, self.NEGRO)
        self.ventana.blit(sombra, (self.ancho//2 - titulo.get_width()//2 + 3, 33))
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 30))
        
        # Panel del jugador
        pygame.draw.rect(self.ventana, (40, 60, 40), (50, 120, 350, 200))
        pygame.draw.rect(self.ventana, self.VERDE, (50, 120, 350, 200), 3)
        
        # Información del jugador
        if jugador:
            jugador_texto = self.fuente.render(f"Jugador: {jugador.nombre}", True, self.VERDE)
            self.ventana.blit(jugador_texto, (70, 140))
            
            vida_texto = self.fuente.render(f"Vida: {round(jugador.vida_actual)}/{round(jugador.vida_maxima)}", True, self.BLANCO)
            self.ventana.blit(vida_texto, (70, 170))
            
            # Barra de vida del jugador
            pygame.draw.rect(self.ventana, (100, 0, 0), (70, 200, 300, 20))
            vida_porcentaje = jugador.vida_actual / jugador.vida_maxima
            pygame.draw.rect(self.ventana, self.VERDE, (70, 200, 300 * vida_porcentaje, 20))
            pygame.draw.rect(self.ventana, self.BLANCO, (70, 200, 300, 20), 2)
        
        # Panel del enemigo
        pygame.draw.rect(self.ventana, (60, 40, 40), (self.ancho - 400, 120, 350, 200))
        pygame.draw.rect(self.ventana, self.ROJO, (self.ancho - 400, 120, 350, 200), 3)
        
        # Información del enemigo
        if enemigo:
            enemigo_texto = self.fuente.render(f"Enemigo: {enemigo.nombre}", True, self.ROJO)
            self.ventana.blit(enemigo_texto, (self.ancho - 380, 140))
            
            vida_texto = self.fuente.render(f"Vida: {round(enemigo.vida_actual)}/{round(enemigo.vida_maxima)}", True, self.BLANCO)
            self.ventana.blit(vida_texto, (self.ancho - 380, 170))
            
            # Barra de vida del enemigo
            pygame.draw.rect(self.ventana, (100, 0, 0), (self.ancho - 380, 200, 300, 20))
            vida_porcentaje = enemigo.vida_actual / enemigo.vida_maxima
            pygame.draw.rect(self.ventana, self.ROJO, (self.ancho - 380, 200, 300 * vida_porcentaje, 20))
            pygame.draw.rect(self.ventana, self.BLANCO, (self.ancho - 380, 200, 300, 20), 2)
        
        # Panel central de mensaje
        pygame.draw.rect(self.ventana, (60, 60, 60), (self.ancho//2 - 250, 350, 500, 150))
        pygame.draw.rect(self.ventana, self.AMARILLO, (self.ancho//2 - 250, 350, 500, 150), 3)
        
        # Mensaje
        if mensaje:
            mensaje_texto = self.fuente.render(mensaje, True, self.BLANCO)
            self.ventana.blit(mensaje_texto, (self.ancho//2 - mensaje_texto.get_width()//2, 380))
        
        # Panel de instrucciones
        pygame.draw.rect(self.ventana, (40, 40, 60), (50, 530, self.ancho - 100, 60))
        pygame.draw.rect(self.ventana, self.AMARILLO, (50, 530, self.ancho - 100, 60), 3)
        
        # Instrucciones
        instrucciones = self.fuente.render("Presiona cualquier tecla para continuar", True, self.AMARILLO)
        self.ventana.blit(instrucciones, (70, 550))
    
    def dibujar_pantalla_fin_historia(self, resultado: str, decision_final: str):
        """Dibuja la pantalla de fin de historia"""
        # Fondo degradado
        for y in range(self.alto):
            color = (
                int(60 + (y / self.alto) * 40),
                int(40 + (y / self.alto) * 60),
                int(20 + (y / self.alto) * 40)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Panel del título
        pygame.draw.rect(self.ventana, (80, 60, 40), (0, 0, self.ancho, 120))
        pygame.draw.rect(self.ventana, self.DORADO, (0, 0, self.ancho, 120), 3)
        
        # Título con sombra
        titulo = self.fuente_grande.render("FIN DE LA HISTORIA", True, self.DORADO)
        sombra = self.fuente_grande.render("FIN DE LA HISTORIA", True, self.NEGRO)
        self.ventana.blit(sombra, (self.ancho//2 - titulo.get_width()//2 + 3, 33))
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 30))
        
        # Panel central de información
        pygame.draw.rect(self.ventana, (60, 50, 40), (self.ancho//2 - 300, 150, 600, 200))
        pygame.draw.rect(self.ventana, self.DORADO, (self.ancho//2 - 300, 150, 600, 200), 3)
        
        # Resultado
        resultado_texto = self.fuente.render(f"Resultado: {resultado}", True, self.BLANCO)
        self.ventana.blit(resultado_texto, (self.ancho//2 - resultado_texto.get_width()//2, 180))
        
        # Decisión final
        decision_texto = self.fuente.render(f"Decisión: {decision_final}", True, self.BLANCO)
        self.ventana.blit(decision_texto, (self.ancho//2 - decision_texto.get_width()//2, 220))
        
        # Panel de instrucciones
        pygame.draw.rect(self.ventana, (40, 40, 60), (50, 400, self.ancho - 100, 60))
        pygame.draw.rect(self.ventana, self.AMARILLO, (50, 400, self.ancho - 100, 60), 3)
        
        # Instrucciones
        instrucciones = self.fuente.render("Presiona ESC para volver al menú principal", True, self.AMARILLO)
        self.ventana.blit(instrucciones, (70, 420)) 