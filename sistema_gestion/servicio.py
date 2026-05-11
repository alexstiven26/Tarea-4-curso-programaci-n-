# Nombre del estudiante: Alex Stiven Ordoñez Solano
# Grupo: 213023_254
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

from abc import ABC, abstractmethod
from exceptions import ErrorServicio, ErrorValidacion
from logger import Logger

log = Logger()

class Servicio(ABC):
    def __init__(self, codigo, nombre, precio_base):
        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = precio_base
    
    def get_codigo(self):
        return self._codigo
    
    def get_nombre(self):
        return self._nombre
    
    def get_precio_base(self):
        return self._precio_base
    
    @abstractmethod
    def calcular_costo(self, duracion):
        pass
    
    @abstractmethod
    def descripcion(self):
        pass
    
    def validar_duracion(self, duracion):
        if duracion <= 0:
            log.error(f"Duración inválida: {duracion}")
            raise ErrorValidacion("La duración debe ser mayor a 0")
        return True

class ReservaSala(Servicio):
    def __init__(self, codigo, nombre, precio_base, capacidad):
        super().__init__(codigo, nombre, precio_base)
        self._capacidad = capacidad
    
    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self._precio_base * duracion
    
    def descripcion(self):
        return f"Reserva de sala - Capacidad: {self._capacidad} personas"
    
    def get_capacidad(self):
        return self._capacidad

class AlquilerEquipo(Servicio):
    def __init__(self, codigo, nombre, precio_base, tipo_equipo):
        super().__init__(codigo, nombre, precio_base)
        self._tipo_equipo = tipo_equipo
    
    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        costo = self._precio_base * duracion
        if duracion > 5:
            costo = costo * 0.9
        return costo
    
    def descripcion(self):
        return f"Alquiler de equipo - Tipo: {self._tipo_equipo}"
    
    def get_tipo_equipo(self):
        return self._tipo_equipo

class AsesoriaEspecializada(Servicio):
    def __init__(self, codigo, nombre, precio_base, especialidad):
        super().__init__(codigo, nombre, precio_base)
        self._especialidad = especialidad
    
    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        costo = self._precio_base * duracion
        if self._especialidad.lower() == "avanzada":
            costo = costo * 1.2
        return costo
    
    def descripcion(self):
        return f"Asesoría especializada - Especialidad: {self._especialidad}"
    
    def get_especialidad(self):
        return self._especialidad
