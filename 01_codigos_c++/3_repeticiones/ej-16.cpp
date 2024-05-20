#include <iostream>
using namespace std;

//* Ingresar e informar valores, mientras que el valor ingresado no sea negativo. Informar la cantidad de valores ingresados.
int main()
{
    int num;
    int numIngresados = 0;

    do
    {
        cout << "Ingrese un numero: ";
        cin >> num;
        if (num >= 0)
        {
            numIngresados++;
        }
    } while (num >= 0);

    /*
    //* pido primer numero
    cout << "Ingrese un numero: ";
    cin >> num;

    //* ingreso un num inicial
    numIngresados++;

    while (num >= 0) {
        //* pido siguiente numero
        cout << "Ingrese un numero: ";
        cin >> num;
        //* se incrementa el contador por cada num ingresado
        if (num >= 0) {
            numIngresados++;
        }
    }
    */

    cout << "Numero de valores ingresados: " << numIngresados << endl;

    return 0;
}