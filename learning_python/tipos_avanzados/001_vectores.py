N = 5
vector = [None] * N

for i in range(N):
    numero = int(input(f"Ingresa el numero {i+1}: "))
    vector[i] = numero
print("---------------------- \n")
for i in range(N):
    print(vector[i])
