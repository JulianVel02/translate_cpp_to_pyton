"""10 - SETS
        |> Significa grupo o conjunto
            print(primer)
            ^--- Python se va a encargar de remover los elementos duplicados"""
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
print(f"--ORIGINALES--\nPrimero: {primer}\nSegundo: {segundo}")

print("\n--OPERACIONES--")
print(f"Unión de sets: {primer | segundo}")  # Union de sets

print(f"\nIntersección de sets: {primer & segundo}")  # Interseccion de sets

print(f"\nDiferencia de sets: {primer - segundo}")  # Diferencia de sets
# (1, 2) - (2, 3) elimina los elementos del segundo que coincidan en el primero: (1, 3)

print(f"\nDiferencia simetrica: {primer ^ segundo}")
# (1,2,3) ^ (2,3,4) elimina los elementos DUPLICADOS

if 5 in segundo:
    print("Hola mundo")
