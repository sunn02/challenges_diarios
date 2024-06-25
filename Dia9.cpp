#include <iostream>

using namespace std;

int suma(int a, int b) {
	return (a+b);
}

int main(){
    int num1, num2, resultado;
    cout << "Ingrese un numero: " ;
    cin >> num1;

    cout << "Ingrese otro numero: " ;
    cin >> num2;

    resultado = suma(num1,num2);
    cout << "La suma es: " << resultado  << endl;

    return 0;   

}