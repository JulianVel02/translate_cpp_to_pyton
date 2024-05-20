#include <iostream>
using namespace std;

/*
* 1. Exactas
   ! a.Según un valor constante
   ! b.Según una cantidad conocida a priori

* 2. No Exacta
   ! a.Pre Condicional(0..N)
   ! b.Pos Condicional(1..N)
*/

int main()
{
    //* Repeticiones Exactas

    /*
    *A) Segun un valor constante
    Este tipo de repetición se ejecuta un número fijo de veces, conocido de antemano.
    Se utiliza cuando sabemos exactamente cuántas veces queremos que se repita el código*/
    for (int i = 0; i < 5; i++)
    {
        // Bloque de código que se repite 5 veces
    }

    /*
    *B) Segun una cantidad conocida a priori
    Similar al caso anterior, pero la cantidad de veces que se repite en el codigo se define en una variable o expresion.
    */
    int n = 10;
    for (int i = 0; i < n; i++)
    {
        // Bloque de código se repite n veces
    }

    //* Repeticiones No Exactas

    /*
    *A) Pre Condicional(0..N)
    Se ejecuta un numero indeterminado de veces, pero siempre se ejecuta al menos una vez. La condicion de repeticion se verifica al principio del bucle.
    */
    int condicion = 0;
    while (true)
    {
        // Bloque de código que se repite hasta que la condición sea falsa
        if (condicion)
        {
            break; // Sale del bucle
        }
    }

    /*
    *B) Post-Condicional(n..0)
    La condición de repetición se verifica al final del bucle.
    Esto significa que el código dentro del bucle se ejecuta al menos una vez, antes de verificar la condición.
    */
    int contador = 10;
    do
    {
        // Bloque de código que se repite hasta que la condición sea falsa
    } while (contador);

    return 0;
}