# Nombre del estudiante: Alex Stiven Ordoñez Solano
# Grupo: 213023_254
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

class ErrorSistema(Exception):
    pass

class ErrorCliente(ErrorSistema):
    pass

class ErrorServicio(ErrorSistema):
    pass

class ErrorReserva(ErrorSistema):
    pass

class ErrorValidacion(ErrorSistema):
    pass
