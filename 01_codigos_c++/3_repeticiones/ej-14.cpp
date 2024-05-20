#include <iostream>
using namespace std;

//* Dados 50 números enteros, informar el promedio de los mayores que 100 y la suma de los menores que –10
int main()
{
  int contadorMayores = 0;
  int sumaMayores = 0;
  int sumaMenores = 0;
  int numero;


  for (int i = 0; i < 50; i++) {
    cout << "Ingrese un número: ";
    cin >> numero;

    if (numero > 100) {
      contadorMayores++;
      sumaMayores += numero;
    } else if (numero < -10) {
      sumaMenores += numero;
    }
  }

  // Calcular el promedio de los mayores si hay al menos uno
  if (contadorMayores > 0) {
    float promedioMayores = sumaMayores / contadorMayores;
    cout << "Promedio de mayores que 100: " << promedioMayores << endl;
  }

  cout << "Suma de menores que -10: " << sumaMenores << endl;

  return 0;
    return 0;
}