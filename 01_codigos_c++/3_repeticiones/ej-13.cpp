#include <iostream>
using namespace std;

//* Dados N y M números naturales, informar su producto por sumas sucesivas.
int main () {
    int n;
    int m;
    int producto = 0;

    cout << "Ingrese N: ";
    cin >> n;
    cout << "Ingrese M: ";
    cin >> m;

    // El prodcuto de N por M es equivalente a sumar N a si mismo M veces.
    for (int i = 0; i < m; i++)
    {
        producto += n;
    }
    
    cout << "El producto de " << n << " por " << m << " es: " << producto << endl;

    return 0;
}