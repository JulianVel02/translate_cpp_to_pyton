#include <iostream>
using namespace std;

/*
* Dado un conjunto de valores, que finaliza con un valor nulo, determinar e imprimir (si hubo valores):
?a) El valor máximo negativo
?b) El valor mínimo positivo
?c) El valor mínimo dentro del rango -17.3 y 26.9
?d) El promedio de todos los valores​
*/
int main()
{
    float valorActual, valorMaxNegativo, valorMinPositivo, valorMinRango, sumaValores, promedio;
    int cantidadValores;
    bool hayValores;

    valorMaxNegativo = valorMinPositivo = valorMinRango = 1000;
    sumaValores = 0;
    cantidadValores = 0;
    hayValores = false;

    cout << "Ingrese un conjunto de valores. Finalice con un valor nulo (0)" << endl;

    while (true)
    {
        cout << "Ingrese un valor: ";
        cin >> valorActual;

        if (valorActual == 0)
        {
            break;
        }

        if (!hayValores)
        {
            hayValores = true;
        }

        cantidadValores++;
        sumaValores += valorActual;

        // Determinar el valor máximo negativo
        if (valorActual < 0 && valorActual > valorMaxNegativo)
        {
            valorMaxNegativo = valorActual;
        }

        // Determinar el valor mínimo positivo
        if (valorActual > 0 && valorActual < valorMinPositivo)
        {
            valorMinPositivo = valorActual;
        }

        // Determinar el valor mínimo dentro del rango
        if (valorActual >= -17.3 && valorActual <= 26.9 && valorActual < valorMinRango)
        {
            valorMinRango = valorActual;
        }
    }

    if (hayValores)
    {
        promedio = sumaValores / cantidadValores;

        cout << "Valor maximo negativo: " << valorMaxNegativo << endl;
        cout << "Valor minimo positivo: " << valorMinPositivo << endl;
        cout << "Valor minimo dentro del rango (-17.3 y 26.9): " << valorMinRango << endl;
        cout << "Promedio: " << promedio << endl;
    }
    else
    {
        cout << "No se ha introducido ningun valor." << endl;
    }

    return 0;
}