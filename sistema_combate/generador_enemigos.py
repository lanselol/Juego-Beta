import random
from clases.personaje import Personaje, ClasePersonaje
from clases.jefe import Jefe

class GeneradorEnemigos:
    def __init__(self):
        self.jefes_disponibles = self._crear_jefes()
        self.jefes_derrotados = []
    
    def _crear_jefes(self):
        jefes = [
            ("Ragnaros el Señor del Fuego", ClasePersonaje.MAGO),
            ("Thrall el Jefe de Guerra", ClasePersonaje.GUERRERO),
            ("Sylvanas la Reina Banshee", ClasePersonaje.ARQUERO),
            ("Uther el Portador de Luz", ClasePersonaje.PALADIN),
            ("Valeera la Sombra", ClasePersonaje.ASESINO),
            ("Gul'dan el Destructor", ClasePersonaje.MAGO),
            ("Grommash Puño de Hierro", ClasePersonaje.GUERRERO),
            ("Alleria Brisaveloz", ClasePersonaje.ARQUERO),
            ("Tirion Fordring", ClasePersonaje.PALADIN),
            ("Garona la Asesina", ClasePersonaje.ASESINO)
        ]
        return jefes
    
    def crear_enemigo(self, piso_actual):
        # Verificar si es un piso de jefe (múltiplo de 10)
        if piso_actual % 10 == 0:
            return self._crear_jefe(piso_actual)
        else:
            return self._crear_enemigo_normal(piso_actual)
    
    def _crear_jefe(self, piso_actual):
        # Seleccionar un jefe aleatorio que no haya sido derrotado
        jefes_disponibles = [j for j in self.jefes_disponibles if j[0] not in self.jefes_derrotados]
        if not jefes_disponibles:
            # Si todos los jefes han sido derrotados, reiniciar
            self.jefes_derrotados = []
            jefes_disponibles = self.jefes_disponibles
        
        nombre_jefe, clase_jefe = random.choice(jefes_disponibles)
        return Jefe(nombre_jefe, clase_jefe, piso_actual)
    
    def _crear_enemigo_normal(self, piso_actual):
        clases = list(ClasePersonaje)
        clase_enemigo = random.choice(clases)
        
        # Multiplicador de dificultad basado en el piso
        multiplicador = 1 + (piso_actual - 1) * 0.1
        
        nombres_enemigos = {
            ClasePersonaje.GUERRERO: ["Grommash", "Thrall", "Garrosh", "Orgrim", "Saurfang"],
            ClasePersonaje.MAGO: ["Gul'dan", "Jaina", "Medivh", "Khadgar", "Antonidas"],
            ClasePersonaje.ARQUERO: ["Sylvanas", "Alleria", "Nathanos", "Rexxar", "Halduron"],
            ClasePersonaje.PALADIN: ["Uther", "Tirion", "Arthas", "Liadrin", "Maraad"],
            ClasePersonaje.ASESINO: ["Valeera", "Garona", "Edwin", "Mathias", "Shaw"]
        }
        
        nombre_enemigo = random.choice(nombres_enemigos[clase_enemigo])
        enemigo = Personaje(nombre_enemigo, clase_enemigo)
        
        # Aplicar multiplicador de dificultad
        enemigo.vida_maxima = int(enemigo.vida_maxima * multiplicador)
        enemigo.vida_actual = enemigo.vida_maxima
        enemigo.ataque = int(enemigo.ataque * multiplicador)
        enemigo.defensa = int(enemigo.defensa * multiplicador)
        enemigo.energia = int(enemigo.energia * multiplicador)
        enemigo.energia_actual = enemigo.energia
        
        return enemigo
    
    def marcar_jefe_derrotado(self, nombre_jefe):
        """Marca un jefe como derrotado"""
        if nombre_jefe not in self.jefes_derrotados:
            self.jefes_derrotados.append(nombre_jefe)
    
    def reiniciar_jefes(self):
        """Reinicia la lista de jefes derrotados"""
        self.jefes_derrotados = [] 