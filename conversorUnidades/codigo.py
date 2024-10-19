import tkinter as tk
from tkinter import messagebox

# Función para convertir USD a CRC
def convertir():
    try:
        usd = entrada_usd.get()
        if not usd:  # Verifica si el campo está vacío
            raise ValueError("El campo no puede estar vacío.")
        
        usd = float(usd) 
        tasa = 513.70  # Actualiza la tasa según la conversión actual (17 de octubre 2024)
        crc = usd * tasa
        resultado.config(text=f"{crc:.2f} CRC")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

# Función para limpiar los campos de entrada y salida
def limpiar():
    entrada_usd.delete(0, tk.END)
    resultado.config(text="0.00 CRC")

# Función para confirmar la salida
def salir():
    if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
        ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()  
ventana.title("Conversor de Moneda USD a CRC")
ventana.geometry("300x150")  # Tamaño ajustado para que sea adecuado

# Widgets
tk.Label(ventana, text="USD:").grid(row=0, column=0, padx=5, pady=5)
entrada_usd = tk.Entry(ventana)
entrada_usd.grid(row=0, column=1, padx=5, pady=5)

# Botones
tk.Button(ventana, text="Convertir", command=convertir).grid(row=1, column=0, columnspan=2, pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).grid(row=2, column=0, columnspan=2, pady=5)

# Resultado de la conversión
resultado = tk.Label(ventana, text="0.00 CRC")
resultado.grid(row=3, column=0, columnspan=2, pady=5)

# Confirmar salida al cerrar la ventana
ventana.protocol("WM_DELETE_WINDOW", salir)

# Ejecutar la aplicación
ventana.mainloop()  
