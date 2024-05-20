#include <iostream>
using namespace std;

// void vectorRecibido(int vector[])
// {
// }

int main()
{
    int n = 5;
    int vector[n];
    int numero = 0;
    for (int i = 0; i < n; i++)
    {
        cout << "Ingresa el numero " << i + 1 << ": ";
        cin >> numero;
        vector[i] = numero;
    }

    cout << "---------------- \n";

    for (int i = 0; i < n; i++)
    {
        cout << vector[i] << endl;
    }

    vectorRecibido(vector);

    return 0;
}