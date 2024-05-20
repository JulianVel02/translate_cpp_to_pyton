#include <iostream>
using namespace std;

// Dadas dos fechas informar cual es la más reciente. Determine cuáles serían los datos de entrada y las leyendas a informar de acuerdo al proceso solicitado.
int main()
{
    // AAAMMDD
    int fechaUno, fechaDos;
    cout << "Ingrese la primera fecha (AAAAMMDD): \n";
    cin >> fechaUno;

    cout << "Ingrese la segunda fecha (AAAAMMDD): \n";
    cin >> fechaDos;

    if (fechaUno > fechaDos) {
        cout << "La fecha 1 es mas reciente que la  fecha 2." << endl;
    } else if (fechaDos > fechaUno) {
        cout << "La fecha 2 es mas reciente que la fecha 1." << endl;
    } else {
        cout << "Las fechas son iguales." << endl;
    }

    return 0;
}