

from datetime import datetime

class Logger:
    def __init__(self, archivo="logs.txt"):
        self.archivo = archivo
    
    def registrar(self, mensaje, tipo="INFO"):
        try:
            with open(self.archivo, "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] [{tipo}] {mensaje}\n")
        except Exception as e:
            print(f"Error al escribir en log: {e}")
    
    def error(self, mensaje):
        self.registrar(mensaje, "ERROR")
    
    def info(self, mensaje):
        self.registrar(mensaje, "INFO")