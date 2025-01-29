"""Clase 'Libro': Crea una clase llamada 'Libro' que tenga los atributos: Titulo y Autor,
impletementa un metodo 'descripcion' que devulve un texto como: "El Libro{titulo} fue escrito 
por {Autor}"""

class Libro:
    #Atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    #Metodos
    def descripcion(self):
        return f"El libro {self.titulo} fue escrito por {self.autor}"
    
libro1 = Libro("El señor del los anillos", "JJR Tolkien") 
libro2 = Libro("Harry Potter y la piedra filosofal", "J.K Rowling") 
    
print(libro1.descripcion())
print("------------------------------------------------------------------------")
print(libro2.descripcion())