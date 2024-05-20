#include <iostream>
using namespace std;

//​Dado tres valores determinar e imprimir una leyenda según sea: “Forman triangulo” o “No forman triángulo”.

/*  
Desigualdad de triangulos:
- Si dos lados son iguales y el tercer lado es menor, no se puede formar un triangulo.
- Si los tres lados son diferentes y ninguno de ellos es mayor que la suma de los otros dos, se puede formar un
- Si todos los lados son diferentes entre sí, se puede formar un triangulo equilatero (todos tienen la misma medida).
- Si los dos lados mayores son menores que la suma del tercer y mayor, no se puede formar un triangulo.

- a + b > c
- a + c > b
- b + c > a
*/

int main () {
    int a,b,c;
    
    cout << "Ingrese valor de A: ";
    cin >> a;
    cout << "Ingrese valor de B: ";
    cin >> b;
    cout << "Ingrese valor de C: ";
    cin >> c;

    if ((a != b) && (a != c) && (b != c)) { // Verifica si los tres lados son diferentes
        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            cout << "Forman un triangulo";
        } else {
            cout << "No forman un triangulo";
        }
    } else {
        cout << "No forman un triangulo"; // Si los tres lados son iguales, no forman un triángulo
    }
    
    return 0;
}