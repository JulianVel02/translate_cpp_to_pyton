#include <iostream>
using namespace std;

int calcularMCD(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main()
{
    int p, q;
    cout << " ingrese numerador y denominador: ";
    cin >> p;
    cin >> q;
    int mcd;

    mcd = calcularMCD(p, q);

    cout << " la fraccion simplificada es : " << p / mcd << "/" << q / mcd << endl;

    return 0;
}