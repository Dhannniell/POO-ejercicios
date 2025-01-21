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
    def __init__(self, fecha, hora, servicio, veterinario):
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
            nombre = input("Por favor, ingrese el nombre del cliente:").strip()
            contacto = input("Por favor, ingrese el contacto: ").strip()
            direccion = input("Por favor, ingrese la direccion: ").strip()
            
            if not nombre or not contacto or not direccion:
                raise ValueError("Es obligatorio completar todos los campos.")
            
            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print("¡Cliente registrado con éxito!")
        
        except ValueError as e:
            print(f"Error: {e}")
    
    
    def registrar_mascota(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente para asociar la mascota:").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("No se encontró al cliente.")
            
            nombre_mascota = input("Por favor, ingrese el nombre de la mascota:").strip()
            especie = input("Por favor, ingrese la especie: ").strip()
            raza = input("Por favor, ingrese la raza: ").strip()
            edad = int(input("Por favor, ingrese la edad: ").strip())
            
            if not nombre_mascota or not especie or not raza or edad <=0:
                raise ValueError("Detalles de la mascota inválidos.")
            
            mascota = RegistrarMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("¡Mascota registrada con éxito!")
            
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def programar_cita(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente:").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota:").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            mascota =next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            servicio = input("Ingrese el servicio (consulta, vacunacion, etc): ").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()
            
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora , "%H:%M")

            if not servicio or not veterinario:
                raise ValueError("Detalles de la cita inválidos.")

            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print("¡Cita programada con éxito!")
            
        except ValueError as e:
            print(f"Error: {e}") 
            
    def actualizar_cita(self):
        try:
            
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            mascota =next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            if not mascota.historial_citas:
                raise ValueError("No hay citas registradas para esta mascota.")
            
            print("Citas disponibles para actualizar:")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i+1}. Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}")
            
            indice = int(input("Seleccione el número de la cita que desea actualizar: ").strip()) -1
            if indice < 0 or indice >= len(mascota.historial_citas):
                raise ValueError("Selección inválida..")
            
            cita = mascota.historial_citas[indice]
            
            print("Deje en blanco los campos que no desee actualizar.")
            
            nueva_fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
            nueva_hora = input("Nueva hora(HH:MM): ").strip()
            nuevo_servicio = input("Nuevo servicio (consulta, vacunacion, etc): ").strip()
            nuevo_veterinario = input("Nuevo veterinario: ").strip()
            
            if nueva_fecha:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                cita.actualizar(fecha = nueva_fecha)
            
            if nueva_hora:
                datetime.strptime(nueva_hora, "%H:%M")
                cita.actualizar(hora = nueva_hora)
                
            if nuevo_servicio:
                cita.actualizar(servicio = nuevo_servicio)
                
            if nuevo_veterinario:
                cita.actualizar(veterinario = nuevo_veterinario)
                
            print("¡Cita actualizada con éxito!")
            
        except ValueError as e:
            print(f"Error: {e}") 
            
    def consultar_historial(self):
        try:
        
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
        
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            mascota =next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            historial = mascota.obtener_historial()
            if not historial:
                print("No hay historial disponible para esta mascota. ")
            else:
                for entrada in historial:
                    print(f"Fecha: {entrada.fecha}, Hora: {entrada.hora}, Servicio: {entrada.servicio}, Veterinario: {entrada.veterinario}")
        
        except ValueError as e:
            print(f"Error: {e}") 
            
    def iniciar(self):
        while True:
            print("\nSistema de Gestión Veterinaria: Huella Feliz.")
            print("1. Registrar Cliente.")
            print("2. Registrar Mascota.")
            print("3. Programar Cita.")
            print("4. Actualizar Cita.")
            print("5. Consultar Historial.")
            print("6. Salir.")
            
            opcion = input("Ingrese su opcion: ").strip()
            
            if opcion == "1":
                self.registrar_clientes()
            elif opcion == "2":
                self.registrar_mascota()
            elif opcion == "3":
                self.programar_cita()
            elif opcion == "4":
                self.actualizar_cita()
            elif opcion == "5":
                self.consultar_historial()
            elif opcion == "6":
                print("¡Gracias por usar nuestro sistema! ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
                
                

if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()
    