import json
import os
from enum import Enum
from typing import Dict, List, Optional

class TipoDecision(Enum):
    """Tipos de decisiones que puede tomar el jugador"""
    COMBATE = "combate"
    DIALOGO = "dialogo"
    EXPLORACION = "exploracion"
    MORAL = "moral"

class EstadoHistoria(Enum):
    """Estados de la historia"""
    INTRODUCCION = "introduccion"
    SELECCION_CLASE = "seleccion_clase"
    CAPITULO_1 = "capitulo_1"
    CAPITULO_2 = "capitulo_2"
    CAPITULO_3 = "capitulo_3"
    CAPITULO_4 = "capitulo_4"
    CAPITULO_5 = "capitulo_5"
    BATALLA_JEFE_1 = "batalla_jefe_1"
    BATALLA_JEFE_2 = "batalla_jefe_2"
    BATALLA_JEFE_FINAL = "batalla_jefe_final"
    TIENDA_ARMAS = "tienda_armas"
    TIENDA_ARMADURAS = "tienda_armaduras"
    LUGAR_ENTRENAMIENTO = "lugar_entrenamiento"
    FINAL_BUENO = "final_bueno"
    FINAL_MALO = "final_malo"
    GAME_OVER = "game_over"

class Narrativa:
    def __init__(self):
        self.estado_actual = EstadoHistoria.INTRODUCCION
        self.decisiones_tomadas = []
        self.puntos_moral = 0  # +10 bueno, -10 malo
        self.puntos_descaro = 0  # +10 malo, -10 bueno
        self.capitulo_actual = 1
        self.historia_completa = False
        
        # Cargar historias
        self.historias = self._cargar_historias()
        self.decisiones = self._cargar_decisiones()
        
    def _cargar_historias(self) -> Dict:
        """Carga las historias desde el archivo JSON"""
        return {
            EstadoHistoria.INTRODUCCION: {
                "titulo": "El Despertar del Héroe",
                "texto": [
                    "En el reino de Eldoria, una antigua profecía habla de un héroe que surgirá",
                    "en tiempos de oscuridad para enfrentar al Señor Oscuro Malakar.",
                    "",
                    "Tú eres ese héroe. Despiertas en una pequeña aldea con recuerdos",
                    "confusos de tu pasado, pero con una misión clara en tu corazón.",
                    "",
                    "Los aldeanos te miran con esperanza y temor. Saben que el destino",
                    "de Eldoria está en tus manos.",
                    "",
                    "¿Qué camino tomarás?"
                ],
                "opciones": [
                    "Aceptar tu destino y partir hacia la fortaleza de Malakar",
                    "Primero explorar la aldea para entender mejor la situación",
                    "Rechazar tu destino y vivir una vida normal"
                ]
            },
            
            EstadoHistoria.SELECCION_CLASE: {
                "titulo": "Elige tu Destino",
                "texto": [
                    "Antes de comenzar tu viaje, debes elegir tu clase de héroe.",
                    "Cada clase tiene sus propias fortalezas y debilidades.",
                    "",
                    "El anciano sabio te observa mientras tomas tu decisión:",
                    "",
                    "«Tu elección determinará no solo tu poder, sino también",
                    "el tipo de héroe que serás en esta historia.»"
                ],
                "opciones": [
                    "Guerrero - Fuerte y resistente",
                    "Mago - Poder mágico devastador",
                    "Arquero - Ataques a distancia",
                    "Paladín - Equilibrio ataque/defensa",
                    "Asesino - Ataques críticos rápidos"
                ]
            },
            
            EstadoHistoria.CAPITULO_1: {
                "titulo": "El Camino del Héroe",
                "texto": [
                    "Has decidido aceptar tu destino. Mientras preparas tu equipamiento,",
                    "un anciano sabio se acerca a ti.",
                    "",
                    "«Héroe, el camino que vas a emprender está lleno de peligros.",
                    "Malakar ha corrompido las tierras del norte y sus esbirros",
                    "patrullan los caminos.»",
                    "",
                    "El sabio te entrega un amuleto antiguo que brilla con energía mágica.",
                    "",
                    "«Este amuleto te protegerá, pero también te pondrá a prueba.",
                    "Cada decisión que tomes afectará tu destino y el de Eldoria.»"
                ],
                "opciones": [
                    "Aceptar el amuleto y partir inmediatamente",
                    "Preguntar más sobre los peligros que te esperan",
                    "Rechazar el amuleto y confiar solo en tus habilidades"
                ]
            },
            
            EstadoHistoria.CAPITULO_2: {
                "titulo": "La Prueba de Carácter",
                "texto": [
                    "En tu viaje, encuentras una aldea en llamas. Los gritos de",
                    "desesperación llenan el aire. Un grupo de bandidos está",
                    "saqueando las casas y secuestrando a los aldeanos.",
                    "",
                    "El líder de los bandidos, un hombre cruel llamado Garrok,",
                    "te ve y sonríe maliciosamente.",
                    "",
                    "«¡Mira qué tenemos aquí! Un héroe que viene a salvar el día.»",
                    "Los bandidos rodean a los aldeanos indefensos.",
                    "",
                    "¿Qué harás?"
                ],
                "opciones": [
                    "Atacar a los bandidos para salvar a los aldeanos",
                    "Intentar negociar con Garrok para liberar a los aldeanos",
                    "Ignorar la situación y continuar tu misión principal"
                ]
            },
            
            EstadoHistoria.CAPITULO_3: {
                "titulo": "El Camino de la Oscuridad",
                "texto": [
                    "En tu viaje hacia la fortaleza, encuentras un antiguo templo",
                    "abandonado. Dentro, hay un altar con un cristal oscuro que",
                    "pulsa con energía maligna.",
                    "",
                    "Un susurro en tu mente te dice que este poder podría",
                    "hacerte más fuerte, pero a un precio terrible.",
                    "",
                    "¿Qué harás con este poder prohibido?"
                ],
                "opciones": [
                    "Destruir el cristal para evitar la tentación",
                    "Estudiar el cristal sin tocarlo",
                    "Absorber el poder del cristal oscuro"
                ]
            },
            
            EstadoHistoria.CAPITULO_4: {
                "titulo": "La Ciudad de las Sombras",
                "texto": [
                    "Llegas a la ciudad de Noxhaven, gobernada por el Señor",
                    "de las Sombras, un aliado de Malakar.",
                    "",
                    "La ciudad está en ruinas, pero aún hay ciudadanos",
                    "que sufren bajo su yugo.",
                    "",
                    "En la plaza central, ves a guardias maltratando a",
                    "un grupo de civiles indefensos.",
                    "",
                    "¿Cómo actuarás?"
                ],
                "opciones": [
                    "Intervenir para salvar a los civiles",
                    "Observar desde las sombras",
                    "Aprovechar el caos para infiltrarte"
                ]
            },
            
            EstadoHistoria.CAPITULO_5: {
                "titulo": "La Fortaleza de Malakar",
                "texto": [
                    "Finalmente llegas a la fortaleza de Malakar. Las torres negras",
                    "se elevan hacia el cielo oscuro. El aire está cargado de",
                    "energía maligna.",
                    "",
                    "En la entrada, encuentras a un guardián anciano que te mira",
                    "con tristeza.",
                    "",
                    "«Héroe, Malakar no siempre fue así. Una vez fue un gran",
                    "mago que intentó salvar a Eldoria de una plaga, pero el",
                    "poder lo corrompió.»",
                    "",
                    "«Puedes intentar salvarlo o destruirlo. La elección es tuya.»"
                ],
                "opciones": [
                    "Intentar redimir a Malakar con el poder del amuleto",
                    "Enfrentar a Malakar en combate para destruirlo",
                    "Usar el amuleto para absorber su poder y convertirlo en el tuyo"
                ]
            },
            
            EstadoHistoria.BATALLA_JEFE_1: {
                "titulo": "Batalla: Señor de las Sombras",
                "texto": [
                    "El Señor de las Sombras emerge de las sombras, sus",
                    "ojos brillan con malicia pura.",
                    "",
                    "«¡Insolente! ¿Crees que puedes desafiar el poder",
                    "de las sombras?»",
                    "",
                    "La batalla está a punto de comenzar..."
                ],
                "opciones": [
                    "Preparar defensa y atacar con cautela",
                    "Atacar con toda tu fuerza",
                    "Intentar negociar antes del combate"
                ]
            },
            
            EstadoHistoria.BATALLA_JEFE_2: {
                "titulo": "Batalla: Guardián de la Corrupción",
                "texto": [
                    "Un ser corrupto, mitad humano mitad demonio, bloquea",
                    "tu camino hacia Malakar.",
                    "",
                    "«Solo los corruptos pueden pasar. ¿Estás listo",
                    "para abrazar la oscuridad?»",
                    "",
                    "La corrupción se extiende por el suelo..."
                ],
                "opciones": [
                    "Mantener la pureza y luchar",
                    "Usar magia oscura para vencer",
                    "Intentar purificar al guardián"
                ]
            },
            
            EstadoHistoria.BATALLA_JEFE_FINAL: {
                "titulo": "Batalla Final: Malakar",
                "texto": [
                    "Malakar, el Señor Oscuro, se levanta de su trono.",
                    "Su presencia llena la sala con energía maligna.",
                    "",
                    "«¡Héroe! Has llegado hasta aquí, pero ¿estás",
                    "preparado para enfrentar tu destino?»",
                    "",
                    "La batalla final está por comenzar..."
                ],
                "opciones": [
                    "Intentar redimir a Malakar",
                    "Luchar con todas tus fuerzas",
                    "Absorber su poder para vencer"
                ]
            },
            
            EstadoHistoria.TIENDA_ARMAS: {
                "titulo": "Tienda de Armas - El Herrero",
                "texto": [
                    "Encuentras a un herrero experto que puede forjar",
                    "armas legendarias para tu misión.",
                    "",
                    "«¡Héroe! Mis armas son las mejores de Eldoria.",
                    "¿Qué necesitas para tu viaje?»",
                    "",
                    "Tienes 500 monedas de oro disponibles."
                ],
                "opciones": [
                    "Espada de Luz (300 oro) - +20 ataque",
                    "Daga de Sombras (250 oro) - +15 ataque, crítico",
                    "Arco Élfico (280 oro) - +18 ataque, distancia",
                    "No comprar nada"
                ]
            },
            
            EstadoHistoria.TIENDA_ARMADURAS: {
                "titulo": "Tienda de Armaduras - El Forjador",
                "texto": [
                    "Un forjador de armaduras te ofrece protección",
                    "contra los ataques de tus enemigos.",
                    "",
                    "«¡Héroe! Una buena armadura puede salvar tu vida.",
                    "¿Qué protección necesitas?»",
                    "",
                    "Tienes 400 monedas de oro disponibles."
                ],
                "opciones": [
                    "Armadura de Mithril (350 oro) - +25 defensa",
                    "Túnica Mágica (300 oro) - +15 defensa, +10 energía",
                    "Cota de Escamas (320 oro) - +20 defensa, resistencia",
                    "No comprar nada"
                ]
            },
            
            EstadoHistoria.LUGAR_ENTRENAMIENTO: {
                "titulo": "Lugar de Entrenamiento",
                "texto": [
                    "Un maestro de combate te ofrece entrenamiento",
                    "para mejorar tus habilidades.",
                    "",
                    "«¡Héroe! El entrenamiento es la clave del éxito.",
                    "¿Qué habilidad quieres mejorar?»",
                    "",
                    "Tienes 200 monedas de oro disponibles."
                ],
                "opciones": [
                    "Entrenar ataque (150 oro) - +10 ataque",
                    "Entrenar defensa (150 oro) - +10 defensa",
                    "Entrenar energía (150 oro) - +20 energía",
                    "No entrenar"
                ]
            },
            
            EstadoHistoria.FINAL_BUENO: {
                "titulo": "El Final de la Redención",
                "texto": [
                    "Usando el poder del amuleto, logras llegar al corazón",
                    "de Malakar. En lugar de destruirlo, le muestras la luz",
                    "que una vez tuvo.",
                    "",
                    "Las lágrimas corren por el rostro de Malakar mientras",
                    "recuerda quién era antes de la corrupción.",
                    "",
                    "«Gracias, héroe. Has salvado no solo a Eldoria, sino",
                    "también mi alma.»",
                    "",
                    "Malakar usa su magia restaurada para curar las tierras",
                    "corrompidas. Eldoria florece nuevamente y tú eres",
                    "recordado como el héroe que eligió la compasión.",
                    "",
                    "¡FINAL BUENO ALCANZADO!"
                ],
                "opciones": [
                    "Continuar jugando en modo libre",
                    "Reiniciar la historia",
                    "Salir al menú principal"
                ]
            },
            
            EstadoHistoria.FINAL_MALO: {
                "titulo": "El Final de la Corrupción",
                "texto": [
                    "En tu búsqueda de poder, has absorbido la energía",
                    "maligna de Malakar. Pero el precio es alto.",
                    "",
                    "Sientes cómo la oscuridad se apodera de tu corazón.",
                    "Los aldeanos que una vez confiaron en ti ahora",
                    "huyen de tu presencia.",
                    "",
                    "Te has convertido en lo que juraste destruir. Eldoria",
                    "cae en una nueva era de oscuridad, y tú eres su",
                    "nuevo señor.",
                    "",
                    "¡FINAL MALO ALCANZADO!"
                ],
                "opciones": [
                    "Intentar redimirte en una nueva partida",
                    "Aceptar tu destino oscuro",
                    "Salir al menú principal"
                ]
            },
            
            EstadoHistoria.GAME_OVER: {
                "titulo": "Game Over",
                "texto": [
                    "Tu viaje ha terminado prematuramente. Las decisiones",
                    "que tomaste te llevaron por un camino sin retorno.",
                    "",
                    "Eldoria sigue bajo el yugo de Malakar, y tu historia",
                    "se convierte en una advertencia para futuros héroes.",
                    "",
                    "Pero siempre hay esperanza. Una nueva oportunidad",
                    "espera para aquellos que eligen sabiamente."
                ],
                "opciones": [
                    "Reintentar la historia",
                    "Volver al menú principal",
                    "Salir del juego"
                ]
            }
        }
    
    def _cargar_decisiones(self) -> Dict:
        """Carga las consecuencias de las decisiones"""
        return {
            EstadoHistoria.INTRODUCCION: {
                0: {  # Aceptar destino
                    "texto": "Has aceptado tu destino. El camino del héroe te espera.",
                    "moral": 5,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.SELECCION_CLASE
                },
                1: {  # Explorar aldea
                    "texto": "Decides explorar la aldea. Los aldeanos te cuentan sobre los horrores que Malakar ha traído a Eldoria.",
                    "moral": 10,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.SELECCION_CLASE
                },
                2: {  # Rechazar destino
                    "texto": "Rechazas tu destino. Pero el destino no se puede rechazar.",
                    "moral": -10,
                    "descaro": 15,
                    "siguiente": EstadoHistoria.GAME_OVER
                }
            },
            
            EstadoHistoria.SELECCION_CLASE: {
                0: {  # Guerrero
                    "texto": "Has elegido el camino del Guerrero. La fuerza bruta será tu aliada.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.CAPITULO_1
                },
                1: {  # Mago
                    "texto": "Has elegido el camino del Mago. El poder arcano fluye en tus venas.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.CAPITULO_1
                },
                2: {  # Arquero
                    "texto": "Has elegido el camino del Arquero. La precisión será tu arma.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.CAPITULO_1
                },
                3: {  # Paladín
                    "texto": "Has elegido el camino del Paladín. La luz sagrada te guía.",
                    "moral": 5,
                    "descaro": -5,
                    "siguiente": EstadoHistoria.CAPITULO_1
                },
                4: {  # Asesino
                    "texto": "Has elegido el camino del Asesino. Las sombras serán tu refugio.",
                    "moral": -5,
                    "descaro": 10,
                    "siguiente": EstadoHistoria.CAPITULO_1
                }
            },
            
            EstadoHistoria.CAPITULO_1: {
                0: {  # Aceptar amuleto
                    "texto": "Aceptas el amuleto. Su poder te protege y te guía.",
                    "moral": 5,
                    "siguiente": EstadoHistoria.CAPITULO_2
                },
                1: {  # Preguntar más
                    "texto": "El sabio te advierte sobre las pruebas que enfrentarás.",
                    "moral": 10,
                    "siguiente": EstadoHistoria.CAPITULO_2
                },
                2: {  # Rechazar amuleto
                    "texto": "Confías solo en tus habilidades. Un camino peligroso.",
                    "moral": -5,
                    "siguiente": EstadoHistoria.CAPITULO_2
                }
            },
            
            EstadoHistoria.CAPITULO_2: {
                0: {  # Atacar bandidos
                    "texto": "Atacas a los bandidos. Garrok huye, pero los aldeanos están a salvo. Tu valentía es recompensada.",
                    "moral": 15,
                    "siguiente": EstadoHistoria.CAPITULO_3
                },
                1: {  # Negociar
                    "texto": "Negocias con Garrok. Libera a los aldeanos, pero tú debes pagar un precio en oro.",
                    "moral": 5,
                    "siguiente": EstadoHistoria.CAPITULO_3
                },
                2: {  # Ignorar
                    "texto": "Ignoras la situación. Los aldeanos sufren, pero tu misión continúa. La culpa te persigue.",
                    "moral": -15,
                    "siguiente": EstadoHistoria.CAPITULO_3
                }
            },
            
            EstadoHistoria.CAPITULO_3: {
                0: {  # Destruir cristal
                    "texto": "Destruyes el cristal oscuro. Has resistido la tentación del poder maligno.",
                    "moral": 15,
                    "descaro": -10,
                    "siguiente": EstadoHistoria.CAPITULO_4
                },
                1: {  # Estudiar cristal
                    "texto": "Estudias el cristal con cautela. Aprendes sobre su naturaleza sin tocarlo.",
                    "moral": 5,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.CAPITULO_4
                },
                2: {  # Absorber poder
                    "texto": "Absorbes el poder del cristal oscuro. Sientes una energía maligna fluyendo en ti.",
                    "moral": -10,
                    "descaro": 20,
                    "siguiente": EstadoHistoria.CAPITULO_4
                }
            },
            
            EstadoHistoria.CAPITULO_4: {
                0: {  # Intervenir
                    "texto": "Intervienes para salvar a los civiles. Tu valentía inspira a la ciudad.",
                    "moral": 20,
                    "descaro": -5,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_1
                },
                1: {  # Observar
                    "texto": "Observas desde las sombras. Mantienes tu presencia oculta.",
                    "moral": 0,
                    "descaro": 5,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_1
                },
                2: {  # Aprovechar caos
                    "texto": "Aprovechas el caos para infiltrarte. Tu pragmatismo te lleva al objetivo.",
                    "moral": -5,
                    "descaro": 15,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_1
                }
            },
            
            EstadoHistoria.CAPITULO_5: {
                0: {  # Redimir
                    "texto": "Intentas redimir a Malakar. El amuleto brilla con poder purificador.",
                    "moral": 20,
                    "descaro": -10,
                    "siguiente": EstadoHistoria.FINAL_BUENO
                },
                1: {  # Destruir
                    "texto": "Decides destruir a Malakar. La batalla será épica.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.FINAL_BUENO
                },
                2: {  # Absorber poder
                    "texto": "Absorbes el poder de Malakar. La corrupción se apodera de ti.",
                    "moral": -20,
                    "descaro": 25,
                    "siguiente": EstadoHistoria.FINAL_MALO
                }
            },
            
            EstadoHistoria.BATALLA_JEFE_1: {
                0: {  # Cautela
                    "texto": "Luchas con cautela y estrategia. Derrotas al Señor de las Sombras.",
                    "moral": 10,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.TIENDA_ARMAS
                },
                1: {  # Fuerza bruta
                    "texto": "Atacas con toda tu fuerza. La batalla es intensa pero victoriosa.",
                    "moral": 0,
                    "descaro": 10,
                    "siguiente": EstadoHistoria.TIENDA_ARMAS
                },
                2: {  # Negociar
                    "texto": "Intentas negociar. El Señor de las Sombras se rinde ante tu diplomacia.",
                    "moral": 15,
                    "descaro": -5,
                    "siguiente": EstadoHistoria.TIENDA_ARMAS
                }
            },
            
            EstadoHistoria.BATALLA_JEFE_2: {
                0: {  # Pureza
                    "texto": "Mantienes tu pureza y luchas con honor. Purificas al guardián.",
                    "moral": 20,
                    "descaro": -10,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                },
                1: {  # Magia oscura
                    "texto": "Usas magia oscura para vencer. El poder corrupto te fortalece.",
                    "moral": -10,
                    "descaro": 20,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                },
                2: {  # Purificar
                    "texto": "Intentas purificar al guardián. Tu compasión lo redime.",
                    "moral": 15,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                }
            },
            
            EstadoHistoria.BATALLA_JEFE_FINAL: {
                0: {  # Redimir
                    "texto": "Intentas redimir a Malakar. Tu compasión toca su corazón.",
                    "moral": 25,
                    "descaro": -15,
                    "siguiente": EstadoHistoria.FINAL_BUENO
                },
                1: {  # Luchar
                    "texto": "Luchas con todas tus fuerzas. La batalla es épica y victoriosa.",
                    "moral": 10,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.FINAL_BUENO
                },
                2: {  # Absorber
                    "texto": "Absorbes el poder de Malakar. Te conviertes en el nuevo Señor Oscuro.",
                    "moral": -25,
                    "descaro": 30,
                    "siguiente": EstadoHistoria.FINAL_MALO
                }
            },
            
            EstadoHistoria.TIENDA_ARMAS: {
                0: {  # Espada de Luz
                    "texto": "Compras la Espada de Luz. Su poder sagrado te fortalece.",
                    "moral": 5,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.LUGAR_ENTRENAMIENTO
                },
                1: {  # Daga de Sombras
                    "texto": "Compras la Daga de Sombras. Su poder oscuro te atrae.",
                    "moral": -5,
                    "descaro": 10,
                    "siguiente": EstadoHistoria.LUGAR_ENTRENAMIENTO
                },
                2: {  # Arco Élfico
                    "texto": "Compras el Arco Élfico. Su precisión élfica te acompaña.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.LUGAR_ENTRENAMIENTO
                },
                3: {  # No comprar
                    "texto": "Decides no comprar nada. Continúas con tu equipamiento actual.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.LUGAR_ENTRENAMIENTO
                }
            },
            
            EstadoHistoria.TIENDA_ARMADURAS: {
                0: {  # Armadura de Mithril
                    "texto": "Compras la Armadura de Mithril. Su protección legendaria te protege.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_FINAL
                },
                1: {  # Túnica Mágica
                    "texto": "Compras la Túnica Mágica. Su magia te fortalece.",
                    "moral": 5,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_FINAL
                },
                2: {  # Cota de Escamas
                    "texto": "Compras la Cota de Escamas. Su resistencia te protege.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_FINAL
                },
                3: {  # No comprar
                    "texto": "Decides no comprar nada. Confías en tu habilidad natural.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.BATALLA_JEFE_FINAL
                }
            },
            
            EstadoHistoria.LUGAR_ENTRENAMIENTO: {
                0: {  # Entrenar ataque
                    "texto": "Entrenas tu ataque. Tu fuerza de combate mejora significativamente.",
                    "moral": 0,
                    "descaro": 5,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                },
                1: {  # Entrenar defensa
                    "texto": "Entrenas tu defensa. Tu resistencia mejora significativamente.",
                    "moral": 5,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                },
                2: {  # Entrenar energía
                    "texto": "Entrenas tu energía. Tu poder mágico mejora significativamente.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                },
                3: {  # No entrenar
                    "texto": "Decides no entrenar. Confías en tus habilidades actuales.",
                    "moral": 0,
                    "descaro": 0,
                    "siguiente": EstadoHistoria.TIENDA_ARMADURAS
                }
            }
        }
    
    def obtener_historia_actual(self) -> Dict:
        """Obtiene la historia actual"""
        return self.historias.get(self.estado_actual, {})
    
    def tomar_decision(self, indice_decision: int) -> Dict:
        """Toma una decisión y retorna las consecuencias"""
        if self.estado_actual not in self.decisiones:
            return {"texto": "No hay decisiones disponibles", "moral": 0, "siguiente": None}
        
        if indice_decision >= len(self.decisiones[self.estado_actual]):
            return {"texto": "Decisión inválida", "moral": 0, "siguiente": None}
        
        decision = self.decisiones[self.estado_actual][indice_decision]
        
        # Registrar la decisión
        self.decisiones_tomadas.append({
            "estado": self.estado_actual.value,
            "decision": indice_decision,
            "moral": decision["moral"]
        })
        
        # Actualizar puntos de moral y descaro
        self.puntos_moral += decision["moral"]
        self.puntos_descaro += decision.get("descaro", 0)
        
        # Cambiar estado
        if decision["siguiente"]:
            self.estado_actual = decision["siguiente"]
            if self.estado_actual in [EstadoHistoria.FINAL_BUENO, EstadoHistoria.FINAL_MALO]:
                self.historia_completa = True
        
        return decision
    
    def reiniciar_historia(self):
        """Reinicia la historia al estado inicial"""
        self.estado_actual = EstadoHistoria.INTRODUCCION
        self.decisiones_tomadas = []
        self.puntos_moral = 0
        self.puntos_descaro = 0
        self.capitulo_actual = 1
        self.historia_completa = False
    
    def obtener_progreso(self) -> Dict:
        """Obtiene el progreso actual de la historia"""
        return {
            "estado": self.estado_actual.value,
            "puntos_moral": self.puntos_moral,
            "puntos_descaro": self.puntos_descaro,
            "decisiones_tomadas": len(self.decisiones_tomadas),
            "historia_completa": self.historia_completa,
            "capitulo": self.capitulo_actual
        } 