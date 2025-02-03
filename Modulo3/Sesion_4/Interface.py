import tkinter as tk

def convertir():
    try:
        celcius = float(entry.get())
        fahrenheit = (celcius * 9/5) + 32
        resultado.config(text= f"Resultado: {fahrenheit:.1f} °F")
    
    except:
        resultado.config(text = "Ingrese un numero valido")

#configuracion de la ventana
root = tk.Tk()
root.title("Conversor de Temperatura.")
root.geometry("400x300")

#Wifgets 
tk.Label(root, text = "Ingrese temperatura en °C:")
entry = tk.Entry(root)
entry.pack(pady = 5)

tk.Button(root, text = "Convertir", command = convertir).pack(pady = 5)
resultado = tk.Label(root, text = "Resultado: ")
resultado.pack(pady = 5)


root.mainloop()

