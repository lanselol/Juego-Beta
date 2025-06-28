from clases.personaje import ClasePersonaje

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