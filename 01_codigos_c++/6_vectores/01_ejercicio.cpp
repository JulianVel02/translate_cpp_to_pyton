#include <iostream>
#include "../libreria.h"
using namespace std;

int main()
{
    int N;
    cout << "Ingrese el tamanio del vector menor a 25: ";
    cin >> N;
    int vector[N];

    int cont = 0;
    for (int i = 0; i < N; i++)
    {
        vector[i] = cont;
        cont += 2;
    }
    for (int i = 0; i < N; i++)
    {
        cout << vector[i]
             << endl;
    }

    return 0;
}