#include <iostream>
using namespace std;

//* Dado un valor M determinar y emitir un listado con los M primeros múltiplos de 3 que no lo sean de 5, dentro del conjunto de los números naturales
int main()
{
    int m;
    int i = 1;
    int multiplos3No5 = 0;

    // Mensaje de bienvenida
    cout << "**Programa para encontrar los M primeros multiplos de 3 que no lo sean de 5**" << endl;
    // Ingreso de la cant de numeros
    cout << "Ingrese la cantidad de numeros a evaluar: ";
    cin >> m;

    // Bucle para encontrar los M primeros multiplos
    while (multiplos3No5 < m)
    {
        if (i % 3 == 0)
        {
            // se podria agregar (i % 5 != 0), pero es redundante pq si un número es divisible por 3, significa que no puede ser divisible por 5 al mismo tiempo
            cout << "-> " << i << endl;
            multiplos3No5++;
        }
        i++;
    }

    return 0;
}