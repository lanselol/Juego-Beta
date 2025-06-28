import pygame
import random
import sys
from enum import Enum

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO = 1200
ALTO = 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Fantasy Battle - Juego de Peleas por Turnos")

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

class TipoObjeto(Enum):
    POCION_VIDA = "Poción de Vida"
    POCION_ENERGIA = "Poción de Energía"
    ELIXIR_FUERZA = "Elixir de Fuerza"
    ELIXIR_VELOCIDAD = "Elixir de Velocidad"
    ESCUDO_TEMPORAL = "Escudo Temporal"
    BOMBA_VENENO = "Bomba de Veneno"

class Objeto:
    def __init__(self, tipo, precio, descripcion, efecto):
        self.tipo = tipo
        self.precio = precio
        self.descripcion = descripcion
        self.efecto = efecto
        self.cantidad = 1

class Tienda:
    def __init__(self):
        self.objetos_disponibles = [
            Objeto(TipoObjeto.POCION_VIDA, 50, "Restaura 50 puntos de vida", {"vida": 50}),
            Objeto(TipoObjeto.POCION_ENERGIA, 40, "Restaura 40 puntos de energía", {"energia": 40}),
            Objeto(TipoObjeto.ELIXIR_FUERZA, 80, "Aumenta el ataque en 10 por 3 turnos", {"ataque": 10, "duracion": 3}),
            Objeto(TipoObjeto.ELIXIR_VELOCIDAD, 70, "Aumenta la velocidad de ataque por 2 turnos", {"velocidad": True, "duracion": 2}),
            Objeto(TipoObjeto.ESCUDO_TEMPORAL, 60, "Aumenta la defensa en 15 por 2 turnos", {"defensa": 15, "duracion": 2}),
            Objeto(TipoObjeto.BOMBA_VENENO, 100, "Causa 30 daño por veneno por 3 turnos", {"veneno": 30, "duracion": 3})
        ]

class MaestroHabilidades:
    def __init__(self):
        self.mejoras_disponibles = {
            ClasePersonaje.GUERRERO: [
                {"nombre": "Mejorar Espadazo", "descripcion": "Aumenta daño de Espadazo en 0.3", "precio": 100, "habilidad": 0, "mejora": "daño", "valor": 0.3},
                {"nombre": "Mejorar Golpe Defensivo", "descripcion": "Reduce energía de Golpe Defensivo en 5", "precio": 120, "habilidad": 1, "mejora": "energia", "valor": -5},
                {"nombre": "Mejorar Furia Berserker", "descripcion": "Aumenta daño de Furia Berserker en 0.5", "precio": 200, "habilidad": 2, "mejora": "daño", "valor": 0.5},
                {"nombre": "Aprender Golpe Crítico", "descripcion": "Nueva habilidad: 25% probabilidad de crítico", "precio": 300, "habilidad": -1, "mejora": "nueva", "valor": {"nombre": "Golpe Crítico", "daño": 1.8, "energia": 35, "descripcion": "Ataque con probabilidad de crítico"}}
            ],
            ClasePersonaje.MAGO: [
                {"nombre": "Mejorar Bola de Fuego", "descripcion": "Aumenta daño de Bola de Fuego en 0.4", "precio": 100, "habilidad": 0, "mejora": "daño", "valor": 0.4},
                {"nombre": "Mejorar Rayo Eléctrico", "descripcion": "Aumenta probabilidad de paralizar en 10%", "precio": 150, "habilidad": 1, "mejora": "probabilidad", "valor": 0.1},
                {"nombre": "Mejorar Meteorito", "descripcion": "Reduce energía de Meteorito en 10", "precio": 200, "habilidad": 2, "mejora": "energia", "valor": -10},
                {"nombre": "Aprender Tormenta de Hielo", "descripcion": "Nueva habilidad: Congela al enemigo", "precio": 300, "habilidad": -1, "mejora": "nueva", "valor": {"nombre": "Tormenta de Hielo", "daño": 2.0, "energia": 50, "descripcion": "Congela al enemigo por 1 turno"}}
            ],
            ClasePersonaje.ARQUERO: [
                {"nombre": "Mejorar Flecha Rápida", "descripcion": "Reduce energía de Flecha Rápida en 3", "precio": 80, "habilidad": 0, "mejora": "energia", "valor": -3},
                {"nombre": "Mejorar Lluvia de Flechas", "descripcion": "Aumenta daño de Lluvia de Flechas en 0.3", "precio": 120, "habilidad": 1, "mejora": "daño", "valor": 0.3},
                {"nombre": "Mejorar Flecha Venenosa", "descripcion": "Aumenta daño de Flecha Venenosa en 0.2", "precio": 100, "habilidad": 2, "mejora": "daño", "valor": 0.2},
                {"nombre": "Aprender Flecha Explosiva", "descripcion": "Nueva habilidad: Daño en área", "precio": 250, "habilidad": -1, "mejora": "nueva", "valor": {"nombre": "Flecha Explosiva", "daño": 1.9, "energia": 45, "descripcion": "Flecha que explota causando daño extra"}}
            ],
            ClasePersonaje.PALADIN: [
                {"nombre": "Mejorar Golpe Sagrado", "descripcion": "Aumenta daño de Golpe Sagrado en 0.3", "precio": 100, "habilidad": 0, "mejora": "daño", "valor": 0.3},
                {"nombre": "Mejorar Curación", "descripcion": "Aumenta curación en 0.2", "precio": 120, "habilidad": 1, "mejora": "daño", "valor": -0.2},
                {"nombre": "Mejorar Escudo Divino", "descripcion": "Reduce energía de Escudo Divino en 5", "precio": 100, "habilidad": 2, "mejora": "energia", "valor": -5},
                {"nombre": "Aprender Bendición", "descripcion": "Nueva habilidad: Curación masiva", "precio": 300, "habilidad": -1, "mejora": "nueva", "valor": {"nombre": "Bendición", "daño": -1.2, "energia": 60, "descripcion": "Curación masiva y protección"}}
            ],
            ClasePersonaje.ASESINO: [
                {"nombre": "Mejorar Puñalada", "descripcion": "Aumenta probabilidad de crítico en 5%", "precio": 120, "habilidad": 0, "mejora": "probabilidad", "valor": 0.05},
                {"nombre": "Mejorar Golpe Crítico", "descripcion": "Aumenta daño de Golpe Crítico en 0.4", "precio": 150, "habilidad": 1, "mejora": "daño", "valor": 0.4},
                {"nombre": "Mejorar Invisibilidad", "descripcion": "Reduce energía de Invisibilidad en 5", "precio": 100, "habilidad": 2, "mejora": "energia", "valor": -5},
                {"nombre": "Aprender Golpe Mortal", "descripcion": "Nueva habilidad: Daño crítico garantizado", "precio": 350, "habilidad": -1, "mejora": "nueva", "valor": {"nombre": "Golpe Mortal", "daño": 3.0, "energia": 80, "descripcion": "Golpe crítico devastador"}}
            ]
        }

