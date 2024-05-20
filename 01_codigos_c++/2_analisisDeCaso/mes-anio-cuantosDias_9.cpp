#include <iostream>
using namespace std;

int main()
{
    int mes, anio, dias;
    cout << "Ingrese el mes (en formato numerico, ej. enero=1, febrero=2, etc.): ";
    cin >> mes;
    cout << "Ingrese el anio: ";
    cin >> anio;

    if (mes == 2)
    {
        if ((anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0))
        { // es bisiesto
            dias = 29;
        }
        else
        {
            dias = 28;
        }
    }
    else if (mes % 2 != 0)
    {
        dias = 30;
    }
    else
    {
        dias = 31;
    }

    cout << "El mes " << mes << " del anio " << anio << " tiene " << dias << " dias." << endl;

    return 0;
}