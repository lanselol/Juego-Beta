import random
from clases.personaje import Personaje, ClasePersonaje
from objetos.objeto import Objeto, TipoObjeto

class Jefe(Personaje):
    def __init__(self, nombre, clase, piso):
        super().__init__(nombre, clase)
        self.piso = piso
        self.es_jefe = True
        
        # Multiplicador de dificultad basado en el piso
        multiplicador = 1 + (piso // 10) * 0.5
        
        self.nivel = piso
        self.vida_maxima = int(self._obtener_vida_base() * multiplicador)
        self.vida_actual = self.vida_maxima
        self.ataque = int(self._obtener_ataque_base() * multiplicador)
        self.defensa = int(self._obtener_defensa_base() * multiplicador)
        self.energia = int(self._obtener_energia_base() * multiplicador)
        self.energia_actual = self.energia
        self.habilidades = self._obtener_habilidades_jefe()
        
        # Actualizar valores base después de aplicar multiplicador
        self.ataque_base = self.ataque
        self.defensa_base = self.defensa
        
        # Limpiar objetos iniciales y agregar objetos de jefe
        self.bolsa_objetos = []
        self._agregar_objetos_iniciales_jefe()
        
    def _agregar_objetos_iniciales_jefe(self):
        # Los jefes comienzan con más objetos que los personajes normales
        pocion_vida = Objeto(TipoObjeto.POCION_VIDA, 50, "Restaura 50 puntos de vida", {"vida": 50})
        pocion_energia = Objeto(TipoObjeto.POCION_ENERGIA, 40, "Restaura 40 puntos de energía", {"energia": 40})
        
        # Los jefes tienen objetos adicionales según su clase
        if self.clase == ClasePersonaje.GUERRERO:
            elixir_fuerza = Objeto(TipoObjeto.ELIXIR_FUERZA, 80, "Aumenta el ataque en 10 por 3 turnos", {"ataque": 10, "duracion": 3})
            self.bolsa_objetos.append(elixir_fuerza)
        elif self.clase == ClasePersonaje.MAGO:
            elixir_velocidad = Objeto(TipoObjeto.ELIXIR_VELOCIDAD, 70, "Aumenta la velocidad de ataque por 2 turnos", {"velocidad": True, "duracion": 2})
            self.bolsa_objetos.append(elixir_velocidad)
        elif self.clase == ClasePersonaje.ARQUERO:
            bomba_veneno = Objeto(TipoObjeto.BOMBA_VENENO, 100, "Causa 30 daño por veneno por 3 turnos", {"veneno": 30, "duracion": 3})
            self.bolsa_objetos.append(bomba_veneno)
        elif self.clase == ClasePersonaje.PALADIN:
            escudo_temporal = Objeto(TipoObjeto.ESCUDO_TEMPORAL, 60, "Aumenta la defensa en 15 por 2 turnos", {"defensa": 15, "duracion": 2})
            self.bolsa_objetos.append(escudo_temporal)
        elif self.clase == ClasePersonaje.ASESINO:
            elixir_fuerza = Objeto(TipoObjeto.ELIXIR_FUERZA, 80, "Aumenta el ataque en 10 por 3 turnos", {"ataque": 10, "duracion": 3})
            self.bolsa_objetos.append(elixir_fuerza)
        
        self.bolsa_objetos.append(pocion_vida)
        self.bolsa_objetos.append(pocion_energia)
    
    def _obtener_vida_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 150
        elif self.clase == ClasePersonaje.MAGO:
            return 120
        elif self.clase == ClasePersonaje.ARQUERO:
            return 130
        elif self.clase == ClasePersonaje.PALADIN:
            return 140
        elif self.clase == ClasePersonaje.ASESINO:
            return 125
        return 130
    
    def _obtener_ataque_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 35
        elif self.clase == ClasePersonaje.MAGO:
            return 40
        elif self.clase == ClasePersonaje.ARQUERO:
            return 38
        elif self.clase == ClasePersonaje.PALADIN:
            return 32
        elif self.clase == ClasePersonaje.ASESINO:
            return 42
        return 35
    
    def _obtener_defensa_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 30
        elif self.clase == ClasePersonaje.MAGO:
            return 15
        elif self.clase == ClasePersonaje.ARQUERO:
            return 18
        elif self.clase == ClasePersonaje.PALADIN:
            return 25
        elif self.clase == ClasePersonaje.ASESINO:
            return 12
        return 20
    
    def _obtener_energia_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 150
        elif self.clase == ClasePersonaje.MAGO:
            return 180
        elif self.clase == ClasePersonaje.ARQUERO:
            return 160
        elif self.clase == ClasePersonaje.PALADIN:
            return 150
        elif self.clase == ClasePersonaje.ASESINO:
            return 200
        return 150
    
    def _obtener_habilidades_jefe(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return [
                {"nombre": "Espadazo Brutal", "daño": 1.8, "energia": 30, "descripcion": "Ataque devastador con espada"},
                {"nombre": "Grito de Guerra", "daño": 1.2, "energia": 25, "descripcion": "Aumenta ataque y defensa"},
                {"nombre": "Furia Legendaria", "daño": 3.0, "energia": 80, "descripcion": "Ataque épico del guerrero"}
            ]
        elif self.clase == ClasePersonaje.MAGO:
            return [
                {"nombre": "Tormenta de Fuego", "daño": 2.2, "energia": 50, "descripcion": "Invoca una tormenta de fuego"},
                {"nombre": "Rayo Mortal", "daño": 2.5, "energia": 60, "descripcion": "Rayo que siempre paraliza"},
                {"nombre": "Apocalipsis", "daño": 4.0, "energia": 100, "descripcion": "Hechizo destructivo final"}
            ]
        elif self.clase == ClasePersonaje.ARQUERO:
            return [
                {"nombre": "Flecha Mortal", "daño": 1.8, "energia": 25, "descripcion": "Flecha que nunca falla"},
                {"nombre": "Tormenta de Flechas", "daño": 2.2, "energia": 45, "descripcion": "Lluvia devastadora de flechas"},
                {"nombre": "Flecha del Destino", "daño": 3.2, "energia": 70, "descripcion": "Flecha que busca el corazón"}
            ]
        elif self.clase == ClasePersonaje.PALADIN:
            return [
                {"nombre": "Golpe Divino", "daño": 2.0, "energia": 35, "descripcion": "Ataque bendecido por los dioses"},
                {"nombre": "Curación Mayor", "daño": -1.5, "energia": 50, "descripcion": "Curación masiva"},
                {"nombre": "Escudo Sagrado", "daño": 1.0, "energia": 60, "descripcion": "Protección divina absoluta"}
            ]
        elif self.clase == ClasePersonaje.ASESINO:
            return [
                {"nombre": "Puñalada Mortal", "daño": 2.5, "energia": 30, "descripcion": "Ataque letal con puñal"},
                {"nombre": "Golpe Crítico Perfecto", "daño": 4.0, "energia": 70, "descripcion": "Crítico devastador"},
                {"nombre": "Sombra Eterna", "daño": 2.8, "energia": 50, "descripcion": "Ataque desde las sombras profundas"}
            ]
        return [] 