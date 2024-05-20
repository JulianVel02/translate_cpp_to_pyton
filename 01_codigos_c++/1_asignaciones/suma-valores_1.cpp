#include <iostream>
using namespace std;

int main()
{
    int a, b;
    int suma, resta, producto;

    cout << "Iingresar el valor de a: ";
    cin >> a;

    cout << "ingresar el balor de b: ";
    cin >> b;

    // suma
    suma = a + b;
    // resta
    resta = a - b;
    // producto
    producto = a * b;

    cout << "La suma de a + b: " << suma << endl;
    cout << "La resta de a - b: " << resta << endl;
    cout << "El producto entre a y b: " << producto << endl;


    return 0;
}