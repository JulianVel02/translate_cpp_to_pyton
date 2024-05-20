// #include <iostream>
// #include <string>
// using namespace std;

// int main()
// {
//     string nombre;
//     string nombrePersonaMasJoven = "";
//     string nombrePersonaMayor = "";
//     string fechaNacimientoStr;
//     int fechaNacimientoPersonaMasJoven = 99991231; // Una fecha muy temprana (AAAAMMDD)
//     int fechaNacimientoPersonaMayor = 00000101;    // Una fecha muy tardía (AAAAMMDD)
//     int fechaNacimiento;

//     cout << "Ingrese el nombre de la persona o FIN para finalizar: ";
//     cin >> nombre;

//     while (nombre != "FIN")
//     {
//         cout << "Ingrese la fecha de nacimiento (AAAAMMDD) de la persona: ";
//         cin >> fechaNacimientoStr;

//         // Convertir la fecha de nacimiento de string a int
//         fechaNacimiento = stoi(fechaNacimientoStr);

//         if (fechaNacimiento < fechaNacimientoPersonaMasJoven)
//         {
//             nombrePersonaMasJoven = nombre;
//             fechaNacimientoPersonaMasJoven = fechaNacimiento;
//         }
//         if (fechaNacimiento > fechaNacimientoPersonaMayor)
//         {
//             nombrePersonaMayor = nombre;
//             fechaNacimientoPersonaMayor = fechaNacimiento;
//         }
        
//         cout << "Ingrese el nombre de la siguiente persona o FIN para finalizar: ";
//         cin >> nombre;
//     }
    
//     cout << "La persona más joven es: " << nombrePersonaMasJoven << endl;
//     cout << "La persona mayor es: " << nombrePersonaMayor << endl;

//     return 0;
// }
