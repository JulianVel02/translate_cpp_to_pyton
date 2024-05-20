#include <iostream>
using namespace std;

int factorial (int);

int main () {
    int nro;
    
    cout << "De que num queres saber el factorial: ";
    cin >> nro;

    cout << "El factorial de " << nro << ", es: " << factorial(nro);

    return 0;
}


int factorial(int n) {
    int result = 1;
    if (n < 0) {
        cout << "Factorial no esta definido para los negativos. \n";
        return -1;
    }
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}