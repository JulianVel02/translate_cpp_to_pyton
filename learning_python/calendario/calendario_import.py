"""Calendario"""
# import calendar

# year = int(input("Ingrese el año (4 digitos): "))
# month = int(input("Ingrese el mes (1-12): "))

# print(calendar.month(year, month))


import tkinter as tk
from tkinter import messagebox
import calendar

def mostrar_calendario():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        
        if month < 1 or month > 12:
            raise ValueError("Mes fuera de rango")
        
        cal_text = calendar.month(year, month)
        text_calendar.config(state=tk.NORMAL)
        text_calendar.delete('1.0', tk.END)
        text_calendar.insert(tk.END, cal_text)
        text_calendar.config(state=tk.DISABLED)
    except ValueError as ve:
        messagebox.showerror("Entrada no válida", str(ve))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calendario")

# Etiqueta y campo de entrada para el año
label_year = tk.Label(ventana, text="Año (4 dígitos):")
label_year.grid(row=0, column=0, padx=10, pady=10)
entry_year = tk.Entry(ventana)
entry_year.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y campo de entrada para el mes
label_month = tk.Label(ventana, text="Mes (1-12):")
label_month.grid(row=1, column=0, padx=10, pady=10)
entry_month = tk.Entry(ventana)
entry_month.grid(row=1, column=1, padx=10, pady=10)

# Botón para mostrar el calendario
button_show = tk.Button(ventana, text="Mostrar Calendario", command=mostrar_calendario)
button_show.grid(row=2, column=0, columnspan=2, pady=10)

# Campo de texto para mostrar el calendario
text_calendar = tk.Text(ventana, width=20, height=8, state=tk.DISABLED)
text_calendar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
