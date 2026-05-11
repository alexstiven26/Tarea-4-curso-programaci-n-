# Nombre del estudiante: Alex Stiven Ordoñez Solano
# Grupo: 213023_254
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

from datetime import datetime
from exceptions import ErrorReserva, ErrorValidacion
from logger import Logger

log = Logger()

class Reserva:
    def __init__(self, codigo_reserva, cliente, servicio, duracion):
        self._codigo_reserva = codigo_reserva
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._fecha_reserva = datetime.now()
        self._estado = "PENDIENTE"
        self._costo_total = 0
    
    def get_codigo(self):
        return self._codigo_reserva
    
    def get_cliente(self):
        return self._cliente
    
    def get_servicio(self):
        return self._servicio
    
    def get_duracion(self):
        return self._duracion
    
    def get_estado(self):
        return self._estado
    
    def get_fecha(self):
        return self._fecha_reserva
    
    def get_costo_total(self):
        return self._costo_total
    
    def confirmar(self):
        try:
            if self._estado != "PENDIENTE":
                log.error(f"No se puede confirmar reserva {self._codigo_reserva}")
                raise ErrorReserva("Solo se pueden confirmar reservas en estado PENDIENTE")
            
            self._costo_total = self._servicio.calcular_costo(self._duracion)
            self._estado = "CONFIRMADA"
            log.info(f"Reserva {self._codigo_reserva} confirmada. Costo: ${self._costo_total}")
            return True
            
        except ErrorReserva as e:
            log.error(str(e))
            raise
        except Exception as e:
            log.error(f"Error inesperado: {str(e)}")
            raise ErrorReserva("Error al procesar la confirmación")
    
    def cancelar(self):
        try:
            if self._estado == "COMPLETADA":
                log.error(f"No se puede cancelar reserva {self._codigo_reserva}")
                raise ErrorReserva("No se puede cancelar una reserva ya completada")
            
            self._estado = "CANCELADA"
            log.info(f"Reserva {self._codigo_reserva} cancelada")
            return True
            
        except ErrorReserva as e:
            log.error(str(e))
            raise
        except Exception as e:
            log.error(f"Error al cancelar: {str(e)}")
            raise ErrorReserva("Error al procesar la cancelación")
    
    def completar(self):
        try:
            if self._estado != "CONFIRMADA":
                log.error(f"No se puede completar reserva {self._codigo_reserva}")
                raise ErrorReserva("Solo se pueden completar reservas CONFIRMADAS")
            
            self._estado = "COMPLETADA"
            log.info(f"Reserva {self._codigo_reserva} completada")
            return True
            
        except ErrorReserva as e:
            log.error(str(e))
            raise
        except Exception as e:
            log.error(f"Error al completar: {str(e)}")
            raise ErrorReserva("Error al procesar la finalización")
    
    def mostrar_info(self):
        estado_texto = {
            "PENDIENTE": "Pendiente",
            "CONFIRMADA": "Confirmada",
            "CANCELADA": "Cancelada",
            "COMPLETADA": "Completada"
        }
        return f"""
=== RESERVA {self._codigo_reserva} ===
Cliente: {self._cliente.get_nombre()}
Servicio: {self._servicio.get_nombre()}
Duracion: {self._duracion} horas
Estado: {estado_texto.get(self._estado, self._estado)}
Costo total: ${self._costo_total:.2f}
Fecha: {self._fecha_reserva.strftime('%Y-%m-%d %H:%M')}
"""
    
