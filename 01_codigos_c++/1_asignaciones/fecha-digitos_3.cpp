#include <iostream>
using namespace std;

//Dada un número entero de la forma (AAAAMMDD), que representa una fecha valida mostrar el dia, mes y año que representa.
int main()
{
    int fecha;
    cout << "Ingrese la fecha en formato AAAAMMDD: ";
    cin >> fecha;

    int dia = fecha % 100; // Obtiene el último par de dígitos que representan el día
    fecha /= 100; // Elimina los últimos dos dígitos para obtener AAAAMM
    int mes = fecha % 100; // Obtiene el siguiente par de dígitos que representan el mes
    int anio = fecha / 100; // Obtiene los primeros cuatro dígitos que representan el año

    cout << "La fecha ingresada es: " << dia << "/" << mes << "/" << anio << endl;

    return 0;
}