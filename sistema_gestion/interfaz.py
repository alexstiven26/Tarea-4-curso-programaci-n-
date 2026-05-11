

import tkinter as tk
from tkinter import messagebox, scrolledtext
from usuario import Usuario
from sistema import SistemaGestion
from exceptions import ErrorCliente, ErrorReserva, ErrorValidacion

class AplicacionGestion:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Login - Sistema de Gestion")
        self.ventana_login.geometry("350x280")
        
        self.usuario = Usuario()
        self.sistema = SistemaGestion()
        
        self.crear_login()
        self.ventana_login.mainloop()
    
    def crear_login(self):
        tk.Label(self.ventana_login, text="SISTEMA DE GESTION", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.ventana_login, text="Login", font=("Arial", 12)).pack(pady=5)
        
        tk.Label(self.ventana_login, text="Usuario:").pack()
        self.usuario_entry = tk.Entry(self.ventana_login)
        self.usuario_entry.pack(pady=5)
        
        tk.Label(self.ventana_login, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self.ventana_login, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Button(self.ventana_login, text="Ingresar", command=self.validar_login, bg="lightblue", width=15).pack(pady=10)
    
    def validar_login(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()
        
        if self.usuario.validar(usuario, password):
            self.ventana_login.destroy()
            self.abrir_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def abrir_principal(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestion - Clientes, Servicios y Reservas")
        self.ventana.geometry("750x600")
        
        tk.Label(self.ventana, text="SISTEMA DE GESTION", font=("Arial", 16)).pack(pady=10)
        
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)
        
        botones = [
            ("1. Registrar Cliente", self.ventana_cliente),
            ("2. Ver Clientes", self.ver_clientes),
            ("3. Ver Servicios", self.ver_servicios),
            ("4. Crear Reserva", self.ventana_reserva),
            ("5. Confirmar Reserva", self.ventana_confirmar),
            ("6. Cancelar Reserva", self.ventana_cancelar),
            ("7. Ver Reservas", self.ver_reservas),
            ("8. Simular Operaciones", self.simular_operaciones),
            ("9. Ver Logs", self.ver_logs),
            ("10. Salir", self.ventana.quit)
        ]
        
        for texto, comando in botones:
            tk.Button(frame_botones, text=texto, command=comando, width=25, height=1).pack(pady=3)
        
        tk.Label(self.ventana, text="RESULTADOS:", font=("Arial", 10)).pack()
        self.texto_resultado = scrolledtext.ScrolledText(self.ventana, height=15, width=85)
        self.texto_resultado.pack(pady=10)
        
        self.ventana.mainloop()
    
    def mostrar(self, texto):
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, texto)
    
    def ventana_cliente(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Cliente")
        ventana.geometry("350x350")
        
        tk.Label(ventana, text="REGISTRAR CLIENTE", font=("Arial", 12)).pack(pady=10)
        
        tk.Label(ventana, text="Nombre:").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack(pady=3)
        
        tk.Label(ventana, text="Email:").pack()
        email_entry = tk.Entry(ventana)
        email_entry.pack(pady=3)
        
        tk.Label(ventana, text="Teléfono:").pack()
        telefono_entry = tk.Entry(ventana)
        telefono_entry.pack(pady=3)
        
        tk.Label(ventana, text="ID Cliente:").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack(pady=3)
        
        def guardar():
            try:
                self.sistema.registrar_cliente(
                    nombre_entry.get(),
                    email_entry.get(),
                    telefono_entry.get(),
                    id_entry.get()
                )
                messagebox.showinfo("Exito", "Cliente registrado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="Guardar", command=guardar, bg="lightgreen").pack(pady=10)
    
    def ver_clientes(self):
        self.mostrar(self.sistema.listar_clientes())
    
    def ver_servicios(self):
        self.mostrar(self.sistema.listar_servicios())
    
    def ventana_reserva(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Crear Reserva")
        ventana.geometry("350x300")
        
        tk.Label(ventana, text="CREAR RESERVA", font=("Arial", 12)).pack(pady=10)
        
        tk.Label(ventana, text="ID Cliente:").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack(pady=3)
        
        tk.Label(ventana, text="Código Servicio:").pack()
        codigo_entry = tk.Entry(ventana)
        codigo_entry.pack(pady=3)
        
        tk.Label(ventana, text="Duración (horas):").pack()
        duracion_entry = tk.Entry(ventana)
        duracion_entry.pack(pady=3)
        
        def crear():
            try:
                duracion = float(duracion_entry.get())
                reserva = self.sistema.crear_reserva(
                    id_entry.get(),
                    codigo_entry.get(),
                    duracion
                )
                messagebox.showinfo("Exito", f"Reserva {reserva.get_codigo()} creada. Estado: PENDIENTE")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="Crear", command=crear, bg="lightgreen").pack(pady=10)
    
    def ventana_confirmar(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Confirmar Reserva")
        ventana.geometry("300x150")
        
        tk.Label(ventana, text="CONFIRMAR RESERVA", font=("Arial", 12)).pack(pady=10)
        
        tk.Label(ventana, text="Código Reserva:").pack()
        codigo_entry = tk.Entry(ventana)
        codigo_entry.pack(pady=3)
        
        def confirmar():
            try:
                self.sistema.confirmar_reserva(codigo_entry.get())
                messagebox.showinfo("Exito", "Reserva confirmada")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="Confirmar", command=confirmar, bg="lightblue").pack(pady=10)
    
    def ventana_cancelar(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Cancelar Reserva")
        ventana.geometry("300x150")
        
        tk.Label(ventana, text="CANCELAR RESERVA", font=("Arial", 12)).pack(pady=10)
        
        tk.Label(ventana, text="Código Reserva:").pack()
        codigo_entry = tk.Entry(ventana)
        codigo_entry.pack(pady=3)
        
        def cancelar():
            try:
                self.sistema.cancelar_reserva(codigo_entry.get())
                messagebox.showinfo("Exito", "Reserva cancelada")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="Cancelar", command=cancelar, bg="lightcoral").pack(pady=10)
    
    def ver_reservas(self):
        self.mostrar(self.sistema.listar_reservas())
    
    def simular_operaciones(self):
        self.mostrar(self.sistema.simular_operaciones())
    
    def ver_logs(self):
        try:
            with open("logs.txt", "r", encoding="utf-8") as file:
                contenido = file.read()
                self.mostrar(contenido if contenido else "No hay logs registrados")
        except FileNotFoundError:
            self.mostrar("Archivo de logs no encontrado")
        except Exception as e:
            self.mostrar(f"Error al leer logs: {str(e)}")
            