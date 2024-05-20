#include <iostream>
using namespace std;

/*
* Dado un conjunto de valores enteros, calcular e informar: 
a) cuántos valores cero hubo
b) promedio de valores positivos
c) sumatoria de valores negativos.       

TODO: Resolver el ejercicio para los siguientes lotes de datos:  
1) 167 valores enteros  
2) N valores, donde el valor de N debe ser leído previamente  
3) El conjunto de valores termina con un valor igual al anterior  
4) Se dan N valores, pero el proceso deberá finalizar si se procesan todos los valores o si la cantidad de ceros supera a cuatro  
5) Se dan N valores, pero el proceso deberá finalizar si se cumple alguna de las condiciones de 4) o si el promedio de positivos resulta mayor que seis.
*/
int main () {
    // variables
    int valor, cantCeros = 0, cantPos = 0, sumNeg = 0;
    double sumPos;
    int contador = 0;

    cout << " <- EJ: Conjunto de valores enteros -> \n \n";
    cout << "Ingrese el primer valor: ";
    cin >> valor;
    int valAnt = valor; // almaceno el valor anterior para detectar la finalizacion

    while (true) {
        contador++; // incremento el contador

        //cuento los 0
        if (valor == 0) {
            cantCeros++;
        } else if (valor > 0) { // cuento y sumo los positivos
            sumPos += valor;
            cantPos++;
        } else { // sumo los negativos
            sumNeg += valor;
        }

        cout << "Ingrese el valor " << (contador + 1) << " (o ingrese 0 para finalizar): ";
        cin >> valor; // entrada del siguiente valor

        if (valor == valAnt) {
            break; // corto el ciclo si el valor es igual al anterior
        }

        // se actualiza el valor anterior
        valAnt = valor;
    }

    float prom = sumPos/cantPos;

    cout << ">----------------------------------------> \n"; 
    cout << "a) Cantidad de ceros: " << cantCeros << endl;
    if (cantPos > 0) {
        cout << "b) Promedio de valores positivos: " << prom << endl;
    } else {
        cout << "b) No se ingresaron valores positivos." << endl;
    }
    cout << "c) Sumatoria de valores negativos: " << sumNeg << endl; 

    return 0;
}