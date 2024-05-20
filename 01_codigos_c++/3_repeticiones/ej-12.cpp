#include <iostream>
using namespace std;

//* Informar los primeros 100 números naturales y su sumatoria
int main () {
    int n = 0;
    int sumatoria = 0;
    int contador = 100;

    cout << "Los primeros 100 numeros natrales son: \n";
    for (int i = 0; i < contador; i++) {
        n++;
        cout << n << endl;
        sumatoria += n; // es lo mismo que poner: sumatoria = sumatoria + n
    }
    
    cout << "La sumatoria de los primeros 100 numeros naturales es: " << sumatoria << endl;

    return 0;
}