class Animal:
    
    def __init__(self):
        pass
    
    def hablar(self):
        pass
    
class Perro(Animal):
        
    def __init__(self):
            pass
        
    def hablar(self):
            return f" Guau Guau"
        
class Gato(Animal):
        
    def __init__(self):
            pass
        
    def hablar(self):
            return f" Miau Miau"
        
animales = [Perro(),
            Gato()

]

for animal in animales:
    print(animal.hablar())