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
    
    
    def registrar_mascota(self):
        try:
            nombre_cliente = input("Ingrese el nombre del Cliente al asociar la mascota: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie: ").strip()
            raza = input("ingrese la raza: ").strip()
            edad = int(input("Ingrese la edad: ").strip())
            
            if not nombre_mascota or not especie or not raza or edad <=0:
                raise ValueError("Detalles de la mascota invalidos")
            
            mascota = RegistrarMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("Mascota registrada con exito")
            
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def programar_cita(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            mascota =next((m for m in self.cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            servicio = input("Ingrese el servicio (consulta, vacunacion, etc): ").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()
            
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora , "%H:%M")

            if not servicio or not veterinario:
                raise ValueError("Detalle de la cita invalidos.")

            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print("Cita programada con extio")
            
        except ValueError as e:
            print(f"Error: {e}") 