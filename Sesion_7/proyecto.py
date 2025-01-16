from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre 
        self.contacto = contacto
        self.direccion = direccion
        
    @abstractmethod
    def mostrar_informacion(self):
        pass 
    
class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = []
        
    @abstractmethod
    def agregar_al_historial(self, detalles_servicio):
        pass
    
class Cita(ABC):
    def __intit__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora 
        self.servicio = servicio
        self.veterinario = veterinario

        @abstractmethod
        def actualizar(self, **kwargs):
            pass 

# Definicion de las Subclases
class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []
        
        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)
        
        def mostrar_informacion(self):
            return f"Cliente: {self.nombre}, Contacto {self.contacto}, Direccion {self.direccion}"
        
class RegistrarMascota(Mascota):
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)
        
    def obtener_historial(self):
        return self.historial_citas
    
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)

class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []
        
    def registrar_clientes(self):
        try:
            nombre = input("Ingrese el nombre del cliente: ").strip()
            contacto = input("Ingrese el contacto: ").strip
            direccion = input("Ingrese la direccion: ").strip()
            
            if not nombre or not contacto or not direccion:
                raise ValueError("Todos los campos son obligatorios")
            
            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print("Cliente registrado con exito!")
        
        except ValueError as e:
            print(f"Error: {e}")
    
    
    def registrar_mascota