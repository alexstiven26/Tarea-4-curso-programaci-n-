

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