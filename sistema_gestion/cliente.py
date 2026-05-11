# Nombre del estudiante: Alex Stiven Ordoñez Solano
# Grupo: 213023_254
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

from exceptions import ErrorCliente, ErrorValidacion
from logger import Logger

log = Logger()

class Cliente:
    def __init__(self, nombre, email, telefono, id_cliente):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._id_cliente = id_cliente
        self._reservas = []
    
    def get_nombre(self):
        return self._nombre
    
    def get_email(self):
        return self._email
    
    def get_telefono(self):
        return self._telefono
    
    def get_id(self):
        return self._id_cliente
    
    def get_reservas(self):
        return self._reservas
    
    def set_nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 2:
            log.error(f"Nombre inválido: {nombre}")
            raise ErrorValidacion("El nombre debe tener al menos 2 caracteres")
        self._nombre = nombre
    
    def set_email(self, email):
        if not email or "@" not in email:
            log.error(f"Email inválido: {email}")
            raise ErrorValidacion("El email debe contener @")
        self._email = email
    
    def set_telefono(self, telefono):
        if not telefono or len(telefono) < 7:
            log.error(f"Teléfono inválido: {telefono}")
            raise ErrorValidacion("El teléfono debe tener al menos 7 dígitos")
        self._telefono = telefono
    
    def agregar_reserva(self, reserva):
        self._reservas.append(reserva)
    
    def mostrar_info(self):
        return f"ID: {self._id_cliente} | Nombre: {self._nombre} | Email: {self._email} | Tel: {self._telefono}"
