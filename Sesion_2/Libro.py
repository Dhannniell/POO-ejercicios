class Libro:
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def descripcion(self):
        return f"Libro: {self.titulo} Autor:{self.autor}"
    
    def __str__(self):
        return f"Libro: {self.titulo} Autor:{self.autor} STR"
    

class LibroDigital(Libro):
    
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor,)
        self.formato = formato
    
    def descripcion(self):
        return f"Libro: {self.titulo} Autor:{self.autor} Formato: {self.formato}"
    
    def __str__(self):
        return f"Libro: {self.titulo} Autor:{self.autor} Formato: {self.formato} STR"
    
    
libro1 = Libro("La Peste", "Albert Camus")
librodigital1 = LibroDigital("El Conde de Montecristo","Alexandre Dumas", "PDF")

print(libro1.__str__())
print(libro1.descripcion())

print("-------------------------------------------------------------------------------------------")

print(librodigital1.__str__())
print(librodigital1.descripcion())


# Si ya existe una variable en Python que nos permite convertir 
#clases en caracteres no es necesario implementar un metodo (__str__)

