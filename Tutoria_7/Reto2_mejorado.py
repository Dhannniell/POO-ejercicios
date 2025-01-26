#Variable Global
Clientes = []

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
    
    def registrar_mascota():
        pass

    def programar_cita():
        pass
    
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