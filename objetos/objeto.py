from enum import Enum

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