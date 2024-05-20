#include <iostream>
using namespace std;
/*
* Se dispone de un lote de valores enteros positivos que finaliza con un numero negativo.
todo: El lote esta dividido en sublotes por medio de valores cero. Desarrollar un programa que determine e informe:
?a Por cada sublote el promedio de valores.
?b El total de sublotes procesados.
?c El valor maximo del conjunto, indicando en que sublote se encontró y la posicion relativa del mismo dentro del sublote.
*/
int main()
{
    int numero, cantSublotes = 0, mayor = 0, subloteMayor, posMayor;
    cout << "Ingresar un numero: ";
    cin >> numero;
    while (numero >= 0)
    {
        float acum = 0, promedio;
        int cantNumSublote = 0, menor = 0;
        cout << "Ingrese un numero: " << endl;
        cin >> numero;
        // se suma la cant de sublotes
        cantSublotes++;
        while (numero >= 0)
        {
            if (cantNumSublote == 0)
            {
                menor = numero;
            }

            acum += numero;
            cantNumSublote++;

            if (numero > mayor)
            {
                mayor = numero;
                subloteMayor = cantSublotes;
                posMayor = cantNumSublote;
            }

            if (numero < menor)
            {
                menor = numero;
            }

            cout << "Ingrese un numero: " << endl;
            cin >> numero;
        }
        if (cantNumSublote > 0)
        {
            // se calcula el promedio fuera del while
            promedio = acum / cantNumSublote;
            cout << "El promedio del sublote es: " << promedio << endl;
            cout << "El minimo del sublote es: " << menor << endl;
        }
        if (numero > 0)
        {
            cout << "Ingrese un numero: " << endl;
            cin >> numero;
        }
    }
    cout << "El valor maximo de los sublotes fue: " << mayor << ". En el sublote :" << subloteMayor << ". En la Pos: " << posMayor << endl;
    cout << "La cantidad de sublotes es: " << cantSublotes << endl;

    return 0;
}