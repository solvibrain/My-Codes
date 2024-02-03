#include <iostream>
using namespace std;

int main()
{
    // Explicityly initilaixe with nullptr
    int *p_number1{nullptr};
    int *p_fractional_number1{nullptr};
    // int *number = 456;
    char *p_mesage = "Hello wordd";

    // pointer to different variables are of the same size
    cout << "sizeof ( int)" << sizeof(int) << endl;
    cout << "sizeof ( double)" << sizeof(double) << endl;
    cout << "sizeof ( double*)" << sizeof(double *) << endl;
    cout << "sizeof ( int*)" << sizeof(int *) << endl;
    cout << "sizeof ( p_number1)" << sizeof(p_number1) << endl;
    cout << "sizeof ( p_fractional_number1)" << sizeof(p_fractional_number1) << endl;
    cout << " lets see wat thsi is printing" << *p_mesage << endl;
    cout << " lets see wat thsi is printing" << sizeof(p_mesage) << endl;
}