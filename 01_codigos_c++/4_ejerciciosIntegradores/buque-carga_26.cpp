#include <iostream>
using namespace std;
/*
*Un buque de carga traslada 100 contenedores a tres diferentes puertos del país.
*Los puertos se identifican con los números 1, 2 y 3.
*De cada contenedor que el buque traslade se registran los siguientes datos:
TODO Identificación del contenedor
TODO Peso del contenedor en kg
TODO Puerto de arribo (un valor de 1 a 3).
* Se pide calcular e informar:
1) El peso total que el buque debe trasladar
2) La identificación del contenedor de mayor peso
3) La cantidad de contenedores que debe trasladar a cada puerto
*/
int main()
{
    int cantContenedores = 3;
    int puertoArribo, cantPuerto1 = 0, cantPuerto2 = 0, cantPuerto3 = 0;
    float peso, acum = 0, mayorPeso = 0;
    string identificacion, identMayor;

    for (int i = 0; i < cantContenedores; i++)
    {
        cout << "Ingrese identif. del contenedor: ";
        cin >> identificacion;

        cout << "Ingrese el peso del contenedor: ";
        cin >> peso;

        cout << "Ingrese el puerto de arribo (1, 2 o 3): ";
        cin >> puertoArribo;

        acum += peso;
        if (peso > mayorPeso)
        {
            mayorPeso = peso;
            identMayor = identificacion;
        }

        if (puertoArribo == 1)
        {
            cantPuerto1++;
        }
        else if (puertoArribo == 2)
        {
            cantPuerto2++;
        }
        else
        {
            cantPuerto3++;
        }

        cout << endl
             << endl;
    }

    cout << "La cantidad de peso del buque es: " << acum << endl;
    cout << "La identificacion del contenedor con mas peso es: " << identMayor << endl;
    cout << "Cantidad de contenedores al puerto 1: " << cantPuerto1 << endl;
    cout << "Cantidad de contenedores al puerto 2: " << cantPuerto2 << endl;
    cout << "Cantidad de contenedores al puerto 3: " << cantPuerto3 << endl;

    return 0;
}