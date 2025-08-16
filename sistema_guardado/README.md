# Sistema de Guardado - Fantasy Battle

## Descripción

El Sistema de Guardado permite a los jugadores guardar y cargar su progreso en el juego. Está diseñado para ser eficiente y confiable, con un límite de 2 archivos de guardado para mantener la simplicidad.

## Características

### Gestión de Archivos
- **Máximo 2 archivos**: Limitación para mantener simplicidad
- **Reemplazo automático**: El archivo más antiguo se reemplaza
- **Información completa**: Guarda todos los datos relevantes del juego
- **Formato binario**: Uso de pickle para eficiencia

### Datos Guardados
- **Estado del jugador**: Vida, energía, nivel, experiencia
- **Progreso del juego**: Piso actual, monedas de oro, jefes derrotados
- **Objetos y mejoras**: Bolsa de objetos y mejoras aplicadas
- **Historia**: Estado de la narrativa y decisiones tomadas

## Estructura de Archivos

### Directorio de Guardado
```
partidas_guardadas/
├── info_guardado.json          # Información de archivos guardados
├── partida_YYYYMMDD_HHMMSS.save # Archivo de partida 1
└── partida_YYYYMMDD_HHMMSS.save # Archivo de partida 2
```

### Archivo de Información (`info_guardado.json`)
```json
{
  "archivos_disponibles": [
    {
      "nombre_archivo": "partida_20241202_143022.save",
      "nombre_partida": "Historia_capitulo_1",
      "fecha_creacion": "2024-12-02T14:30:22",
      "tamaño": 2048
    }
  ],
  "ultima_actualizacion": "2024-12-02T14:30:22"
}
```

## Clase GestorGuardado

### Métodos Principales

#### `guardar_partida(datos_partida, nombre_partida)`
- Guarda una partida con timestamp automático
- Reemplaza el archivo más antiguo si no hay espacio
- Retorna `True` si se guardó exitosamente

#### `cargar_partida(nombre_archivo)`
- Carga una partida guardada
- Retorna los datos de la partida o `None` si falla

#### `eliminar_partida(nombre_archivo)`
- Elimina una partida guardada
- Actualiza la información de archivos
- Retorna `True` si se eliminó exitosamente

#### `obtener_archivos_guardado()`
- Retorna lista de archivos guardados disponibles
- Incluye información de cada archivo

### Métodos de Datos

#### `crear_datos_partida(juego)`
- Crea diccionario con todos los datos del juego
- Incluye estado del jugador, progreso e historia
- Formato optimizado para guardado

#### `aplicar_datos_partida(juego, datos_partida)`
- Restaura el estado del juego desde datos guardados
- Aplica todos los datos al juego actual
- Retorna `True` si se aplicó exitosamente

## Uso en el Juego

### Guardar Partida
```python
# En el modo historia
if tecla == pygame.K_s:
    datos_partida = gestor_guardado.crear_datos_partida(juego)
    nombre_partida = f"Historia_{narrativa.estado_actual.value}"
    gestor_guardado.guardar_partida(datos_partida, nombre_partida)
```

### Cargar Partida
```python
# Desde la pantalla de guardado
archivos = gestor_guardado.obtener_archivos_guardado()
if archivos:
    archivo = archivos[archivo_seleccionado]
    datos_partida = gestor_guardado.cargar_partida(archivo["nombre_archivo"])
    if datos_partida:
        gestor_guardado.aplicar_datos_partida(juego, datos_partida)
```

### Eliminar Partida
```python
# Desde la pantalla de guardado
archivos = gestor_guardado.obtener_archivos_guardado()
if archivos:
    archivo = archivos[archivo_seleccionado]
    gestor_guardado.eliminar_partida(archivo["nombre_archivo"])
```

## Estructura de Datos

### Datos de Partida
```python
{
    "jugador": {
        "nombre": "Héroe",
        "clase": "guerrero",
        "vida_actual": 100,
        "vida_maxima": 100,
        "energia_actual": 50,
        "energia": 50,
        "nivel": 1,
        "experiencia": 0,
        "bolsa_objetos": [...],
        "mejoras_aplicadas": [...]
    },
    "progreso": {
        "piso_actual": 1,
        "monedas_oro": 0,
        "jefes_derrotados": [],
        "estado": "batalla",
        "turno": "jugador"
    },
    "historia": {
        "estado_actual": "introduccion",
        "puntos_moral": 0,
        "decisiones_tomadas": 0,
        "historia_completa": False
    },
    "fecha_guardado": "2024-12-02T14:30:22",
    "version_juego": "1.0"
}
```

## Optimizaciones

### Gestión de Memoria
- **Limpieza automática**: Elimina archivos antiguos
- **Cache de información**: Evita lecturas repetidas
- **Serialización eficiente**: Uso de pickle para datos complejos

### Rendimiento
- **Operaciones asíncronas**: No bloquea el juego
- **Validación de datos**: Verifica integridad de archivos
- **Manejo de errores**: Recuperación ante fallos

## Seguridad

### Validación de Datos
- Verificación de formato de archivos
- Comprobación de integridad de datos
- Manejo de archivos corruptos

### Backup Automático
- Preserva archivos importantes
- Recuperación ante pérdida de datos
- Logs de operaciones

## Integración

### Con Modo Historia
- Guardado automático en puntos clave
- Carga de progreso narrativo
- Sincronización de decisiones

### Con Juego Principal
- Guardado de estado de batalla
- Preservación de objetos y mejoras
- Continuidad de progreso

## Notas Técnicas

- **Formato pickle**: Eficiente para datos complejos
- **Codificación UTF-8**: Soporte completo de caracteres
- **Gestión de errores**: Manejo robusto de excepciones
- **Documentación JSON**: Información legible de archivos 