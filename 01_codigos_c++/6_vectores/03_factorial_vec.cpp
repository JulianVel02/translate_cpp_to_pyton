#include <iostream>
#include "../libreria.h"
using namespace std;

int main()
{
    int N;
    cout << "Ingrese el tamanio del vector: ";
    cin >> N;

    int numero;
    int vec[N], vecFactorial[N];

    for (int i = 0; i < N; i++)
    {
        cout << "Ingresa el numero " << i + 1 << ": ";
        cin >> numero;
        vec[i] = numero;
        vecFactorial[i] = fact(vecFactorial[i]);
        cout << "El factorial de: " << vec[i] << " es: " << vecFactorial[i] << "\n";
    }

    // for (int i = 0; i < N; i++)
    // {
    // fact[i] = factorial(fact[i])
    //       cout
    //   << "El factorial de: " << vec[i] << " es: " << fact[i] << "\n";
    // }

    return 0;
}