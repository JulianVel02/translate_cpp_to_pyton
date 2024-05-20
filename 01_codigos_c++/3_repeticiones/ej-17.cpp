#include <iostream>
using namespace std;

/*
*Se ingresa un conjunto de valores float, cada uno de los cuales representan el sueldo de un empleado, excepto el último valor que es cero e indica el fin del conjunto. Se pide desarrollar un programa que determine e informe:  
?a) Cuántos empleados ganan menos $1.520.  
?b) Cuántos ganan $1.520 o más pero menos de $2.780.  
?c) Cuántos ganan $2.780 o más pero menos de $5.999.  
?d) Cuántos ganan $5.999 o más.
*/
int main () {
    float sueldo = 0;
    int contMenos1520 = 0;
    int cont1520o2780 = 0;
    int cont2780o5999 = 0;
    int contMayor5999 = 0;

/*
    while (sueldo != 0) {
        //* Se lee el sueldo dentro del while
        cout << "ingrese su sueldo (ingrese 0 para terminar el programa): ";
        cin >> sueldo;
        
        if (sueldo < 1520) {
            contMenos1520++;
        } else if (sueldo >= 1520 && sueldo < 2780) {
            cont1520o2780++;
        } else if (sueldo >= 2780 && sueldo < 5999) {
            cont2780o5999++;
        } else {
            contMayor5999++;
        }
    }
*/

    // Bucle N-1
    //* Se lee el primer sueldo fuera del while
    cout << "Ingrese el sueldo: ";
    cin >> sueldo;

    while (sueldo != 0) {
        if (sueldo < 1520) {
        contMenos1520++;
        } else if (sueldo >= 1520 && sueldo < 2780) {
            cont1520o2780++;
        } else if (sueldo >= 2780 && sueldo < 5999) {
            cont2780o5999++;
        } else {
      contMayor5999++;
    }
    // Leer el siguiente sueldo
    cout << "Ingrese el sueldo (0 para finalizar la computacion): ";
    cin >> sueldo;
  }
    
    // do {
    //     cout << "Ingrese su sueldo (ingrese 0 para terminar el programa): ";
    //     cin >> sueldo;

    //     if (sueldo < 1520) {
    //     contMenos1520++;
    //     } else if (sueldo >= 1520 && sueldo < 2780) {
    //     cont1520o2780++;
    //     } else if (sueldo >= 2780 && sueldo < 5999) {
    //     cont2780o5999++;
    //     } else {
    //     contMayor5999++;
    //     }
    // } while (sueldo != 0);
    
    
    cout << "A) La cantidad de empleados que ganan menos de $1.520 es: " << contMenos1520 << endl;
    cout << "B) La cantidad de empleados que ganan $1.520 pero menos de $2.780 es: " << cont1520o2780 << endl;
    cout << "C) La cantidad de empleados que ganan $2.780 pero menos de $5.999 es: " << cont2780o5999 << endl;
    cout << "D) La cantidad de empleados que ganan mas de $5.999 es: " << contMayor5999 << endl;

    return 0;
}