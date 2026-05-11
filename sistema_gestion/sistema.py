

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from exceptions import ErrorCliente, ErrorServicio, ErrorReserva, ErrorValidacion
from logger import Logger
from datetime import datetime

log = Logger()

class SistemaGestion:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.contador_reservas = 1
        self.cargar_servicios_base()
    
    def cargar_servicios_base(self):
        try:
            self.servicios.append(ReservaSala("S001", "Sala Pequeña", 50000, 10))
            self.servicios.append(ReservaSala("S002", "Sala Grande", 80000, 30))
            self.servicios.append(AlquilerEquipo("E001", "Proyector", 20000, "Multimedia"))
            self.servicios.append(AlquilerEquipo("E002", "Computador Portátil", 15000, "Computo"))
            self.servicios.append(AsesoriaEspecializada("A001", "Asesoría Básica", 60000, "basica"))
            self.servicios.append(AsesoriaEspecializada("A002", "Asesoría Avanzada", 100000, "avanzada"))
            log.info("Servicios base cargados correctamente")
        except Exception as e:
            log.error(f"Error al cargar servicios base: {str(e)}")
    
    def registrar_cliente(self, nombre, email, telefono, id_cliente):
        try:
            for c in self.clientes:
                if c.get_id() == id_cliente:
                    raise ErrorCliente("Ya existe un cliente con esa identificación")
            
            cliente = Cliente(nombre, email, telefono, id_cliente)
            
            try:
                cliente.set_nombre(nombre)
                cliente.set_email(email)
                cliente.set_telefono(telefono)
            except ErrorValidacion as e:
                raise ErrorCliente(str(e))
            
            self.clientes.append(cliente)
            log.info(f"Cliente registrado: {nombre} (ID: {id_cliente})")
            return cliente
            
        except ErrorCliente as e:
            log.error(f"Error al registrar cliente: {str(e)}")
            raise
        except Exception as e:
            log.error(f"Error inesperado al registrar cliente: {str(e)}")
            raise ErrorCliente("No se pudo registrar el cliente")
    
    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.get_id() == id_cliente:
                return cliente
        return None
    
    def listar_clientes(self):
        if not self.clientes:
            return "No hay clientes registrados"
        
        resultado = "=== LISTA DE CLIENTES ===\n"
        for c in self.clientes:
            resultado += c.mostrar_info() + "\n"
        return resultado
    
    def listar_servicios(self):
        if not self.servicios:
            return "No hay servicios disponibles"
        
        resultado = "=== SERVICIOS DISPONIBLES ===\n"
        for s in self.servicios:
            resultado += f"Código: {s.get_codigo()} | {s.get_nombre()} | ${s.get_precio_base()}/hora\n"
            resultado += f"  {s.descripcion()}\n"
        return resultado
    
    def buscar_servicio(self, codigo):
        for servicio in self.servicios:
            if servicio.get_codigo() == codigo:
                return servicio
        return None
    
    def crear_reserva(self, id_cliente, codigo_servicio, duracion):
        try:
            if duracion <= 0:
                raise ErrorValidacion("La duración debe ser mayor a 0")
            
            cliente = self.buscar_cliente(id_cliente)
            if not cliente:
                raise ErrorReserva(f"No se encontró cliente con ID: {id_cliente}")
            
            servicio = self.buscar_servicio(codigo_servicio)
            if not servicio:
                raise ErrorReserva(f"No se encontró servicio con código: {codigo_servicio}")
            
            servicio.validar_duracion(duracion)
            
            codigo_reserva = f"R{self.contador_reservas:04d}"
            reserva = Reserva(codigo_reserva, cliente, servicio, duracion)
            
            self.reservas.append(reserva)
            cliente.agregar_reserva(reserva)
            self.contador_reservas += 1
            
            log.info(f"Reserva creada: {codigo_reserva}")
            return reserva
            
        except (ErrorValidacion, ErrorReserva) as e:
            log.error(f"Error al crear reserva: {str(e)}")
            raise
        except Exception as e:
            log.error(f"Error inesperado al crear reserva: {str(e)}")
            raise ErrorReserva("No se pudo crear la reserva")
    
    def confirmar_reserva(self, codigo_reserva):
        reserva = self.buscar_reserva(codigo_reserva)
        if not reserva:
            raise ErrorReserva(f"No se encontró reserva con código: {codigo_reserva}")
        return reserva.confirmar()
    
    def cancelar_reserva(self, codigo_reserva):
        reserva = self.buscar_reserva(codigo_reserva)
        if not reserva:
            raise ErrorReserva(f"No se encontró reserva con código: {codigo_reserva}")
        return reserva.cancelar()
    
    def completar_reserva(self, codigo_reserva):
        reserva = self.buscar_reserva(codigo_reserva)
        if not reserva:
            raise ErrorReserva(f"No se encontró reserva con código: {codigo_reserva}")
        return reserva.completar()
    
    def buscar_reserva(self, codigo_reserva):
        for reserva in self.reservas:
            if reserva.get_codigo() == codigo_reserva:
                return reserva
        return None
    
    def listar_reservas(self):
        if not self.reservas:
            return "No hay reservas registradas"
        
        resultado = "=== LISTA DE RESERVAS ===\n"
        for r in self.reservas:
            resultado += f"Código: {r.get_codigo()} | Estado: {r.get_estado()} | Cliente: {r.get_cliente().get_nombre()}\n"
        return resultado
    
    def simular_operaciones(self):
        resultados = []
        resultados.append("=== SIMULACIÓN DE OPERACIONES ===\n")
        
        try:
            self.registrar_cliente("Juan Perez", "juan@mail.com", "1234567", "C001")
            resultados.append("1. Cliente C001 registrado correctamente")
        except Exception as e:
            resultados.append(f"1. Error: {str(e)}")
        
        try:
            self.registrar_cliente("Maria Lopez", "maria.mail.com", "7654321", "C002")
            resultados.append("2. Cliente registrado (esto no debería pasar)")
        except Exception as e:
            resultados.append(f"2. Error esperado - Email invalido: {str(e)}")
        
        try:
            self.registrar_cliente("Carlos Ruiz", "carlos@mail.com", "5551234", "C003")
            resultados.append("3. Cliente C003 registrado correctamente")
        except Exception as e:
            resultados.append(f"3. Error: {str(e)}")
        
        try:
            reserva = self.crear_reserva("C001", "S001", 3)
            resultados.append(f"4. Reserva {reserva.get_codigo()} creada correctamente")
        except Exception as e:
            resultados.append(f"4. Error: {str(e)}")
        
        try:
            reserva = self.crear_reserva("C999", "S001", 2)
            resultados.append("5. Reserva creada (esto no debería pasar)")
        except Exception as e:
            resultados.append(f"5. Error esperado - Cliente no existe: {str(e)}")
        
        try:
            reserva = self.crear_reserva("C001", "X999", 2)
            resultados.append("6. Reserva creada (esto no debería pasar)")
        except Exception as e:
            resultados.append(f"6. Error esperado - Servicio no existe: {str(e)}")
        
        try:
            reserva = self.crear_reserva("C001", "S001", -5)
            resultados.append("7. Reserva creada (esto no debería pasar)")
        except Exception as e:
            resultados.append(f"7. Error esperado - Duración invalida: {str(e)}")
        
        try:
            reserva = self.buscar_reserva("R0001")
            if reserva:
                self.confirmar_reserva("R0001")
                resultados.append(f"8. Reserva R0001 confirmada - Costo: ${reserva.get_costo_total()}")
            else:
                resultados.append("8. No se encontró la reserva R0001")
        except Exception as e:
            resultados.append(f"8. Error: {str(e)}")
        
        try:
            self.cancelar_reserva("R9999")
            resultados.append("9. Cancelación procesada (esto no debería pasar)")
        except Exception as e:
            resultados.append(f"9. Error esperado - Reserva no existe: {str(e)}")
        
        try:
            reserva = self.buscar_reserva("R0001")
            if reserva:
                self.completar_reserva("R0001")
                resultados.append(f"10. Reserva R0001 completada")
            else:
                resultados.append("10. No se encontró la reserva R0001")
        except Exception as e:
            resultados.append(f"10. Error: {str(e)}")
        
        resultados.append("\n" + self.listar_clientes())
        resultados.append("\n" + self.listar_servicios())
        resultados.append("\n" + self.listar_reservas())
        
        return "\n".join(resultados)
    