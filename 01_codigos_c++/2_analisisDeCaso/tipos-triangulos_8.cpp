#include <iostream>
using namespace std;

/*
 * Dado un triángulo representado por sus lados L1, L2, L3, determinar e imprimir una leyenda según sea:
 * Si el triángulo es equilatero (todos los lados son iguales) : "Es un Triangulo Equilatero"
 * Si el triángulo es isósceles (dos lados son iguales y uno diferente) : "Es un Triangulo Isóceles"
 * Si el triángulo es escaleno (ningún lado es igual) : "Es un Triangulo Escaleno".
 */

int main()
{
    int ladoUno, ladoDos, ladoTres;
    cout << "Ingrese el L1: ";
    cin >> ladoUno;

    cout << "Ingrese el L2: ";
    cin >> ladoDos;

    cout << "Ingrese el L3: ";
    cin >> ladoTres;

    if (ladoUno == ladoDos && ladoUno == ladoTres)
    {
        cout << "Es un Triangulo Equilatero\n";
    }
    else if (ladoUno == ladoDos || ladoUno == ladoTres || ladoDos == ladoTres)
    {
        cout << "Es un Triangulo Isoceles\n";
    }
    else
    {
        cout << "Es un Triangulo Escaleno\n";
    }

    return 0;
}