# Nombre del estudiante: Alex Stiven Ordoñez Solano
# Grupo: 213023_254
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia

class Usuario:
    def __init__(self):
        self._usuario = "programacion"
        self._password = "programacion"
    
    def validar(self, usuario_ingresado, password_ingresada):
        if usuario_ingresado == self._usuario and password_ingresada == self._password:
            return True
        else:
            return False