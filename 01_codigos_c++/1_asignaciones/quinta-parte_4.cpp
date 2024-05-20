#include <iostream>
using namespace std;

/*
A partir de un valor entero ingresado por teclado, se pide informar:
a) La quinta parte de dicho valor
b) El resto de la división por 5
c) La séptima parte del resultado del punto a)
*/
int main()
{
    int num;

    cout << "Ingrese un numero entero: ";
    cin >> num;

    // Calcular la quinta parte
    float quintaParte = (float)num / 5;
    cout << "La quinta parte es: " << quintaParte << endl;

    // Calcular el residuo de la division por 5
    float resto = num % 5;
    cout << "El residuo de la division por 5 es: " << resto << endl;

    // Calcular la septima parte
    float septimaParte = quintaParte / 7;
    cout << "La septima parte es: " << septimaParte << endl;

    return 0;
}