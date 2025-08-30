# Sistema de Centrado Responsivo - Fantasy Battle

## Descripción

Se ha implementado un sistema de centrado automático y responsivo para todas las interfaces del juego Fantasy Battle. Este sistema asegura que todos los elementos de la interfaz se centren correctamente tanto en pantalla completa (1920x1080) como en pantallas más pequeñas.

## Características Principales

### 1. Centrado Automático
- **Títulos**: Todos los títulos principales se centran horizontalmente en la pantalla
- **Elementos de interfaz**: Paneles, botones y textos se posicionan automáticamente al centro
- **Responsive**: Se adapta a diferentes resoluciones de pantalla

### 2. Ajuste de Tamaños
- **Pantalla completa (1920x1080)**: Tamaños originales
- **Pantalla mediana (≥1200px)**: 80% del tamaño original
- **Pantalla pequeña (<1200px)**: 60% del tamaño original

### 3. Fuentes Adaptativas
- **Pantalla completa**: Fuentes grandes para mejor legibilidad
- **Pantalla mediana**: Fuentes medianas
- **Pantalla pequeña**: Fuentes pequeñas para evitar desbordamiento

## Métodos de Centrado

### `_centrar_horizontal(elemento_ancho)`
Centra un elemento horizontalmente en la pantalla.

```python
# Ejemplo de uso
titulo_x = self._centrar_horizontal(titulo.get_width())
```

### `_centrar_vertical(elemento_alto, offset_y=0)`
Centra un elemento verticalmente con offset opcional.

```python
# Ejemplo de uso
titulo_y = self._centrar_vertical(100, -300)
```

### `_ajustar_tamano_elemento(tamano_base)`
Ajusta el tamaño de los elementos según la resolución.

```python
# Ejemplo de uso
panel_ancho = self._ajustar_tamano_elemento(600)
```

## Interfaces Afectadas

### 1. Selección de Clase
- Título principal centrado
- Cajas de clases centradas
- Modo historia centrado
- Instrucciones centradas en la parte inferior

### 2. Tienda
- Título centrado
- Panel de información centrado
- Objetos distribuidos uniformemente
- Instrucciones centradas

### 3. Maestro de Habilidades
- Título centrado
- Panel de información centrado
- Mejoras distribuidas uniformemente
- Instrucciones centradas

### 4. Batalla
- Información del piso centrada
- Área de batalla central centrada
- Mensajes centrados
- Botones de acción centrados

### 5. Modo Historia
- Títulos centrados
- Texto de historia centrado línea por línea
- Opciones centradas
- Instrucciones centradas

## Cambio de Resolución

El juego ahora maneja automáticamente el cambio entre pantalla completa y ventana normal:

- **F11 o ESC**: Cambia entre pantalla completa y ventana normal
- **Actualización automática**: Las dimensiones se actualizan en tiempo real
- **Reajuste de fuentes**: Las fuentes se ajustan automáticamente

## Archivos Modificados

1. **`interfaz/renderizador.py`**: Sistema principal de centrado
2. **`modo_historia/renderizador_historia.py`**: Centrado para modo historia
3. **`main/main.py`**: Manejo de cambios de resolución

## Pruebas

Para probar el sistema de centrado, ejecuta:

```bash
python test_centrado.py
```

Este script probará el centrado en diferentes resoluciones y mostrará las posiciones calculadas.

## Beneficios

1. **Mejor experiencia visual**: Todos los elementos están perfectamente centrados
2. **Responsive design**: Se adapta a diferentes tamaños de pantalla
3. **Mantenimiento fácil**: Sistema centralizado de centrado
4. **Consistencia**: Todas las interfaces siguen el mismo patrón de diseño

## Compatibilidad

- ✅ Pantalla completa (1920x1080)
- ✅ Pantalla mediana (≥1200px)
- ✅ Pantalla pequeña (<1200px)
- ✅ Cambio dinámico de resolución
- ✅ Todas las interfaces del juego

## Notas Técnicas

- El sistema calcula las posiciones en tiempo real
- No hay posiciones hardcodeadas
- Las fuentes se ajustan automáticamente
- Los elementos mantienen proporciones correctas
- Compatible con el sistema de eventos existente
