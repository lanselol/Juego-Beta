#!/usr/bin/env python3
"""
Archivo de prueba para verificar el sistema de centrado responsivo
"""

import pygame
import sys
import os

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from interfaz.renderizador import Renderizador

def test_centrado():
    """Prueba el sistema de centrado con diferentes resoluciones"""
    
    # Inicializar pygame
    pygame.init()
    
    # Probar diferentes resoluciones
    resoluciones = [
        (1920, 1080),  # Pantalla completa
        (1200, 800),   # Pantalla mediana
        (800, 600)     # Pantalla pequeña
    ]
    
    for ancho, alto in resoluciones:
        print(f"\nProbando resolución: {ancho}x{alto}")
        
        # Crear ventana de prueba
        ventana = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption(f"Test Centrado - {ancho}x{alto}")
        
        # Crear renderizador
        renderizador = Renderizador(ventana, ancho, alto)
        
        # Verificar métodos de centrado
        elemento_ancho = 500
        elemento_alto = 300
        
        centrado_x = renderizador._centrar_horizontal(elemento_ancho)
        centrado_y = renderizador._centrar_vertical(elemento_alto)
        
        print(f"  Elemento de 500x300 centrado en: ({centrado_x}, {centrado_y})")
        print(f"  Posición esperada: ({(ancho - 500) // 2}, {(alto - 300) // 2})")
        
        # Verificar ajuste de tamaños
        tamano_base = 100
        tamano_ajustado = renderizador._ajustar_tamano_elemento(tamano_base)
        print(f"  Tamaño base 100 ajustado a: {tamano_ajustado}")
        
        # Dibujar pantalla de selección de clase
        renderizador.dibujar_seleccion_clase()
        pygame.display.flip()
        
        # Esperar un momento para ver la pantalla
        pygame.time.wait(2000)
        
        # Cerrar ventana
        pygame.display.quit()
    
    pygame.quit()
    print("\nPrueba completada!")

if __name__ == "__main__":
    test_centrado()
