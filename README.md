# Fantasy Battle - Juego de Peleas por Turnos

Un emocionante juego de peleas por turnos ambientado en un mundo de fantasía donde puedes elegir entre 5 clases únicas de personajes, escalar una torre de 100 pisos llena de desafíos, gestionar tu economía para comprar objetos poderosos, mejorar tus habilidades con el maestro de habilidades y aprovechar las fortalezas y debilidades entre clases.

## 🎮 Características

### Sistema de Progresión por Pisos
- **100 pisos** de dificultad progresiva
- **Jefes únicos** cada 10 pisos (pisos 10, 20, 30, etc.)
- **Dificultad escalable** - Los enemigos se vuelven más fuertes cada piso
- **10 jefes legendarios** con habilidades especiales
- **Curación automática** al completar cada piso

### Sistema de Economía y Objetos
- **Monedas de oro** como recompensa por cada victoria
- **Tienda disponible** cada 5 pisos (pisos 5, 10, 15, etc.)
- **6 tipos de objetos** con efectos únicos
- **Bolsa de objetos** para usar durante el combate
- **Efectos temporales** que mejoran tus estadísticas
- **Objetos iniciales** - Cada clase comienza con pociones de vida y energía

### Maestro de Habilidades
- **Disponible después de derrotar jefes** (pisos 10, 20, 30, etc.)
- **4 mejoras únicas** por clase de personaje
- **Mejoras de daño, energía y probabilidad de crítico**
- **Nuevas habilidades** que se pueden aprender
- **Sistema de progresión permanente** de habilidades

### Sistema de Fortalezas y Debilidades
- **Cada clase tiene ventajas y desventajas** contra otras clases
- **50% más de daño** cuando tienes ventaja de clase
- **30% menos de daño** cuando tienes desventaja de clase
- **Indicadores visuales** de fortalezas y debilidades
- **Mensajes informativos** durante el combate

### 5 Clases de Personajes

1. **Guerrero** ⚔️
   - **Vida**: 120 | **Ataque**: 25 | **Defensa**: 20 | **Energía**: 100
   - **Objetos iniciales**: Poción de Vida + Poción de Energía
   - **Fortaleza**: Fuerte contra Asesino (+50% daño)
   - **Debilidad**: Débil contra Mago (-30% daño)
   - **Habilidades**:
     - Espadazo (Energía: 20) - Ataque básico con espada
     - Golpe Defensivo (Energía: 15) - Ataque que aumenta defensa
     - Furia Berserker (Energía: 50) - Ataque devastador
   - **Mejoras disponibles**:
     - Mejorar Espadazo (+0.3 daño, 100 oro)
     - Mejorar Golpe Defensivo (-5 energía, 120 oro)
     - Mejorar Furia Berserker (+0.5 daño, 200 oro)
     - Aprender Golpe Crítico (nueva habilidad, 300 oro)

2. **Mago** 🔮
   - **Vida**: 80 | **Ataque**: 30 | **Defensa**: 10 | **Energía**: 120
   - **Objetos iniciales**: Poción de Vida + Poción de Energía
   - **Fortaleza**: Fuerte contra Guerrero (+50% daño)
   - **Debilidad**: Débil contra Arquero (-30% daño)
   - **Habilidades**:
     - Bola de Fuego (Energía: 30) - Lanza una bola de fuego
     - Rayo Eléctrico (Energía: 40) - Rayo que puede paralizar
     - Meteorito (Energía: 70) - Invoca un meteorito
   - **Mejoras disponibles**:
     - Mejorar Bola de Fuego (+0.4 daño, 100 oro)
     - Mejorar Rayo Eléctrico (+10% paralizar, 150 oro)
     - Mejorar Meteorito (-10 energía, 200 oro)
     - Aprender Tormenta de Hielo (nueva habilidad, 300 oro)