class ClasePersonaje(Enum):
    GUERRERO = "Guerrero"
    MAGO = "Mago"
    ARQUERO = "Arquero"
    PALADIN = "Paladín"
    ASESINO = "Asesino"

class Jefe:
    def __init__(self, nombre, clase, piso):
        self.nombre = nombre
        self.clase = clase
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
        self.estado = "Normal"
        self.turnos_estado = 0
        
        # Sistema de objetos y efectos (para jefes)
        self.bolsa_objetos = []
        self.efectos_temporales = []
        self.ataque_base = self.ataque
        self.defensa_base = self.defensa
        self.veneno_activo = 0
        self.velocidad_extra = False
        
        # Sistema de mejoras de habilidades (para jefes)
        self.mejoras_aplicadas = []
        self.probabilidad_critico_extra = 0.0
        
        # Agregar objetos iniciales para jefes
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
        
        if objeto.tipo == TipoObjeto.POCION_VIDA:
            curacion = objeto.efecto["vida"]
            self.vida_actual = min(self.vida_maxima, self.vida_actual + curacion)
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y se cura {curacion} puntos de vida"
        
        elif objeto.tipo == TipoObjeto.POCION_ENERGIA:
            energia = objeto.efecto["energia"]
            self.energia_actual = min(self.energia, self.energia_actual + energia)
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y recupera {energia} puntos de energía"
        
        elif objeto.tipo == TipoObjeto.ELIXIR_FUERZA:
            self.ataque = self.ataque_base + objeto.efecto["ataque"]
            self.efectos_temporales.append({
                "tipo": "ataque",
                "duracion": objeto.efecto["duracion"],
                "valor": objeto.efecto["ataque"]
            })
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y aumenta su ataque por {objeto.efecto['duracion']} turnos"
        
        elif objeto.tipo == TipoObjeto.ELIXIR_VELOCIDAD:
            self.velocidad_extra = True
            self.efectos_temporales.append({
                "tipo": "velocidad",
                "duracion": objeto.efecto["duracion"]
            })
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y obtiene velocidad extra por {objeto.efecto['duracion']} turnos"
        
        elif objeto.tipo == TipoObjeto.ESCUDO_TEMPORAL:
            self.defensa = self.defensa_base + objeto.efecto["defensa"]
            self.efectos_temporales.append({
                "tipo": "defensa",
                "duracion": objeto.efecto["duracion"],
                "valor": objeto.efecto["defensa"]
            })
            self._remover_objeto(indice_objeto)
            return f"{self.nombre} usa {objeto.tipo.value} y aumenta su defensa por {objeto.efecto['duracion']} turnos"
        
        elif objeto.tipo == TipoObjeto.BOMBA_VENENO:
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

