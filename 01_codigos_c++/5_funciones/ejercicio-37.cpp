#include <iostream>
using namespace std;

void sumarTiempo(int horaInicial, int tiempoAdicional, int &nuevaHora) {
    int segundosTotales = (horaInicial % 100 + tiempoAdicional % 100) % 60;
    int minutosTotales = ((horaInicial % 10000 / 100 + tiempoAdicional % 10000 / 100) + (horaInicial % 100 + tiempoAdicional % 100) / 60) % 60;
    int horasTotales = ((horaInicial / 10000 + tiempoAdicional / 10000) + (horaInicial % 10000 / 100 + tiempoAdicional % 10000 / 100 + (horaInicial % 100 + tiempoAdicional % 100) / 60) / 60) % 24;

    nuevaHora = horasTotales * 10000 + minutosTotales * 100 + segundosTotales;
}

int main() {
    int horaInicial, tiempoAdicional, nuevaHora;
    cout << "Ingrese la hora inicial (HHMMSS): ";
    cin >> horaInicial;
    cout << "Ingrese el tiempo adicional (HHMMSS): ";
    cin >> tiempoAdicional;

    sumarTiempo(horaInicial, tiempoAdicional, nuevaHora);

    cout << "La nueva hora es: " << nuevaHora << endl;

    return 0;
}
