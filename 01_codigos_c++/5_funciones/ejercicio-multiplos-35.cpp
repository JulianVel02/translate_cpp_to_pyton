// * Dada una serie de números enteros, informar:
// a) su factorial
// b) cuantos múltiplos de 3
// c) cuantos múltiplos de 5
// d) cuantos múltiplos de 3 y de 5
// Utilice las funciones de ejercicios anteriores.

#include <iostream>
#include "../libreria.h"
using namespace std;
int main()
{
    int n;
    cout << "Ingrese la cantidad de numeros: ";
    cin >> n;

    int numero,
        cantMultiplos3 = 0,
        contador3 = 0, contador5 = 0,
        contadorDos = 0;

    for (int i = 0; i < n; i++)
    {
        cout << "Ingrese un numero: \n";
        cin >> numero;

        cout << "Su factorial es: " << factorial(numero) << endl;
        cantidadMultiplos3(numero, contador3);
        cantidadMultiplos5(numero, contador5);
        cantMultiplos3y5(numero, contadorDos);
    }

    cout << "Cantidad de multiplos de 3: " << contador3 << endl;
    cout << "Cantidad de multiplos de 5: " << contador5 << endl;
    cout << "Cantidad de multiplos de 3 y 5: " << contadorDos << endl;

    return 0;
}