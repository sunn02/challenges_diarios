#include <iostream>
#include <string>

using namespace std;

void pol(){
    string palabra;
    string invert = "";
    cout << "Ingrese una palabra: " ;
    cin >> palabra;
    
    for(char carac : palabra){
        invert = carac + invert;
    }
    if (palabra == invert){
        cout << "Es palindromo" << endl;
    } 
    else {
        cout << "No es palindromo" << endl;
    }
}
int main(){
    pol();
    return 0;
}