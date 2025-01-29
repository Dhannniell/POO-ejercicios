#Metodo de Instancia: vamos a extraer el objeto; usa el prefijo "self"
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def saludar(self):
        return f"Mi animalito se llama {self.name} y tiene {self.age} años"
    
animal1 = Animal("Ginebra", 3)
animal2 = Animal("Toby", 1)

print(animal1.name)
print(animal1.age)
print(animal1.saludar())