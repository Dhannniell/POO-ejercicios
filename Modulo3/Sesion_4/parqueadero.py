import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class Vehiculo:
    def __init__(self, placa, hora_entrada):
        self.placa = placa
        self.hora_entrada = hora_entrada
        
    def calcular_tiempo(self):
        hora_salida = datetime.datetime.now()
        tiempo_total = hora_salida - self.hora_entrada
        return tiempo_total.total_seconds() / 60
    
class ParqueaderoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Parqueadero")
        self.root.geometry("500x400")
        
        self.vehiculos = {}
        
        # Entrada de la placa
        tk.Label(root, text= "Placa del Vehiculo: ").pack(pady=5) # Texto
        self.entry_placa = tk.Entry(root) # Caja de texto
        self.entry_placa.pack(pady=5)
        
        # Botones
        tk.Button(root, text= "Registro de Entrada", command= "").pack(pady = 5)
        tk.Button(root, text= "Registro de Salida", command= "").pack(pady = 5)
        
        #Tabla de Vehiculos 
        self.tree = ttk.Treeview(root, columns=("Placa", "Hora de Entrada"), show="headings")
        self.tree.heading("Placa", text="Placa")
        self.tree.heading("Hora de Entrada", text= "Hora de Entrada")
        self.tree.pack(pady=10, fill="both", expand=True)
        
root = tk.Tk()
app = ParqueaderoApp(root)
root.mainloop()