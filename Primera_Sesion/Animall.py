#Metodo de clase: 
class Animall:
    
        cantidadAnimales = 0
        
        def __init__(self, name):
            self.name = name
            Animall.cantidadAnimales += 1
            
        # Los decoradores pueden cambiar, mutar un metodo  y documentar el codigo, (es una buena practica )   
        @classmethod 
        def totalAnimales(cls):
            return f"Tengo {cls.cantidadAnimales} animalitos"
    
animalito1 = Animall("Ron")
animalito2 = Animall("Rayo")
animalito25 = Animall("Toby")

print(animalito1.name)
print(Animall.totalAnimales())