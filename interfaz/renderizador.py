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
    
    def dibujar_seleccion_clase(self):
        # Fondo degradado mejorado para 1920x1080
        for y in range(self.alto):
            color = (
                int(15 + (y / self.alto) * 35),
                int(8 + (y / self.alto) * 45),
                int(35 + (y / self.alto) * 65)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título principal con sombra mejorada
        titulo = self.fuente_grande.render("FANTASY BATTLE", True, DORADO)
        sombra = self.fuente_grande.render("FANTASY BATTLE", True, NEGRO)
        self.ventana.blit(sombra, (self.ancho//2 - titulo.get_width()//2 + 4, 104))
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 100))
        
        # Subtítulo centrado
        subtitulo = self.fuente.render("Selecciona tu clase", True, BLANCO)
        self.ventana.blit(subtitulo, (self.ancho//2 - subtitulo.get_width()//2, 180))
        
        # Clases disponibles con cajas decorativas - Distribuidas perfectamente para 1920x1080
        clases = [
            (ClasePersonaje.GUERRERO, "Guerrero", "Fuerte y resistente, especialista en combate cuerpo a cuerpo", ROJO, VERDE_OSCURO),
            (ClasePersonaje.MAGO, "Mago", "Poder mágico devastador, controla elementos y hechizos", MORADO, AZUL_OSCURO),
            (ClasePersonaje.ARQUERO, "Arquero", "Ataques a distancia precisos, evasión y velocidad", VERDE, VERDE_OSCURO),
            (ClasePersonaje.PALADIN, "Paladín", "Equilibrio perfecto entre ataque y defensa, santo", AZUL, AZUL_OSCURO),
            (ClasePersonaje.ASESINO, "Asesino", "Ataques críticos rápidos, sigilo y precisión", NARANJA, ROJO_OSCURO)
        ]
        
        # Calcular posiciones centradas para 1920x1080
        clase_ancho = 700
        clase_x = (self.ancho - clase_ancho) // 2
        clase_espaciado = 110
        
        for i, (clase, nombre, desc, color, color_oscuro) in enumerate(clases):
            y = 250 + i * clase_espaciado
            
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
        
        # Modo historia con caja decorativa - Posicionado mejor para 1920x1080
        x_historia = clase_x
        y_historia = 820
        pygame.draw.rect(self.ventana, (30, 20, 15), (x_historia-12, y_historia-12, clase_ancho+4, 84))
        pygame.draw.rect(self.ventana, MARRON, (x_historia-10, y_historia-10, clase_ancho, 80))
        pygame.draw.rect(self.ventana, ROSA, (x_historia-5, y_historia-5, clase_ancho-10, 70), 3)
        
        historia = self.fuente.render("H. Modo Historia", True, ROSA)
        self.ventana.blit(historia, (x_historia + 20, y_historia + 10))
        
        desc_historia = self.fuente_pequena.render("Aventura narrativa con decisiones que afectan la historia", True, BLANCO)
        self.ventana.blit(desc_historia, (x_historia + 20, y_historia + 45))
        
        # Instrucciones con fondo mejorado - Posicionadas en la parte inferior para 1920x1080
        instrucciones = self.fuente.render("Presiona 1-5 para seleccionar clase o H para modo historia", True, AMARILLO)
        fondo_inst = pygame.Rect(50, 980, instrucciones.get_width() + 60, 60)
        pygame.draw.rect(self.ventana, (20, 20, 20), fondo_inst)
        pygame.draw.rect(self.ventana, AMARILLO, fondo_inst, 4)
        self.ventana.blit(instrucciones, (80, 1000))
        
        # Información adicional del juego
        info_texto = self.fuente_pequena.render("Fantasy Battle - Juego de Peleas por Turnos", True, GRIS)
        self.ventana.blit(info_texto, (self.ancho - 400, 1020))
    
    def dibujar_tienda(self, tienda, monedas_oro, piso_actual, objeto_seleccionado):
        # Fondo de tienda mejorado para 1920x1080
        for y in range(self.alto):
            color = (
                int(25 + (y / self.alto) * 25),
                int(15 + (y / self.alto) * 35),
                int(35 + (y / self.alto) * 45)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título de la tienda con sombra mejorada
        titulo = self.fuente_grande.render("TIENDA", True, DORADO)
        sombra = self.fuente_grande.render("TIENDA", True, NEGRO)
        self.ventana.blit(sombra, (self.ancho//2 - titulo.get_width()//2 + 4, 24))
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 20))
        
        # Panel de información del jugador - Posicionado mejor para 1920x1080
        panel_ancho = 600
        panel_x = 80
        pygame.draw.rect(self.ventana, (70, 50, 90), (panel_x, 80, panel_ancho, 120))
        pygame.draw.rect(self.ventana, DORADO, (panel_x, 80, panel_ancho, 120), 4)
        
        oro_texto = self.fuente.render(f"Monedas de Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (panel_x + 30, 90))
        
        piso_texto = self.fuente.render(f"Piso {piso_actual}", True, BLANCO)
        self.ventana.blit(piso_texto, (panel_x + 30, 125))
        
        # Panel de piso en el lado derecho - Mejor posicionado
        piso_panel_x = self.ancho - 400
        pygame.draw.rect(self.ventana, (70, 50, 90), (piso_panel_x, 80, 320, 120))
        pygame.draw.rect(self.ventana, DORADO, (piso_panel_x, 80, 320, 120), 4)
        
        piso_derecho = self.fuente.render(f"Piso {piso_actual}", True, DORADO)
        self.ventana.blit(piso_derecho, (piso_panel_x + 30, 90))
        
        # Información adicional del piso
        if piso_actual % 5 == 0:
            tienda_disponible = self.fuente_pequena.render("¡Tienda disponible!", True, VERDE)
            self.ventana.blit(tienda_disponible, (piso_panel_x + 30, 125))
        
        # Objetos disponibles con cajas decorativas - Distribuidos mejor para 1920x1080
        objetos_x = 80
        objetos_ancho = self.ancho - 160
        
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
        
        # Instrucciones con fondo mejorado - Posicionadas en la parte inferior para 1920x1080
        instrucciones = self.fuente.render("Flechas para navegar | Enter para comprar | T para salir", True, AMARILLO)
        fondo_inst = pygame.Rect(80, 980, instrucciones.get_width() + 60, 60)
        pygame.draw.rect(self.ventana, (20, 20, 20), fondo_inst)
        pygame.draw.rect(self.ventana, AMARILLO, fondo_inst, 4)
        self.ventana.blit(instrucciones, (110, 1000))
        
        # Información adicional
        info_texto = self.fuente_pequena.render("Compra objetos para mejorar tu personaje", True, GRIS)
        self.ventana.blit(info_texto, (self.ancho - 450, 1020))
    
    def dibujar_maestro_habilidades(self, maestro_habilidades, jugador, monedas_oro, piso_actual, mejora_seleccionada):
        # Fondo del maestro mejorado para 1920x1080
        for y in range(self.alto):
            color = (
                int(30 + (y / self.alto) * 30),
                int(15 + (y / self.alto) * 25),
                int(20 + (y / self.alto) * 20)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Título del maestro con sombra mejorada
        titulo = self.fuente_grande.render("MAESTRO DE HABILIDADES", True, DORADO)
        sombra = self.fuente_grande.render("MAESTRO DE HABILIDADES", True, NEGRO)
        self.ventana.blit(sombra, (self.ancho//2 - titulo.get_width()//2 + 4, 24))
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 20))
        
        # Panel de información del jugador - Posicionado mejor para 1920x1080
        panel_ancho = 600
        panel_x = 80
        pygame.draw.rect(self.ventana, (100, 50, 70), (panel_x, 80, panel_ancho, 120))
        pygame.draw.rect(self.ventana, DORADO, (panel_x, 80, panel_ancho, 120), 4)
        
        oro_texto = self.fuente.render(f"Monedas de Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (panel_x + 30, 90))
        
        clase_texto = self.fuente.render(f"Clase: {jugador.clase.value}", True, BLANCO)
        self.ventana.blit(clase_texto, (panel_x + 30, 125))
        
        # Panel de clase en el lado derecho - Mejor posicionado
        clase_panel_x = self.ancho - 400
        pygame.draw.rect(self.ventana, (100, 50, 70), (clase_panel_x, 80, 320, 120))
        pygame.draw.rect(self.ventana, DORADO, (clase_panel_x, 80, 320, 120), 4)
        
        clase_derecho = self.fuente.render(f"Clase: {jugador.clase.value}", True, DORADO)
        self.ventana.blit(clase_derecho, (clase_panel_x + 30, 90))
        
        # Información adicional de la clase
        nivel_texto = self.fuente_pequena.render("Mejora tus habilidades", True, VERDE)
        self.ventana.blit(nivel_texto, (clase_panel_x + 30, 125))
        
        # Mejoras disponibles con cajas decorativas - Distribuidos mejor para 1920x1080
        mejoras = maestro_habilidades.mejoras_disponibles.get(jugador.clase, [])
        
        mejoras_x = 80
        mejoras_ancho = self.ancho - 160
        
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
        
        # Instrucciones con fondo mejorado - Posicionadas en la parte inferior para 1920x1080
        instrucciones = self.fuente.render("Flechas para navegar | Enter para comprar | M para salir", True, AMARILLO)
        fondo_inst = pygame.Rect(80, 980, instrucciones.get_width() + 60, 60)
        pygame.draw.rect(self.ventana, (20, 20, 20), fondo_inst)
        pygame.draw.rect(self.ventana, AMARILLO, fondo_inst, 4)
        self.ventana.blit(instrucciones, (110, 1000))
        
        # Información adicional
        info_texto = self.fuente_pequena.render("Mejora tus habilidades para ser más poderoso", True, GRIS)
        self.ventana.blit(info_texto, (self.ancho - 450, 1020))
    
    def dibujar_batalla(self, jugador, enemigo, piso_actual, monedas_oro, mensaje, turno, 
                       habilidad_seleccionada, objeto_seleccionado_bolsa, jefe_derrotado_reciente):
        # Fondo de batalla degradado mejorado para 1920x1080
        for y in range(self.alto):
            color = (
                int(15 + (y / self.alto) * 45),
                int(35 + (y / self.alto) * 70),
                int(15 + (y / self.alto) * 45)
            )
            pygame.draw.line(self.ventana, color, (0, y), (self.ancho, y))
        
        # Panel superior de información - Optimizado para 1920x1080
        pygame.draw.rect(self.ventana, (45, 70, 45), (0, 0, self.ancho, 160))
        pygame.draw.rect(self.ventana, VERDE, (0, 0, self.ancho, 160), 4)
        
        # Información del piso y oro - Centrados y mejor distribuidos
        piso_texto = self.fuente_grande.render(f"Piso {piso_actual}", True, DORADO)
        self.ventana.blit(piso_texto, (self.ancho//2 - piso_texto.get_width()//2, 40))
        
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
        
        # Indicador de jefe
        if piso_actual % 10 == 0:
            jefe_texto = self.fuente_grande.render("¡JEFE!", True, ROSA)
            self.ventana.blit(jefe_texto, (self.ancho//2 - jefe_texto.get_width()//2, 80))
        
        # Información del jugador - Posicionado mejor para 1920x1080
        if jugador:
            self.dibujar_personaje(jugador, 100, 200, VERDE)
        
        # Información del enemigo - Posicionado mejor para 1920x1080
        if enemigo:
            color_enemigo = ROSA if enemigo.es_jefe else ROJO
            self.dibujar_personaje(enemigo, self.ancho - 570, 200, color_enemigo)
        
        # Área de batalla central - Optimizada para 1920x1080
        area_ancho = 700
        area_x = (self.ancho - area_ancho) // 2
        pygame.draw.rect(self.ventana, (70, 100, 70), (area_x, 480, area_ancho, 220))
        pygame.draw.rect(self.ventana, VERDE, (area_x, 480, area_ancho, 220), 4)
        
        # Mensaje de batalla
        if mensaje:
            mensaje_texto = self.fuente.render(mensaje, True, BLANCO)
            self.ventana.blit(mensaje_texto, (self.ancho//2 - mensaje_texto.get_width()//2, 500))
        
        # Turno actual
        turno_texto = self.fuente.render(f"Turno: {turno.title()}", True, AMARILLO)
        self.ventana.blit(turno_texto, (self.ancho//2 - turno_texto.get_width()//2, 550))
        
        # Habilidades del jugador - Posicionadas mejor para 1920x1080
        if turno == "jugador":
            self.dibujar_habilidades(jugador, habilidad_seleccionada)
            self.dibujar_bolsa_objetos(jugador, objeto_seleccionado_bolsa)
        
        # Botones de acción - Centrados y mejor distribuidos para 1920x1080
        if turno == "jugador":
            boton_ancho = 320
            boton_x = (self.ancho - boton_ancho) // 2
            pygame.draw.rect(self.ventana, AZUL, (boton_x, 720, boton_ancho, 70))
            pygame.draw.rect(self.ventana, BLANCO, (boton_x, 720, boton_ancho, 70), 4)
            descanso_texto = self.fuente.render("Descansar (R)", True, BLANCO)
            self.ventana.blit(descanso_texto, (self.ancho//2 - descanso_texto.get_width()//2, 745))
            
            # Instrucciones adicionales
            instrucciones = self.fuente_pequena.render("Flechas para seleccionar | Enter para atacar | O/I para objetos", True, AMARILLO)
            self.ventana.blit(instrucciones, (self.ancho//2 - instrucciones.get_width()//2, 800))
    
    def dibujar_personaje(self, personaje, x, y, color):
        if not personaje:
            return
        
        try:
            # Marco del personaje - Optimizado para 1920x1080
            marco_ancho = 450
            marco_alto = 240
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
                barra_vida_ancho = 300
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
                barra_energia_ancho = 300
                barra_energia_x = x + 20
                barra_energia_y = y + 120
                
                pygame.draw.rect(self.ventana, GRIS, (barra_energia_x, barra_energia_y, barra_energia_ancho, 20))
                pygame.draw.rect(self.ventana, AZUL, (barra_energia_x, barra_energia_y, int(barra_energia_ancho * energia_porcentaje), 20))
                pygame.draw.rect(self.ventana, BLANCO, (barra_energia_x, barra_energia_y, barra_energia_ancho, 20), 2)
                
                energia_texto = self.fuente_pequena.render(f"Energía: {personaje.energia_actual}/{personaje.energia}", True, BLANCO)
                self.ventana.blit(energia_texto, (barra_energia_x, barra_energia_y + 25))
            
            # Estadísticas del personaje - Distribuidas mejor
            y_stats = y + 160
            stats_ancho = 200
            
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
            # Panel de habilidades - Optimizado para 1920x1080
            panel_ancho = 550
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
            # Panel de bolsa de objetos - Optimizado para 1920x1080
            panel_ancho = 550
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