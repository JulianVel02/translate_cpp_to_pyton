"""Ejercicio donde se calculan los puntos por partido de K cantidad de equipos"""

k = int(input("Ingrese el num de equipos: "))
for equipo in range(1, k+1):
    PUNTAJE = 0
    print(f"Equipo {equipo}:")
    for partido in range(1, k+1):
        resultado = input(f"Ingrese el resultado del partido {
                          partido} (P/E/G): ").upper()
        if resultado == 'G':
            PUNTAJE += 3
        elif resultado == 'E':
            PUNTAJE += 1
    print(f"Equipo {equipo} -> Puntaje total: {PUNTAJE}. \n")
