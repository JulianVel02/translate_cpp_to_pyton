#include <iostream>
using namespace std;

//* ​Dados N valores informar el mayor, el menor y en qué posición del conjunto fueron ingresados.
int main()
{
    int n;
    int mayor, menor;
    int posicionMayor, posicionMenor;
    int valorActual, posicionActual = 1; // Inicializamos posicionActual en 1 aquí

    cout << "Ingrese la cantidad de valores a analizar: ";
    cin >> n;

    cout << "Ingrese un numero: ";
    cin >> valorActual;

    // inicializar variables
    mayor = menor = valorActual;
    posicionMayor = posicionMenor = posicionActual;

    for (int i = 1; i < n; i++)
    {
        // lee el valor actual
        cout << "Ingrese un numero: ";
        cin >> valorActual;

        posicionActual++;

        if (valorActual > mayor)
        {
            mayor = valorActual;
            posicionMayor = posicionActual;
        }
        if (valorActual < menor)
        {
            menor = valorActual;
            posicionMenor = posicionActual;
        }
    }

    cout << "- El numero menor es: " << menor << ". Y se ubica en la posicion: " << posicionMenor << endl;
    cout << "- El numero Mayor es: " << mayor << ". Y se ubica en la posicion: " << posicionMayor << endl;

    return 0;
}