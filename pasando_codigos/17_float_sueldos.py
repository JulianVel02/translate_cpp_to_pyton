from shared_libraries.funciones_generales import leer_enteros
cont_menos1520 = 0
cont_1520_2780 = 0
cont_2780_5999 = 0
cont_mayor_5999 = 0

while True:
    sueldo = leer_enteros(
        "Ingrese el sueldo (0 para finalizar la computacion): ")
    if sueldo == 0:
        break
    if sueldo < 1520:
        cont_menos1520 += 1
    elif 1520 <= sueldo < 2780:
        cont_1520_2780 += 1
    elif 2780 <= sueldo < 5999:
        cont_2780_5999 += 1
    else:
        cont_mayor_5999 += 1

print(f"A) La cantidad de empleados que ganan menos de $1.520 es: {
      cont_menos1520}\n")
print(f"B) La cantidad de empleados que ganan $1.520 pero menos de $2.780 es: {
      cont_1520_2780}\n")
print(f"C) La cantidad de empleados que ganan $2.780 pero menos de $5.599 es: {
      cont_2780_5999}\n")
print(f"D) La cantidad de empleados que ganan mas de $5.999 es: {
      cont_mayor_5999}\n")