3. **Arquero** 🏹
   - **Vida**: 90 | **Ataque**: 28 | **Defensa**: 12 | **Energía**: 110
   - **Objetos iniciales**: Poción de Vida + Poción de Energía
   - **Fortaleza**: Fuerte contra Mago (+50% daño)
   - **Debilidad**: Débil contra Paladín (-30% daño)
   - **Habilidades**:
     - Flecha Rápida (Energía: 15) - Dispara una flecha rápida
     - Lluvia de Flechas (Energía: 35) - Múltiples flechas
     - Flecha Venenosa (Energía: 25) - Flecha con veneno
   - **Mejoras disponibles**:
     - Mejorar Flecha Rápida (-3 energía, 80 oro)
     - Mejorar Lluvia de Flechas (+0.3 daño, 120 oro)
     - Mejorar Flecha Venenosa (+0.2 daño, 100 oro)
     - Aprender Flecha Explosiva (nueva habilidad, 250 oro)

4. **Paladín** 🛡️
   - **Vida**: 110 | **Ataque**: 22 | **Defensa**: 18 | **Energía**: 100
   - **Objetos iniciales**: Poción de Vida + Poción de Energía
   - **Fortaleza**: Fuerte contra Arquero (+50% daño)
   - **Debilidad**: Débil contra Asesino (-30% daño)
   - **Habilidades**:
     - Golpe Sagrado (Energía: 25) - Ataque bendecido
     - Curación (Energía: 30) - Se cura a sí mismo
     - Escudo Divino (Energía: 40) - Aumenta defensa temporalmente
   - **Mejoras disponibles**:
     - Mejorar Golpe Sagrado (+0.3 daño, 100 oro)
     - Mejorar Curación (+0.2 curación, 120 oro)
     - Mejorar Escudo Divino (-5 energía, 100 oro)
     - Aprender Bendición (nueva habilidad, 300 oro)

5. **Asesino** 🗡️
   - **Vida**: 85 | **Ataque**: 32 | **Defensa**: 8 | **Energía**: 130
   - **Objetos iniciales**: Poción de Vida + Poción de Energía
   - **Fortaleza**: Fuerte contra Paladín (+50% daño)
   - **Debilidad**: Débil contra Guerrero (-30% daño)
   - **Habilidades**:
     - Puñalada (Energía: 20) - Ataque rápido con puñal
     - Golpe Crítico (Energía: 45) - Alto daño crítico
     - Invisibilidad (Energía: 35) - Ataque desde las sombras
   - **Mejoras disponibles**:
     - Mejorar Puñalada (+5% crítico, 120 oro)
     - Mejorar Golpe Crítico (+0.4 daño, 150 oro)
     - Mejorar Invisibilidad (-5 energía, 100 oro)
     - Aprender Golpe Mortal (nueva habilidad, 350 oro)

## 👑 Los 10 Jefes Legendarios

### Jefes de Mago 🔮
- **Ragnaros el Señor del Fuego** - Maestro del fuego destructivo
- **Gul'dan el Destructor** - Señor de las sombras

### Jefes de Guerrero ⚔️
- **Thrall el Jefe de Guerra** - Líder de los orcos
- **Grommash Puño de Hierro** - Guerrero legendario

### Jefes de Arquero 🏹
- **Sylvanas la Reina Banshee** - Reina de los no-muertos
- **Alleria Brisaveloz** - Arquera élfica suprema

### Jefes de Paladín 🛡️
- **Uther el Portador de Luz** - Paladín de la Luz
- **Tirion Fordring** - Campeón de la justicia

### Jefes de Asesino 🗡️
- **Valeera la Sombra** - Asesina de las sombras
- **Garona la Asesina** - Maestra del sigilo

### Objetos de Jefes
Los jefes comienzan con objetos adicionales según su clase:
- **Guerreros**: Poción de Vida + Poción de Energía + Elixir de Fuerza
- **Magos**: Poción de Vida + Poción de Energía + Elixir de Velocidad
- **Arqueros**: Poción de Vida + Poción de Energía + Bomba de Veneno
- **Paladines**: Poción de Vida + Poción de Energía + Escudo Temporal
- **Asesinos**: Poción de Vida + Poción de Energía + Elixir de Fuerza

## 🛒 Sistema de Objetos

### Objetos Disponibles en la Tienda

