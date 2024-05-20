#include <iostream>
using namespace std;

/*
​En un torneo de fútbol participan K equipos. El torneo se juega con el sistema de todos contra todos. Por cada partido disputado por un equipo se dispone de la siguiente información:
a) Nro. de equipo,
b) Código del resultado ('P'= Perdido, 'E'= Empatado, 'G'= Ganado).

Se arma un lote de datos con todos los resultados del torneo, agrupados por Nro. de equipo. Desarrollar el programa que imprima:
Por cada equipo, su número y el puntaje total que obtuvo (suma 3 si gana, y 1 si empata).
*/
int main()
{
    int K; // cantidad de equipos
    cout << "Ingrese el num de equipos: ";
    cin >> K;

    // bucle para cda equipo
    for (int equipo = 1; equipo <= K; equipo++) {
        int puntajeTotal = 0; // puntaje total del equipo
        // solicito resultados de cada partido para este equipo
        cout << "Equipo " << equipo << ": \n";
        for (int partido = 1; partido <= K; partido++) {
            char resultado;
            cout << "Ingrese el resultado del partido " << partido << " (P/E/G): ";
            cin >> resultado;

            // sumo puntos segun el resultado
            if (resultado == 'G') {
                puntajeTotal += 3; //ganan 3ptos.
            } else if (resultado == 'E') {
                puntajeTotal += 1; //empatan 1pto.
            }
        }

        // muestro el num del equipo y su puntaje total
        cout << "Equipo " << equipo << " -> Puntaje total: " << puntajeTotal << endl;
    }

    return 0;
}