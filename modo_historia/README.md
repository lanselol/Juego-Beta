# Modo Historia - Fantasy Battle

## Descripción

El Modo Historia es una experiencia narrativa inmersiva que complementa el juego de batalla por turnos. Los jugadores toman decisiones que afectan el desarrollo de la historia y pueden llevar a diferentes finales.

## Características

### Narrativa Completa
- **Historia épica**: Aventura en el reino de Eldoria
- **Toma de decisiones**: Cada elección afecta el desarrollo
- **Sistema de moral**: Las decisiones acumulan puntos de moral
- **Dos finales**: Final bueno y final malo según las decisiones

### Estados de la Historia
1. **Introducción**: El despertar del héroe
2. **Capítulo 1**: El camino del héroe
3. **Capítulo 2**: La prueba de carácter
4. **Capítulo 3**: La fortaleza de Malakar
5. **Finales**: Redención o corrupción
6. **Game Over**: Cuando las decisiones llevan a un final prematuro

### Sistema de Decisiones
- **Decisiones morales**: Afectan los puntos de moral
- **Consecuencias**: Cada decisión tiene repercusiones
- **Ramas narrativas**: Diferentes caminos según las elecciones

## Controles

### En la Historia
- **Flechas Arriba/Abajo**: Navegar opciones
- **Enter**: Seleccionar opción
- **S**: Guardar partida
- **L**: Cargar partida
- **ESC**: Volver al menú principal

### En la Pantalla de Guardado
- **Flechas Arriba/Abajo**: Navegar archivos
- **Enter**: Cargar partida seleccionada
- **D**: Eliminar partida
- **ESC**: Volver a la historia

## Sistema de Guardado

### Características
- **Máximo 2 archivos**: Solo se pueden tener 2 partidas guardadas
- **Reemplazo automático**: El archivo más antiguo se reemplaza
- **Información completa**: Guarda progreso, decisiones y estado del jugador

### Datos Guardados
- Estado del jugador (vida, energía, nivel, etc.)
- Progreso del juego (piso actual, monedas, etc.)
- Estado de la historia (decisiones, puntos de moral)
- Objetos y mejoras del jugador

## Finales

### Final Bueno - La Redención
- **Condición**: Puntos de moral positivos y decisiones compasivas
- **Resultado**: Malakar es redimido, Eldoria se salva
- **Recompensa**: Continuar en modo libre

### Final Malo - La Corrupción
- **Condición**: Puntos de moral negativos y decisiones egoístas
- **Resultado**: El héroe se convierte en el nuevo señor oscuro
- **Consecuencia**: Eldoria cae en una nueva era de oscuridad

### Game Over
- **Condición**: Decisiones que llevan a un final prematuro
- **Resultado**: La historia termina sin completarse
- **Opción**: Reintentar la historia

## Integración con el Juego Principal

### Modo Libre
- Después del final bueno, se puede continuar jugando
- Acceso completo al sistema de batalla
- Progresión normal de pisos y enemigos

### Transiciones
- **Historia → Batalla**: Al completar la historia
- **Batalla → Historia**: Desde el menú principal
- **Guardado**: Accesible desde cualquier punto

## Archivos del Sistema

### `narrativa.py`
- Clase `Narrativa`: Maneja la lógica de la historia
- Estados y transiciones de la narrativa
- Sistema de decisiones y consecuencias

### `renderizador_historia.py`
- Clase `RenderizadorHistoria`: Interfaz visual
- Pantallas de historia, finales y game over
- Optimización de rendimiento con cache

### `controlador_historia.py`
- Clase `ControladorHistoria`: Lógica principal
- Manejo de eventos y estados
- Integración con el juego principal

## Uso

1. **Iniciar modo historia**: Presionar 'H' en la selección de clase
2. **Navegar decisiones**: Usar flechas para seleccionar opciones
3. **Guardar progreso**: Presionar 'S' en cualquier momento
4. **Cargar partida**: Presionar 'L' para acceder al guardado
5. **Completar historia**: Tomar decisiones hasta llegar a un final

## Notas Técnicas

- **Optimización de memoria**: Cache de texto renderizado
- **Gestión de archivos**: Sistema robusto de guardado
- **Integración modular**: Fácil extensión y modificación
- **Interfaz consistente**: Diseño coherente con el juego principal 