#include <iostream>
using namespace std;
/*
Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas:
❖ ​‘menor’ si la edad es menor o igual a 12  
❖ ​‘cadete’ si la edad está comprendida entre 13 y 18  
❖ ​‘juvenil’ si la edad es mayor que 18 y no supera los 26  
❖ ​‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores 
*/

int main () {
    int edad = 0;

    cout << "Ingrese su edad: ";
    cin >> edad;

    string resultado;

    if (edad <= 12)
    {
        cout << "Es menor. \n";
    }  else if (edad >= 13 && edad <= 18)
    {
        cout << "Es Cadete. \n";
    } else if (edad > 18 && edad <= 26)
    {
        cout << "Es Juvenil. \n";
    } else {
        cout << "Es Mayor. \n";
    }
    
    return 0;
}