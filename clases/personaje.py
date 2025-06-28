import pygame
import random
from enum import Enum

class ClasePersonaje(Enum):
    GUERRERO = "Guerrero"
    MAGO = "Mago"
    ARQUERO = "Arquero"
    PALADIN = "Paladín"
    ASESINO = "Asesino"

class Personaje:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.nivel = 1
        self.vida_maxima = self._obtener_vida_base()
        self.vida_actual = self.vida_maxima
        self.ataque = self._obtener_ataque_base()
        self.defensa = self._obtener_defensa_base()
        self.energia = self._obtener_energia_base()
        self.energia_actual = self.energia
        self.habilidades = self._obtener_habilidades()
        self.estado = "Normal"
        self.turnos_estado = 0
        self.es_jefe = False
        
        # Sistema de objetos y efectos
        self.bolsa_objetos = []
        self.efectos_temporales = []
        self.ataque_base = self.ataque
        self.defensa_base = self.defensa
        self.veneno_activo = 0
        self.velocidad_extra = False
        
        # Sistema de mejoras de habilidades
        self.mejoras_aplicadas = []
        self.probabilidad_critico_extra = 0.0
        
        # Agregar objetos iniciales según la clase
        self._agregar_objetos_iniciales()
        
    def _agregar_objetos_iniciales(self):
        # Cada clase comienza con una poción de vida y una de energía
        from objetos.objeto import Objeto, TipoObjeto
        
        pocion_vida = Objeto(TipoObjeto.POCION_VIDA, 50, "Restaura 50 puntos de vida", {"vida": 50})
        pocion_energia = Objeto(TipoObjeto.POCION_ENERGIA, 40, "Restaura 40 puntos de energía", {"energia": 40})
        
        self.agregar_objeto(pocion_vida)
        self.agregar_objeto(pocion_energia)
    
    def obtener_modificador_clase(self, objetivo):
        """Retorna el modificador de daño basado en las fortalezas y debilidades entre clases"""
        fortalezas = {
            ClasePersonaje.GUERRERO: ClasePersonaje.ASESINO,  # Guerrero es fuerte contra Asesino
            ClasePersonaje.MAGO: ClasePersonaje.GUERRERO,     # Mago es fuerte contra Guerrero
            ClasePersonaje.ARQUERO: ClasePersonaje.MAGO,      # Arquero es fuerte contra Mago
            ClasePersonaje.PALADIN: ClasePersonaje.ARQUERO,   # Paladín es fuerte contra Arquero
            ClasePersonaje.ASESINO: ClasePersonaje.PALADIN    # Asesino es fuerte contra Paladín
        }
        
        debilidades = {
            ClasePersonaje.GUERRERO: ClasePersonaje.MAGO,     # Guerrero es débil contra Mago
            ClasePersonaje.MAGO: ClasePersonaje.ARQUERO,      # Mago es débil contra Arquero
            ClasePersonaje.ARQUERO: ClasePersonaje.PALADIN,   # Arquero es débil contra Paladín
            ClasePersonaje.PALADIN: ClasePersonaje.ASESINO,   # Paladín es débil contra Asesino
            ClasePersonaje.ASESINO: ClasePersonaje.GUERRERO   # Asesino es débil contra Guerrero
        }
        
        if fortalezas.get(self.clase) == objetivo.clase:
            return 1.5  # 50% más de daño (fortaleza)
        elif debilidades.get(self.clase) == objetivo.clase:
            return 0.7  # 30% menos de daño (debilidad)
        else:
            return 1.0  # Daño normal
    
    def aplicar_mejora_habilidad(self, mejora):
        if mejora["mejora"] == "daño":
            if mejora["habilidad"] >= 0 and mejora["habilidad"] < len(self.habilidades):
                self.habilidades[mejora["habilidad"]]["daño"] += mejora["valor"]
        elif mejora["mejora"] == "energia":
            if mejora["habilidad"] >= 0 and mejora["habilidad"] < len(self.habilidades):
                self.habilidades[mejora["habilidad"]]["energia"] += mejora["valor"]
        elif mejora["mejora"] == "probabilidad":
            if mejora["habilidad"] >= 0 and mejora["habilidad"] < len(self.habilidades):
                self.probabilidad_critico_extra += mejora["valor"]
        elif mejora["mejora"] == "nueva":
            self.habilidades.append(mejora["valor"])
        
        self.mejoras_aplicadas.append(mejora["nombre"])
        return f"Habilidad mejorada: {mejora['nombre']}"
    
    def agregar_objeto(self, objeto):
        # Buscar si ya existe el objeto en la bolsa
        for obj in self.bolsa_objetos:
            if obj.tipo == objeto.tipo:
                obj.cantidad += 1
                return
        # Si no existe, agregarlo
        self.bolsa_objetos.append(objeto)
    
    def usar_objeto(self, indice_objeto, objetivo=None):
        if indice_objeto >= len(self.bolsa_objetos):
            return f"No hay objeto en la posición {indice_objeto + 1}"
        
        objeto = self.bolsa_objetos[indice_objeto]
        
        if objeto.tipo.value == "Poción de Vida":
            curacion = objeto.efecto["vida"]
            self.vida_actual = min(self.vida_maxima, self.vida_actual + curacion)
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y se cura {curacion} puntos de vida"
        
        elif objeto.tipo.value == "Poción de Energía":
            energia = objeto.efecto["energia"]
            self.energia_actual = min(self.energia, self.energia_actual + energia)
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y recupera {energia} puntos de energía"
        
        elif objeto.tipo.value == "Elixir de Fuerza":
            self.ataque = self.ataque_base + objeto.efecto["ataque"]
            self.efectos_temporales.append({
                "tipo": "ataque",
                "duracion": objeto.efecto["duracion"],
                "valor": objeto.efecto["ataque"]
            })
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y aumenta su ataque por {objeto.efecto['duracion']} turnos"
        
        elif objeto.tipo.value == "Elixir de Velocidad":
            self.velocidad_extra = True
            self.efectos_temporales.append({
                "tipo": "velocidad",
                "duracion": objeto.efecto["duracion"]
            })
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y obtiene velocidad extra por {objeto.efecto['duracion']} turnos"
        
        elif objeto.tipo.value == "Escudo Temporal":
            self.defensa = self.defensa_base + objeto.efecto["defensa"]
            self.efectos_temporales.append({
                "tipo": "defensa",
                "duracion": objeto.efecto["duracion"],
                "valor": objeto.efecto["defensa"]
            })
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y aumenta su defensa por {objeto.efecto['duracion']} turnos"
        
        elif objeto.tipo.value == "Bomba de Veneno":
            if objetivo:
                objetivo.veneno_activo = objeto.efecto["veneno"]
                objetivo.efectos_temporales.append({
                    "tipo": "veneno",
                    "duracion": objeto.efecto["duracion"],
                    "valor": objeto.efecto["veneno"]
                })
                self._remover_objeto(indice_objeto)
                return f"{self.nombre} usa {objeto.tipo.value} en {objetivo.nombre} causando veneno por {objeto.efecto['duracion']} turnos"
            else:
                return f"Necesitas seleccionar un objetivo para usar {objeto.tipo.value}"
    
    def _remover_objeto(self, indice):
        objeto = self.bolsa_objetos[indice]
        if objeto.cantidad > 1:
            objeto.cantidad -= 1
        else:
            self.bolsa_objetos.pop(indice)
    
    def actualizar_efectos(self):
        # Aplicar daño por veneno
        if self.veneno_activo > 0:
            self.vida_actual = max(0, self.vida_actual - self.veneno_activo)
        
        # Actualizar efectos temporales
        efectos_a_remover = []
        for efecto in self.efectos_temporales:
            efecto["duracion"] -= 1
            if efecto["duracion"] <= 0:
                efectos_a_remover.append(efecto)
        
        # Remover efectos expirados
        for efecto in efectos_a_remover:
            if efecto["tipo"] == "ataque":
                self.ataque = self.ataque_base
            elif efecto["tipo"] == "defensa":
                self.defensa = self.defensa_base
            elif efecto["tipo"] == "velocidad":
                self.velocidad_extra = False
            elif efecto["tipo"] == "veneno":
                self.veneno_activo = 0
            self.efectos_temporales.remove(efecto)
        
    def _obtener_vida_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 120
        elif self.clase == ClasePersonaje.MAGO:
            return 80
        elif self.clase == ClasePersonaje.ARQUERO:
            return 90
        elif self.clase == ClasePersonaje.PALADIN:
            return 110
        elif self.clase == ClasePersonaje.ASESINO:
            return 85
        return 100
    
    def _obtener_ataque_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 25
        elif self.clase == ClasePersonaje.MAGO:
            return 30
        elif self.clase == ClasePersonaje.ARQUERO:
            return 28
        elif self.clase == ClasePersonaje.PALADIN:
            return 22
        elif self.clase == ClasePersonaje.ASESINO:
            return 32
        return 25
    
    def _obtener_defensa_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 20
        elif self.clase == ClasePersonaje.MAGO:
            return 10
        elif self.clase == ClasePersonaje.ARQUERO:
            return 12
        elif self.clase == ClasePersonaje.PALADIN:
            return 18
        elif self.clase == ClasePersonaje.ASESINO:
            return 8
        return 15
    
    def _obtener_energia_base(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return 100
        elif self.clase == ClasePersonaje.MAGO:
            return 120
        elif self.clase == ClasePersonaje.ARQUERO:
            return 110
        elif self.clase == ClasePersonaje.PALADIN:
            return 100
        elif self.clase == ClasePersonaje.ASESINO:
            return 130
        return 100
    
    def _obtener_habilidades(self):
        if self.clase == ClasePersonaje.GUERRERO:
            return [
                {"nombre": "Espadazo", "daño": 1.2, "energia": 20, "descripcion": "Ataque básico con espada"},
                {"nombre": "Golpe Defensivo", "daño": 0.8, "energia": 15, "descripcion": "Ataque que aumenta defensa"},
                {"nombre": "Furia Berserker", "daño": 2.0, "energia": 50, "descripcion": "Ataque devastador"}
            ]
        elif self.clase == ClasePersonaje.MAGO:
            return [
                {"nombre": "Bola de Fuego", "daño": 1.5, "energia": 30, "descripcion": "Lanza una bola de fuego"},
                {"nombre": "Rayo Eléctrico", "daño": 1.8, "energia": 40, "descripcion": "Rayo que puede paralizar"},
                {"nombre": "Meteorito", "daño": 2.5, "energia": 70, "descripcion": "Invoca un meteorito"}
            ]
        elif self.clase == ClasePersonaje.ARQUERO:
            return [
                {"nombre": "Flecha Rápida", "daño": 1.1, "energia": 15, "descripcion": "Dispara una flecha rápida"},
                {"nombre": "Lluvia de Flechas", "daño": 1.6, "energia": 35, "descripcion": "Múltiples flechas"},
                {"nombre": "Flecha Venenosa", "daño": 1.3, "energia": 25, "descripcion": "Flecha con veneno"}
            ]
        elif self.clase == ClasePersonaje.PALADIN:
            return [
                {"nombre": "Golpe Sagrado", "daño": 1.3, "energia": 25, "descripcion": "Ataque bendecido"},
                {"nombre": "Curación", "daño": -0.8, "energia": 30, "descripcion": "Se cura a sí mismo"},
                {"nombre": "Escudo Divino", "daño": 0.5, "energia": 40, "descripcion": "Aumenta defensa temporalmente"}
            ]
        elif self.clase == ClasePersonaje.ASESINO:
            return [
                {"nombre": "Puñalada", "daño": 1.4, "energia": 20, "descripcion": "Ataque rápido con puñal"},
                {"nombre": "Golpe Crítico", "daño": 2.2, "energia": 45, "descripcion": "Alto daño crítico"},
                {"nombre": "Invisibilidad", "daño": 1.0, "energia": 35, "descripcion": "Ataque desde las sombras"}
            ]
        return []
    
    def usar_habilidad(self, habilidad, objetivo):
        if self.energia_actual < habilidad["energia"]:
            return f"{self.nombre} no tiene suficiente energía para usar {habilidad['nombre']}"
        
        self.energia_actual -= habilidad["energia"]
        
        # Calcular daño
        daño_base = self.ataque * habilidad["daño"]
        
        # Aplicar modificador de fortaleza/debilidad entre clases
        modificador_clase = self.obtener_modificador_clase(objetivo)
        daño_base *= modificador_clase
        
        # Modificadores por clase
        if self.clase == ClasePersonaje.ASESINO and random.random() < (0.3 + self.probabilidad_critico_extra):
            daño_base *= 1.5  # 30% + mejoras de probabilidad de crítico
        elif self.clase == ClasePersonaje.MAGO and random.random() < (0.2 + self.probabilidad_critico_extra):
            daño_base *= 1.3  # 20% + mejoras de probabilidad de crítico
        
        # Aplicar defensa del objetivo
        daño_final = max(1, daño_base - objetivo.defensa)
        
        if habilidad["daño"] < 0:  # Habilidad de curación
            curacion = abs(daño_final)
            self.vida_actual = min(self.vida_maxima, self.vida_actual + curacion)
            return f"{self.nombre} se cura {curacion} puntos de vida"
        else:
            objetivo.vida_actual = max(0, objetivo.vida_actual - daño_final)
            
            # Efectos especiales
            if self.clase == ClasePersonaje.MAGO and "Rayo" in habilidad["nombre"]:
                if random.random() < 0.3:
                    objetivo.estado = "Paralizado"
                    objetivo.turnos_estado = 2
            
            # Mensaje con información de fortaleza/debilidad
            mensaje_base = f"{self.nombre} usa {habilidad['nombre']} y causa {round(daño_final)} de daño a {objetivo.nombre}"
            
            if modificador_clase > 1.0:
                mensaje_base += " (¡Fortaleza!)"
            elif modificador_clase < 1.0:
                mensaje_base += " (Debilidad)"
            
            return mensaje_base
    
    def recuperar_energia(self):
        recuperacion = self.energia // 10
        self.energia_actual = min(self.energia, self.energia_actual + recuperacion)
    
    def actualizar_estado(self):
        if self.estado == "Paralizado" and self.turnos_estado > 0:
            self.turnos_estado -= 1
            if self.turnos_estado == 0:
                self.estado = "Normal"
        
        # Actualizar efectos temporales
        self.actualizar_efectos() 