class Juego:
    def __init__(self):
        self.jugador = None
        self.enemigo = None
        self.estado = "seleccion_clase"
        self.turno = "jugador"
        self.mensaje = ""
        self.habilidad_seleccionada = 0
        self.piso_actual = 1
        self.jefes_derrotados = []
        self.jefes_disponibles = self._crear_jefes()
        
        # Sistema de economía y objetos
        self.monedas_oro = 0
        self.tienda = Tienda()
        self.estado_tienda = False
        self.objeto_seleccionado_tienda = 0
        self.objeto_seleccionado_bolsa = 0
        
        # Sistema de maestro de habilidades
        self.maestro_habilidades = MaestroHabilidades()
        self.estado_maestro = False
        self.mejora_seleccionada = 0
        self.jefe_derrotado_reciente = False
        
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
    
    def dar_recompensa_oro(self):
        # Recompensa base por piso
        oro_base = 10 + (self.piso_actual * 2)
        
        # Bonus por jefe
        if self.enemigo.es_jefe:
            oro_base *= 3
        
        self.monedas_oro += oro_base
        return oro_base
    
    def comprar_objeto(self, indice):
        if indice >= len(self.tienda.objetos_disponibles):
            return "Objeto no disponible"
        
        objeto = self.tienda.objetos_disponibles[indice]
        
        if self.monedas_oro >= objeto.precio:
            self.monedas_oro -= objeto.precio
            # Crear una copia del objeto para el jugador
            objeto_copia = Objeto(objeto.tipo, objeto.precio, objeto.descripcion, objeto.efecto)
            self.jugador.agregar_objeto(objeto_copia)
            return f"Compraste {objeto.tipo.value} por {objeto.precio} monedas de oro"
        else:
            return f"No tienes suficientes monedas. Necesitas {objeto.precio} pero tienes {self.monedas_oro}"
    
    def comprar_mejora_habilidad(self, indice):
        if not self.jugador:
            return "No hay jugador"
        
        mejoras = self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, [])
        if indice >= len(mejoras):
            return "Mejora no disponible"
        
        mejora = mejoras[indice]
        
        # Verificar si ya se aplicó esta mejora
        if mejora["nombre"] in self.jugador.mejoras_aplicadas:
            return f"Ya tienes la mejora: {mejora['nombre']}"
        
        if self.monedas_oro >= mejora["precio"]:
            self.monedas_oro -= mejora["precio"]
            resultado = self.jugador.aplicar_mejora_habilidad(mejora)
            return f"{resultado} por {mejora['precio']} monedas de oro"
        else:
            return f"No tienes suficientes monedas. Necesitas {mejora['precio']} pero tienes {self.monedas_oro}"
    
    def crear_enemigo(self):
        # Verificar si es un piso de jefe (múltiplo de 10)
        if self.piso_actual % 10 == 0:
            return self._crear_jefe()
        else:
            return self._crear_enemigo_normal()
    
    def _crear_jefe(self):
        # Seleccionar un jefe aleatorio que no haya sido derrotado
        jefes_disponibles = [j for j in self.jefes_disponibles if j[0] not in self.jefes_derrotados]
        if not jefes_disponibles:
            # Si todos los jefes han sido derrotados, reiniciar
            self.jefes_derrotados = []
            jefes_disponibles = self.jefes_disponibles
        
        nombre_jefe, clase_jefe = random.choice(jefes_disponibles)
        return Jefe(nombre_jefe, clase_jefe, self.piso_actual)
    
    def _crear_enemigo_normal(self):
        clases = list(ClasePersonaje)
        clase_enemigo = random.choice(clases)
        
        # Multiplicador de dificultad basado en el piso
        multiplicador = 1 + (self.piso_actual - 1) * 0.1
        
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
    
    def dibujar_interfaz(self):
        ventana.fill(NEGRO)
        
        if self.estado == "seleccion_clase":
            self.dibujar_seleccion_clase()
        elif self.estado == "batalla":
            if self.estado_tienda:
                self.dibujar_tienda()
            elif self.estado_maestro:
                self.dibujar_maestro_habilidades()
            else:
                self.dibujar_batalla()
        
        pygame.display.flip()
    
    def dibujar_seleccion_clase(self):
        # Título
        titulo = fuente_grande.render("FANTASY BATTLE", True, DORADO)
        ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 50))
        
        subtitulo = fuente_mediana.render("Selecciona tu clase de héroe", True, BLANCO)
        ventana.blit(subtitulo, (ANCHO//2 - subtitulo.get_width()//2, 120))
        
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
            pygame.draw.rect(ventana, color, rect, 3)
            
            texto = fuente_mediana.render(nombre, True, color)
            ventana.blit(texto, (120, y + 10))
            
            desc_texto = fuente_pequena.render(desc, True, BLANCO)
            ventana.blit(desc_texto, (120, y + 35))
        
        # Instrucciones
        instrucciones = fuente_pequena.render("Presiona 1-5 para seleccionar tu clase", True, AMARILLO)
        ventana.blit(instrucciones, (ANCHO//2 - instrucciones.get_width()//2, 650))
    
    def dibujar_tienda(self):
        # Fondo de tienda
        pygame.draw.rect(ventana, (40, 20, 60), (0, 0, ANCHO, ALTO))
        
        # Título de la tienda
        titulo = fuente_grande.render("TIENDA", True, DORADO)
        ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 20))
        
        # Información del jugador
        oro_texto = fuente_mediana.render(f"Monedas de Oro: {self.monedas_oro}", True, DORADO)
        ventana.blit(oro_texto, (50, 80))
        
        piso_texto = fuente_mediana.render(f"Piso {self.piso_actual}", True, BLANCO)
        ventana.blit(piso_texto, (ANCHO - 200, 80))
        
        # Objetos disponibles
        for i, objeto in enumerate(self.tienda.objetos_disponibles):
            y = 150 + i * 80
            color = DORADO if i == self.objeto_seleccionado_tienda else BLANCO
            
            # Marco del objeto
            if i == self.objeto_seleccionado_tienda:
                pygame.draw.rect(ventana, DORADO, (50, y - 5, 500, 70), 3)
            
            # Nombre y precio
            nombre_texto = fuente_mediana.render(f"{objeto.tipo.value} - {objeto.precio} oro", True, color)
            ventana.blit(nombre_texto, (60, y))
            
            # Descripción
            desc_texto = fuente_pequena.render(objeto.descripcion, True, BLANCO)
            ventana.blit(desc_texto, (60, y + 30))
        
        # Instrucciones
        instrucciones = fuente_pequena.render("Flechas para navegar | Enter para comprar | T para salir", True, AMARILLO)
        ventana.blit(instrucciones, (ANCHO//2 - instrucciones.get_width()//2, 650))
    
    def dibujar_maestro_habilidades(self):
        # Fondo del maestro
        pygame.draw.rect(ventana, (60, 20, 40), (0, 0, ANCHO, ALTO))
        
        # Título del maestro
        titulo = fuente_grande.render("MAESTRO DE HABILIDADES", True, DORADO)
        ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 20))
        
        # Información del jugador
        oro_texto = fuente_mediana.render(f"Monedas de Oro: {self.monedas_oro}", True, DORADO)
        ventana.blit(oro_texto, (50, 80))
        
        piso_texto = fuente_mediana.render(f"Piso {self.piso_actual}", True, BLANCO)
        ventana.blit(piso_texto, (ANCHO - 200, 80))
        
        clase_texto = fuente_mediana.render(f"Clase: {self.jugador.clase.value}", True, AZUL)
        ventana.blit(clase_texto, (ANCHO//2 - clase_texto.get_width()//2, 80))
        
        # Mejoras disponibles
        mejoras = self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, [])
        
        for i, mejora in enumerate(mejoras):
            y = 150 + i * 80
            color = DORADO if i == self.mejora_seleccionada else BLANCO
            
            # Verificar si ya se aplicó esta mejora
            if mejora["nombre"] in self.jugador.mejoras_aplicadas:
                color = VERDE
            
            # Marco de la mejora
            if i == self.mejora_seleccionada:
                pygame.draw.rect(ventana, DORADO, (50, y - 5, 500, 70), 3)
            
            # Nombre y precio
            nombre_texto = fuente_mediana.render(f"{mejora['nombre']} - {mejora['precio']} oro", True, color)
            ventana.blit(nombre_texto, (60, y))
            
            # Descripción
            desc_texto = fuente_pequena.render(mejora['descripcion'], True, BLANCO)
            ventana.blit(desc_texto, (60, y + 30))
            
            # Indicador de ya comprada
            if mejora["nombre"] in self.jugador.mejoras_aplicadas:
                comprada_texto = fuente_pequena.render("✓ YA COMPRADA", True, VERDE)
                ventana.blit(comprada_texto, (60, y + 50))
        
        # Instrucciones
        instrucciones = fuente_pequena.render("Flechas para navegar | Enter para comprar | M para salir", True, AMARILLO)
        ventana.blit(instrucciones, (ANCHO//2 - instrucciones.get_width()//2, 650))
    
    def dibujar_batalla(self):
        # Fondo de batalla
        pygame.draw.rect(ventana, (20, 40, 20), (0, 0, ANCHO, ALTO))
        
        # Información del piso y oro
        piso_texto = fuente_mediana.render(f"Piso {self.piso_actual}", True, DORADO)
        ventana.blit(piso_texto, (ANCHO//2 - piso_texto.get_width()//2, 20))
        
        oro_texto = fuente_pequena.render(f"Oro: {self.monedas_oro}", True, DORADO)
        ventana.blit(oro_texto, (ANCHO - 150, 20))
        
        # Indicador de tienda disponible
        if self.piso_actual % 5 == 0:
            tienda_texto = fuente_pequena.render("¡Tienda disponible! (T)", True, VERDE)
            ventana.blit(tienda_texto, (ANCHO - 200, 50))
        
        # Indicador de maestro de habilidades disponible
        if self.jefe_derrotado_reciente:
            maestro_texto = fuente_pequena.render("¡Maestro de Habilidades disponible! (M)", True, AZUL)
            ventana.blit(maestro_texto, (ANCHO - 300, 80))
        
        # Indicador de jefe
        if self.piso_actual % 10 == 0:
            jefe_texto = fuente_mediana.render("¡JEFE!", True, ROSA)
            ventana.blit(jefe_texto, (ANCHO//2 - jefe_texto.get_width()//2, 50))
        
        # Información del jugador
        self.dibujar_personaje(self.jugador, 50, 100, VERDE)
        
        # Información del enemigo
        color_enemigo = ROSA if self.enemigo.es_jefe else ROJO
        self.dibujar_personaje(self.enemigo, ANCHO - 450, 100, color_enemigo)
        
        # Área de batalla central
        pygame.draw.rect(ventana, (40, 60, 40), (ANCHO//2 - 200, 300, 400, 200))
        
        # Mensaje de batalla
        if self.mensaje:
            mensaje_texto = fuente_pequena.render(self.mensaje, True, BLANCO)
            ventana.blit(mensaje_texto, (ANCHO//2 - mensaje_texto.get_width()//2, 320))
        
        # Turno actual
        turno_texto = fuente_mediana.render(f"Turno: {self.turno.title()}", True, AMARILLO)
        ventana.blit(turno_texto, (ANCHO//2 - turno_texto.get_width()//2, 350))
        
        # Habilidades del jugador
        if self.turno == "jugador":
            self.dibujar_habilidades()
            self.dibujar_bolsa_objetos()
        
        # Botones de acción
        if self.turno == "jugador":
            pygame.draw.rect(ventana, AZUL, (ANCHO//2 - 100, 500, 200, 40))
            descanso_texto = fuente_mediana.render("Descansar (R)", True, BLANCO)
            ventana.blit(descanso_texto, (ANCHO//2 - descanso_texto.get_width()//2, 510))
    
    def dibujar_bolsa_objetos(self):
        # Título de la bolsa
        bolsa_titulo = fuente_mediana.render("Bolsa de Objetos:", True, AMARILLO)
        ventana.blit(bolsa_titulo, (ANCHO - 450, 550))
        
        if not self.jugador.bolsa_objetos:
            sin_objetos = fuente_pequena.render("Sin objetos", True, GRIS)
            ventana.blit(sin_objetos, (ANCHO - 450, 590))
            return
        
        for i, objeto in enumerate(self.jugador.bolsa_objetos):
            y = 590 + i * 40
            color = DORADO if i == self.objeto_seleccionado_bolsa else BLANCO
            
            # Marco del objeto
            if i == self.objeto_seleccionado_bolsa:
                pygame.draw.rect(ventana, DORADO, (ANCHO - 460, y - 5, 400, 35), 2)
            
            # Nombre y cantidad
            nombre_texto = fuente_pequena.render(f"{i+1}. {objeto.tipo.value} (x{objeto.cantidad})", True, color)
            ventana.blit(nombre_texto, (ANCHO - 450, y))
    
    def dibujar_personaje(self, personaje, x, y, color):
        # Marco del personaje
        grosor = 5 if personaje.es_jefe else 3
        pygame.draw.rect(ventana, color, (x, y, 400, 200), grosor)
        
        # Nombre y clase
        nombre_texto = fuente_mediana.render(personaje.nombre, True, color)
        ventana.blit(nombre_texto, (x + 10, y + 10))
        
        clase_texto = fuente_pequena.render(f"Clase: {personaje.clase.value}", True, BLANCO)
        ventana.blit(clase_texto, (x + 10, y + 40))
        
        # Indicador de jefe
        if personaje.es_jefe:
            jefe_texto = fuente_pequena.render("JEFE", True, ROSA)
            ventana.blit(jefe_texto, (x + 10, y + 60))
        
        # Barra de vida
        y_vida = y + 70 if personaje.es_jefe else y + 70
        pygame.draw.rect(ventana, ROJO, (x + 10, y_vida, 380, 20))
        vida_porcentaje = personaje.vida_actual / personaje.vida_maxima
        pygame.draw.rect(ventana, VERDE, (x + 10, y_vida, 380 * vida_porcentaje, 20))
        vida_texto = fuente_pequena.render(f"Vida: {round(personaje.vida_actual)}/{round(personaje.vida_maxima)}", True, BLANCO)
        ventana.blit(vida_texto, (x + 10, y_vida + 25))
        
        # Barra de energía
        y_energia = y_vida + 45
        pygame.draw.rect(ventana, GRIS, (x + 10, y_energia, 380, 15))
        energia_porcentaje = personaje.energia_actual / personaje.energia
        pygame.draw.rect(ventana, AZUL, (x + 10, y_energia, 380 * energia_porcentaje, 15))
        energia_texto = fuente_pequena.render(f"Energía: {round(personaje.energia_actual)}/{round(personaje.energia)}", True, BLANCO)
        ventana.blit(energia_texto, (x + 10, y_energia + 20))
        
        # Estadísticas
        y_stats = y_energia + 40
        stats_texto = fuente_pequena.render(f"Ataque: {round(personaje.ataque)} | Defensa: {round(personaje.defensa)}", True, BLANCO)
        ventana.blit(stats_texto, (x + 10, y_stats))
        
        # Estado y efectos
        if personaje.estado != "Normal":
            estado_texto = fuente_pequena.render(f"Estado: {personaje.estado}", True, AMARILLO)
            ventana.blit(estado_texto, (x + 10, y_stats + 20))
        
        if personaje.veneno_activo > 0:
            veneno_texto = fuente_pequena.render(f"Veneno: {round(personaje.veneno_activo)}", True, VERDE)
            ventana.blit(veneno_texto, (x + 10, y_stats + 40))
        
        if personaje.velocidad_extra:
            velocidad_texto = fuente_pequena.render("Velocidad Extra", True, AZUL)
            ventana.blit(velocidad_texto, (x + 10, y_stats + 60))
        
        # Mostrar fortalezas y debilidades si es el jugador
        if hasattr(self, 'jugador') and hasattr(self, 'enemigo') and personaje == self.jugador:
            self.dibujar_fortalezas_debilidades(x, y)
    
    def dibujar_fortalezas_debilidades(self, x, y):
        """Dibuja información sobre fortalezas y debilidades del jugador contra el enemigo"""
        if not hasattr(self, 'jugador') or not hasattr(self, 'enemigo'):
            return
        
        fortalezas = {
            ClasePersonaje.GUERRERO: "Fuerte vs Asesino",
            ClasePersonaje.MAGO: "Fuerte vs Guerrero", 
            ClasePersonaje.ARQUERO: "Fuerte vs Mago",
            ClasePersonaje.PALADIN: "Fuerte vs Arquero",
            ClasePersonaje.ASESINO: "Fuerte vs Paladín"
        }
        
        debilidades = {
            ClasePersonaje.GUERRERO: "Débil vs Mago",
            ClasePersonaje.MAGO: "Débil vs Arquero",
            ClasePersonaje.ARQUERO: "Débil vs Paladín", 
            ClasePersonaje.PALADIN: "Débil vs Asesino",
            ClasePersonaje.ASESINO: "Débil vs Guerrero"
        }
        
        # Mostrar fortaleza
        fortaleza_texto = fuente_pequena.render(fortalezas.get(self.jugador.clase, ""), True, VERDE)
        ventana.blit(fortaleza_texto, (x + 10, y + 220))
        
        # Mostrar debilidad
        debilidad_texto = fuente_pequena.render(debilidades.get(self.jugador.clase, ""), True, ROJO)
        ventana.blit(debilidad_texto, (x + 10, y + 240))
        
        # Mostrar relación con el enemigo actual
        if self.enemigo:
            modificador = self.jugador.obtener_modificador_clase(self.enemigo)
            if modificador > 1.0:
                relacion_texto = fuente_pequena.render(f"¡Ventaja vs {self.enemigo.clase.value}!", True, VERDE)
                ventana.blit(relacion_texto, (x + 10, y + 260))
            elif modificador < 1.0:
                relacion_texto = fuente_pequena.render(f"Desventaja vs {self.enemigo.clase.value}", True, ROJO)
                ventana.blit(relacion_texto, (x + 10, y + 260))
    
    def dibujar_habilidades(self):
        # Título de habilidades
        habilidades_titulo = fuente_mediana.render("Habilidades:", True, AMARILLO)
        ventana.blit(habilidades_titulo, (50, 550))
        
        for i, habilidad in enumerate(self.jugador.habilidades):
            color = DORADO if i == self.habilidad_seleccionada else BLANCO
            y = 590 + i * 50
            
            # Marco de la habilidad
            if i == self.habilidad_seleccionada:
                pygame.draw.rect(ventana, DORADO, (50, y - 5, 500, 40), 2)
            
            # Nombre y descripción
            nombre_texto = fuente_pequena.render(f"{i+1}. {habilidad['nombre']}", True, color)
            ventana.blit(nombre_texto, (60, y))
            
            desc_texto = fuente_pequena.render(f"   {habilidad['descripcion']} (Energía: {habilidad['energia']})", True, BLANCO)
            ventana.blit(desc_texto, (60, y + 20))
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.KEYDOWN:
                if self.estado == "seleccion_clase":
                    self.manejar_seleccion_clase(evento.key)
                elif self.estado == "batalla":
                    if self.estado_tienda:
                        self.manejar_tienda(evento.key)
                    elif self.estado_maestro:
                        self.manejar_maestro(evento.key)
                    else:
                        self.manejar_batalla(evento.key)
        
        return True
    
    def manejar_seleccion_clase(self, tecla):
        clases = list(ClasePersonaje)
        if tecla == pygame.K_1 and len(clases) >= 1:
            self.jugador = Personaje("Héroe", clases[0])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_2 and len(clases) >= 2:
            self.jugador = Personaje("Héroe", clases[1])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_3 and len(clases) >= 3:
            self.jugador = Personaje("Héroe", clases[2])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_4 and len(clases) >= 4:
            self.jugador = Personaje("Héroe", clases[3])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
        elif tecla == pygame.K_5 and len(clases) >= 5:
            self.jugador = Personaje("Héroe", clases[4])
            self.enemigo = self.crear_enemigo()
            self.estado = "batalla"
    
    def manejar_tienda(self, tecla):
        if tecla == pygame.K_UP:
            self.objeto_seleccionado_tienda = (self.objeto_seleccionado_tienda - 1) % len(self.tienda.objetos_disponibles)
        elif tecla == pygame.K_DOWN:
            self.objeto_seleccionado_tienda = (self.objeto_seleccionado_tienda + 1) % len(self.tienda.objetos_disponibles)
        elif tecla == pygame.K_RETURN:
            self.mensaje = self.comprar_objeto(self.objeto_seleccionado_tienda)
        elif tecla == pygame.K_t:
            self.estado_tienda = False
            self.mensaje = "Tienda cerrada"
    
    def manejar_batalla(self, tecla):
        if self.turno == "jugador":
            if tecla == pygame.K_UP:
                self.habilidad_seleccionada = (self.habilidad_seleccionada - 1) % len(self.jugador.habilidades)
            elif tecla == pygame.K_DOWN:
                self.habilidad_seleccionada = (self.habilidad_seleccionada + 1) % len(self.jugador.habilidades)
            elif tecla == pygame.K_RETURN:
                self.ejecutar_turno_jugador()
            elif tecla == pygame.K_r:
                self.jugador.recuperar_energia()
                self.mensaje = f"{self.jugador.nombre} descansa y recupera energía"
                self.turno = "enemigo"
            elif tecla == pygame.K_t and self.piso_actual % 5 == 0:
                self.estado_tienda = True
                self.mensaje = "Tienda abierta"
            elif tecla == pygame.K_m and self.jefe_derrotado_reciente:
                self.estado_maestro = True
                self.mensaje = "Maestro de Habilidades abierto"
            elif tecla == pygame.K_o and self.jugador.bolsa_objetos:
                self.objeto_seleccionado_bolsa = (self.objeto_seleccionado_bolsa + 1) % len(self.jugador.bolsa_objetos)
            elif tecla == pygame.K_i and self.jugador.bolsa_objetos:
                self.usar_objeto_jugador()
    
    def manejar_maestro(self, tecla):
        if tecla == pygame.K_UP:
            self.mejora_seleccionada = (self.mejora_seleccionada - 1) % len(self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, []))
        elif tecla == pygame.K_DOWN:
            self.mejora_seleccionada = (self.mejora_seleccionada + 1) % len(self.maestro_habilidades.mejoras_disponibles.get(self.jugador.clase, []))
        elif tecla == pygame.K_RETURN:
            self.mensaje = self.comprar_mejora_habilidad(self.mejora_seleccionada)
        elif tecla == pygame.K_m:
            self.estado_maestro = False
            self.mensaje = "Maestro de Habilidades cerrado"
    
    def usar_objeto_jugador(self):
        if not self.jugador.bolsa_objetos:
            self.mensaje = "No tienes objetos para usar"
            return
        
        objeto = self.jugador.bolsa_objetos[self.objeto_seleccionado_bolsa]
        
        # Determinar objetivo para objetos que lo requieren
        objetivo = None
        if objeto.tipo == TipoObjeto.BOMBA_VENENO:
            objetivo = self.enemigo
        
        self.mensaje = self.jugador.usar_objeto(self.objeto_seleccionado_bolsa, objetivo)
        self.turno = "enemigo"
    
    def ejecutar_turno_jugador(self):
        if self.jugador.estado == "Paralizado":
            self.mensaje = f"{self.jugador.nombre} está paralizado y no puede atacar"
            self.turno = "enemigo"
            return
        
        habilidad = self.jugador.habilidades[self.habilidad_seleccionada]
        self.mensaje = self.jugador.usar_habilidad(habilidad, self.enemigo)
        self.turno = "enemigo"
        
        if self.enemigo.vida_actual <= 0:
            # Dar recompensa de oro
            oro_ganado = self.dar_recompensa_oro()
            
            if self.enemigo.es_jefe:
                self.jefes_derrotados.append(self.enemigo.nombre)
                self.mensaje = f"¡{self.jugador.nombre} ha derrotado al JEFE {self.enemigo.nombre}! +{oro_ganado} oro"
                self.jefe_derrotado_reciente = True  # Activar maestro de habilidades
            else:
                self.mensaje = f"¡{self.jugador.nombre} ha derrotado a {self.enemigo.nombre}! +{oro_ganado} oro"
            
            # Avanzar al siguiente piso
            self.piso_actual += 1
            self.enemigo = self.crear_enemigo()
            self.jugador.vida_actual = self.jugador.vida_maxima  # Curar al jugador
            self.jugador.energia_actual = self.jugador.energia   # Recuperar energía
    
    def ejecutar_turno_enemigo(self):
        if self.enemigo.estado == "Paralizado":
            self.mensaje = f"{self.enemigo.nombre} está paralizado y no puede atacar"
            self.turno = "jugador"
            return
        
        # IA simple del enemigo
        if self.enemigo.energia_actual < 20:
            self.enemigo.recuperar_energia()
            self.mensaje = f"{self.enemigo.nombre} descansa y recupera energía"
        else:
            # Seleccionar habilidad aleatoria
            habilidad = random.choice(self.enemigo.habilidades)
            self.mensaje = self.enemigo.usar_habilidad(habilidad, self.jugador)
        
        self.turno = "jugador"
        
        if self.jugador.vida_actual <= 0:
            self.mensaje = f"¡{self.enemigo.nombre} ha derrotado a {self.jugador.nombre}!"
            # Reiniciar al piso 1
            self.piso_actual = 1
            self.jefes_derrotados = []
            self.monedas_oro = 0  # Perder todo el oro
            self.estado = "seleccion_clase"
    
    def actualizar(self):
        if self.estado == "batalla" and self.turno == "enemigo":
            # Pequeño delay para el turno del enemigo
            pygame.time.wait(1000)
            self.ejecutar_turno_enemigo()
        
        # Actualizar estados de los personajes
        if self.jugador:
            self.jugador.actualizar_estado()
        if self.enemigo:
            self.enemigo.actualizar_estado()

def main():
    juego = Juego()
    reloj = pygame.time.Clock()
    
    ejecutando = True
    while ejecutando:
        ejecutando = juego.manejar_eventos()
        juego.actualizar()
        juego.dibujar_interfaz()
        reloj.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
