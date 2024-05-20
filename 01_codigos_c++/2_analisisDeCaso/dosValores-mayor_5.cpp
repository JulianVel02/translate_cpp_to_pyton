#include <iostream>
using namespace std;

// Dados dos valores enteros y distintos, emitir una leyenda apropiada que informe cuál es el mayor entre ellos.
int main()
{
    int a, b;
    cout << "Ingrese dos numeros enteros y distintos para informarle cual es el mayor entre ellos. \n";
    cout << "numero A: " << endl;
    cin >> a;
    cout << "numero B: " << endl;
    cin >> b;

    if (a > b)
    {
        cout << "A es mayor que B" << endl;
    }
    else if (b > a)
    {
        cout << "B es mayor que A" << b << endl;
    }
    else
    {
        cout << "Los numeros son iguales." << endl;
    }

    return 0;
}