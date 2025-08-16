import json
import os
import pickle
from datetime import datetime
from typing import Dict, List, Optional, Any
from modo_historia.narrativa import EstadoHistoria

class GestorGuardado:
    def __init__(self, directorio_guardado: str = "partidas_guardadas"):
        self.directorio_guardado = directorio_guardado
        self.max_archivos = 2  # Solo 2 archivos de guardado
        self.archivo_info = "info_guardado.json"
        
        # Crear directorio si no existe
        if not os.path.exists(self.directorio_guardado):
            os.makedirs(self.directorio_guardado)
        
        # Inicializar información de guardado
        self._inicializar_info_guardado()
    
    def _inicializar_info_guardado(self):
        """Inicializa el archivo de información de guardado"""
        ruta_info = os.path.join(self.directorio_guardado, self.archivo_info)
        
        if not os.path.exists(ruta_info):
            info_inicial = {
                "archivos_disponibles": [],
                "ultima_actualizacion": datetime.now().isoformat()
            }
            self._guardar_json(ruta_info, info_inicial)
    
    def _cargar_info_guardado(self) -> Dict:
        """Carga la información de guardado"""
        ruta_info = os.path.join(self.directorio_guardado, self.archivo_info)
        return self._cargar_json(ruta_info)
    
    def _guardar_info_guardado(self, info: Dict):
        """Guarda la información de guardado"""
        ruta_info = os.path.join(self.directorio_guardado, self.archivo_info)
        info["ultima_actualizacion"] = datetime.now().isoformat()
        self._guardar_json(ruta_info, info)
    
    def _guardar_json(self, ruta: str, datos: Dict):
        """Guarda datos en formato JSON"""
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
    
    def _cargar_json(self, ruta: str) -> Dict:
        """Carga datos en formato JSON"""
        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {}
    
    def _guardar_pickle(self, ruta: str, datos: Any):
        """Guarda datos usando pickle"""
        with open(ruta, 'wb') as archivo:
            pickle.dump(datos, archivo)
    
    def _cargar_pickle(self, ruta: str) -> Any:
        """Carga datos usando pickle"""
        try:
            with open(ruta, 'rb') as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return None
    
    def obtener_archivos_guardado(self) -> List[Dict]:
        """Obtiene la lista de archivos de guardado disponibles"""
        info = self._cargar_info_guardado()
        return info.get("archivos_disponibles", [])
    
    def guardar_partida(self, datos_partida: Dict, nombre_partida: str = None) -> bool:
        """
        Guarda una partida. Si no hay espacio, reemplaza el archivo más antiguo.
        
        Args:
            datos_partida: Datos de la partida a guardar
            nombre_partida: Nombre opcional para la partida
        
        Returns:
            bool: True si se guardó exitosamente, False en caso contrario
        """
        try:
            # Generar nombre de archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"partida_{timestamp}.save"
            
            # Si se proporciona un nombre, usarlo
            if nombre_partida:
                nombre_archivo = f"{nombre_partida}_{timestamp}.save"
            
            ruta_archivo = os.path.join(self.directorio_guardado, nombre_archivo)
            
            # Verificar si hay espacio disponible
            archivos_actuales = self.obtener_archivos_guardado()
            
            if len(archivos_actuales) >= self.max_archivos:
                # Eliminar el archivo más antiguo
                archivo_antiguo = min(archivos_actuales, key=lambda x: x["fecha_creacion"])
                ruta_antiguo = os.path.join(self.directorio_guardado, archivo_antiguo["nombre_archivo"])
                
                if os.path.exists(ruta_antiguo):
                    os.remove(ruta_antiguo)
                
                # Remover de la lista
                archivos_actuales = [a for a in archivos_actuales if a["nombre_archivo"] != archivo_antiguo["nombre_archivo"]]
            
            # Guardar datos de la partida
            datos_guardado = {
                "datos_partida": datos_partida,
                "fecha_guardado": datetime.now().isoformat(),
                "version": "1.0"
            }
            
            self._guardar_pickle(ruta_archivo, datos_guardado)
            
            # Actualizar información de guardado
            nuevo_archivo = {
                "nombre_archivo": nombre_archivo,
                "nombre_partida": nombre_partida or f"Partida {timestamp}",
                "fecha_creacion": datetime.now().isoformat(),
                "tamaño": os.path.getsize(ruta_archivo)
            }
            
            archivos_actuales.append(nuevo_archivo)
            
            info_actualizada = {
                "archivos_disponibles": archivos_actuales,
                "ultima_actualizacion": datetime.now().isoformat()
            }
            
            self._guardar_info_guardado(info_actualizada)
            
            return True
            
        except Exception as e:
            print(f"Error al guardar partida: {e}")
            return False
    
    def cargar_partida(self, nombre_archivo: str) -> Optional[Dict]:
        """
        Carga una partida guardada
        
        Args:
            nombre_archivo: Nombre del archivo a cargar
        
        Returns:
            Dict con los datos de la partida o None si no se puede cargar
        """
        try:
            ruta_archivo = os.path.join(self.directorio_guardado, nombre_archivo)
            
            if not os.path.exists(ruta_archivo):
                return None
            
            datos_guardado = self._cargar_pickle(ruta_archivo)
            
            if datos_guardado and "datos_partida" in datos_guardado:
                return datos_guardado["datos_partida"]
            
            return None
            
        except Exception as e:
            print(f"Error al cargar partida: {e}")
            return None
    
    def eliminar_partida(self, nombre_archivo: str) -> bool:
        """
        Elimina una partida guardada
        
        Args:
            nombre_archivo: Nombre del archivo a eliminar
        
        Returns:
            bool: True si se eliminó exitosamente
        """
        try:
            ruta_archivo = os.path.join(self.directorio_guardado, nombre_archivo)
            
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)
                
                # Actualizar información de guardado
                archivos_actuales = self.obtener_archivos_guardado()
                archivos_actuales = [a for a in archivos_actuales if a["nombre_archivo"] != nombre_archivo]
                
                info_actualizada = {
                    "archivos_disponibles": archivos_actuales,
                    "ultima_actualizacion": datetime.now().isoformat()
                }
                
                self._guardar_info_guardado(info_actualizada)
                return True
            
            return False
            
        except Exception as e:
            print(f"Error al eliminar partida: {e}")
            return False
    
    def crear_datos_partida(self, juego) -> Dict:
        """
        Crea un diccionario con todos los datos necesarios para guardar una partida
        
        Args:
            juego: Instancia del juego actual
        
        Returns:
            Dict con todos los datos de la partida
        """
        datos = {
            "jugador": {
                "nombre": juego.jugador.nombre if juego.jugador else "",
                "clase": juego.jugador.clase.value if juego.jugador else "",
                "vida_actual": juego.jugador.vida_actual if juego.jugador else 0,
                "vida_maxima": juego.jugador.vida_maxima if juego.jugador else 0,
                "energia_actual": juego.jugador.energia_actual if juego.jugador else 0,
                "energia": juego.jugador.energia if juego.jugador else 0,
                "nivel": juego.jugador.nivel if juego.jugador else 1,
                "experiencia": juego.jugador.experiencia if juego.jugador else 0,
                "bolsa_objetos": [obj.__dict__ for obj in juego.jugador.bolsa_objetos] if juego.jugador else [],
                "mejoras_aplicadas": juego.jugador.mejoras_aplicadas if juego.jugador else []
            },
            "progreso": {
                "piso_actual": juego.piso_actual,
                "monedas_oro": juego.monedas_oro,
                "jefes_derrotados": juego.jefes_derrotados,
                "estado": juego.estado,
                "turno": juego.turno
            },
            "historia": {
                "estado_actual": juego.narrativa.estado_actual.value if hasattr(juego, 'narrativa') else "introduccion",
                "puntos_moral": juego.narrativa.puntos_moral if hasattr(juego, 'narrativa') else 0,
                "decisiones_tomadas": len(juego.narrativa.decisiones_tomadas) if hasattr(juego, 'narrativa') else 0,
                "historia_completa": juego.narrativa.historia_completa if hasattr(juego, 'narrativa') else False
            },
            "fecha_guardado": datetime.now().isoformat(),
            "version_juego": "1.0"
        }
        
        return datos
    
    def aplicar_datos_partida(self, juego, datos_partida: Dict) -> bool:
        """
        Aplica los datos de una partida guardada al juego actual
        
        Args:
            juego: Instancia del juego
            datos_partida: Datos de la partida guardada
        
        Returns:
            bool: True si se aplicó exitosamente
        """
        try:
            # Restaurar datos del jugador
            if datos_partida.get("jugador"):
                jugador_data = datos_partida["jugador"]
                if juego.jugador:
                    juego.jugador.nombre = jugador_data.get("nombre", "Héroe")
                    juego.jugador.vida_actual = jugador_data.get("vida_actual", 100)
                    juego.jugador.vida_maxima = jugador_data.get("vida_maxima", 100)
                    juego.jugador.energia_actual = jugador_data.get("energia_actual", 50)
                    juego.jugador.energia = jugador_data.get("energia", 50)
                    juego.jugador.nivel = jugador_data.get("nivel", 1)
                    juego.jugador.experiencia = jugador_data.get("experiencia", 0)
                    juego.jugador.mejoras_aplicadas = jugador_data.get("mejoras_aplicadas", [])
                    
                    # Restaurar objetos
                    juego.jugador.bolsa_objetos.clear()
                    for obj_data in jugador_data.get("bolsa_objetos", []):
                        # Aquí necesitarías recrear los objetos desde los datos
                        pass
            
            # Restaurar progreso
            if datos_partida.get("progreso"):
                progreso = datos_partida["progreso"]
                juego.piso_actual = progreso.get("piso_actual", 1)
                juego.monedas_oro = progreso.get("monedas_oro", 0)
                juego.jefes_derrotados = progreso.get("jefes_derrotados", [])
                juego.estado = progreso.get("estado", "batalla")
                juego.turno = progreso.get("turno", "jugador")
            
            # Restaurar historia
            if datos_partida.get("historia") and hasattr(juego, 'narrativa'):
                historia = datos_partida["historia"]
                juego.narrativa.estado_actual = EstadoHistoria(historia.get("estado_actual", "introduccion"))
                juego.narrativa.puntos_moral = historia.get("puntos_moral", 0)
                juego.narrativa.historia_completa = historia.get("historia_completa", False)
            
            return True
            
        except Exception as e:
            print(f"Error al aplicar datos de partida: {e}")
            return False 