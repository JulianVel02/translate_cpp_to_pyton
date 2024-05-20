#include <iostream>
#include <cmath>
using namespace std;

// Leer valor entero
int leerValorEntero(string mensaje)
{
    int valor;
    cout << mensaje;
    cin >> valor;
    return valor;
}

// Escribir valor entero
void escribirValorEntero(int valor, string mensaje)
{
    cout << mensaje << valor << endl;
}

// Separar fecha en año, mes, día (AAAAMMDD)
void separarFecha(int fecha, int &anio, int &mes, int &dia)
{
    anio = fecha / 10000;
    mes = (fecha % 10000) / 100;
    dia = fecha % 100;
}

// Calcular factorial
int factorial(int n)
{
    int result = 1;
    if (n < 0)
    {
        cout << "Factorial no esta definido para los negativos. \n";
        return -1;
    }
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

// Calcular factorial con recursividad
long fact(int n)
{
    if (n == 1) // Se asegura que termine.
        return 1;

    return n * fact(n - 1); // Si no es 1, sigue la recursion.
}

// Calcular fibonacci con recursividad
int fibonacci(int n)
{
    if (n <= 1)
    {
        return 1;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

// Calcular potencia
int potencia(int base, int exponente)
{
    int resultado = 1;
    for (int i = 0; i < exponente; i++)
    {
        resultado *= base;
    }
    return resultado;
}

// Verificar si un número es par
bool esPar(int num)
{
    return num % 2 == 0;
}

// Verificar si un número es múltiplo de 3
bool esMultTres(int num)
{
    return num % 3 == 0;
}

// Contar múltiplos de 3
void cantidadMultiplos3(int num, int &contador)
{
    if (num % 3 == 0)
    {
        contador++;
    }
}

// Contar múltiplos de 5
void cantidadMultiplos5(int num, int &contador)
{
    if (num % 5 == 0)
    {
        contador++;
    }
}

// Contar múltiplos de 3 y 5
void cantMultiplos3y5(int num, int &contador)
{
    if (num % 3 == 0 && num % 5 == 0)
    {
        contador++;
    }
}

// Calcular porcentaje de diferencia
float calcularPorcentajeDiferencia(int A, int B)
{
    return (B - A) * 100 / (A + B);
}

// Convertir edad a grupo etario
int EdadAGrupoEtario(int edad)
{
    if (edad <= 14)
    {
        return 1;
    }
    else if (edad <= 21)
    {
        return 2;
    }
    else if (edad <= 28)
    {
        return 3;
    }
    else if (edad <= 35)
    {
        return 4;
    }
    else if (edad <= 42)
    {
        return 5;
    }
    else if (edad <= 49)
    {
        return 6;
    }
    else if (edad <= 63)
    {
        return 7;
    }
    else
    {
        return 8;
    }
}

// Pedir datos
void pedirDatos(string mensaje, int &valor)
{
    cout << mensaje;
    cin >> valor;
}

// Obtener el máximo entre dos números
int maximo(int a, int b)
{
    return (a > b) ? a : b;
}

// Obtener el mínimo entre dos números
int minimo(int a, int b)
{
    return (a < b) ? a : b;
}

// Calcular raíz cuadrada
float raizCuadrada(float numero)
{
    if (numero < 0)
    {
        // Manejar error de número negativo para la raíz cuadrada
        return -1;
    }
    else
    {
        return sqrt(numero);
    }
}

// // -------------------------- CADENAS -------------------------- //

// // longitud de cadena
// int longitudCadena(string cadena)
// {
//     return cadena.length();
// }

// // concatenar strings
// string concatenarCadenas(string cadena1, string cadena2)
// {
//     return cadena1 + cadena2;
// }

// // cadena a minusculas
// string toMinusculas(string cadena)
// {
//     transform(cadena.begin(), cadena.end(), cadena.begin(), ::tolower);
//     return cadena;
// }

// // cadena a mayusculas
// string toMayusculas(string cadena)
// {
//     transform(cadena.begin(), cadena.end(), cadena.begin(), ::toupper);
//     return cadena;
// }

// // obtener fecha actual
// #include <ctime>

// string obtenerFechaActual()
// {
//     time_t tiempo = time(NULL);
//     struct tm *tiempoLocal = localtime(&tiempo);
//     char fecha[26];
//     strftime(fecha, sizeof(fecha), "%Y-%m-%d", tiempoLocal);
//     return fecha;
// }

// // hora actual
// #include <ctime>

// string obtenerHoraActual()
// {
//     time_t tiempo = time(NULL);
//     struct tm *tiempoLocal = localtime(&tiempo);
//     char hora[11];
//     strftime(hora, sizeof(hora), "%H:%M:%S", tiempoLocal);
//     return hora;
// }

// // validar si es entero
// bool esEntero(string cadena)
// {
//     for (char c : cadena)
//     {
//         if (!isdigit(c))
//         {
//             return false;
//         }
//     }
//     return true;
// }

// // validar si es float
// #include <regex>

// bool esFlotante(string cadena)
// {
//     regex regex("[0-9]+([.][0-9]{1,2})?");
//     return regex_match(cadena, regex);
// }