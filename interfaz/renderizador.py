import pygame
from clases.personaje import ClasePersonaje

# Colores mejorados
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
MORADO = (128, 0, 128)
NARANJA = (255, 165, 0)
DORADO = (255, 215, 0)
ROSA = (255, 192, 203)
VERDE_OSCURO = (0, 100, 0)
AZUL_OSCURO = (0, 0, 100)
ROJO_OSCURO = (100, 0, 0)
MARRON = (139, 69, 19)

class Renderizador:
    def __init__(self, ventana, ancho, alto):
        self.ventana = ventana
        self.ancho = ancho
        self.alto = alto
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 48)
        self.fuente_pequena = pygame.font.Font(None, 24)
        
        # Ajustar tamaños de fuente según la resolución
        self._ajustar_fuentes()
    
    def _ajustar_fuentes(self):
        """Ajusta el tamaño de las fuentes según la resolución de pantalla"""
        if self.ancho >= 1920:  # Pantalla completa
            self.fuente = pygame.font.Font(None, 36)
            self.fuente_grande = pygame.font.Font(None, 48)
            self.fuente_pequena = pygame.font.Font(None, 24)
        elif self.ancho >= 1200:  # Pantalla mediana
            self.fuente = pygame.font.Font(None, 32)
            self.fuente_grande = pygame.font.Font(None, 42)
            self.fuente_pequena = pygame.font.Font(None, 22)
        else:  # Pantalla pequeña
            self.fuente = pygame.font.Font(None, 28)
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
    
    def dibujar_seleccion_clase(self):
        # Fondo degradado mejorado
        for y in range(self.alto):
            color = (
                int(15 + (y / self.alto) * 35),
                int(8 + (y / self.alto) * 45),
                int(35 + (y / self.alto) * 65)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título principal centrado
        titulo = self.fuente_grande.render("FANTASY BATTLE", True, DORADO)
        sombra = self.fuente_grande.render("FANTASY BATTLE", True, NEGRO)
        titulo_x = self._centrar_horizontal(titulo.get_width())
        titulo_y = self._centrar_vertical(100, -300)
        
        self.ventana.blit(sombra, (titulo_x + 4, titulo_y + 4))
        self.ventana.blit(titulo, (titulo_x, titulo_y))
        
        # Subtítulo centrado
        subtitulo = self.fuente.render("Selecciona tu clase", True, BLANCO)
        subtitulo_x = self._centrar_horizontal(subtitulo.get_width())
        subtitulo_y = titulo_y + 80
        self.ventana.blit(subtitulo, (subtitulo_x, subtitulo_y))
        
        # Clases disponibles con cajas decorativas - Centradas
        clases = [
            (ClasePersonaje.GUERRERO, "Guerrero", "Fuerte y resistente, especialista en combate cuerpo a cuerpo", ROJO, VERDE_OSCURO),
            (ClasePersonaje.MAGO, "Mago", "Poder mágico devastador, controla elementos y hechizos", MORADO, AZUL_OSCURO),
            (ClasePersonaje.ARQUERO, "Arquero", "Ataques a distancia precisos, evasión y velocidad", VERDE, VERDE_OSCURO),
            (ClasePersonaje.PALADIN, "Paladín", "Equilibrio perfecto entre ataque y defensa, santo", AZUL, AZUL_OSCURO),
            (ClasePersonaje.ASESINO, "Asesino", "Ataques críticos rápidos, sigilo y precisión", NARANJA, ROJO_OSCURO)
        ]
        
        # Calcular posiciones centradas
        clase_ancho = self._ajustar_tamano_elemento(700)
        clase_x = self._centrar_horizontal(clase_ancho)
        clase_espaciado = self._ajustar_tamano_elemento(110)
        clase_inicio_y = subtitulo_y + 80
        
        for i, (clase, nombre, desc, color, color_oscuro) in enumerate(clases):
            y = clase_inicio_y + i * clase_espaciado
            
            # Caja principal con sombra
            pygame.draw.rect(self.ventana, (20, 30, 20), (clase_x-12, y-12, clase_ancho+4, 84))
            pygame.draw.rect(self.ventana, color_oscuro, (clase_x-10, y-10, clase_ancho, 80))
            pygame.draw.rect(self.ventana, color, (clase_x-5, y-5, clase_ancho-10, 70), 3)
            
            # Número de clase
            num_texto = self.fuente_grande.render(f"{i+1}", True, color)
            self.ventana.blit(num_texto, (clase_x + 15, y + 5))
            
            # Nombre de la clase
            nombre_texto = self.fuente.render(nombre, True, color)
            self.ventana.blit(nombre_texto, (clase_x + 80, y + 10))
            
            # Descripción
            desc_texto = self.fuente_pequena.render(desc, True, BLANCO)
            self.ventana.blit(desc_texto, (clase_x + 80, y + 45))
        
        # Modo historia con caja decorativa - Centrado
        x_historia = clase_x
        y_historia = clase_inicio_y + len(clases) * clase_espaciado + 20
        pygame.draw.rect(self.ventana, (30, 20, 15), (x_historia-12, y_historia-12, clase_ancho+4, 84))
        pygame.draw.rect(self.ventana, MARRON, (x_historia-10, y_historia-10, clase_ancho, 80))
        pygame.draw.rect(self.ventana, ROSA, (x_historia-5, y_historia-5, clase_ancho-10, 70), 3)
        
        historia = self.fuente.render("H. Modo Historia", True, ROSA)
        self.ventana.blit(historia, (x_historia + 20, y_historia + 10))
        
        desc_historia = self.fuente_pequena.render("Aventura narrativa con decisiones que afectan la historia", True, BLANCO)
        self.ventana.blit(desc_historia, (x_historia + 20, y_historia + 45))
        
        # Instrucciones centradas en la parte inferior
        instrucciones = self.fuente.render("Presiona 1-5 para seleccionar clase o H para modo historia", True, AMARILLO)
        fondo_inst = pygame.Rect(
            self._centrar_horizontal(instrucciones.get_width() + 60),
            self.alto - 80,
            instrucciones.get_width() + 60,
            60
        )
        pygame.draw.rect(self.ventana, (20, 20, 20), fondo_inst)
        pygame.draw.rect(self.ventana, AMARILLO, fondo_inst, 4)
        self.ventana.blit(instrucciones, (fondo_inst.x + 30, fondo_inst.y + 20))
        
        # Información adicional del juego centrada
        info_texto = self.fuente_pequena.render("Fantasy Battle - Juego de Peleas por Turnos", True, GRIS)
        info_x = self._centrar_horizontal(info_texto.get_width())
        self.ventana.blit(info_texto, (info_x, self.alto - 30))
    
    def dibujar_tienda(self, tienda, monedas_oro, piso_actual, objeto_seleccionado):
        # Fondo de tienda mejorado
        for y in range(self.alto):
            color = (
                int(25 + (y / self.alto) * 25),
                int(15 + (y / self.alto) * 35),
                int(35 + (y / self.alto) * 45)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título de la tienda centrado
        titulo = self.fuente_grande.render("TIENDA", True, DORADO)
        sombra = self.fuente_grande.render("TIENDA", True, NEGRO)
        titulo_x = self._centrar_horizontal(titulo.get_width())
        self.ventana.blit(sombra, (titulo_x + 4, 24))
        self.ventana.blit(titulo, (titulo_x, 20))
        
        # Panel de información del jugador - Centrado
        panel_ancho = self._ajustar_tamano_elemento(600)
        panel_x = self._centrar_horizontal(panel_ancho)
        pygame.draw.rect(self.ventana, (70, 50, 90), (panel_x, 80, panel_ancho, 120))
        pygame.draw.rect(self.ventana, DORADO, (panel_x, 80, panel_ancho, 120), 4)
        
        oro_texto = self.fuente.render(f"Monedas de Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (panel_x + 30, 90))
        
        piso_texto = self.fuente.render(f"Piso {piso_actual}", True, BLANCO)
        self.ventana.blit(piso_texto, (panel_x + 30, 125))
        
        # Panel de piso en el lado derecho - Centrado
        piso_panel_ancho = self._ajustar_tamano_elemento(320)
        piso_panel_x = self.ancho - piso_panel_ancho - 50
        pygame.draw.rect(self.ventana, (70, 50, 90), (piso_panel_x, 80, piso_panel_ancho, 120))
        pygame.draw.rect(self.ventana, DORADO, (piso_panel_x, 80, piso_panel_ancho, 120), 4)
        
        piso_derecho = self.fuente.render(f"Piso {piso_actual}", True, DORADO)
        self.ventana.blit(piso_derecho, (piso_panel_x + 30, 90))
        
        # Información adicional del piso
        if piso_actual % 5 == 0:
            tienda_disponible = self.fuente_pequena.render("¡Tienda disponible!", True, VERDE)
            self.ventana.blit(tienda_disponible, (piso_panel_x + 30, 125))
        
        # Objetos disponibles con cajas decorativas - Centrados
        objetos_ancho = self.ancho - 160
        objetos_x = 80
        
        for i, objeto in enumerate(tienda.objetos_disponibles):
            y = 230 + i * 130
            color = DORADO if i == objeto_seleccionado else BLANCO
            color_fondo = (100, 70, 120) if i == objeto_seleccionado else (80, 50, 100)
            
            # Marco del objeto con sombra
            pygame.draw.rect(self.ventana, (60, 40, 80), (objetos_x-8, y-8, objetos_ancho+6, 108))
            pygame.draw.rect(self.ventana, color_fondo, (objetos_x-5, y-5, objetos_ancho, 100))
            pygame.draw.rect(self.ventana, color, (objetos_x, y, objetos_ancho-10, 90), 3)
            
            # Nombre y precio
            nombre_texto = self.fuente.render(f"{objeto.tipo.value} - {objeto.precio} oro", True, color)
            self.ventana.blit(nombre_texto, (objetos_x + 20, y + 10))
            
            # Descripción
            desc_texto = self.fuente_pequena.render(objeto.descripcion, True, BLANCO)
            self.ventana.blit(desc_texto, (objetos_x + 20, y + 45))
            
            # Efecto del objeto
            efecto_texto = self.fuente_pequena.render(f"Efecto: {objeto.efecto}", True, AMARILLO)
            self.ventana.blit(efecto_texto, (objetos_x + 20, y + 70))
        
        # Instrucciones centradas en la parte inferior
        instrucciones = self.fuente.render("Flechas para navegar | Enter para comprar | T para salir", True, AMARILLO)
        fondo_inst = pygame.Rect(
            self._centrar_horizontal(instrucciones.get_width() + 60),
            self.alto - 80,
            instrucciones.get_width() + 60,
            60
        )
        pygame.draw.rect(self.ventana, (20, 20, 20), fondo_inst)
        pygame.draw.rect(self.ventana, AMARILLO, fondo_inst, 4)
        self.ventana.blit(instrucciones, (fondo_inst.x + 30, fondo_inst.y + 20))
        
        # Información adicional centrada
        info_texto = self.fuente_pequena.render("Compra objetos para mejorar tu personaje", True, GRIS)
        info_x = self._centrar_horizontal(info_texto.get_width())
        self.ventana.blit(info_texto, (info_x, self.alto - 30))
    
    def dibujar_maestro_habilidades(self, maestro_habilidades, jugador, monedas_oro, piso_actual, mejora_seleccionada):
        # Fondo del maestro mejorado
        for y in range(self.alto):
            color = (
                int(30 + (y / self.alto) * 30),
                int(15 + (y / self.alto) * 25),
                int(20 + (y / self.alto) * 20)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título del maestro centrado
        titulo = self.fuente_grande.render("MAESTRO DE HABILIDADES", True, DORADO)
        sombra = self.fuente_grande.render("MAESTRO DE HABILIDADES", True, NEGRO)
        titulo_x = self._centrar_horizontal(titulo.get_width())
        self.ventana.blit(sombra, (titulo_x + 4, 24))
        self.ventana.blit(titulo, (titulo_x, 20))
        
        # Panel de información del jugador - Centrado
        panel_ancho = self._ajustar_tamano_elemento(600)
        panel_x = self._centrar_horizontal(panel_ancho)
        pygame.draw.rect(self.ventana, (100, 50, 70), (panel_x, 80, panel_ancho, 120))
        pygame.draw.rect(self.ventana, DORADO, (panel_x, 80, panel_ancho, 120), 4)
        
        oro_texto = self.fuente.render(f"Monedas de Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (panel_x + 30, 90))
        
        clase_texto = self.fuente.render(f"Clase: {jugador.clase.value}", True, BLANCO)
        self.ventana.blit(clase_texto, (panel_x + 30, 125))
        
        # Panel de clase en el lado derecho - Centrado
        clase_panel_ancho = self._ajustar_tamano_elemento(320)
        clase_panel_x = self.ancho - clase_panel_ancho - 50
        pygame.draw.rect(self.ventana, (100, 50, 70), (clase_panel_x, 80, clase_panel_ancho, 120))
        pygame.draw.rect(self.ventana, DORADO, (clase_panel_x, 80, clase_panel_ancho, 120), 4)
        
        clase_derecho = self.fuente.render(f"Clase: {jugador.clase.value}", True, DORADO)
        self.ventana.blit(clase_derecho, (clase_panel_x + 30, 90))
        
        # Información adicional de la clase
        nivel_texto = self.fuente_pequena.render("Mejora tus habilidades", True, VERDE)
        self.ventana.blit(nivel_texto, (clase_panel_x + 30, 125))
        
        # Mejoras disponibles con cajas decorativas - Centradas
        mejoras = maestro_habilidades.mejoras_disponibles.get(jugador.clase, [])
        
        mejoras_ancho = self.ancho - 160
        mejoras_x = 80
        
        for i, mejora in enumerate(mejoras):
            y = 230 + i * 130
            color = DORADO if i == mejora_seleccionada else BLANCO
            if mejora["nombre"] in jugador.mejoras_aplicadas:
                color = VERDE
            
            color_fondo = (120, 70, 90) if i == mejora_seleccionada else (100, 50, 70)
            
            # Marco de la mejora con sombra
            pygame.draw.rect(self.ventana, (80, 40, 60), (mejoras_x-8, y-8, mejoras_ancho+6, 108))
            pygame.draw.rect(self.ventana, color_fondo, (mejoras_x-5, y-5, mejoras_ancho, 100))
            pygame.draw.rect(self.ventana, color, (mejoras_x, y, mejoras_ancho-10, 90), 3)
            
            # Nombre y precio
            nombre_texto = self.fuente.render(f"{mejora['nombre']} - {mejora['precio']} oro", True, color)
            self.ventana.blit(nombre_texto, (mejoras_x + 20, y + 10))
            
            # Descripción
            desc_texto = self.fuente_pequena.render(mejora['descripcion'], True, BLANCO)
            self.ventana.blit(desc_texto, (mejoras_x + 20, y + 45))
            
            # Indicador de ya comprada
            if mejora["nombre"] in jugador.mejoras_aplicadas:
                comprada_texto = self.fuente_pequena.render("✓ YA COMPRADA", True, VERDE)
                self.ventana.blit(comprada_texto, (mejoras_x + 20, y + 70))
            else:
                # Mostrar estadísticas de la mejora
                if 'ataque' in mejora:
                    stats_texto = self.fuente_pequena.render(f"Bonus: +{mejora['ataque']} Ataque", True, AMARILLO)
                    self.ventana.blit(stats_texto, (mejoras_x + 20, y + 70))
                elif 'defensa' in mejora:
                    stats_texto = self.fuente_pequena.render(f"Bonus: +{mejora['defensa']} Defensa", True, AMARILLO)
                    self.ventana.blit(stats_texto, (mejoras_x + 20, y + 70))
        
        # Instrucciones centradas en la parte inferior
        instrucciones = self.fuente.render("Flechas para navegar | Enter para comprar | M para salir", True, AMARILLO)
        fondo_inst = pygame.Rect(
            self._centrar_horizontal(instrucciones.get_width() + 60),
            self.alto - 80,
            instrucciones.get_width() + 60,
            60
        )
        pygame.draw.rect(self.ventana, (20, 20, 20), fondo_inst)
        pygame.draw.rect(self.ventana, AMARILLO, fondo_inst, 4)
        self.ventana.blit(instrucciones, (fondo_inst.x + 30, fondo_inst.y + 20))
        
        # Información adicional centrada
        info_texto = self.fuente_pequena.render("Mejora tus habilidades para ser más poderoso", True, GRIS)
        info_x = self._centrar_horizontal(info_texto.get_width())
        self.ventana.blit(info_texto, (info_x, self.alto - 30))
    
    def dibujar_batalla(self, jugador, enemigo, piso_actual, monedas_oro, mensaje, turno, 
                       habilidad_seleccionada, objeto_seleccionado_bolsa, jefe_derrotado_reciente):
        # Fondo de batalla degradado mejorado
        for y in range(self.alto):
            color = (
                int(15 + (y / self.alto) * 45),
                int(35 + (y / self.alto) * 70),
                int(15 + (y / self.alto) * 45)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Panel superior de información - Centrado
        pygame.draw.rect(self.ventana, (45, 70, 45), (0, 0, self.ancho, 160))
        pygame.draw.rect(self.ventana, VERDE, (0, 0, self.ancho, 160), 4)
        
        # Información del piso y oro - Centrados
        piso_texto = self.fuente_grande.render(f"Piso {piso_actual}", True, DORADO)
        self.ventana.blit(piso_texto, (self._centrar_horizontal(piso_texto.get_width()), 40))
        
        oro_texto = self.fuente.render(f"Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (self.ancho - 300, 40))
        
        # Indicador de tienda disponible
        if piso_actual % 5 == 0:
            tienda_texto = self.fuente.render("¡Tienda disponible! (T)", True, VERDE)
            self.ventana.blit(tienda_texto, (self.ancho - 400, 80))
        
        # Indicador de maestro de habilidades disponible
        if jefe_derrotado_reciente:
            maestro_texto = self.fuente.render("¡Maestro de Habilidades disponible! (M)", True, AZUL)
            self.ventana.blit(maestro_texto, (self.ancho - 450, 110))
        
        # Indicador de jefe - Centrado
        if piso_actual % 10 == 0:
            jefe_texto = self.fuente_grande.render("¡JEFE!", True, ROSA)
            self.ventana.blit(jefe_texto, (self._centrar_horizontal(jefe_texto.get_width()), 80))
        
        # Información del jugador - Posicionado mejor
        if jugador:
            jugador_x = 100
            self.dibujar_personaje(jugador, jugador_x, 200, VERDE)
        
        # Información del enemigo - Posicionado mejor
        if enemigo:
            color_enemigo = ROSA if enemigo.es_jefe else ROJO
            enemigo_x = self.ancho - 570
            self.dibujar_personaje(enemigo, enemigo_x, 200, color_enemigo)
        
        # Área de batalla central - Centrada
        area_ancho = self._ajustar_tamano_elemento(700)
        area_x = self._centrar_horizontal(area_ancho)
        pygame.draw.rect(self.ventana, (70, 100, 70), (area_x, 480, area_ancho, 220))
        pygame.draw.rect(self.ventana, VERDE, (area_x, 480, area_ancho, 220), 4)
        
        # Mensaje de batalla - Centrado
        if mensaje:
            mensaje_texto = self.fuente.render(mensaje, True, BLANCO)
            self.ventana.blit(mensaje_texto, (self._centrar_horizontal(mensaje_texto.get_width()), 500))
        
        # Turno actual - Centrado
        turno_texto = self.fuente.render(f"Turno: {turno.title()}", True, AMARILLO)
        self.ventana.blit(turno_texto, (self._centrar_horizontal(turno_texto.get_width()), 550))
        
        # Habilidades del jugador - Posicionadas mejor
        if turno == "jugador":
            self.dibujar_habilidades(jugador, habilidad_seleccionada)
            self.dibujar_bolsa_objetos(jugador, objeto_seleccionado_bolsa)
        
        # Botones de acción - Centrados
        if turno == "jugador":
            boton_ancho = self._ajustar_tamano_elemento(320)
            boton_x = self._centrar_horizontal(boton_ancho)
            pygame.draw.rect(self.ventana, AZUL, (boton_x, 720, boton_ancho, 70))
            pygame.draw.rect(self.ventana, BLANCO, (boton_x, 720, boton_ancho, 70), 4)
            descanso_texto = self.fuente.render("Descansar (R)", True, BLANCO)
            self.ventana.blit(descanso_texto, (self._centrar_horizontal(descanso_texto.get_width()), 745))
            
            # Instrucciones adicionales - Centradas
            instrucciones = self.fuente_pequena.render("Flechas para seleccionar | Enter para atacar | O/I para objetos", True, AMARILLO)
            self.ventana.blit(instrucciones, (self._centrar_horizontal(instrucciones.get_width()), 800))
    
    def dibujar_personaje(self, personaje, x, y, color):
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
                clase_texto = self.fuente.render(f"Clase: {personaje.clase.value}", True, BLANCO)
                self.ventana.blit(clase_texto, (x, y + 35))
            
            # Indicador de jefe
            if hasattr(personaje, 'es_jefe') and personaje.es_jefe:
                jefe_texto = self.fuente_pequena.render("JEFE", True, ROSA)
                self.ventana.blit(jefe_texto, (x, y + 60))
            
            # Barra de vida
            if hasattr(personaje, 'vida_actual') and hasattr(personaje, 'vida_maxima'):
                vida_porcentaje = personaje.vida_actual / personaje.vida_maxima
                barra_vida_ancho = self._ajustar_tamano_elemento(300)
                barra_vida_x = x + 20
                barra_vida_y = y + 90
                
                pygame.draw.rect(self.ventana, ROJO, (barra_vida_x, barra_vida_y, barra_vida_ancho, 25))
                pygame.draw.rect(self.ventana, VERDE, (barra_vida_x, barra_vida_y, int(barra_vida_ancho * vida_porcentaje), 25))
                pygame.draw.rect(self.ventana, BLANCO, (barra_vida_x, barra_vida_y, barra_vida_ancho, 25), 2)
                
                vida_texto = self.fuente_pequena.render(f"Vida: {personaje.vida_actual}/{personaje.vida_maxima}", True, BLANCO)
                self.ventana.blit(vida_texto, (barra_vida_x, barra_vida_y + 30))
            
            # Barra de energía
            if hasattr(personaje, 'energia_actual') and hasattr(personaje, 'energia'):
                energia_porcentaje = personaje.energia_actual / personaje.energia
                barra_energia_ancho = self._ajustar_tamano_elemento(300)
                barra_energia_x = x + 20
                barra_energia_y = y + 120
                
                pygame.draw.rect(self.ventana, GRIS, (barra_energia_x, barra_energia_y, barra_energia_ancho, 20))
                pygame.draw.rect(self.ventana, AZUL, (barra_energia_x, barra_energia_y, int(barra_energia_ancho * energia_porcentaje), 20))
                pygame.draw.rect(self.ventana, BLANCO, (barra_energia_x, barra_energia_y, barra_energia_ancho, 20), 2)
                
                energia_texto = self.fuente_pequena.render(f"Energía: {personaje.energia_actual}/{personaje.energia}", True, BLANCO)
                self.ventana.blit(energia_texto, (barra_energia_x, barra_energia_y + 25))
            
            # Estadísticas del personaje - Distribuidas mejor
            y_stats = y + 160
            stats_ancho = self._ajustar_tamano_elemento(200)
            
            # Columna izquierda
            if hasattr(personaje, 'ataque'):
                ataque_texto = self.fuente_pequena.render(f"Ataque: {personaje.ataque}", True, ROJO)
                self.ventana.blit(ataque_texto, (x, y_stats))
            
            if hasattr(personaje, 'defensa'):
                defensa_texto = self.fuente_pequena.render(f"Defensa: {personaje.defensa}", True, AZUL)
                self.ventana.blit(defensa_texto, (x, y_stats + 25))
            
            if hasattr(personaje, 'velocidad'):
                velocidad_texto = self.fuente_pequena.render(f"Velocidad: {personaje.velocidad}", True, VERDE)
                self.ventana.blit(velocidad_texto, (x, y_stats + 50))
            
            # Columna derecha
            x_derecha = x + stats_ancho + 20
            if hasattr(personaje, 'probabilidad_critico'):
                critico_texto = self.fuente_pequena.render(f"Crítico: {personaje.probabilidad_critico}%", True, AMARILLO)
                self.ventana.blit(critico_texto, (x_derecha, y_stats))
            
            if hasattr(personaje, 'probabilidad_esquiva'):
                esquiva_texto = self.fuente_pequena.render(f"Esquiva: {personaje.probabilidad_esquiva}%", True, MORADO)
                self.ventana.blit(esquiva_texto, (x_derecha, y_stats + 25))
            
            # Estado del personaje
            if hasattr(personaje, 'estado') and personaje.estado != "Normal":
                estado_texto = self.fuente_pequena.render(f"Estado: {personaje.estado}", True, NARANJA)
                self.ventana.blit(estado_texto, (x, y_stats + 75))
            
            # Indicador de velocidad extra
            if hasattr(personaje, 'velocidad_extra') and personaje.velocidad_extra > 0:
                velocidad_texto = self.fuente_pequena.render("Velocidad Extra", True, AZUL)
                self.ventana.blit(velocidad_texto, (x, y_stats + 75))
                
        except Exception as e:
            # Si hay algún error, dibujar solo información básica
            print(f"Error al dibujar personaje: {e}")
            nombre_texto = self.fuente.render(str(personaje.nombre) if hasattr(personaje, 'nombre') else "Personaje", True, color)
            self.ventana.blit(nombre_texto, (x, y))
    
    def dibujar_habilidades(self, jugador, habilidad_seleccionada):
        if not jugador or not hasattr(jugador, 'habilidades'):
            return
            
        try:
            # Panel de habilidades - Optimizado
            panel_ancho = self._ajustar_tamano_elemento(550)
            panel_x = 100
            pygame.draw.rect(self.ventana, (50, 70, 50), (panel_x, 800, panel_ancho, 280))
            pygame.draw.rect(self.ventana, VERDE, (panel_x, 800, panel_ancho, 280), 4)
            
            # Título de habilidades
            habilidades_titulo = self.fuente.render("Habilidades:", True, AMARILLO)
            self.ventana.blit(habilidades_titulo, (panel_x + 20, 820))
            
            for i, habilidad in enumerate(jugador.habilidades):
                y = 870 + i * 70
                color = AMARILLO if i == habilidad_seleccionada else BLANCO
                
                # Marco de selección
                if i == habilidad_seleccionada:
                    pygame.draw.rect(self.ventana, AMARILLO, (panel_x + 15, y - 8, panel_ancho - 30, 60), 3)
                
                # Nombre y descripción
                nombre_texto = self.fuente_pequena.render(f"{i+1}. {habilidad.get('nombre', 'Habilidad')}", True, color)
                self.ventana.blit(nombre_texto, (panel_x + 30, y))
                
                desc_texto = self.fuente_pequena.render(f"   {habilidad.get('descripcion', 'Sin descripción')}", True, BLANCO)
                self.ventana.blit(desc_texto, (panel_x + 30, y + 25))
                
                energia_texto = self.fuente_pequena.render(f"   Energía: {habilidad.get('energia', 0)}", True, AZUL)
                self.ventana.blit(energia_texto, (panel_x + 30, y + 45))
        except Exception as e:
            print(f"Error al dibujar habilidades: {e}")
    
    def dibujar_bolsa_objetos(self, jugador, objeto_seleccionado):
        if not jugador or not hasattr(jugador, 'bolsa_objetos'):
            return
            
        try:
            # Panel de bolsa de objetos - Optimizado
            panel_ancho = self._ajustar_tamano_elemento(550)
            panel_x = self.ancho - panel_ancho - 100
            pygame.draw.rect(self.ventana, (50, 70, 50), (panel_x, 800, panel_ancho, 280))
            pygame.draw.rect(self.ventana, VERDE, (panel_x, 800, panel_ancho, 280), 4)
            
            # Título de la bolsa
            bolsa_titulo = self.fuente.render("Bolsa de Objetos:", True, AMARILLO)
            self.ventana.blit(bolsa_titulo, (panel_x + 20, 820))
            
            if not jugador.bolsa_objetos:
                sin_objetos = self.fuente_pequena.render("Sin objetos", True, GRIS)
                self.ventana.blit(sin_objetos, (panel_x + 30, 870))
                return
            
            for i, objeto in enumerate(jugador.bolsa_objetos):
                y = 870 + i * 70
                color = AMARILLO if i == objeto_seleccionado else BLANCO
                
                # Marco de selección
                if i == objeto_seleccionado:
                    pygame.draw.rect(self.ventana, AMARILLO, (panel_x + 15, y - 8, panel_ancho - 30, 60), 3)
                
                # Nombre y cantidad
                nombre_texto = self.fuente_pequena.render(f"{i+1}. {objeto.tipo.value} (x{objeto.cantidad})", True, color)
                self.ventana.blit(nombre_texto, (panel_x + 30, y))
                
                # Descripción del objeto
                desc_texto = self.fuente_pequena.render(f"   {objeto.descripcion}", True, BLANCO)
                self.ventana.blit(desc_texto, (panel_x + 30, y + 25))
                
                # Efecto del objeto
                efecto_texto = self.fuente_pequena.render(f"   Efecto: {objeto.efecto}", True, AMARILLO)
                self.ventana.blit(efecto_texto, (panel_x + 30, y + 45))
        except Exception as e:
            print(f"Error al dibujar bolsa de objetos: {e}")
    
    def limpiar_cache(self):
        """Método vacío para mantener compatibilidad"""
        pass 