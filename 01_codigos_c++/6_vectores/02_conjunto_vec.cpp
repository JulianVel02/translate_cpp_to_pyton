#include <iostream>
using namespace std;

/*
Ingresar un valor entero N (< 30) y a continuación un conjunto de N elementos.
Si el último elemento del conjunto tiene un valor menor que 10 imprimir los
negativos y en caso contrario los demás.
*/

int main()
{
    int N = 0;
    cout << "Ingrese un valor entero para el tamanio (< 30): ";
    cin >> N;

    int vector[N];
    int numero = 0;

    // Entrada de numeros en vector
    for (int i = 0; i < N; i++)
    {
        cout << "Ingresa el numero " << i + 1 << ": ";
        cin >> numero;
        vector[i] = numero;
    }
    if (vector[N - 1] < 10)
    {
        cout << "Los valores negativos: \n";
        for (int i = 0; i < N; i++)
        {
            if (vector[i] < 0)
            {
                cout << vector[i] << " ";
            }
        }
        cout << "\n";
    }
    else
    {
        cout << "Todos los elementos menos el ultimo: \n";
        for (int i = 0; i < N - 1; i++)
        {
            cout << vector[i] << " ";
        }
        cout << "\n";
    }

    return 0;
}