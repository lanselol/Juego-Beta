import pygame
from clases.personaje import ClasePersonaje

# Colores
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

# Fuentes
fuente_grande = pygame.font.Font(None, 48)
fuente_mediana = pygame.font.Font(None, 36)
fuente_pequena = pygame.font.Font(None, 24)

class Renderizador:
    def __init__(self, ventana, ancho, alto):
        self.ventana = ventana
        self.ancho = ancho
        self.alto = alto
    
    def dibujar_seleccion_clase(self):
        # Título
        titulo = fuente_grande.render("FANTASY BATTLE", True, DORADO)
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 50))
        
        subtitulo = fuente_mediana.render("Selecciona tu clase de héroe", True, BLANCO)
        self.ventana.blit(subtitulo, (self.ancho//2 - subtitulo.get_width()//2, 120))
        
        # Clases disponibles
        clases = [
            (ClasePersonaje.GUERRERO, "Guerrero", "Fuerte y resistente", ROJO),
            (ClasePersonaje.MAGO, "Mago", "Poder mágico devastador", MORADO),
            (ClasePersonaje.ARQUERO, "Arquero", "Ataques a distancia", VERDE),
            (ClasePersonaje.PALADIN, "Paladín", "Equilibrio ataque/defensa", AZUL),
            (ClasePersonaje.ASESINO, "Asesino", "Ataques críticos rápidos", NARANJA)
        ]
        
        for i, (clase, nombre, desc, color) in enumerate(clases):
            y = 200 + i * 80
            rect = pygame.Rect(100, y, 400, 60)
            pygame.draw.rect(self.ventana, color, rect, 3)
            
            texto = fuente_mediana.render(nombre, True, color)
            self.ventana.blit(texto, (120, y + 10))
            
            desc_texto = fuente_pequena.render(desc, True, BLANCO)
            self.ventana.blit(desc_texto, (120, y + 35))
        
        # Instrucciones
        instrucciones = fuente_pequena.render("Presiona 1-5 para seleccionar tu clase", True, AMARILLO)
        self.ventana.blit(instrucciones, (self.ancho//2 - instrucciones.get_width()//2, 650))
    
    def dibujar_tienda(self, tienda, monedas_oro, piso_actual, objeto_seleccionado):
        # Fondo de tienda
        pygame.draw.rect(self.ventana, (40, 20, 60), (0, 0, self.ancho, self.alto))
        
        # Título de la tienda
        titulo = fuente_grande.render("TIENDA", True, DORADO)
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 20))
        
        # Información del jugador
        oro_texto = fuente_mediana.render(f"Monedas de Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (50, 80))
        
        piso_texto = fuente_mediana.render(f"Piso {piso_actual}", True, BLANCO)
        self.ventana.blit(piso_texto, (self.ancho - 200, 80))
        
        # Objetos disponibles
        for i, objeto in enumerate(tienda.objetos_disponibles):
            y = 150 + i * 80
            color = DORADO if i == objeto_seleccionado else BLANCO
            
            # Marco del objeto
            if i == objeto_seleccionado:
                pygame.draw.rect(self.ventana, DORADO, (50, y - 5, 500, 70), 3)
            
            # Nombre y precio
            nombre_texto = fuente_mediana.render(f"{objeto.tipo.value} - {objeto.precio} oro", True, color)
            self.ventana.blit(nombre_texto, (60, y))
            
            # Descripción
            desc_texto = fuente_pequena.render(objeto.descripcion, True, BLANCO)
            self.ventana.blit(desc_texto, (60, y + 30))
        
        # Instrucciones
        instrucciones = fuente_pequena.render("Flechas para navegar | Enter para comprar | T para salir", True, AMARILLO)
        self.ventana.blit(instrucciones, (self.ancho//2 - instrucciones.get_width()//2, 650))
    
    def dibujar_maestro_habilidades(self, maestro_habilidades, jugador, monedas_oro, piso_actual, mejora_seleccionada):
        # Fondo del maestro
        pygame.draw.rect(self.ventana, (60, 20, 40), (0, 0, self.ancho, self.alto))
        
        # Título del maestro
        titulo = fuente_grande.render("MAESTRO DE HABILIDADES", True, DORADO)
        self.ventana.blit(titulo, (self.ancho//2 - titulo.get_width()//2, 20))
        
        # Información del jugador
        oro_texto = fuente_mediana.render(f"Monedas de Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (50, 80))
        
        piso_texto = fuente_mediana.render(f"Piso {piso_actual}", True, BLANCO)
        self.ventana.blit(piso_texto, (self.ancho - 200, 80))
        
        clase_texto = fuente_mediana.render(f"Clase: {jugador.clase.value}", True, AZUL)
        self.ventana.blit(clase_texto, (self.ancho//2 - clase_texto.get_width()//2, 80))
        
        # Mejoras disponibles
        mejoras = maestro_habilidades.mejoras_disponibles.get(jugador.clase, [])
        
        for i, mejora in enumerate(mejoras):
            y = 150 + i * 80
            color = DORADO if i == mejora_seleccionada else BLANCO
            
            # Verificar si ya se aplicó esta mejora
            if mejora["nombre"] in jugador.mejoras_aplicadas:
                color = VERDE
            
            # Marco de la mejora
            if i == mejora_seleccionada:
                pygame.draw.rect(self.ventana, DORADO, (50, y - 5, 500, 70), 3)
            
            # Nombre y precio
            nombre_texto = fuente_mediana.render(f"{mejora['nombre']} - {mejora['precio']} oro", True, color)
            self.ventana.blit(nombre_texto, (60, y))
            
            # Descripción
            desc_texto = fuente_pequena.render(mejora['descripcion'], True, BLANCO)
            self.ventana.blit(desc_texto, (60, y + 30))
            
            # Indicador de ya comprada
            if mejora["nombre"] in jugador.mejoras_aplicadas:
                comprada_texto = fuente_pequena.render("✓ YA COMPRADA", True, VERDE)
                self.ventana.blit(comprada_texto, (60, y + 50))
        
        # Instrucciones
        instrucciones = fuente_pequena.render("Flechas para navegar | Enter para comprar | M para salir", True, AMARILLO)
        self.ventana.blit(instrucciones, (self.ancho//2 - instrucciones.get_width()//2, 650))
    
    def dibujar_batalla(self, jugador, enemigo, piso_actual, monedas_oro, mensaje, turno, 
                       habilidad_seleccionada, objeto_seleccionado_bolsa, jefe_derrotado_reciente):
        # Fondo de batalla
        pygame.draw.rect(self.ventana, (20, 40, 20), (0, 0, self.ancho, self.alto))
        
        # Información del piso y oro
        piso_texto = fuente_mediana.render(f"Piso {piso_actual}", True, DORADO)
        self.ventana.blit(piso_texto, (self.ancho//2 - piso_texto.get_width()//2, 20))
        
        oro_texto = fuente_pequena.render(f"Oro: {monedas_oro}", True, DORADO)
        self.ventana.blit(oro_texto, (self.ancho - 150, 20))
        
        # Indicador de tienda disponible
        if piso_actual % 5 == 0:
            tienda_texto = fuente_pequena.render("¡Tienda disponible! (T)", True, VERDE)
            self.ventana.blit(tienda_texto, (self.ancho - 200, 50))
        
        # Indicador de maestro de habilidades disponible
        if jefe_derrotado_reciente:
            maestro_texto = fuente_pequena.render("¡Maestro de Habilidades disponible! (M)", True, AZUL)
            self.ventana.blit(maestro_texto, (self.ancho - 300, 80))
        
        # Indicador de jefe
        if piso_actual % 10 == 0:
            jefe_texto = fuente_mediana.render("¡JEFE!", True, ROSA)
            self.ventana.blit(jefe_texto, (self.ancho//2 - jefe_texto.get_width()//2, 50))
        
        # Información del jugador
        self.dibujar_personaje(jugador, 50, 100, VERDE)
        
        # Información del enemigo
        color_enemigo = ROSA if enemigo.es_jefe else ROJO
        self.dibujar_personaje(enemigo, self.ancho - 450, 100, color_enemigo)
        
        # Área de batalla central
        pygame.draw.rect(self.ventana, (40, 60, 40), (self.ancho//2 - 200, 300, 400, 200))
        
        # Mensaje de batalla
        if mensaje:
            mensaje_texto = fuente_pequena.render(mensaje, True, BLANCO)
            self.ventana.blit(mensaje_texto, (self.ancho//2 - mensaje_texto.get_width()//2, 320))
        
        # Turno actual
        turno_texto = fuente_mediana.render(f"Turno: {turno.title()}", True, AMARILLO)
        self.ventana.blit(turno_texto, (self.ancho//2 - turno_texto.get_width()//2, 350))
        
        # Habilidades del jugador
        if turno == "jugador":
            self.dibujar_habilidades(jugador, habilidad_seleccionada)
            self.dibujar_bolsa_objetos(jugador, objeto_seleccionado_bolsa)
        
        # Botones de acción
        if turno == "jugador":
            pygame.draw.rect(self.ventana, AZUL, (self.ancho//2 - 100, 500, 200, 40))
            descanso_texto = fuente_mediana.render("Descansar (R)", True, BLANCO)
            self.ventana.blit(descanso_texto, (self.ancho//2 - descanso_texto.get_width()//2, 510))
    
    def dibujar_personaje(self, personaje, x, y, color):
        # Marco del personaje
        grosor = 5 if personaje.es_jefe else 3
        pygame.draw.rect(self.ventana, color, (x, y, 400, 200), grosor)
        
        # Nombre y clase
        nombre_texto = fuente_mediana.render(personaje.nombre, True, color)
        self.ventana.blit(nombre_texto, (x + 10, y + 10))
        
        clase_texto = fuente_pequena.render(f"Clase: {personaje.clase.value}", True, BLANCO)
        self.ventana.blit(clase_texto, (x + 10, y + 40))
        
        # Indicador de jefe
        if personaje.es_jefe:
            jefe_texto = fuente_pequena.render("JEFE", True, ROSA)
            self.ventana.blit(jefe_texto, (x + 10, y + 60))
        
        # Barra de vida
        y_vida = y + 70 if personaje.es_jefe else y + 70
        pygame.draw.rect(self.ventana, ROJO, (x + 10, y_vida, 380, 20))
        vida_porcentaje = personaje.vida_actual / personaje.vida_maxima
        pygame.draw.rect(self.ventana, VERDE, (x + 10, y_vida, 380 * vida_porcentaje, 20))
        vida_texto = fuente_pequena.render(f"Vida: {round(personaje.vida_actual)}/{round(personaje.vida_maxima)}", True, BLANCO)
        self.ventana.blit(vida_texto, (x + 10, y_vida + 25))
        
        # Barra de energía
        y_energia = y_vida + 45
        pygame.draw.rect(self.ventana, GRIS, (x + 10, y_energia, 380, 15))
        energia_porcentaje = personaje.energia_actual / personaje.energia
        pygame.draw.rect(self.ventana, AZUL, (x + 10, y_energia, 380 * energia_porcentaje, 15))
        energia_texto = fuente_pequena.render(f"Energía: {round(personaje.energia_actual)}/{round(personaje.energia)}", True, BLANCO)
        self.ventana.blit(energia_texto, (x + 10, y_energia + 20))
        
        # Estadísticas
        y_stats = y_energia + 40
        stats_texto = fuente_pequena.render(f"Ataque: {round(personaje.ataque)} | Defensa: {round(personaje.defensa)}", True, BLANCO)
        self.ventana.blit(stats_texto, (x + 10, y_stats))
        
        # Estado y efectos
        if personaje.estado != "Normal":
            estado_texto = fuente_pequena.render(f"Estado: {personaje.estado}", True, AMARILLO)
            self.ventana.blit(estado_texto, (x + 10, y_stats + 20))
        
        if personaje.veneno_activo > 0:
            veneno_texto = fuente_pequena.render(f"Veneno: {round(personaje.veneno_activo)}", True, VERDE)
            self.ventana.blit(veneno_texto, (x + 10, y_stats + 40))
        
        if personaje.velocidad_extra:
            velocidad_texto = fuente_pequena.render("Velocidad Extra", True, AZUL)
            self.ventana.blit(velocidad_texto, (x + 10, y_stats + 60))
    
    def dibujar_habilidades(self, jugador, habilidad_seleccionada):
        # Título de habilidades
        habilidades_titulo = fuente_mediana.render("Habilidades:", True, AMARILLO)
        self.ventana.blit(habilidades_titulo, (50, 550))
        
        for i, habilidad in enumerate(jugador.habilidades):
            color = DORADO if i == habilidad_seleccionada else BLANCO
            y = 590 + i * 50
            
            # Marco de la habilidad
            if i == habilidad_seleccionada:
                pygame.draw.rect(self.ventana, DORADO, (50, y - 5, 500, 40), 2)
            
            # Nombre y descripción
            nombre_texto = fuente_pequena.render(f"{i+1}. {habilidad['nombre']}", True, color)
            self.ventana.blit(nombre_texto, (60, y))
            
            desc_texto = fuente_pequena.render(f"   {habilidad['descripcion']} (Energía: {habilidad['energia']})", True, BLANCO)
            self.ventana.blit(desc_texto, (60, y + 20))
    
    def dibujar_bolsa_objetos(self, jugador, objeto_seleccionado):
        # Título de la bolsa
        bolsa_titulo = fuente_mediana.render("Bolsa de Objetos:", True, AMARILLO)
        self.ventana.blit(bolsa_titulo, (self.ancho - 450, 550))
        
        if not jugador.bolsa_objetos:
            sin_objetos = fuente_pequena.render("Sin objetos", True, GRIS)
            self.ventana.blit(sin_objetos, (self.ancho - 450, 590))
            return
        
        for i, objeto in enumerate(jugador.bolsa_objetos):
            y = 590 + i * 40
            color = DORADO if i == objeto_seleccionado else BLANCO
            
            # Marco del objeto
            if i == objeto_seleccionado:
                pygame.draw.rect(self.ventana, DORADO, (self.ancho - 460, y - 5, 400, 35), 2)
            
            # Nombre y cantidad
            nombre_texto = fuente_pequena.render(f"{i+1}. {objeto.tipo.value} (x{objeto.cantidad})", True, color)
            self.ventana.blit(nombre_texto, (self.ancho - 450, y)) 