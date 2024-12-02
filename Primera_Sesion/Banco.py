#Ejercicio para practicar 

class Banco:
    
    TASA_INTERES = 0.3
    
    def __init__(self,nombre):
        self.nombre = nombre
        
    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.TASA_INTERES = nuevaTasa
    
    @staticmethod
    def conversionDolaresEuros(dolares): 
        return dolares * 0.85

banco1 = Banco("Davivienda")
print("-----------")
print(Banco.conversionDolaresEuros)
print("-----------")
print(banco1.nombre)
print("-----------")
print(Banco.nuevaTasaE())



''' @classmethod
    def nuevaTasaE(self):
        return f"La nueva tasa es {self.TASA_INTERES} con el banco {banco1.nombre}"'''