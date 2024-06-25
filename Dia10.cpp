#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int array[] = {10, 8, 9};
    int size = sizeof(array) / sizeof(array[0]);
    sort(array, array + size);
    for (int i = 0; i < size; ++i)
        cout << array[i] << " - ";
    
    cout << endl;

    getchar();
    return 0;
}