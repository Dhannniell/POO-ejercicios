#Ejercicio para practicar 

class Banco:
    TASA_INTERES = 0.3  #Tasa de interes inicial
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    @classmethod
    def cambiarTasa(cls,nuevaTasa):
        cls.TASA_INTERES = nuevaTasa
    
    @classmethod
    def nuevaTasaDescripcion(cls, banco):
        return f"La nueva tasa es {cls.TASA_INTERES} con el banco {banco.nombre}"
    
    @staticmethod
    def conversionDolaresEuros(dolares):
        return dolares * 0.85
    
# Crear un obejeto de la clase Banco

banco1 = Banco("Davivivenda")

# Cambiar la tasa de interes 
Banco.cambiarTasa(0.35)

# Imprimir la conversion de dolares a euros

print("---------------")
print(Banco.conversionDolaresEuros(100)) #ejemplo con 100 dolares

# Imprimir el nombre del banco
print("---------------")
print(banco1.nombre)

# Imprimir la nueva tasa de interes 
print("---------------")
print(Banco.nuevaTasaDescripcion(banco1))
