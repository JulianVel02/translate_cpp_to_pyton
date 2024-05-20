#include <iostream>
#include "../libreria.h"
using namespace std;

int main()
{
    int edad;
    cout << "Ingrese su edad para conocer su Grupo Etario: ";
    cin >> edad;

    cout << "Pertenece al Grupo Etario Nro: " << EdadAGrupoEtario(edad);

    return 0;
}