1. **Poción de Vida** (50 oro)
   - Restaura 50 puntos de vida instantáneamente

2. **Poción de Energía** (40 oro)
   - Restaura 40 puntos de energía instantáneamente

3. **Elixir de Fuerza** (80 oro)
   - Aumenta el ataque en 10 puntos por 3 turnos

4. **Elixir de Velocidad** (70 oro)
   - Otorga velocidad extra por 2 turnos

5. **Escudo Temporal** (60 oro)
   - Aumenta la defensa en 15 puntos por 2 turnos

6. **Bomba de Veneno** (100 oro)
   - Causa 30 daño por veneno por 3 turnos al enemigo

### Efectos de los Objetos
- **Efectos instantáneos**: Poción de Vida y Poción de Energía
- **Efectos temporales**: Elixires y Escudo Temporal
- **Efectos de daño**: Bomba de Veneno
- **Duración**: Los efectos temporales se muestran en la interfaz

## 🎯 Cómo Jugar

### Selección de Clase
1. Ejecuta el juego con `python main/main.py`
2. Presiona las teclas **1-5** para seleccionar tu clase de héroe
3. Cada clase tiene estadísticas, habilidades únicas y objetos iniciales

### Combate por Turnos
- **Flechas Arriba/Abajo**: Navegar entre habilidades
- **Enter**: Usar la habilidad seleccionada
- **R**: Descansar y recuperar energía
- **O**: Navegar entre objetos en la bolsa
- **I**: Usar el objeto seleccionado en la bolsa
- **T**: Abrir/cerrar tienda (solo en pisos múltiplos de 5)
- **M**: Abrir/cerrar maestro de habilidades (solo después de derrotar jefes)

### Tienda
- **Flechas Arriba/Abajo**: Navegar entre objetos
- **Enter**: Comprar objeto seleccionado
- **T**: Salir de la tienda

### Maestro de Habilidades
- **Flechas Arriba/Abajo**: Navegar entre mejoras
- **Enter**: Comprar mejora seleccionada
- **M**: Salir del maestro de habilidades
- **Indicadores visuales**: Mejoras ya compradas se muestran en verde

### Progresión del Juego
- **Pisos 1-4**: Enemigos normales con dificultad creciente
- **Piso 5**: Primera tienda disponible
- **Pisos 6-9**: Enemigos más fuertes
- **Piso 10**: Primer jefe legendario + tienda + maestro de habilidades
- **Y así sucesivamente...**

### Sistema de Recompensas
- **Enemigos normales**: 10 + (piso × 2) monedas de oro
- **Jefes**: 3× la recompensa normal de enemigos
- **Ejemplo**: Piso 5 = 20 oro, Piso 10 (jefe) = 60 oro

### Mecánicas del Juego
- **Vida**: Cuando llega a 0, el personaje es derrotado
- **Energía**: Necesaria para usar habilidades, se recupera descansando
- **Estados**: Algunas habilidades pueden causar efectos como "Paralizado"
- **Críticos**: Los Asesinos tienen 30% de probabilidad de crítico, los Magos 20%
- **Dificultad Progresiva**: Los enemigos se vuelven 10% más fuertes cada piso
- **Jefes**: 50% más fuertes que enemigos normales + habilidades especiales
- **Veneno**: Causa daño por turno hasta que expire
- **Efectos Temporales**: Se muestran en la interfaz y expiran automáticamente
- **Números redondeados**: Todas las estadísticas se muestran sin decimales
- **Fortalezas/Debilidades**: Sistema de ventajas y desventajas entre clases

### Sistema de Fortalezas y Debilidades
- **Guerrero**: Fuerte vs Asesino, Débil vs Mago
- **Mago**: Fuerte vs Guerrero, Débil vs Arquero
- **Arquero**: Fuerte vs Mago, Débil vs Paladín
- **Paladín**: Fuerte vs Arquero, Débil vs Asesino
- **Asesino**: Fuerte vs Paladín, Débil vs Guerrero
- **Ventaja**: +50% de daño
- **Desventaja**: -30% de daño
- **Normal**: Daño estándar

