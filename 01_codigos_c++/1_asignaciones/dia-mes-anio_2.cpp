#include <iostream>
using namespace std;

//Dada una terna de números naturales que representan al día, al mes y al año de una determinada fecha informarla como un solo número natural de 8 dígitos con la forma (AAAAMMDD).
int main()
{
    int anio;
    int mes;
    int dia;

    cout << "Ingrese el anio: " << endl;
    cin >> anio;

    cout << "Ingrese el mes: " << endl;
    cin >> mes;

    cout << "Ingrese el dia: " << endl;
    cin >> dia;

    //Concateno los datos en un sólo número de 8 digitos (AAAAMMDD)
    int fecha =  anio * 1000 + mes * 100 + dia;

    cout << "La fecha es: " << fecha << endl;

    return 0;
}