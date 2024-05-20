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
    int valorActual;    // Valor actual del lote
    int valorMaximo;    // Mayor valor del lote
    int pos;        // Posicion en la que se encuentra el mayor valor
    int contador = 0;   // Contador para los sublotes
    int suma = 0;       // Sumatoria de los valores del sublote
    float promedio = 0; // Promedio del sublote

    cout << "Ingrese el primer valor del sublote: ";
    cin >> valorActual;

    while (valorActual >= 0)
    {
        contador++;
        suma += valorActual;
        
        // actualizacion del valor max y su pos.
        if (valorActual > valorMaximo) {
            valorMaximo = valorActual;
            pos = contador; // actualizo la posicion relativa del valor maximo dentro del sublote.
        }

        // solicito el siguiente valor del sublote.
        cout << "Ingrese el siguiente valor del sublote (o un valor negativo para finalizar): ";
        cin >> valorActual;
    }

    
    // calcular el promedio del sublote si entraron valores.
    if (contador > 0) {
        promedio = float(suma)/float(contador);
    }

    cout << "El mayor valor encontrado en el sublote fue: ( " << valorMaximo << " ) en la posicion: " << pos << endl;
    cout << "El promedio de los valores del sublote fue: (" << promedio << ")" << endl; 

    return 0;
}