### Sistema de Jefes
- **Habilidades Únicas**: Cada jefe tiene 3 habilidades especiales más poderosas
- **Estadísticas Mejoradas**: Vida, ataque, defensa y energía superiores
- **Dificultad Escalable**: Los jefes se vuelven más fuertes cada 10 pisos
- **Rotación**: Los jefes aparecen en orden aleatorio
- **Maestro de Habilidades**: Se desbloquea después de derrotar cada jefe
- **Objetos Especiales**: Los jefes comienzan con objetos adicionales según su clase

### Estrategia
- **Guerrero**: Ideal para principiantes, equilibrado y resistente
- **Mago**: Alto daño pero poca defensa, usa ataques a distancia
- **Arquero**: Bueno para ataques consistentes y control
- **Paladín**: Puede curarse, perfecto para batallas largas
- **Asesino**: Alto riesgo/recompensa con ataques críticos

### Consejos para Jefes
- **Prepara tu energía**: Asegúrate de tener suficiente energía antes de enfrentar un jefe
- **Usa habilidades poderosas**: Los jefes tienen mucha vida, usa tus mejores ataques
- **Mantén tu vida alta**: Los jefes pueden causar mucho daño de una vez
- **Aprovecha los efectos**: Algunas habilidades de jefes pueden paralizar
- **Compra objetos**: Usa la tienda para prepararte antes de enfrentar jefes
- **Mejora habilidades**: Después de derrotar jefes, visita al maestro de habilidades
- **Considera las fortalezas**: Elige tu clase sabiamente según los jefes que enfrentes

### Gestión de Economía
- **Ahorra oro**: Los jefes dan más oro, pero los objetos y mejoras son caros
- **Prioriza objetos**: Compra pociones de vida para emergencias
- **Usa efectos temporales**: Los elixires pueden cambiar el curso de una batalla
- **Planifica**: Guarda oro para la tienda y maestro antes de enfrentar jefes
- **Invierte en mejoras**: Las mejoras de habilidades son permanentes
- **Usa objetos iniciales**: Cada clase comienza con pociones, úsalas estratégicamente

### Estrategia de Clases
- **Elige según el enemigo**: Considera las fortalezas y debilidades
- **Aprovecha ventajas**: Usa clases que sean fuertes contra jefes específicos
- **Planifica a largo plazo**: Las mejoras de habilidades son permanentes
- **Gestiona recursos**: Usa objetos iniciales y comprados estratégicamente

## 🚀 Instalación

1. Asegúrate de tener Python instalado
2. Instala pygame: `pip install pygame`
3. Ejecuta el juego: `python main/main.py`

## 🎨 Características Técnicas

- **Motor**: Pygame
- **Resolución**: 1200x800
- **FPS**: 60
- **IA**: Sistema simple para el enemigo
- **Interfaz**: Gráfica con barras de vida y energía
- **Progresión**: Sistema de pisos con 100 niveles
- **Jefes**: 10 jefes únicos con habilidades especiales
- **Economía**: Sistema de monedas y tienda
- **Objetos**: 6 tipos con efectos únicos
- **Mejoras**: Sistema de progresión permanente de habilidades
- **Visualización**: Números redondeados para mejor legibilidad
- **Fortalezas**: Sistema de ventajas y desventajas entre clases
- **Objetos iniciales**: Cada clase comienza con pociones básicas

## 🏆 Objetivo del Juego

¡Llega al piso 100 y derrota a todos los jefes legendarios para convertirte en el campeón definitivo de Fantasy Battle! Cada piso te acerca más a la gloria, pero también aumenta el desafío. Gestiona tu economía sabiamente, compra objetos estratégicos, mejora tus habilidades permanentemente, aprovecha las fortalezas de tu clase y usa tus efectos temporales para superar los obstáculos más difíciles.

¿Podrás escalar toda la torre, derrotar a todos los jefes, maximizar tus habilidades, dominar las fortalezas de tu clase y convertirte en el héroe legendario?

¡Disfruta del combate épico en el mundo de Fantasy Battle! ⚔️✨ 