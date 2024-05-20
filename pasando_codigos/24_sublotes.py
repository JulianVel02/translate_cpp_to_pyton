from shared_libraries.funciones_generales import leer_enteros
sublote_mayor = pos_mayor = None
cant_sublotes = mayor = 0

num = leer_enteros("Ingrese un número: ")
while num >= 0:
    acum = promedio = cant_num_sublote = menor = 0
    cant_sublotes += 1
    while num >= 0:
        if cant_num_sublote == 0:
            menor = num

        acum += num
        cant_num_sublote += 1

        if num > mayor:
            mayor = num
            sublote_mayor = cant_sublotes
            pos_mayor = cant_num_sublote

        if num < menor:
            menor = num
        num = leer_enteros("Ingrese un número: ")
    if cant_num_sublote > 0:
        promedio = acum / cant_num_sublote
        print(f"El promedio del sublote es: {promedio:.2f}")
        print(f"El mínimo del sublote es: {menor}")

    num = leer_enteros("Ingrese un número: ")

print(f"El valor máximo de los sublotes fue: {mayor}. En el sublote: {
    sublote_mayor}. En la posición: {pos_mayor}")
print(f"La cantidad de sublotes es: {cant_sublotes}")
