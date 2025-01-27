#Variable Global
clientes = []

#Clases principales
class SistemaVeterinaria:
    class Persona:
        id_contador = 1
        
        def __init__(self, nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_contador
            self.nombre = nombre
            self.contacto = contacto
            #operacion 
            SistemaVeterinaria.Persona.id_contador += 1
            
    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion, ):
            super().__init__(nombre, contacto)
            self.direccion = direccion 
            self.mascota = []
            
        def agregar_mascota(self, mascota):
            self.mascota.append(mascota)
            
    class Mascota:
        id_contador = 1
        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterinaria.Mascota.id_contador 
            self.nombre = nombre
            self.especie = especie
            self.raza = raza 
            self.edad = edad
            self.historial_citas = []
            
            SistemaVeterinaria.Mascota.id_contador += 1
            
    class Cita:
        id_contador = 1
        
        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterinaria.Cita.id_contador
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            
            SistemaVeterinaria.Cita.id_contador += 1
            
            
#Funciones del sistema

    def registrar_clientes():
            print("╔══════════════════════════════════════════╗")
            print("║         REGISTRO DE CLIENTE              ║")
            print("╚══════════════════════════════════════════╝")
            
            # Solicita los datos del cliente mediante la entrada del usuario.
            nombre = input("Por favor, ingrese el nombre del cliente:").strip()
            contacto = input("Por favor, ingrese el contacto: ").strip()
            direccion = input("Por favor, ingrese la direccion: ").strip()
            
            cliente = SistemaVeterinaria.Cliente(nombre, contacto, direccion)
    
    #def registrar_mascota():
        
            print("╔══════════════════════════════════════════╗")
            print("║         REGISTRO DE MASCOTA              ║")
            print("╚══════════════════════════════════════════╝")
            
            # Solicita los detalles de la mascota.
            nombre_mascota = input("Por favor, ingrese el nombre de la mascota:").strip()
            especie = input("Por favor, ingrese la especie: ").strip()
            raza = raza = input("Por favor, ingrese la raza: ").strip()
            edad = int(input("Por favor, ingrese la edad: "))
            
            mascota = SistemaVeterinaria.Mascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            
            clientes.append(cliente)
            
    def programar_cita():
        
        cliente_id = int(input("Ingrese el ID del cliente: "))
        cliente = next((c for c in clientes if c.id == cliente_id), None)

        if not clientes:
            print("Cliente no encontrado.")
            return
        
    def actualizar_citas():
        pass
        
    def consultar_historial():
        pass

#Menu Principal 
    def iniciar(self):
        while True:
            print("╔══════════════════════════════════════════╗")
            print("║         Sistema de Gestión Veterinaria   ║")
            print("║               Huella Feliz               ║")
            print("╠══════════════════════════════════════════╣")
            print("║ 1. Registrar Cliente.                    ║")
            print("║ 2. Registrar Mascota.                    ║")
            print("║ 3. Programar Cita.                       ║")
            print("║ 4. Actualizar Cita.                      ║")
            print("║ 5. Consultar Historial.                  ║")
            print("║ 6. Salir.                                ║")
            print("╚══════════════════════════════════════════╝")
            
            opcion = input("Ingrese su opcion: ").strip()
            
            if opcion == "1":
                self.registrar_clientes()
            elif opcion == "2":
                self.registrar_mascota()
            elif opcion == "3":
                self.programar_cita()
            elif opcion == "4":
                self.actualizar_citas()
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